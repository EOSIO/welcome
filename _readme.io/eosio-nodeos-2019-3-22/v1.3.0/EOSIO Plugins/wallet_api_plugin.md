---
title: "wallet_api_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
**wallet_api_plugin** exposes functionality from the [wallet_plugin](doc:wallet_plugin) to the RPC API interface managed by the [http_plugin](doc:http_plugin)
[block:callout]
{
  "type": "danger",
  "body": "This plugin exposes wallets and so running this plugin on a publicly accessible node is not recommended. As of 1.2.0 Nodeos will no longer allow **wallet_api_plugin**."
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
      "code": "# config.ini\nplugin = eosio::wallet_api_plugin\n\n# nodeos startup params\n--plugin eosio::wallet_api_plugin",
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
- [wallet_plugin](doc:wallet_plugin) 
- [http_plugin](doc:http_plugin) 

## Load Dependency Examples
[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::wallet_plugin\nplugin = eosio::http_plugin\n\n# nodeos startup params\n--plugin eosio::wallet_plugin --plugin eosio::http_plugin\n",
      "language": "shell"
    }
  ]
}
[/block]