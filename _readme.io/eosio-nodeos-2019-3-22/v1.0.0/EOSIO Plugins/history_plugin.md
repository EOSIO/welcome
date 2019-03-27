---
title: "history_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
As the name implies, the **history_plugin** provides a cache layer for blockchain objects that are useful for obtaining historical data. It utilizes the [chain_plugin](doc:chain_plugin) for its data source and [mongo_db_plugin](doc:mongo_db_plugin) for cache storage
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
- [mongo_db_plugin](doc:mongo_db_plugin) 

## Load Dependency Examples
[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::chain_plugin\nplugin = eosio::mongo_db_plugin\n\n\n# nodeos startup params\n--plugin eosio::chain_plugin --plugin eosio::mongo_db_plugin\n",
      "language": "shell"
    }
  ]
}
[/block]