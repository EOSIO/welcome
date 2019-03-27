---
title: "net_api_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
**net_api_plugin** exposes functionality from the [net_plugin](doc:net_plugin) to the RPC API interface managed by the [http_plugin](doc:http_plugin)

Provides four RPC API endpoints:
 - connect
 - disconnect
 - connections
 - status

See [Net section of ROC API] (https://developers.eos.io/eosio-nodeos/reference)
[block:callout]
{
  "type": "danger",
  "body": "This plugin exposes endpoints that allow management of p2p connections, running this plugin on a publicly accessible node is not recommended as it can be exploited."
}
[/block]

[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::net_api_plugin\n\n# nodeos startup params\n--plugin eosio::net_api_plugin",
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
- [net_plugin](doc:net_plugin) 
- [http_plugin](doc:http_plugin) 

## Load Dependency Examples
[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::net_plugin\nplugin = eosio::http_plugin\n\n# nodeos startup params\n--plugin eosio::net_plugin --plugin eosio::http_plugin\n",
      "language": "shell"
    }
  ]
}
[/block]