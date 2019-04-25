---
title: "chain_api_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
  * **chain_api_plugin** exposes functionality from the [chain_plugin](doc:chain_plugin) to the RPC API interface managed by the [http_plugin](doc:http_plugin) 
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::chain_api_plugin\n\n# nodeos startup params\n--plugin eosio::chain_api_plugin",
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
- [chain_plugin](doc:chain_plugin) 
- [http_plugin](doc:http_plugin) 

## Load Dependency Examples
[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::chain_plugin\nplugin = eosio::http_plugin\n\n# nodeos startup params\n--plugin eosio::chain_plugin --plugin eosio::http_plugin\n",
      "language": "shell"
    }
  ]
}
[/block]