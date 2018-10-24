from argparse import ArgumentParser, Namespace
import asyncio
import logging
from typing import (
    Any,
    Dict,
)

from lahja import (
    EventBus,
    Endpoint,
)

from p2p.service import BaseService

from trinity.exceptions import (
    AmbigiousFileSystem,
    MissingPath,
)
from trinity.initialization import (
    initialize_data_dir,
    is_data_dir_initialized,
)
from trinity.cli_parser import (
    parser,
    subparser,
)
from trinity.config import (
    TrinityConfig,
)
from trinity.constants import (
    MAINNET_NETWORK_ID,
    MAIN_EVENTBUS_ENDPOINT,
    NETWORKING_EVENTBUS_ENDPOINT,
    ROPSTEN_NETWORK_ID,
)
from trinity.events import (
    ShutdownRequest
)
from trinity.extensibility import (
    BaseManagerProcessScope,
    MainAndIsolatedProcessScope,
    PluginManager,
    SharedProcessScope,
)
from trinity.plugins.registry import (
    ENABLED_PLUGINS
)
from trinity.utils.ipc import (
    kill_process_gracefully,
)
from trinity.utils.logging import (
    enable_warnings_by_default,
    setup_log_levels,
    setup_trinity_stderr_logging,
    setup_trinity_file_and_queue_logging,
    with_queued_logging,
)
from trinity.utils.mp import (
    ctx,
)
from trinity.utils.profiling import (
    setup_cprofiler,
)
from trinity.utils.shutdown import (
    exit_signal_with_service,
)
from trinity.utils.version import (
    construct_trinity_client_identifier,
    is_prerelease,
)


PRECONFIGURED_NETWORKS = {MAINNET_NETWORK_ID, ROPSTEN_NETWORK_ID}


TRINITY_HEADER = (
    "\n"
    "      ______     _       _ __       \n"
    "     /_  __/____(_)___  (_) /___  __\n"
    "      / / / ___/ / __ \/ / __/ / / /\n"
    "     / / / /  / / / / / / /_/ /_/ / \n"
    "    /_/ /_/  /_/_/ /_/_/\__/\__, /  \n"
    "                           /____/   "
)

TRINITY_AMBIGIOUS_FILESYSTEM_INFO = (
    "Could not initialize data directory\n\n"
    "   One of these conditions must be met:\n"
    "   * HOME environment variable set\n"
    "   * XDG_TRINITY_ROOT environment variable set\n"
    "   * TRINITY_DATA_DIR environment variable set\n"
    "   * --data-dir command line argument is passed\n"
    "\n"
    "   In case the data directory is outside of the trinity root directory\n"
    "   Make sure all paths are pre-initialized as Trinity won't attempt\n"
    "   to create directories outside of the trinity root directory\n"
)


def main() -> None:
    event_bus = EventBus(ctx)
    main_endpoint = event_bus.create_endpoint(MAIN_EVENTBUS_ENDPOINT)
    main_endpoint.connect_no_wait()

    plugin_manager = setup_plugins(
        MainAndIsolatedProcessScope(event_bus, main_endpoint)
    )
    plugin_manager.amend_argparser_config(parser, subparser)
    args = parser.parse_args()

    if args.network_id not in PRECONFIGURED_NETWORKS:
        raise NotImplementedError(
            "Unsupported network id: {0}.  Only the ropsten and mainnet "
            "networks are supported.".format(args.network_id)
        )

    has_ambigous_logging_config = (
        args.log_levels is not None and
        None in args.log_levels and
        args.stderr_log_level is not None
    )
    if has_ambigous_logging_config:
        parser.error(
            "\n"
            "Ambiguous logging configuration: The logging level for stderr was "
            "configured with both `--stderr-log-level` and `--log-level`. "
            "Please remove one of these flags",
        )

    if is_prerelease():
        # this modifies the asyncio logger, but will be overridden by any custom settings below
        enable_warnings_by_default()

    stderr_logger, formatter, handler_stream = setup_trinity_stderr_logging(
        args.stderr_log_level or (args.log_levels and args.log_levels.get(None))
    )

    if args.log_levels:
        setup_log_levels(args.log_levels)

    try:
        trinity_config = TrinityConfig.from_parser_args(args)
    except AmbigiousFileSystem:
        parser.error(TRINITY_AMBIGIOUS_FILESYSTEM_INFO)

    if not is_data_dir_initialized(trinity_config):
        # TODO: this will only work as is for chains with known genesis
        # parameters.  Need to flesh out how genesis parameters for custom
        # chains are defined and passed around.
        try:
            initialize_data_dir(trinity_config)
        except AmbigiousFileSystem:
            parser.error(TRINITY_AMBIGIOUS_FILESYSTEM_INFO)
        except MissingPath as e:
            parser.error(
                "\n"
                f"It appears that {e.path} does not exist. "
                "Trinity does not attempt to create directories outside of its root path. "
                "Either manually create the path or ensure you are using a data directory "
                "inside the XDG_TRINITY_ROOT path"
            )

    # Verify that the database engine that trinity is configured to use matches
    # the existing on-disk engine.
    if trinity_config.db_engine != trinity_config.on_disk_database_engine:
        database_dir = trinity_config.database_dir
        config_engine = trinity_config.db_engine
        on_disk_engine = trinity_config.on_disk_database_engine
        parser.error(
            "\n"
            f"Database engine mismatch.  The on disk database uses the "
            f"`{on_disk_engine}` but trinity is configured to use the "
            f"`{config_engine}.  You must either re-run trinity using the engine "
            "currently used with the on-disk database or remove the database "
            f"from `{database_dir}`."
        )

    file_logger, log_queue, listener = setup_trinity_file_and_queue_logging(
        stderr_logger,
        formatter,
        handler_stream,
        trinity_config.logfile_path,
        args.file_log_level,
    )

    display_launch_logs(trinity_config)

    # compute the minimum configured log level across all configured loggers.
    min_configured_log_level = min(
        stderr_logger.level,
        file_logger.level,
        *(args.log_levels or {}).values()
    )

    extra_kwargs = {
        'log_queue': log_queue,
        'log_level': min_configured_log_level,
        'profile': args.profile,
    }

    # Plugins can provide a subcommand with a `func` which does then control
    # the entire process from here.
    if hasattr(args, 'func'):
        args.func(args, trinity_config)
    else:
        trinity_boot(
            args,
            trinity_config,
            extra_kwargs,
            plugin_manager,
            listener,
            event_bus,
            main_endpoint,
            stderr_logger,
        )


def trinity_boot(args: Namespace,
                 trinity_config: TrinityConfig,
                 extra_kwargs: Dict[str, Any],
                 plugin_manager: PluginManager,
                 listener: logging.handlers.QueueListener,
                 event_bus: EventBus,
                 main_endpoint: Endpoint,
                 logger: logging.Logger) -> None:
    # start the listener thread to handle logs produced by other processes in
    # the local logger.
    listener.start()

    networking_endpoint = event_bus.create_endpoint(NETWORKING_EVENTBUS_ENDPOINT)
    event_bus.start()

    networking_process = ctx.Process(
        target=launch_node,
        args=(args, trinity_config, networking_endpoint,),
        kwargs=extra_kwargs,
    )

    networking_process.start()
    logger.info("Started networking process (pid=%d)", networking_process.pid)

    main_endpoint.subscribe(
        ShutdownRequest,
        lambda ev: kill_trinity_gracefully(
            logger,
            networking_process,
            plugin_manager,
            main_endpoint,
            event_bus,
            ev.reason
        )
    )

    plugin_manager.prepare(args, trinity_config, extra_kwargs)

    try:
        loop = asyncio.get_event_loop()
        loop.run_forever()
        loop.close()
    except KeyboardInterrupt:
        kill_trinity_gracefully(
            logger,
            networking_process,
            plugin_manager,
            main_endpoint,
            event_bus,
            reason="CTRL+C / Keyboard Interrupt"
        )


def kill_trinity_gracefully(logger: logging.Logger,
                            networking_process: Any,
                            plugin_manager: PluginManager,
                            main_endpoint: Endpoint,
                            event_bus: EventBus,
                            reason: str=None) -> None:
    # Notice that we still need the kill_process_gracefully() calls here, for when the user
    # simply uses 'kill' to send a signal to the main process, but also because they will
    # perform a non-gracefull shutdown if the process takes too long to terminate.

    hint = f"({reason})" if reason else f""
    logger.info('Shutting down Trinity %s', hint)
    plugin_manager.shutdown_blocking()
    main_endpoint.stop()
    event_bus.stop()

    # The networking process will have received a SIGINT already (see comment
    # above), so here we wait 2s for it to finish cleanly, and if that fails
    # we kill it.
    networking_process.join(2)
    if networking_process.is_alive():
        kill_process_gracefully(networking_process, logger)
    logger.info('Networking process (pid=%d) terminated', networking_process.pid)

    ArgumentParser().exit(message=f"Trinity shutdown complete {hint}\n")


@setup_cprofiler('launch_node')
@with_queued_logging
def launch_node(args: Namespace, trinity_config: TrinityConfig, endpoint: Endpoint) -> None:
    with trinity_config.process_id_file('networking'):

        NodeClass = trinity_config.node_class
        node = NodeClass(endpoint, trinity_config)
        loop = node.get_event_loop()

        endpoint.connect_no_wait(loop)
        # This is a second PluginManager instance governing plugins in a shared process.
        plugin_manager = setup_plugins(SharedProcessScope(endpoint))
        plugin_manager.prepare(args, trinity_config)

        asyncio.ensure_future(handle_networking_exit(node, plugin_manager, endpoint), loop=loop)
        asyncio.ensure_future(node.run(), loop=loop)
        loop.run_forever()
        loop.close()


def display_launch_logs(trinity_config: TrinityConfig) -> None:
    logger = logging.getLogger('trinity')
    logger.info(TRINITY_HEADER)
    logger.info(construct_trinity_client_identifier())
    logger.info("Trinity DEBUG log file is created at %s", str(trinity_config.logfile_path))


async def handle_networking_exit(service: BaseService,
                                 plugin_manager: PluginManager,
                                 endpoint: Endpoint) -> None:

    async with exit_signal_with_service(service):
        await plugin_manager.shutdown()
        endpoint.stop()


def setup_plugins(scope: BaseManagerProcessScope) -> PluginManager:
    plugin_manager = PluginManager(scope)
    # TODO: Implement auto-discovery of plugins based on some convention/configuration scheme
    plugin_manager.register(ENABLED_PLUGINS)

    return plugin_manager
