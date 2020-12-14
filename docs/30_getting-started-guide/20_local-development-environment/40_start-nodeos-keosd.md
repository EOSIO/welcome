---
content_title: "Start keosd and nodeos"
link_text: "Start keosd and nodeos"
---

Once you have built your smart contract deploy it to a blockchain for testing. In this section we show you the commands for running [Nodeos](../../glossary/index#nodeos) and [Keosd.](../../glossary/index#keosd)   
    

### Starting keosd

To start keosd:

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

**Troubleshooting**

After entering `keosd &`, you may encounter this message:

```shell
"3120000 wallet_exception: Wallet exception Failed to lock access to wallet directory; is another keosd running?"
```

This is because another instance of `keosd` process might be running in the background. Kill all instances by `pkill keosd` and rerun `keosd &`.

### Starting nodeos

Start nodeos now:

```shell
nodeos -e -p eosio \
--plugin eosio::producer_plugin \
--plugin eosio::producer_api_plugin \
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

**Troubleshooting**

After starting `nodeos`, if you see an error message similar to "Database dirty flag set (likely due to unclean shutdown): replay required", try to start `nodeos` with  `--replay-blockchain`. More details on troubleshooting `nodeos` can be found [here](https://developers.eos.io/manuals/eos/latest/nodeos/troubleshooting/index).

## Validating Nodeos

### Check that Nodeos is Producing Blocks

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

### Check the Wallet

Open the shell and run the cleos command to list available wallets. We will talk more about wallets in the future. For now, we need to validate the installation and see that the command line client
[cleos](https://developers.eos.io/manuals/eos/latest/cleos) is working as intended.


```shell
cleos wallet list
```
You should see a response with an empty list of wallets:

```
Wallets:
[]
```

From this point forward, you'll be executing commands from your local system (Linux or Mac)

### Check Nodeos endpoints

This will check that the RPC API is working correctly, pick one.

1. Check the `get_info` endpoint provided by the `chain_api_plugin` in your browser by copy and pasting `http://localhost:8888/v1/chain/get_info` into your browser address bar.  
2. Check the same thing, but in the console on your **host machine**

```shell
curl http://localhost:8888/v1/chain/get_info
```

## What's Next?
[Create Development Accounts](50_create-dev-accounts.md): Steps to create new development accounts for smart contract deployment.

