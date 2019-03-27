---
title: "Local Multi-Node Testnet"
excerpt: ""
---
This tutorial describes how to set up a multi-node blockchain configuration running on a single host.  This is referred to as a _**single host, multi-node testnet**_.  We will set up two nodes on your local computer and have them communicate with each other.  The examples in this section rely on three command-line applications, `nodeos`, `keosd`, and `cleos`.  The following diagram depicts the desired testnet configuration.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a190a39-Single-Host-Multi-Node-Testnet.png",
        "Single-Host-Multi-Node-Testnet.png",
        2700,
        983,
        "#f5f5f5"
      ]
    }
  ]
}
[/block]
It is assumed that `keosd`, `cleos`, and `nodeos` have been installed in your path, or that you know how to start these applications from the location in the file system.  (See [Setting Up A Local Environment](Local-Environment))

Open four "terminal" windows to perform the steps in this tutorial.

### Start the Wallet Manager
In the first terminal window, start `keosd`, the wallet management application:
[block:code]
{
  "codes": [
    {
      "code": "keosd --http-server-address 127.0.0.1:8899",
      "language": "shell"
    }
  ]
}
[/block]
If successful, `keosd` will display some information, starting with:
[block:code]
{
  "codes": [
    {
      "code": "```\n2493323ms thread-0   wallet_plugin.cpp:39          plugin_initialize    ] initializing wallet plugin\n2493323ms thread-0   http_plugin.cpp:141           plugin_initialize    ] host: 127.0.0.1 port: 8899\n2493323ms thread-0   http_plugin.cpp:144           plugin_initialize    ] configured http to listen on 127.0.0.1:8899\n2493323ms thread-0   http_plugin.cpp:213           plugin_startup       ] start listening for http requests\n2493324ms thread-0   wallet_api_plugin.cpp:70      plugin_startup       ] starting wallet_api_plugin\n```",
      "language": "shell"
    }
  ]
}
[/block]
Look for a line saying the wallet is listening on 127.0.0.1:8899. This will indicate that `keosd` started correctly and is listening on the correct port. If you see anything else, or you see some error report prior to "starting wallet_api_plugin", then you need to diagnose the issue and restart.

When `keosd` is running correctly, leave that window open with the wallet app running and move to the next terminal window.

### Create a Default Wallet
In the next terminal window, use `cleos`, the command-line utility, to create the default wallet.
[block:code]
{
  "codes": [
    {
      "code": "cleos --wallet-url http://127.0.0.1:8899  wallet create --to-console",
      "language": "shell"
    }
  ]
}
[/block]
`cleos` will indicate that it created the "default" wallet, and will provide a password for future wallet access. As the message says, be sure to preserve this password for future use. Here is an example of this output:
[block:code]
{
  "codes": [
    {
      "code": "Creating wallet: default\nSave password to use in the future to unlock this wallet.\nWithout password imported keys will not be retrievable.\n\"PW5JsmfYz2wrdUEotTzBamUCAunAA8TeRZGT57Ce6PkvM12tre8Sm\"",
      "language": "shell"
    }
  ]
}
[/block]
`keosd` will generate some status output in its window. We will continue to use this second window for subsequent `cleos` commands.

### Loading the eosio Key

The private blockchain launched in the steps above is created with a default initial key which must be loaded into the wallet.

```
$ cleos --wallet-url http://127.0.0.1:8899 wallet import --private-key 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
imported private key for: EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
```

### Start the First Producer Node
We can now start the first producer node. In the third terminal window run:
[block:code]
{
  "codes": [
    {
      "code": "nodeos --enable-stale-production --producer-name eosio --plugin eosio::chain_api_plugin --plugin eosio::net_api_plugin",
      "language": "shell"
    }
  ]
}
[/block]
This creates a special producer, known as the "bios" producer. Assuming everything has executed correctly to this point, you should see output from the `nodeos` process reporting block creation.

### Start the Second Producer Node
The following commands assume that you are running this tutorial from your `${EOSIO_SOURCE}` directory, from which you ran `./eosio_build.sh` to build.  See [Getting the Code](Local-Environment#1-getting-the-code) for more information if this is not clear.

To start additional nodes, you must first load the `eosio.bios` contract. This contract enables you to have direct control over the resource allocation of other accounts and to access other privileged API calls. Return to the second terminal window and run the following command to load the contract:
[block:code]
{
  "codes": [
    {
      "code": "cleos --wallet-url http://127.0.0.1:8899 set contract eosio build/contracts/eosio.bios",
      "language": "shell"
    }
  ]
}
[/block]
We will create an account to become a producer, using the account name `inita`.  To create the account, we need to generate keys to associate with the account, and import those into our wallet.

Run the create key command:
[block:code]
{
  "codes": [
    {
      "code": "cleos create key",
      "language": "shell"
    }
  ]
}
[/block]
This will report newly generated public and private keypairs that will look similar to the following.

**IMPORTANT:  The command line instructions that follow use the keys shown below.  In order to be able to cut-and-paste the command line instructions directly from this tutorial, do NOT use the keys that you just generated.  If, instead, you want to use your newly generated keys, you will need to replace the key values with yours in the commands.**
[block:code]
{
  "codes": [
    {
      "code": "Private key: 5JgbL2ZnoEAhTudReWH1RnMuQS6DBeLZt4ucV6t8aymVEuYg7sr\nPublic key: EOS6hMjoWRF2L8x9YpeqtUEcsDKAyxSuM1APicxgRU1E3oyV5sDEg",
      "language": "shell"
    }
  ]
}
[/block]
Now import the private key portion into your wallet. If successful, the matching public key will be reported. This should match the previously generated public key:
[block:code]
{
  "codes": [
    {
      "code": "cleos --wallet-url http://127.0.0.1:8899 wallet import 5JgbL2ZnoEAhTudReWH1RnMuQS6DBeLZt4ucV6t8aymVEuYg7sr\nimported private key for: EOS6hMjoWRF2L8x9YpeqtUEcsDKAyxSuM1APicxgRU1E3oyV5sDEg",
      "language": "shell"
    }
  ]
}
[/block]
Create the `inita` account that we will use to become a producer. The `create account` command requires two public keys, one for the account's owner key and one for its active key.  In this example, the newly created public key is used twice, as both the owner key and the active key. Example output from the create command is shown:
[block:code]
{
  "codes": [
    {
      "code": "cleos --wallet-url http://127.0.0.1:8899 create account eosio inita EOS6hMjoWRF2L8x9YpeqtUEcsDKAyxSuM1APicxgRU1E3oyV5sDEg EOS6hMjoWRF2L8x9YpeqtUEcsDKAyxSuM1APicxgRU1E3oyV5sDEg\nexecuted transaction: d1ea511977803d2d88f46deb554f5b6cce355b9cc3174bec0da45fc16fe9d5f3  352 bytes  102400 cycles\n#         eosio <= eosio::newaccount            {\"creator\":\"eosio\",\"name\":\"inita\",\"owner\":{\"threshold\":1,\"keys\":[{\"key\":\"EOS6hMjoWRF2L8x9YpeqtUEcsDK...",
      "language": "shell"
    }
  ]
}
[/block]
We now have an account that is available to have a contract assigned to it, enabling it to do meaningful work. In other tutorials, the account has been used to establish simple contracts. In this case, the account will be designated as a block producer.

In the fourth terminal window, start a second `nodeos` instance. Notice that this command line is substantially longer than the one we used above to create the first producer. This is necessary to avoid collisions with the first `nodeos` instance. Fortunately, you can just cut and paste this command line and adjust the keys:
[block:code]
{
  "codes": [
    {
      "code": "nodeos --producer-name inita --plugin eosio::chain_api_plugin --plugin eosio::net_api_plugin --http-server-address 127.0.0.1:8889 --p2p-listen-endpoint 127.0.0.1:9877 --p2p-peer-address 127.0.0.1:9876 --config-dir node2 --data-dir node2 --private-key [\\\"EOS6hMjoWRF2L8x9YpeqtUEcsDKAyxSuM1APicxgRU1E3oyV5sDEg\\\",\\\"5JgbL2ZnoEAhTudReWH1RnMuQS6DBeLZt4ucV6t8aymVEuYg7sr\\\"]",
      "language": "shell"
    }
  ]
}
[/block]
The output from this new node will show a little activity but will stop reporting until the last step in this tutorial, when the `inita` account is registered as a producer account and activated. Here is some example output from a newly started node. Your output might look a little different, depending on how much time you took entering each of these commands. Furthermore, this example is only the last few lines of output:
[block:code]
{
  "codes": [
    {
      "code": "2393147ms thread-0   producer_plugin.cpp:176       plugin_startup       ] producer plugin:  plugin_startup() end\n2393157ms thread-0   net_plugin.cpp:1271           start_sync           ] Catching up with chain, our last req is 0, theirs is 8249 peer dhcp15.ociweb.com:9876 - 295f5fd\n2393158ms thread-0   chain_controller.cpp:1402     validate_block_heade ] head_block_time 2018-03-01T12:00:00.000, next_block 2018-04-05T22:31:08.500, block_interval 500\n2393158ms thread-0   chain_controller.cpp:1404     validate_block_heade ] Did not produce block within block_interval 500ms, took 3061868500ms)\n2393512ms thread-0   producer_plugin.cpp:241       block_production_loo ] Not producing block because production is disabled until we receive a recent block (see: --enable-stale-production)\n2395680ms thread-0   net_plugin.cpp:1385           recv_notice          ] sync_manager got last irreversible block notice\n2395680ms thread-0   net_plugin.cpp:1271           start_sync           ] Catching up with chain, our last req is 8248, theirs is 8255 peer dhcp15.ociweb.com:9876 - 295f5fd\n2396002ms thread-0   producer_plugin.cpp:226       block_production_loo ] Previous result occurred 5 times\n2396002ms thread-0   producer_plugin.cpp:244       block_production_loo ] Not producing block because it isn't my turn, its eosio",
      "language": "shell"
    }
  ]
}
[/block]
At this point, the second `nodeos` is an idle producer. To turn it into an active producer, `inita` needs to be registered as a producer with the bios node, and the bios node needs to perform an action to update the producer schedule.
[block:code]
{
  "codes": [
    {
      "code": "cleos --wallet-url http://127.0.0.1:8899 push action eosio setprods \"{ \\\"schedule\\\": [{\\\"producer_name\\\": \\\"inita\\\",\\\"block_signing_key\\\": \\\"EOS6hMjoWRF2L8x9YpeqtUEcsDKAyxSuM1APicxgRU1E3oyV5sDEg\\\"}]}\" -p eosio@active\nexecuted transaction: 2cff4d96814752aefaf9908a7650e867dab74af02253ae7d34672abb9c58235a  272 bytes  105472 cycles\n#         eosio <= eosio::setprods              {\"version\":1,\"producers\":[{\"producer_name\":\"inita\",\"block_signing_key\":\"EOS6hMjoWRF2L8x9YpeqtUEcsDKA...",
      "language": "shell"
    }
  ]
}
[/block]
Congratulations, you have now configured a two-node testnet! You can see that the original node is no longer producing blocks but it is receiving them. You can verify this by running the `get info` commmand against each node.

Get info about the first node:
[block:code]
{
  "codes": [
    {
      "code": "cleos get info",
      "language": "shell"
    }
  ]
}
[/block]
This should produce output that looks similar to this:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"server_version\": \"223565e8\",\n  \"head_block_num\": 11412,\n  \"last_irreversible_block_num\": 11411,\n  \"head_block_id\": \"00002c94daf7dff456cd940bd585c4d9b38e520e356d295d3531144329c8b6c3\",\n  \"head_block_time\": \"2018-04-06T00:06:14\",\n  \"head_block_producer\": \"inita\"\n}",
      "language": "json"
    }
  ]
}
[/block]
Now for the second node:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url http://127.0.0.1:8889 get info",
      "language": "shell"
    }
  ]
}
[/block]
This should produce output that looks similar to this:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"server_version\": \"223565e8\",\n  \"head_block_num\": 11438,\n  \"last_irreversible_block_num\": 11437,\n  \"head_block_id\": \"00002cae32697444fa9a2964e4db85b5e8fd4c8b51529a0c13e38587c1bf3c6f\",\n  \"head_block_time\": \"2018-04-06T00:06:27\",\n  \"head_block_producer\": \"inita\"\n}",
      "language": "json"
    }
  ]
}
[/block]
In a later tutorial we will explore how to use more advanced tools to run a multi-host, multi-node testnet.