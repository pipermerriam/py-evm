Trinity 
=======

0.1.0-alpha.17
--------------

Released November 20, 2018

- `#TODO <https://github.com/ethereum/py-evm/pull/TODO>`_: TODO: TODO
- `#TODO <https://github.com/ethereum/py-evm/pull/TODO>`_: TODO: TODO
- `#TODO <https://github.com/ethereum/py-evm/pull/TODO>`_: TODO: TODO
- `#TODO <https://github.com/ethereum/py-evm/pull/TODO>`_: TODO: TODO
- `#TODO <https://github.com/ethereum/py-evm/pull/TODO>`_: TODO: TODO
- `#TODO <https://github.com/ethereum/py-evm/pull/TODO>`_: TODO: TODO
- `#1443 <https://github.com/ethereum/py-evm/pull/1443>`_: Maintenance: Merge the ``--nodekey`` and ``--nodekey-path`` flags.
- `#1438 <https://github.com/ethereum/py-evm/pull/1438>`_: Bugfix: Remove warnings when printing the ASCII Trinity header
- `#1437 <https://github.com/ethereum/py-evm/pull/1437>`_: Maintenance: Update to use f-strings for string formatting
- `#1435 <https://github.com/ethereum/py-evm/pull/1435>`_: Maintenance: Enable Constantinople fork on Ropsten chain
- `#1434 <https://github.com/ethereum/py-evm/pull/1434>`_: Bugfix: Fix incorrect mainnet genesis parameters.
- `#1421 <https://github.com/ethereum/py-evm/pull/1421>`_: Maintenance: Implement ``eth_syncing`` JSON-RPC endpoint
- `#1410 <https://github.com/ethereum/py-evm/pull/1410>`_: Maintenance: Implement EIP1283 for updated logic for ``SSTORE`` opcode gas costs.
- `#1395 <https://github.com/ethereum/py-evm/pull/1395>`_: Bugfix: Fix gas cost calculations for ``CREATE2`` opcode
- `#1386 <https://github.com/ethereum/py-evm/pull/1386>`_: Maintenance: Trinity now prints a message to make it more clear why Trinity was shutdown.
- `#1387 <https://github.com/ethereum/py-evm/pull/1387>`_: Maintenance: Use colorized output for ``WARNING`` and ``ERROR`` level logging messages.
- `#1378 <https://github.com/ethereum/py-evm/pull/1378>`_: Bugfix: Fix address generation for ``CREATE2`` opcode.
- `#1374 <https://github.com/ethereum/py-evm/pull/1374>`_: Maintenance: New ``ChainTipMonitor`` service to keep track of the highest TD chain tip.
- `#1371 <https://github.com/ethereum/py-evm/pull/1371>`_: Maintenance: Upgrade ``mypy`` to ``0.630``
- `#1367 <https://github.com/ethereum/py-evm/pull/1367>`_: Maintenance: Improve logging output to include more contextual information
- `#1361 <https://github.com/ethereum/py-evm/pull/1361>`_: Maintenance: Remove ``HeaderRequestingPeer`` in favor of ``BaseChainPeer``
- `#1353 <https://github.com/ethereum/py-evm/pull/1353>`_: Maintenance: Decouple peer message handling from syncing.
- `#1351 <https://github.com/ethereum/py-evm/pull/1351>`_: Bugfix: Unhandled ``DecryptionError``
- `#1348 <https://github.com/ethereum/py-evm/pull/1348>`_: Maintenance: Add default server URIs for mainnet and ropsten.
- `#1347 <https://github.com/ethereum/py-evm/pull/1347>`_: Maintenance: Improve code organization within ``trinity`` module
- `#1343 <https://github.com/ethereum/py-evm/pull/1343>`_: Bugfix: Rename ``Chain.network_id`` to be ``Chain.chain_id``
- `#1342 <https://github.com/ethereum/py-evm/pull/1342>`_: Maintenance: Internal rename of ``ChainConfig`` to ``TrinityConfig``
- `#1336 <https://github.com/ethereum/py-evm/pull/1336>`_: Maintenance: Implement plugin for EthStats reporting.
- `#1335 <https://github.com/ethereum/py-evm/pull/1335>`_: Maintenance: Relax some constraints on the ordered task management constructs.
- `#1332 <https://github.com/ethereum/py-evm/pull/1332>`_: Maintenance: Upgrade ``pyrlp`` to ``1.0.3``
- `#1317 <https://github.com/ethereum/py-evm/pull/1317>`_: Maintenance: Extract peer selection from the header sync.
- `#1312 <https://github.com/ethereum/py-evm/pull/1312>`_: Maintenance: Turn on warnings by default if in a prerelease

0.1.0-alpha.16
--------------

Released September 27, 2018

- `#1332 <https://github.com/ethereum/py-evm/pull/1332>`_: Bugfix: Comparing rlp objects across processes used to fail sporadically, because of a changing object hash (fixed by upgrading pyrlp to 1.0.3)
- `#1326 <https://github.com/ethereum/py-evm/pull/1326>`_: Maintenance: Squash a stack trace in the logs when a peer sends us an invalid public key during handshake
- `#1325 <https://github.com/ethereum/py-evm/pull/1325>`_: Bugfix: When switching to a new peer to sync headers, it might have started from too far behind the tip, and get stuck
- `#1327 <https://github.com/ethereum/py-evm/pull/1327>`_: Maintenance: Squash some log warnings from trying to make a request to a peer (or receive a response) while it is shutting down
- `#1321 <https://github.com/ethereum/py-evm/pull/1321>`_: Bugfix: Address a couple race condition exceptions when syncing headers from a new peer, and other downstream processing is in progress
- `#1316 <https://github.com/ethereum/py-evm/pull/1316>`_: Maintenance: Reduce size of images in documentation
- `#1313 <https://github.com/ethereum/py-evm/pull/1313>`_: Maintenance: Remove miscellaneous things that are generating python warnings (eg~ using deprecated methods)
- `#1279 <https://github.com/ethereum/py-evm/pull/1279>`_: Reliability: Atomically persist when storing: a block, a chain of headers, or a cluster of trie nodes
- `#1304 <https://github.com/ethereum/py-evm/pull/1304>`_: Maintenance: Refactor AtomicDB to return an explict database instance to write into
- `#1296 <https://github.com/ethereum/py-evm/pull/1296>`_: Maintenance: Require new AtomicDB in chain and header DB layers
- `#1295 <https://github.com/ethereum/py-evm/pull/1295>`_: Maintenance: New AtomicDB interface to enable a batch of atomic writes (all succeed or all fail)
- `#1290 <https://github.com/ethereum/py-evm/pull/1290>`_: Bugfix: more graceful recovery when re-launching sync on a fork
- `#1277 <https://github.com/ethereum/py-evm/pull/1277>`_: Maintenance: add a cancellable ``call_later`` to all services
- `#1226 <https://github.com/ethereum/py-evm/pull/1226>`_: Performance: enable multiple peer requests to a single fast peer when other peers are slow
- `#1254 <https://github.com/ethereum/py-evm/pull/1254>`_: Bugfix: peer selection when two peers have exactly the same throughput
- `#1253 <https://github.com/ethereum/py-evm/pull/1253>`_: Maintenance: prefer f-string formatting in p2p, trinity code

0.1.0-alpha.15
--------------

- `#1249 <https://github.com/ethereum/py-evm/pull/1249>`_: Misc bugfixes for fast sync reliability.
- `#1245 <https://github.com/ethereum/py-evm/pull/1245>`_: Improved exception messaging for ``BaseService``
- `#1244 <https://github.com/ethereum/py-evm/pull/1244>`_: Use ``time.perf_counter`` or ``time.monotonic`` over ``time.time``
- `#1242 <https://github.com/ethereum/py-evm/pull/1242>`_: Bugfix: Unhandled ``MalformedMessage``.
- `#1235 <https://github.com/ethereum/py-evm/pull/1235>`_: Typo cleanup.
- `#1236 <https://github.com/ethereum/py-evm/pull/1236>`_: Documentation cleanup
- `#1237 <https://github.com/ethereum/py-evm/pull/1237>`_: Code cleanup
- `#1232 <https://github.com/ethereum/py-evm/pull/1232>`_: Bugfix: Correctly enforce timeouts on peer requests and add lock mechanism to support concurrency.
- `#1229 <https://github.com/ethereum/py-evm/pull/1229>`_: CI cleanup
- `#1228 <https://github.com/ethereum/py-evm/pull/1228>`_: Merge ``KademliaProtocol`` and ``DiscoveryProtocol``
- `#1225 <https://github.com/ethereum/py-evm/pull/1225>`_: Expand peer stats tracking
- `#1221 <https://github.com/ethereum/py-evm/pull/1221>`_: Implement Discovery V5 Protocol
- `#1219 <https://github.com/ethereum/py-evm/pull/1219>`_: Re-organize and document fixture filler tools
- `#1214 <https://github.com/ethereum/py-evm/pull/1214>`_: Implement ``BaseService.is_operational``.
- `#1210 <https://github.com/ethereum/py-evm/pull/1210>`_: Convert sync to use streaming queue instead of batches.
- `#1209 <https://github.com/ethereum/py-evm/pull/1209>`_: Chain Builder tool
- `#1205 <https://github.com/ethereum/py-evm/pull/1205>`_: Bugfix: ExchangeHandler stats crash
- `#1204 <https://github.com/ethereum/py-evm/pull/1204>`_: Consensus bugfix for uncle validation
- `#1151 <https://github.com/ethereum/py-evm/pull/1151>`_: Change to ``import_block`` to return chain re-organization data.
- `#1197 <https://github.com/ethereum/py-evm/pull/1197>`_: Increase wait time for database IPC socket.
- `#1194 <https://github.com/ethereum/py-evm/pull/1194>`_: Unify ``ValidationError`` to use ``eth-utils`` exception class.
- `#1190 <https://github.com/ethereum/py-evm/pull/1190>`_: Improved testing for peer authentication
- `#1189 <https://github.com/ethereum/py-evm/pull/1189>`_: Detect crashed sub-services and exit
- `#1179 <https://github.com/ethereum/py-evm/pull/1179>`_: ``LightNode`` now uses ``Server`` for incoming peer connections.
- `#1182 <https://github.com/ethereum/py-evm/pull/1182>`_: Convert ``fix-unclean-shutdown`` CLI command to be a plugin


0.1.0-alpha.14
--------------

- `#1081 <https://github.com/ethereum/py-evm/pull/1081>`_ `#1115 <https://github.com/ethereum/py-evm/pull/1115>`_ `#1116 <https://github.com/ethereum/py-evm/pull/1116>`_: Reduce logging output during state sync.
- `#1063 <https://github.com/ethereum/py-evm/pull/1063>`_ `#1035 <https://github.com/ethereum/py-evm/pull/1035>`_ `#1089 <https://github.com/ethereum/py-evm/pull/1089>`_ `#1131 <https://github.com/ethereum/py-evm/pull/1131>`_ `#1132 <https://github.com/ethereum/py-evm/pull/1132>`_ `#1138 <https://github.com/ethereum/py-evm/pull/1138>`_ `#1149 <https://github.com/ethereum/py-evm/pull/1149>`_ `#1159 <https://github.com/ethereum/py-evm/pull/1159>`_: Implement round trip request/response API.
- `#1094 <https://github.com/ethereum/py-evm/pull/1094>`_ `#1124 <https://github.com/ethereum/py-evm/pull/1124>`_: Make the node processing during state sync more async friendly.
- `#1097 <https://github.com/ethereum/py-evm/pull/1097>`_: Keep track of which peers are missing trie nodes during state sync.
- `#1109 <https://github.com/ethereum/py-evm/pull/1109>`_ `#1135 <https://github.com/ethereum/py-evm/pull/1135>`_: Python 3.7 testing and experimental support.
- `#1136 <https://github.com/ethereum/py-evm/pull/1136>`_ `#1120 <https://github.com/ethereum/py-evm/pull/1120>`_: Module re-organization in preparation of extracting ``p2p`` and ``trinity`` modules.
- `#1137 <https://github.com/ethereum/py-evm/pull/1137>`_: Peer subscriber API now supports specifying specific msg types to reduce msg queue traffic.
- `#1142 <https://github.com/ethereum/py-evm/pull/1142>`_ `#1165 <https://github.com/ethereum/py-evm/pull/1165>`_: Implement JSON-RPC endpoints for: ``eth_estimateGas``, ``eth_accounts``, ``eth_call``
- `#1150 <https://github.com/ethereum/py-evm/pull/1150>`_ `#1176 <https://github.com/ethereum/py-evm/pull/1176>`_: Better handling of malformed messages from peers.
- `#1157 <https://github.com/ethereum/py-evm/pull/1157>`_: Use shared pool of workers across all services.
- `#1158 <https://github.com/ethereum/py-evm/pull/1158>`_: Support specifying granular logging levels via CLI.
- `#1161 <https://github.com/ethereum/py-evm/pull/1161>`_: Use a tmpfile based LevelDB database for cache during state sync to reduce memory footprint.
- `#1166 <https://github.com/ethereum/py-evm/pull/1166>`_: Latency and performance tracking for peer requests.
- `#1173 <https://github.com/ethereum/py-evm/pull/1173>`_: Better APIs for background task running for ``Service`` classes.
- `#1182 <https://github.com/ethereum/py-evm/pull/1182>`_: Convert ``fix-unclean-shutdown`` command to be a plugin.


0.1.0-alpha.13
--------------

- Remove specified ``eth-account`` dependency in favor of allowing ``web3.py`` specify the correct version.


0.1.0-alpha.12
--------------

- `#1058 <https://github.com/ethereum/py-evm/pull/1058>`_  `#1044 <https://github.com/ethereum/py-evm/pull/1044>`_: Add ``fix-unclean-shutdown`` CLI command for cleaning up after a dirty shutdown of the ``trinity`` CLI process.
- `#1041 <https://github.com/ethereum/py-evm/pull/1041>`_: Bugfix for ensuring CPU count for process pool is always greater than ``0``
- `#1010 <https://github.com/ethereum/py-evm/pull/1010>`_: Performance tuning during fast sync.  Only check POW on a subset of the received headers.
- `#996 <https://github.com/ethereum/py-evm/pull/996>`_ Experimental new Plugin API:  Both the transaction pool and the ``console`` and ``attach`` commands are now written as plugins.
- `#898 <https://github.com/ethereum/py-evm/pull/898>`_: New experimental transaction pool.  Disabled by default.  Enable with ``--tx-pool``.  (**warning**: has known issues that effect sync performance)
- `#935 <https://github.com/ethereum/py-evm/pull/935>`_: Protection against eclipse attacks.
- `#869 <https://github.com/ethereum/py-evm/pull/869>`_: Ensure connected peers are on the same side of the DAO fork.

Minor Changes

- `#1081 <https://github.com/ethereum/py-evm/pull/1081>`_: Reduce ``DEBUG`` log output during state sync.
- `#1071 <https://github.com/ethereum/py-evm/pull/1071>`_: Minor fix for how version string is generated for trinity
- `#1070 <https://github.com/ethereum/py-evm/pull/1070>`_: Easier profiling of ``ChainSyncer``
- `#1068 <https://github.com/ethereum/py-evm/pull/1068>`_: Optimize ``evm.db.chain.ChainDB.persist_block`` for common case.
- `#1057 <https://github.com/ethereum/py-evm/pull/1057>`_: Additional ``DEBUG`` logging of peer uptime and msg stats.
- `#1049 <https://github.com/ethereum/py-evm/pull/1049>`_: New integration test suite for trinity CLI
- `#1045 <https://github.com/ethereum/py-evm/pull/1045>`_ `#1051 <https://github.com/ethereum/py-evm/pull/1051>`_: Bugfix for generation of block numbers for ``GetBlockHeaders`` requests.
- `#1011 <https://github.com/ethereum/py-evm/pull/1011>`_: Workaround for parity bug `parity #8038 <https://github.com/paritytech/parity-ethereum/issues/8038>`_
- `#987 <https://github.com/ethereum/py-evm/pull/987>`_: Now serving requests from peers during fast sync.
- `#971 <https://github.com/ethereum/py-evm/pull/971>`_ `#909 <https://github.com/ethereum/py-evm/pull/909>`_ `#650 <https://github.com/ethereum/py-evm/pull/650>`_: Benchmarking test suite.
- `#968 <https://github.com/ethereum/py-evm/pull/968>`_: When launching ``console`` and ``attach`` commands, check for presence of IPC socket and log informative message if not found.
- `#934 <https://github.com/ethereum/py-evm/pull/934>`_: Decouple the ``Discovery`` and ``PeerPool`` services.
- `#913 <https://github.com/ethereum/py-evm/pull/913>`_: Add validation of retrieved contract code when operating in ``--light`` mode.
- `#908 <https://github.com/ethereum/py-evm/pull/908>`_: Bugfix for transitioning from syncing chain data to state data during fast sync.
- `#905 <https://github.com/ethereum/py-evm/pull/905>`_: Support for multiple UPNP devices.


0.1.0-alpha.11
--------------

- Bugfix for ``PreferredNodePeerPool`` to respect ``max_peers``


0.1.0-alpha.10
--------------

- More bugfixes to enforce ``--max-peers`` in ``PeerPool._connect_to_nodes``


0.1.0-alpha.9
-------------

- Bugfix to enforce ``--max-peers`` for incoming connections.


0.1.0-alpha.7
-------------

- Remove ``min_peers`` concept from ``PeerPool``
- Add ``--max-peers`` and enforcement of maximum peer connections maintained by
  the ``PeerPool``.


0.1.0-alpha.6
-------------

- Respond to ``GetBlockHeaders`` message during fast sync to prevent being disconnected as a *useless peer*.
- Add ``--profile`` CLI flag to Trinity to enable profiling via ``cProfile``
- Better error messaging with Trinity cannot determine the appropriate location for the data directory.
- Handle ``ListDeserializationError`` during handshake.
- Add ``net_version`` JSON-RPC endpoint.
- Add ``web3_clientVersion`` JSON-RPC endpoint.
- Handle ``rlp.DecodingError`` during handshake.
