[[info]]
| Looking for the version of this series that uses [Docker](https://developers.eos.io/eosio-home/v1.7.0/docs/introduction)?

## Step 1: Boot Node and Wallet
## Step 1.1: Start keosd
First let us start keosd: 

```shell
keosd &
```
You should see some output that looks like this:

```text
info  2018-11-26T06:54:24.789 thread-0  wallet_plugin.cpp:42          plugin_initialize    ] initializing wallet plugin
info  2018-11-26T06:54:24.795 thread-0  http_plugin.cpp:554           add_handler          ] add api url: /v1/keosd/stop
info  2018-11-26T06:54:24.796 thread-0  wallet_api_plugin.cpp:73      plugin_startup       ] starting wallet_api_plugin
info  2018-11-26T06:54:24.796 thread-0  http_plugin.cpp:554           add_handler          ] add api url: /v1/wallet/create
info  2018-11-26T06:54:24.796 thread-0  http_plugin.cpp:554           add_handler          ] add api url: /v1/wallet/create_key
info  2018-11-26T06:54:24.796 thread-0  http_plugin.cpp:554           add_handler          ] add api url: /v1/wallet/get_public_keys
```
Press enter to continue
## Step 1.2: Start nodeos
Start nodeos now:

```shell
nodeos -e -p eosio \
--plugin eosio::producer_plugin \
--plugin eosio::chain_api_plugin \
--plugin eosio::http_plugin \
--plugin eosio::history_plugin \
--plugin eosio::history_api_plugin \
--filter-on="*" \
--access-control-allow-origin='*' \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors >> nodeos.log 2>&1 &
```
These settings accomplish the following:

1. Run **Nodeos. This** command loads all the basic plugins, set the server address, enable CORS and add some contract debugging and logging. 

2. Enable CORS with no restrictions (*) and development logging 


[[warning]]
| In the above configuration, CORS is enabled for `*` **for development purposes only**, you should **never** enable CORS for `*` on a node that is publicly accessible!

## Step 2: Check the installation
## Step 2.1: Check that Nodeos is Producing Blocks

Run the following command

```shell
tail -f nodeos.log
```
You should see some output in the console that looks like this:

```text
1929001ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366974ce4e2a... #13929 @ 2018-05-23T16:32:09.000 signed by eosio [trxs: 0, lib: 13928, confirmed: 0]
1929502ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366aea085023... #13930 @ 2018-05-23T16:32:09.500 signed by eosio [trxs: 0, lib: 13929, confirmed: 0]
1930002ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366b7f074fdd... #13931 @ 2018-05-23T16:32:10.000 signed by eosio [trxs: 0, lib: 13930, confirmed: 0]
1930501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366cd8222adb... #13932 @ 2018-05-23T16:32:10.500 signed by eosio [trxs: 0, lib: 13931, confirmed: 0]
1931002ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366d5c1ec38d... #13933 @ 2018-05-23T16:32:11.000 signed by eosio [trxs: 0, lib: 13932, confirmed: 0]
1931501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366e45c1f235... #13934 @ 2018-05-23T16:32:11.500 signed by eosio [trxs: 0, lib: 13933, confirmed: 0]
1932001ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366f98adb324... #13935 @ 2018-05-23T16:32:12.000 signed by eosio [trxs: 0, lib: 13934, confirmed: 0]
1932501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 00003670a0f01daa... #13936 @ 2018-05-23T16:32:12.500 signed by eosio [trxs: 0, lib: 13935, confirmed: 0]
1933001ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 00003671e8b36e1e... #13937 @ 2018-05-23T16:32:13.000 signed by eosio [trxs: 0, lib: 13936, confirmed: 0]
1933501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000367257fe1623... #13938 @ 2018-05-23T16:32:13.500 signed by eosio [trxs: 0, lib: 13937, confirmed: 0]
```
Press `ctrl + c` to close the log

## Step 2.2: Check the Wallet

Open the shell and run the cleos command to list available wallets. We will talk more about wallets in the future. For now, we need to validate the installation and see that the command line client 
[cleos](https://developers.eos.io/eosio-cleos/docs) is working as intended.


```shell
cleos wallet list
```
You should see a response with an empty list of wallets:

```
Wallets:
[]
```

From this point forward, you'll be executing commands from your local system (Linux or Mac) 

## Step 2.3: Check Nodeos endpoints

This will check that the RPC API is working correctly, pick one. 

1. Check the `get_info` endpoint provided by the `chain_api_plugin` in your browser: [http://localhost:8888/v1/chain/get_info](http://localhost:8888/v1/chain/get_info)
2. Check the same thing, but in the console on your **host machine**

```shell
curl http://localhost:8888/v1/chain/get_info
```
