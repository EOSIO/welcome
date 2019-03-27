---
title: "Benchmarking"
excerpt: ""
---
[block:html]
{
  "html": "<div style=\"padding:57.42% 0 0 0;position:relative;\"><iframe src=\"https://player.vimeo.com/video/266585781\" style=\"position:absolute;top:0;left:0;width:100%;height:100%;\" frameborder=\"0\" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div><script src=\"https://player.vimeo.com/api/player.js\"></script>"
}
[/block]

[block:api-header]
{
  "title": "Step 1: Install and Run htop"
}
[/block]
We want to see how our node is performing during block production.

If you do not have htop, install it now
[block:code]
{
  "codes": [
    {
      "code": "# Debian/Ubunutu\n$ apt-get install htop\n# CentOS\n$ yum install htop",
      "language": "text"
    }
  ]
}
[/block]
Now run `htop` to view your system's load. 
[block:code]
{
  "codes": [
    {
      "code": "$ htop",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 2: Open 4 Terminal Windows"
}
[/block]
We want to see everything that's going on at once. If you're using a terminal that supports panels, create 4 panels, otherwise, make all your terminal windows visible. 
[block:api-header]
{
  "title": "Step 3: Create a Data Directory"
}
[/block]
Create a directory for our nodes' data. 
[block:code]
{
  "codes": [
    {
      "code": "$ mkdir eos.data\n$ cd eos.data",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 4: Turn off Debug Logs"
}
[/block]
The logs can slow the performance of a node, turn turn it off, we write a configuration for the debugger that effectively turns off the debugging. 
[block:code]
{
  "codes": [
    {
      "code": "cat << EOF > ~/eos.data/logging.json",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 5: Start Nodes"
}
[/block]
## Configure and Start Producer Node
Open one of you unused terminal windows and run the following
[block:code]
{
  "codes": [
    {
      "code": "$ nodeos -s ~/eos.data/producer_node \\\n--config-dir ~/eos.data/producer_node -1 ~/eos.data/logging.json \\\n--http-server-address \"\" \\\n-p eosio -e",
      "language": "text"
    }
  ]
}
[/block]
## Generating Node
Open a new terminal window and run the following
[block:code]
{
  "codes": [
    {
      "code": "nodeos -d ~/eos.data/generator_node \\\n--config-dir ~/eos.data/generator_node -1\n~/eos.data/logging.json \\ \n--plugin eosio::txn_test_gen_plugin \\\n--plugin eosio::wallet_api_plugin \\\n--plugin eosio::chain_api_plugin \\\n--p2p-peer-address localhost:9876 \\\n--p2p-listen-endpoint localhost:5555",
      "language": "text"
    }
  ]
}
[/block]
`-d, --data-dir` New data directory
`--config-dir` New config directory
`logging.json` from last step to turn off debugging
`--plugin eosio::txn_test_gen_plugin` Plugin that generates transactions for this test. 
`--plugin eosio::wallet_api_plugin` Needed to upload EOS Bios
`--plugin eosio::chain_api_plugin` Needed to upload EOS Bios
`p2p-peer-address` Point to the node that's already running, so they can comuinicater. 
`--p2p-listen-endpoint ` To avoid port collisions, assign new listener port

Non-producing node is consuming blocks coming from the producing node. 

[block:api-header]
{
  "title": "Step 6: Create a wallet on non-producing node"
}
[/block]
The wallet by default will have the private key for **@eosio** root account, provided this was not changed in the genesis.
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet create\n$ cleos keys import EOSIO_PRIVATE_KEY",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 7: Set the the bios contract"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos set contract eosio ~/eos/build.release/contracts/eosio.bios",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 8: Create the generator accounts"
}
[/block]
Using the `eosio_txn_generator_plugin`. One of the first things we need to do is initialize the various accounts that the `eosio_txn_generator_plugin` uses. Cleos doesn't have a helper command for this plugin. So we're going to do it a little dirty

[block:code]
{
  "codes": [
    {
      "code": "curl --data-binary '[\"eosio\", \"PASSWORD YOU GENERATED EARLIER\"]' http://localhost:8888/v1/txn_test_gen/create_test_accounts",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 9: Start generating transactions."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --data-binary '[\"\", 20, 20]' http://localhost:8888/v1/txn_test_gen/start_generation",
      "language": "text"
    }
  ]
}
[/block]