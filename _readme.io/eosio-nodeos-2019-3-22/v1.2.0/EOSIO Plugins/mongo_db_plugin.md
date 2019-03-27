---
title: "mongo_db_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The optional `eosio::mongo_db_plugin` provides archiving of blockchain data into a MongoDB. It is recommended that the plugin be added to a non-producing node as it is designed to shut down on any failed insert into the MongoDB and is resource intensive. For best results dedicate a nodeos instance to running this one plugin. The rationale behind this shutdown on error is so that any issues with the mongo database or connectivity can be fixed and the nodeos can be restarted without having to resync or replay.

The `mongo_db_plugin` does slow down replay/resync as the conversion of block data to JSON and insertion into MongoDB is resource intensive. The plugin does use a worker thread for processing the block data, but this does not help much when replaying/resyncing. 

It is recommended that a large `--abi-serializer-max-time-ms` value be passed into the nodeos running the `mongo_db_plugin` as the default abi serializer time limit is not large enough to serialize large blocks.

It is also recommended that read-only mode is used to avoid speculative execution. See read-only db mode documentation. Forked data is still recorded (data that never becomes irreversible) but speculative transaction processing and signaling is avoided minimizing the transaction_traces/action_traces stored.

action data is stored on chain as raw bytes. This plugin attempts to use associated ABI on accounts to deserialize the raw bytes into explanded abi_def form for storage into mongo. Note that invalid or missing abi on a contract will result in the action data being stored as raw bytes. For example the eosio system contract does not provide abi for the `onblock` action so it is stored as raw bytes.
[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  -q [ --mongodb-queue-size ] arg (=256)\n                                        The target queue size between nodeos\n                                        and MongoDB plugin thread.\n  --mongodb-abi-cache-size              The maximum size of the abi cache for\n                                        serializing data.\n  --mongodb-wipe                        Required with --replay-blockchain,\n                                        --hard-replay-blockchain, or\n                                        --delete-all-blocks to wipe mongo\n                                        db.This option required to prevent\n                                        accidental wipe of mongo db. \n                                        Defaults to false.\n  --mongodb-block-start arg (=0)        If specified then only abi data pushed\n                                        to mongodb until specified block is\n                                        reached.\n  -m [ --mongodb-uri ] arg              MongoDB URI connection string, see:\n                                        https://docs.mongodb.com/master/referen\n                                        ce/connection-string/. If not specified\n                                        then plugin is disabled. Default\n                                        database 'EOS' is used if not specified\n                                        in URI. Example: mongodb://127.0.0.1:27\n                                        017/EOS\n  --mongodb-store-blocks                Enables storing blocks in mongodb.\n                                        Defaults to true.\n  --mongodb-store-block-states          Enables storing block state in mongodb.\n                                        Defaults to true.\n  --mongodb-store-transactions          Enables storing transactions in mongodb.\n                                        Defaults to true.\n  --mongodb-store-transaction-traces    Enables storing transaction traces in                                             mongodb.\n                                        Defaults to true.\n  --mongodb-store-action-traces         Enables storing action traces in mongodb.\n                                        Defaults to true.\n  --mongodb-filter-on                   Mongodb: Track actions which match\n                                        receiver:action:actor. Actor may be blank\n                                        to include all. Receiver and Action may\n                                        not be blank. Default is * include\n                                        everything.\n  --mongodb-filter-out                  Mongodb: Do not track actions which match\n                                        receiver:action:actor. Action and Actor\n                                        both blank excludes all from reciever.                                           Actor blank excludes all from\n                                        reciever:action. Receiver may not be\n                                        blank.\n  \n",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Notes"
}
[/block]
`--mongodb-store-*` options all default to true.
`--mongodb-filter-*` options currently only applies to the action_traces collection.
[block:api-header]
{
  "title": "Example Filters"
}
[/block]
```
mongodb-filter-out = eosio:onblock:
mongodb-filter-out = gu2tembqgage::
mongodb-filter-out = blocktwitter:: 
```
[block:api-header]
{
  "title": "Collections"
}
[/block]
* accounts - created on applied transaction. Always updated even if `mongodb-store-action-traces=false`.
  * Currently limited to just name and ABI if contract abi on account
  * Mostly for internal use as the stored ABI is used to convert action data into JSON for storage as associated actions on contract are processed.
  * Invalid ABI on account will prevent conversion of action data into JSON for storage resulting in just the action data being stored as hex. For example, the original eosio.system contract did not provide ABI for the `onblock` action and therefore all 'onblock` action data is stored as hex until the time `onblock` ABI is added to the eosio.system contract.

* action_traces - created on applied transaction
  * receipt - action_trace action_receipt - see eosio::chain::action_receipt
  * trx_id - transaction id
  * act - action - see eosio::chain::action
  * elapsed - time in microseconds to execute action
  * console - console output of action. Always empty unless `contracts-console = true` option specified.

* block_states - created on accepted block
  * block_num
  * block_id
  * block_header_state - see eosio::chain::block_header_state
  * validated
  * in_current_chain

* blocks - created on accepted block
  * block_num
  * block_id
  * block - signed block - see eosio::chain::signed_block
  * validated - added on irreversible block
  * in_current_chain - added on irreversible block
  * irreversible=true - added on irreversible block

* transaction_traces - created on applied transaction
  * see chain::eosio::transaction_trace

* transactions - created on accepted transaction - does not include inline actions
  * see eosio::chain::signed_transaction. In addition to signed_transaction data the following are also stored.
  * trx_id - transaction id
  * irreversible=true - added on irreversible block
  * block_id - added on irreversble block
  * block_num - added on irreversible block
  * signing_keys
  * accepted
  * implicit
  * scheduled

* account_controls - created on applied transaction. Always updated even if `mongodb-store-action-traces=false`.
  * controlled_account
  * controlling_permission
  * controlling_account

The equivalent of /v1/history/get_controlled_acounts with mongo: `db.account_controls.find({"controlling_account":"hellozhangyi"}).pretty()`

* pub_keys - created on applied transaction. Always updated even if `mongodb-store-action-traces=false`.
  * account
  * permission
  * public_key


[block:api-header]
{
  "title": "Examples"
}
[/block]
The mongodb equivalent of `/v1/history/get_key_accounts` RPC API endpoint:

[block:code]
{
  "codes": [
    {
      "code": "db.pub_keys.find({\"public_key\":\"EOS7EarnUhcyYqmdnPon8rm7mBCTnBoot6o7fE2WzjvEX2TdggbL3\"}).pretty()",
      "language": "javascript"
    }
  ]
}
[/block]