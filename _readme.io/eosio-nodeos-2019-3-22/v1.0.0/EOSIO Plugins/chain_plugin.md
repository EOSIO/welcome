---
title: "chain_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The **chain_plugin** is a core plugin required to process and aggregate chain data on an EOSIO node. 

[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::chain_plugin\n\n# nodeos startup params\n--plugin eosio::chain_plugin",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Dependencies"
}
[/block]
None