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
You can view how your node is performing during block production using various methods.

A commonly used tool for performance monitoring is 'htop':
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
  "title": "Step 2: Split Panes / Multiple Terminal Windows"
}
[/block]
Split Panes within a terminal is commonly used to maximize the visibility of your node's performance. You can have one pane show htop performance (see above), and another within the same exact window showing a `tail -f` of the logs or nodeos STDOUT. The most popular terminal replacement with split panes is called iTerm2: https://iterm2.com/features.html

Alternatively, you can just open multiple windows and size them so you can see them all on your screen.
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
  "title": "Step 4 (Optional): Turn off Debug Logs"
}
[/block]
The logs can slow the performance of a node. You can write a configuration for the debugger, effectively turning off the debugging:
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
      "code": "$ nodeos -d ~/eos.data/producer_node --config-dir ~/eos.data/producer_node ~/eos.data/logging.json --http-server-address \"\" -p eosio -e\n\nOR with debugging enabled\n\n$ nodeos -d ~/eos.data/producer_node --config-dir ~/eos.data/producer_node -1 --http-server-address \"\" -p eosio -e",
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
      "code": "nodeos -d ~/eos.data/generator_node \\\n--config-dir ~/eos.data/generator_node -1\n--logconf ~/eos.data/logging.json \\ \n--plugin eosio::txn_test_gen_plugin \\\n--plugin eosio::wallet_api_plugin \\\n--plugin eosio::chain_api_plugin \\\n--p2p-peer-address localhost:9876 \\\n--p2p-listen-endpoint localhost:5555",
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
Using the `eosio_txn_generator_plugin`, one of the first things we need to do is initialize the various accounts that the `eosio_txn_generator_plugin` uses. Cleos doesn't have a helper command for this plugin. So we're going to do it a little dirty.

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