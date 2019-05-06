To run a local node connected to a public testnet, a script is provided.

```shell
cd ~/eos/build/scripts
./start_npnode.sh
```
This command will use the data folder provided for the instance called `testnet_np`.

You should see the following response:

```shell
Launched eosd.
See testnet_np/stderr.txt for eosd output.
Synching requires at least 8 minutes, depending on network conditions.
```
To confirm eosd operation and synchronization:

```shell
tail -F testnet_np/stderr.txt
```
To exit tail, use Ctrl-C.  During synchronization, you will see log messages similar to:

```shell
3439731ms            chain_plugin.cpp:272          accept_block         ] Syncing Blockchain --- Got block: #200000 time: 2017-12-09T07:56:32 producer: initu
3454532ms            chain_plugin.cpp:272          accept_block         ] Syncing Blockchain --- Got block: #210000 time: 2017-12-09T13:29:52 producer: initc
```
Synchronization is complete when you see log messages similar to:

```shell
42467ms            net_plugin.cpp:1245           start_sync           ] Catching up with chain, our last req is 351734, theirs is 351962 peer ip-10-160-11-116:9876
42792ms            chain_controller.cpp:208      _push_block          ] initt #351947 @2017-12-12T22:59:44  | 0 trx, 0 pending, exectime_ms=0
42793ms            chain_controller.cpp:208      _push_block          ] inito #351948 @2017-12-12T22:59:46  | 0 trx, 0 pending, exectime_ms=0
42793ms            chain_controller.cpp:208      _push_block          ] initd #351949 @2017-12-12T22:59:48  | 0 trx, 0 pending, exectime_ms=0
```
This eosd instance listens on 127.0.0.1:8888 for http requests, on all interfaces at port 9877
for p2p requests, and includes the wallet plugins.
