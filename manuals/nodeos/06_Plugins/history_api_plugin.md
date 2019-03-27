---
title: "history_api_plugin"
excerpt: ""
---
[block:callout]
{
  "type": "warning",
  "body": "The history plugin that the history api plugin is dependent upon is deprecated and will no longer be maintained, please use the [state history plugin](doc:state_history_plugin) instead"
}
[/block]

[block:api-header]
{
  "title": "Description"
}
[/block]
**history_api_plugin** exposes functionality from the [history_plugin](doc:history_plugin) to the RPC API interface managed by the [http_plugin](doc:http_plugin) providing read-only access to blockchain data.

Provides four RPC API endpoints:

 - get_actions
 - get_transaction
 - get_key_accounts
 - get_controlled_accounts

See [History section of RPC API] (https://developers.eos.io/eosio-nodeos/reference) 

The four actions listed above are used by the following Cleos commands (matching order):
 - get actions
 - get transaction
 - get accounts
 - get servants
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
      "code": "# config.ini\nplugin = eosio::history_api_plugin\n\n# nodeos startup params\n--plugin eosio::history_api_plugin",
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
- [history_plugin](doc:history_plugin) 
- [chain_plugin](doc:chain_plugin) 
- [http_plugin](doc:http_plugin) 

## Load Dependency Examples
[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::history_plugin\nplugin = eosio::chain_plugin\nplugin = eosio::http_plugin\n\n# nodeos startup params\n--plugin eosio::history_plugin --plugin eosio::chain_plugin --plugin eosio::http_plugin\n",
      "language": "shell"
    }
  ]
}
[/block]