---
title: "db_size_api_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Retrieve information about the blockchain

   - free_bytes
   - used_bytes
   - size
   - indices

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
      "code": "# Not available",
      "language": "shell"
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
      "code": "# config.ini\nplugin = eosio::chain_plugin\nplugin = eosio::http_plugin\n\n# nodeos startup params\n--plugin eosio::chain_plugin --plugin eosio::http_plugin",
      "language": "shell"
    }
  ]
}
[/block]