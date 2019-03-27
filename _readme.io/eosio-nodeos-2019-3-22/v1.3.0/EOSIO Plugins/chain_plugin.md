---
title: "chain_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The **chain_plugin** is a core plugin required to process and aggregate chain data on an EOSIO node. 

[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "Config Options for eosio::chain_plugin:\n  --blocks-dir arg (=\"blocks\")          the location of the blocks directory\n                                        (absolute path or relative to\n                                        application data dir)\n  --checkpoint arg                      Pairs of [BLOCK_NUM,BLOCK_ID] that\n                                        should be enforced as checkpoints.\n  --wasm-runtime wavm/wabt              Override default WASM runtime\n  --abi-serializer-max-time-ms arg (=15000)\n                                        Override default maximum ABI\n                                        serialization time allowed in ms\n  --chain-state-db-size-mb arg (=1024)  Maximum size (in MiB) of the chain\n                                        state database\n  --chain-state-db-guard-size-mb arg (=128)\n                                        Safely shut down node when free space\n                                        remaining in the chain state database\n                                        drops below this size (in MiB).\n  --reversible-blocks-db-size-mb arg (=340)\n                                        Maximum size (in MiB) of the reversible\n                                        blocks database\n  --reversible-blocks-db-guard-size-mb arg (=2)\n                                        Safely shut down node when free space\n                                        remaining in the reverseible blocks\n                                        database drops below this size (in\n                                        MiB).\n  --chain-threads arg (=2)              Number of worker threads in controller\n                                        thread pool\n  --contracts-console                   print contract's output to console\n  --actor-whitelist arg                 Account added to actor whitelist (may\n                                        specify multiple times)\n  --actor-blacklist arg                 Account added to actor blacklist (may\n                                        specify multiple times)\n  --contract-whitelist arg              Contract account added to contract\n                                        whitelist (may specify multiple times)\n  --contract-blacklist arg              Contract account added to contract\n                                        blacklist (may specify multiple times)\n  --action-blacklist arg                Action (in the form code::action) added\n                                        to action blacklist (may specify\n                                        multiple times)\n  --key-blacklist arg                   Public key added to blacklist of keys\n                                        that should not be included in\n                                        authorities (may specify multiple\n                                        times)\n  --sender-bypass-whiteblacklist arg    Deferred transactions sent by accounts\n                                        in this list do not have any of the\n                                        subjective whitelist/blacklist checks\n                                        applied to them (may specify multiple\n                                        times)\n  --read-mode arg (=speculative)        Database read mode (\"speculative\",\n                                        \"head\", or \"read-only\").\n                                        In \"speculative\" mode database contains\n                                        changes done up to the head block plus\n                                        changes made by transactions not yet\n                                        included to the blockchain.\n                                        In \"head\" mode database contains\n                                        changes done up to the current head\n                                        block.\n                                        In \"read-only\" mode database contains\n                                        incoming block changes but no\n                                        speculative transaction processing.\n\n  --validation-mode arg (=full)         Chain validation mode (\"full\" or\n                                        \"light\").\n                                        In \"full\" mode all incoming blocks will\n                                        be fully validated.\n                                        In \"light\" mode all incoming blocks\n                                        headers will be fully validated;\n                                        transactions in those validated blocks\n                                        will be trusted\n\n  --disable-ram-billing-notify-checks   Disable the check which subjectively\n                                        fails a transaction if a contract bills\n                                        more RAM to another account within the\n                                        context of a notification handler (i.e.\n                                        when the receiver is not the code of\n                                        the action).\n  --trusted-producer arg                Indicate a producer whose blocks\n                                        headers signed by it will be fully\n                                        validated, but transactions in those\n                                        validated blocks will be trusted.\n\nCommand Line Options for eosio::chain_plugin:\n  --genesis-json arg                    File to read Genesis State from\n  --genesis-timestamp arg               override the initial timestamp in the\n                                        Genesis State file\n  --print-genesis-json                  extract genesis_state from blocks.log\n                                        as JSON, print to console, and exit\n  --extract-genesis-json arg            extract genesis_state from blocks.log\n                                        as JSON, write into specified file, and\n                                        exit\n  --fix-reversible-blocks               recovers reversible block database if\n                                        that database is in a bad state\n  --force-all-checks                    do not skip any checks that can be\n                                        skipped while replaying irreversible\n                                        blocks\n  --disable-replay-opts                 disable optimizations that specifically\n                                        target replay\n  --replay-blockchain                   clear chain state database and replay\n                                        all blocks\n  --hard-replay-blockchain              clear chain state database, recover as\n                                        many blocks as possible from the block\n                                        log, and then replay those blocks\n  --delete-all-blocks                   clear chain state database and block\n                                        log\n  --truncate-at-block arg (=0)          stop hard replay / block log recovery\n                                        at this block number (if set to\n                                        non-zero number)\n  --import-reversible-blocks arg        replace reversible block database with\n                                        blocks imported from specified file and\n                                        then exit\n  --export-reversible-blocks arg        export reversible block database in\n                                        portable format into specified file and\n                                        then exit\n  --snapshot arg",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::chain_plugin\n\n# nodeos startup params\n--plugin eosio::chain_plugin",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Dependencies"
}
[/block]
None