---
title: "http_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The **http_plugin** is a core plugin required to enable any RPC API on an EOSIO node. 
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::http_plugin\n\n# nodeos startup params\n--plugin eosio::http_plugin",
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