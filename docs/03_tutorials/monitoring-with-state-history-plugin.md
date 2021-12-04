In part I [How to monitor state](doc:how-to-monitor-state) we discussed the states of a transaction. In this article we will take a look at monitoring state using the state history plugin.

## State History Plugin
The state history plugin replaces the deprecated History Plugin. It caches data in file, rather than in memory, reducing the running costs of node.

To use the state history plugin run nodeos with the "--plugin eosio::state_history_plugin" option. See the [state_history_plugin](doc:state_history_plugin) 
```shell
nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::state_history_plugin --data-dir /Users/mydir/eosio/data --config-dir /Users/mydir/eosio/config --access-control-allow-origin='*' --contracts-console --http-validate-host=false --state-history-dir /shpdata --trace-history --chain-state-history --verbose-http-errors --filter-on='*' --disable-replay-opts >> nodeos.log 2>&1 &
```
The nodeos command above adds the state history plugin ``--plugin eosio::state_history_plugin`` storing the chain data in a directory called /shpdata under the --data-dir ``--state-history-dir /shpdata`` storing both trace history and chain-state-history ``--trace-history --chain-state-history``. To run the state history plugin you are required to ``--disable-replay-opts ``.

Once nodeos is running the state history plugin, you need to run fill-postgresql (or an alternative connector) to store the chain data in a postgresql database for querying.
[[warning]]
|postgresql is Required
This assumes you have installed [postgesql](https://www.postgresql.org/download/) and have some knowledge of how to use psql
##  fill-postgresql

See [fill-postgresql repo](https://github.com/EOSIO/fill-postgresql)

Configuration options:

| Option | Default | Description |
| ------ | ------ | 
| --host | localhost | state-history-plugin host to connect to |
| --port | 8080 | state-history-plugin port to connect to |
| --schema | chain | Database schema to fill |
| --trim |   | Trim history before irreversible

When running it for the first time, use the --create option to create the schema and tables.
```shell
./fill-postgresql --create
```

```text
$ ./fill-postgresql --create
info  2019-01-22T06:25:43.039 thread-0  main.cpp:84                   main                 ] fill-postgresql version not-a-release-1-gaf49f6d
info  2019-01-22T06:25:43.039 thread-0  main.cpp:85                   main                 ] fill-postgresql using configuration file /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/config/config.ini
info  2019-01-22T06:25:43.039 thread-0  main.cpp:86                   main                 ] fill-postgresql data directory is /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/data
info  2019-01-22T06:25:43.039 thread-0  fill_postgresql_plugin:748    session              ] connect to postgresql
info  2019-01-22T06:25:43.044 thread-0  fill_postgresql_plugin:762    start                ] connect to localhost:8080
info  2019-01-22T06:25:43.053 thread-0  fill_postgresql_plugin:870    create_tables        ] create schema "chain"
info  2019-01-22T06:25:43.294 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 1 - 199
info  2019-01-22T06:25:43.424 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 200 - 399
info  2019-01-22T06:25:43.502 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 400 - 478
info  2019-01-22T06:25:43.502 thread-0  fill_postgresql_plugin:1148   receive_result       ] block 479

```
To wipe the schema and start over, run with --drop --create.
```shell
./fill-postgresql --drop --create
```

```text
$ ./fill-postgresql --drop --create
info  2019-01-24T09:48:04.324 thread-0  main.cpp:84                   main                 ] fill-postgresql version not-a-release-1-gaf49f6d
info  2019-01-24T09:48:04.324 thread-0  main.cpp:85                   main                 ] fill-postgresql using configuration file /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/config/config.ini
info  2019-01-24T09:48:04.324 thread-0  main.cpp:86                   main                 ] fill-postgresql data directory is /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/data
info  2019-01-24T09:48:04.325 thread-0  fill_postgresql_plugin:748    session              ] connect to postgresql
info  2019-01-24T09:48:04.332 thread-0  fill_postgresql_plugin:757    start                ] drop schema "chain"
info  2019-01-24T09:48:04.416 thread-0  fill_postgresql_plugin:762    start                ] connect to localhost:8080
info  2019-01-24T09:48:04.425 thread-0  fill_postgresql_plugin:870    create_tables        ] create schema "chain"
info  2019-01-24T09:48:04.654 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 1 - 199
info  2019-01-24T09:48:04.785 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 200 - 399
info  2019-01-24T09:48:04.917 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 400 - 599
info  2019-01-24T09:48:05.063 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 600 - 799

```
To run normally
```shell
./fill-postgresql
```

```text
$ ./fill-postgresql
info  2019-01-24T09:48:48.664 thread-0  main.cpp:84                   main                 ] fill-postgresql version not-a-release-1-gaf49f6d
info  2019-01-24T09:48:48.664 thread-0  main.cpp:85                   main                 ] fill-postgresql using configuration file /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/config/config.ini
info  2019-01-24T09:48:48.664 thread-0  main.cpp:86                   main                 ] fill-postgresql data directory is /Users/philip.halsall/Library/Application Support/eosio/fill-postgresql/data
info  2019-01-24T09:48:48.664 thread-0  fill_postgresql_plugin:748    session              ] connect to postgresql
info  2019-01-24T09:48:48.675 thread-0  fill_postgresql_plugin:762    start                ] connect to localhost:8080
info  2019-01-24T09:48:48.831 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 4200 - 4399
info  2019-01-24T09:48:48.967 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 4400 - 4599
info  2019-01-24T09:48:49.099 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 4600 - 4799
info  2019-01-24T09:48:49.231 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 4800 - 4999
info  2019-01-24T09:48:49.361 thread-0  fill_postgresql_plugin:1207   close_streams        ] block 5000 - 5199

```
This connects to the State History Plugin and populates a Postgresql database with historical data such as action traces, transaction traces, block states, and other interesting things such as contract table changes at every block.  It will track real-time updates from nodeos.

## Postgres queries, tables and results

To identify the Last Irreversible Block
```sql
eos=> select head, irreversible from chain.fill_status;


  head  | irreversible 
--------+--------------
 134112 |       134111
(1 row)
```

## Examples
### Prerequisites

It is assumed that you have a local `nodeos` server connected to an EOSIO blockchain; that this nodeos is using the state history plugin; that an account has been created for `eosio.token`; and that the `eosio.token` contract has been deployed.  Completing the [Deploy, Issue, and Transfer Tokens](https://developers.eos.io/eosio-home/docs/token-contract) in the 'Getting Started' section prior to this tutorial will have satisfied these prerequisites.

This tutorial uses the transfer action of the `eosio.token` contract. This could be considered as a deposit in one account and a withdrawal in another account.

Transfer A to B
```shell
cleos -u http://127.0.0.1:8889/ push action eosio.token issue '[ "alice", "100.0000 SYS", "memo" ]' -p eosio@active
```
Transfer A to B results in chain.action_trace 
```sql
select block_index, transaction_id, action_index, parent_action_index, transaction_status, receipt_receiver, receipt_global_sequence, account, name  from  chain.action_trace where transaction_id = UPPER('ba42b4b6c7a41e58c29a7cd90bb3dc3b554d2ce8ed9733dcf16bf80ad1d729ff');



 block_index |                          transaction_id                          | action_index | parent_action_index | transaction_status | receipt_receiver | receipt_global_sequence |   account   |   name   
-------------+------------------------------------------------------------------+--------------+---------------------+--------------------+------------------+-------------------------+-------------+----------
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            1 |                   0 | executed           | eosio.token      |                    2877 | eosio.token | transfer
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            2 |                   1 | executed           | alice            |                    2878 | eosio.token | transfer
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            3 |                   1 | executed           | bob              |                    2879 | eosio.token | transfer
(3 rows)

```
Transfer A to B also results in chain.transaction_trace

```sql
select block_index, transaction_id, status from chain.transaction_trace where transaction_id = UPPER('ba42b4b6c7a41e58c29a7cd90bb3dc3b554d2ce8ed9733dcf16bf80ad1d729ff');



 block_index |                          transaction_id                          |  status  
-------------+------------------------------------------------------------------+----------
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF | executed

```
Transfer A to B also results in chain.action_trace_auth_sequence
```sql
select * from chain.action_trace_auth_sequence where transaction_id = UPPER('ba42b4b6c7a41e58c29a7cd90bb3dc3b554d2ce8ed9733dcf16bf80ad1d729ff');



 block_index |                          transaction_id                          | action_index | index | transaction_status | account | sequence 
-------------+------------------------------------------------------------------+--------------+-------+--------------------+---------+----------
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            2 |     1 | executed           | alice   |        5
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            3 |     1 | executed           | alice   |        6
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            1 |     1 | executed           | alice   |        4
(3 rows)

```
Transfer A to B also results in chain.action_trace_authorization
```sql
select * from chain.action_trace_authorization where transaction_id = UPPER('ba42b4b6c7a41e58c29a7cd90bb3dc3b554d2ce8ed9733dcf16bf80ad1d729ff');


 block_index |                          transaction_id                          | action_index | index | transaction_status | actor | permission 
-------------+------------------------------------------------------------------+--------------+-------+--------------------+-------+------------
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            2 |     1 | executed           | alice | active
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            3 |     1 | executed           | alice | active
        2864 | BA42B4B6C7A41E58C29A7CD90BB3DC3B554D2CE8ED9733DCF16BF80AD1D729FF |            1 |     1 | executed           | alice | active
(3 rows)

```

# Alternatives

[Demux](https://github.com/EOSIO/demux-js) is an alternative that piggybacks off the RPC API.

In part III [Monitoring with 3rd Party plugins](doc:monitoring-with-3rd-party) we will discuss 3rd party plugins which may also be used for monitoring state.