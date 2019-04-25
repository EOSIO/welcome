---
title: "history_plugin"
excerpt: ""
---
[block:callout]
{
  "type": "warning",
  "body": "The history plugin is deprecated and will no longer be maintained, please use the [state history plugin](doc:state_history_plugin) instead",
  "title": "Deprecation Notice"
}
[/block]

[block:api-header]
{
  "title": "Description"
}
[/block]
The **history_plugin** provides a cache layer for blockchain objects that are useful for obtaining historical data. It depends on [chain_plugin](doc:chain_plugin) for the data. The history_api_plugin uses this to provide read-only access to blockchain data.
[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  -f [ --filter-on ] arg                Track actions which match\n                                        receiver:action:actor. Actor may be\n                                        blank to include all. Receiver and\n                                        Action may not be blank.\n                                        \n  -f [ --filter-out ] arg               Do not track actions which match\n                                        receiver:action:actor. Action and Actor\n                                        both blank excludes all from Reciever.\n                                        Actor blank excludes all from\n                                        reciever:action. Receiver may not be\n                                        blank.                                      \n",
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
      "code": "# config.ini\nplugin = eosio::history_plugin\n\n# nodeos startup params\n--plugin eosio::history_plugin",
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

## Load Dependency Examples
[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::chain_plugin\n\n\n# nodeos startup params\n--plugin eosio::chain_plugin\n",
      "language": "shell"
    }
  ]
}
[/block]