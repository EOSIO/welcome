---
title: "Monitoring Transactions"
excerpt: ""
---
[block:callout]
{
  "type": "info",
  "body": "This article assumes you have installed the EOSIO software and are familiar with using the EOSIO nodeos and cleos tools. It is recommended that you have completed [the Getting Started section](https://developers.eos.io/eosio-home/docs)"
}
[/block]
# Introduction

This tutorial is a guide for monitoring the status of transactions on the blockchain, 

As an example we will show how an application can monitor EOS transfers, show how a transaction state changes, how this affects the blockchain, and showing when a transaction is irreversible. The example will show the transfer of tokens using  standard-conforming EOSIO token contracts. The EOSIO blockchain's native token (eosio.token) conforms to this standard. 

In this we will discuss using the state history plugin to monitor transaction activity.

In part II we will discuss other means by which this activity can be monitored

# Running Nodeos

It is recommended that a local instance of nodeos is used to monitor activity. This will connect to the blockchain and when run with the state history plugin collect the history of actions on the blockchain. 
  
[block:callout]
{
  "type": "info",
  "body": "This will be run as a non-producing node see [Non-Producing Node](https://developers.eos.io/eosio-nodeos/docs/environment-non-producing-node) for more details."
}
[/block]
Nodeos can be run in three modes:

- **speculative** In "speculative" mode database contains changes done up to the head block plus changes made by transactions not yet included to the blockchain.
- **head** In "head" mode database contains changes done up to the current head  block.
- **read only** In "read-only" mode database contains incoming block changes but no speculative transaction processing.

The default mode is speculative.

For more information see [Read Modes](https://developers.eos.io/eosio-nodeos/docs/read-modes)
[block:callout]
{
  "type": "warning",
  "title": "",
  "body": "A transaction is only complete once it has a status of executed and the block containing the transaction is irreversible."
}
[/block]
 ## Transaction States

Transaction can have the following states:

- **executed**. Transaction has succeeded, no error handler executed
- **soft_fail**. Transaction has objectively failed (not executed), error handler executed (onerror)
- **hard_fail**. Transaction has objectively failed and error handler objectively failed thus no state change (onerror also failed)
- **delayed**. Transaction is delayed/deferred/scheduled for future execution
- **expired**. Transaction is expired and storage space refunded to user

A transaction is not executed until the status is executed, and the transaction can be cancelled up until it is executed, failed or expired, i.e. while it is waiting to be executed.

Transactions can be delayed for up to 45 days and the delay can be set when the transaction is generated. A delayed transaction can be cancelled.
[block:callout]
{
  "type": "warning",
  "body": "A transaction may be executed, but only when the block containing the transaction is irreversible can you be sure that the operation is final and complete. A block is irreversible if the block number is less than the block number of the last irreversible block (LIB). The The last irreversible block (LIB) is the most recent block which has been acknowledged by 2/3 of the block producers."
}
[/block]
## Tracking YOUR transaction

It is always possible that transactions \similar to your transactions are processed while you are monitoring the public main net. It is important to ensure that you use ALL identifying fields to make sure you are looking at the right transaction. 

Some of the fields you could use are: transaction_id, account, name, data, to, receiver, memo, transaction_id. See the example below for more details about postgresql tables.

## Ensuring a Transaction is complete and final

Once the block containing a transaction has a `"block_num" < "last_irreversible_block"`. then the transaction is also irreversible.

Once the last irreversible block has moved past the expiration time of a transaction, you can safely mark a transaction as failed and not worry about it "floating around the ether" to be applied when you least expect.

## Monitoring Options

Now we understand the various states that a transaction can be in, and how this relates to blockchain and the last irreversible block (LIB) we can look at the various options for monitoring transactions and their current state. In this guide we will use the state history plugin and the fill-postgresql connector.
[block:callout]
{
  "type": "info",
  "body": "Nodeos can be run with various plugins which can assist with this. These include plugins developed by the community which can be added to Nodeos by compiling Nodeos with those plugins included. More details about how to do this are available will be available in part II. This information comes from eos/plugins/COMMUNITY.md\n\n| Description | URL |\n| ----------- | --- |\n| BP Heartbeat  | https://github.com/bancorprotocol/eos-producer-heartbeat-plugin |\n| ElasticSearch | https://github.com/EOSLaoMao/elasticsearch_plugin |\n| Kafka | https://github.com/TP-Lab/kafka_plugin |\n| MySQL | https://github.com/eosBLACK/eosio_mysqldb_plugin |\n| SQL | https://github.com/asiniscalchi/eosio_sql_plugin |\n| Watch for specific actions and send them to an HTTP URL | https://github.com/eosauthority/eosio-watcher-plugin |\n| ZMQ / history | https://github.com/cc32d9/eos_zmq_plugin |\n| ZMQ Light History API | https://github.com/cc32d9/eos_zmq_light_api |\n| Chintai ZMQ Watcher | https://github.com/acoutts/chintai-zeromq-watcher-plugin |\n| Mongo History API | https://github.com/CryptoLions/EOS-mongo-history-API |\n| State History API | https://github.com/acoutts/EOS-state-history-API |\n\nOther options include:\n\n| Description | URL |\n| ----------- | --- |\n| dfuse | https://www.dfuse.io/en/technology |\n| rabbitmq | https://github.com/LiquidEOS/eos-rabbitmq-plugin |\n\n\n## DISCLAIMER:\n\nThe fact that an item is listed above does not mean the item has been reviewed by block.one.  No warranties are made, i.e. you are at your own risk if you choose to use them."
}
[/block]

[block:api-header]
{
  "title": "State History Plugin"
}
[/block]
The state history plugin replaces the deprecated History Plugin. It caches data in file, rather than memory, reducing running costs. 

To use the state history plugin run nodeos with the "--plugin eosio::state_history_plugin" option.
[block:code]
{
  "codes": [
    {
      "code": "nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::state_history_plugin --data-dir /Users/mydir/eosio/data --config-dir /Users/mydir/eosio//config --access-control-allow-origin='*' --contracts-console --http-validate-host=false --state-history-dir shp --trace-history --chain-state-history --verbose-http-errors --filter-on='*' --disable-replay-opts >> nodeos.log 2>&1 &",
      "language": "shell"
    }
  ]
}
[/block]
The nodeos command above adds the state history plugin ``--plugin eosio::state_history_plugin`` storing the chain data in a directory called shp under the --data-dir   ``--state-history-dir shp ``storing both trace history and chain-state-history ``--trace-history --chain-state-history``. To run the state history plugin you are required to ``--disable-replay-opts ``.

Once nodeos is running the state history plugin, you need to run fill-postgresql (or an alternative connector) to store the chain data in a postgresql database for querying.

[block:callout]
{
  "type": "info",
  "body": "This assumes you have installed postgesql and have some knowledge of how to use psql"
}
[/block]
##  fill-postgresql

See [fill-postgresql repo] (https://github.com/EOSIO/fill-postgresql)

Configuration options:

| Option | Default | Description |
| ------ | ------ | 
| --host | localhost | state-history-plugin host to connect to |
| --port | 8080 | state-history-plugin port to connect to |
| --schema | chain | Database schema to fill |
| --trim |   | Trim history before irreversible

When running it for the first time, use the --create option to create the schema and tables.
[block:code]
{
  "codes": [
    {
      "code": "./fill-postgresql --create",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HK000114:build philip.halsall$ ./fill-postgresql --create\ninfo  2019-01-22T06:25:43.039 thread-0  main.cpp:84                   main                 ] fill-postgresql version not-a-release-1-gaf49f6d\ninfo  2019-01-22T06:25:43.039 thread-0  main.cpp:85                   main                 ] fill-postgresql using configuration file /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/config/config.ini\ninfo  2019-01-22T06:25:43.039 thread-0  main.cpp:86                   main                 ] fill-postgresql data directory is /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/data\ninfo  2019-01-22T06:25:43.039 thread-0  fill_postgresql_plugin:748    session              ] connect to postgresql\ninfo  2019-01-22T06:25:43.044 thread-0  fill_postgresql_plugin:762    start                ] connect to localhost:8080\ninfo  2019-01-22T06:25:43.053 thread-0  fill_postgresql_plugin:870    create_tables        ] create schema \"chain\"\ninfo  2019-01-22T06:25:43.294 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 1 - 199\ninfo  2019-01-22T06:25:43.424 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 200 - 399\ninfo  2019-01-22T06:25:43.502 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 400 - 478\ninfo  2019-01-22T06:25:43.502 thread-0  fill_postgresql_plugin:1148   receive_result       ] block 479\n",
      "language": "text"
    }
  ]
}
[/block]
To wipe the schema and start over, run with --drop --create.
[block:code]
{
  "codes": [
    {
      "code": "./fill-postgresql --drop --create",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HK000114:build philip.halsall$ ./fill-postgresql --drop --create\ninfo  2019-01-24T09:48:04.324 thread-0  main.cpp:84                   main                 ] fill-postgresql version not-a-release-1-gaf49f6d\ninfo  2019-01-24T09:48:04.324 thread-0  main.cpp:85                   main                 ] fill-postgresql using configuration file /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/config/config.ini\ninfo  2019-01-24T09:48:04.324 thread-0  main.cpp:86                   main                 ] fill-postgresql data directory is /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/data\ninfo  2019-01-24T09:48:04.325 thread-0  fill_postgresql_plugin:748    session              ] connect to postgresql\ninfo  2019-01-24T09:48:04.332 thread-0  fill_postgresql_plugin:757    start                ] drop schema \"chain\"\ninfo  2019-01-24T09:48:04.416 thread-0  fill_postgresql_plugin:762    start                ] connect to localhost:8080\ninfo  2019-01-24T09:48:04.425 thread-0  fill_postgresql_plugin:870    create_tables        ] create schema \"chain\"\ninfo  2019-01-24T09:48:04.654 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 1 - 199\ninfo  2019-01-24T09:48:04.785 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 200 - 399\ninfo  2019-01-24T09:48:04.917 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 400 - 599\ninfo  2019-01-24T09:48:05.063 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 600 - 799\n",
      "language": "text"
    }
  ]
}
[/block]
To run normally
[block:code]
{
  "codes": [
    {
      "code": "./fill-postgresql",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "HK000114:build philip.halsall$ ./fill-postgresql\ninfo  2019-01-24T09:48:48.664 thread-0  main.cpp:84                   main                 ] fill-postgresql version not-a-release-1-gaf49f6d\ninfo  2019-01-24T09:48:48.664 thread-0  main.cpp:85                   main                 ] fill-postgresql using configuration file /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/config/config.ini\ninfo  2019-01-24T09:48:48.664 thread-0  main.cpp:86                   main                 ] fill-postgresql data directory is /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/data\ninfo  2019-01-24T09:48:48.664 thread-0  fill_postgresql_plugin:748    session              ] connect to postgresql\ninfo  2019-01-24T09:48:48.675 thread-0  fill_postgresql_plugin:762    start                ] connect to localhost:8080\ninfo  2019-01-24T09:48:48.831 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 4200 - 4399\ninfo  2019-01-24T09:48:48.967 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 4400 - 4599\ninfo  2019-01-24T09:48:49.099 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 4600 - 4799\ninfo  2019-01-24T09:48:49.231 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 4800 - 4999\ninfo  2019-01-24T09:48:49.361 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 5000 - 5199\n",
      "language": "text"
    }
  ]
}
[/block]
This connects to the State History Plugin and populates a Postgresql database with historical data such as action traces, transaction traces, block states, and other interesting things such as contract table changes at every block.  It will track real-time updates from nodeos.

## Postgres queries, tables and results

To identify the Last Irreversible Block
[block:code]
{
  "codes": [
    {
      "code": "eos=> select head, irreversible from chain.fill_status;\n\n\n  head  | irreversible \n--------+--------------\n 134112 |       134111\n(1 row)",
      "language": "sql"
    }
  ]
}
[/block]


[block:api-header]
{
  "title": "Examples"
}
[/block]
### Prerequisites

It is assumed that you have a local `nodeos` server connected to an EOSIO blockchain; that this nodeos is using the state history plugin; that an account has been created for `eosio.token`; and that the `eosio.token` contract has been deployed.  Completing the [Deploy, Issue, and Transfer Tokens](token-contract) in the 'Getting Started' section prior to this tutorial will have satisfied these prerequisites.

This tutorial uses the transfer action of the `eosio.token` contract. This could be considered as a deposit in one account and a withdrawal in another account.

Transfer  A to B
[block:code]
{
  "codes": [
    {
      "code": "cleos -u http://127.0.0.1:8889/ push action eosio.token issue '[ \"alice\", \"100.0000 SYS\", \"memo\" ]' -p eosio@active",
      "language": "shell"
    }
  ]
}
[/block]
Transfer  A to B results in chain.action_trace 
[block:code]
{
  "codes": [
    {
      "code": "select block_index, transaction_id, action_index, parent_action_index, transaction_status, receipt_receiver, receipt_global_sequence, account, name  from  chain.action_trace where transaction_id = UPPER('ba42b4b6c7a41e58c29a7cd90bb3dc3b554d2ce8ed9733dcf16bf80ad1d729ff');\n\n\n\n block_index |                          transaction_id                          | action_index | parent_action_index | transaction_status | receipt_receiver | receipt_global_sequence |   account   |   name   \n-------------+------------------------------------------------------------------+--------------+---------------------+--------------------+------------------+-------------------------+-------------+----------\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            1 |                   0 | executed           | eosio.token      |                    2877 | eosio.token | transfer\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            2 |                   1 | executed           | alice            |                    2878 | eosio.token | transfer\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            3 |                   1 | executed           | bob              |                    2879 | eosio.token | transfer\n(3 rows)\n",
      "language": "sql"
    }
  ]
}
[/block]
Transfer  A to B results in chain.transaction_trace
[block:code]
{
  "codes": [
    {
      "code": "select block_index, transaction_id, status from chain.transaction_trace where transaction_id = UPPER('ba42b4b6c7a41e58c29a7cd90bb3dc3b554d2ce8ed9733dcf16bf80ad1d729ff');\n\n\n\n block_index |                          transaction_id                          |  status  \n-------------+------------------------------------------------------------------+----------\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF | executed\n",
      "language": "text"
    }
  ]
}
[/block]
Transfer  A to B results in chain.action_trace_auth_sequence
[block:code]
{
  "codes": [
    {
      "code": "select * from chain.action_trace_auth_sequence where transaction_id = UPPER('ba42b4b6c7a41e58c29a7cd90bb3dc3b554d2ce8ed9733dcf16bf80ad1d729ff');\n\n\n\n block_index |                          transaction_id                          | action_index | index | transaction_status | account | sequence \n-------------+------------------------------------------------------------------+--------------+-------+--------------------+---------+----------\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            2 |     1 | executed           | alice   |        5\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            3 |     1 | executed           | alice   |        6\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            1 |     1 | executed           | alice   |        4\n(3 rows)\n",
      "language": "text"
    }
  ]
}
[/block]
Transfer  A to B results in chain.action_trace_authorization
[block:code]
{
  "codes": [
    {
      "code": "select * from chain.action_trace_authorization where transaction_id = UPPER('ba42b4b6c7a41e58c29a7cd90bb3dc3b554d2ce8ed9733dcf16bf80ad1d729ff');\n\n\n block_index |                          transaction_id                          | action_index | index | transaction_status | actor | permission \n-------------+------------------------------------------------------------------+--------------+-------+--------------------+-------+------------\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            2 |     1 | executed           | alice | active\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            3 |     1 | executed           | alice | active\n        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            1 |     1 | executed           | alice | active\n(3 rows)\n",
      "language": "text"
    }
  ]
}
[/block]

Transfer  A to B delayed
Transfer  A to B deferred
Transfer  A to B expired
Transfer  A to B failed

## Handling Errors

Sometimes network issues will cause a transaction to fail and never be included in a block. Your internal database will need to know when this has happened so that it can inform the user and/or try again. If you do not get an immediate error when you submit your local transfer, then you must wait for the transaction to expire. Every transaction has an "expiration", after which the transaction can never be applied. Once the last irreversible block has moved past the expiration time, you can safely mark your attempted withdrawal as failed and not worry about it "floating around the ether" to be applied when you least expect.