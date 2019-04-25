---
title: "How to manage peers with Cleos"
excerpt: ""
---
Managing peers with cleos is an edge case. In general, you should load the `eosio::net_api_plugin` on any publicly accessibly node. So if you're planning to develop a connection manager that safely employs the `eosio::net_api_plugin` or if you're a curious individual, this may be useful for you. 
[block:api-header]
{
  "title": "Configuration"
}
[/block]
Add the following to your `config.ini` file and restart Nodeos and/or Keosd
[block:code]
{
  "codes": [
    {
      "code": "plugin = eosio::net_api_plugin",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Listing Your Peers"
}
[/block]
Running the following will list all your node's peer connections (Keosd an Nodeos) 
[block:code]
{
  "codes": [
    {
      "code": "cleos net peers -H yournode.host -P yourport",
      "language": "shell"
    }
  ]
}
[/block]
This would return an array of peers, something like the following
[block:code]
{
  "codes": [
    {
      "code": "[{\n    \"peer\": \"123.456.78.9:9876\",\n    \"connecting\": false,\n    \"syncing\": false,\n    \"last_handshake\": {\n      \"network_version\": 0,\n      \"chain_id\": \"0000000000000000000000000000000000000000000000000000000000000000\",\n      \"node_id\": \"0000000000000000000000000000000000000000000000000000000000000000\",\n      \"key\": \"EOS1111111111111111111111111111111114T1Anm\",\n      \"time\": 0,\n      \"token\": \"0000000000000000000000000000000000000000000000000000000000000000\",\n      \"sig\": \"EOS111111111111111111111111111111111111111111111111111111111111111115NsAua\",\n      \"p2p_address\": \"\",\n      \"last_irreversible_block_num\": 0,\n      \"last_irreversible_block_id\": \"0000000000000000000000000000000000000000000000000000000000000000\",\n      \"head_num\": 0,\n      \"head_id\": \"0000000000000000000000000000000000000000000000000000000000000000\",\n      \"os\": \"\",\n      \"agent\": \"\",\n      \"generation\": 0\n    }\n  }\n  ...]",
      "language": "text"
    }
  ]
}
[/block]
You notice all peers are returning `"connecting": false` and `"syncing": false`. You start your search for an updated peers list or online peer. 
[block:api-header]
{
  "title": "Listing Peers"
}
[/block]
You can list an active