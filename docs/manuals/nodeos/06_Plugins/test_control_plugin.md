---
title: "test_control_plugin"
excerpt: "This plugin is designed for testing nodeos"
---
[block:api-header]
{
  "title": "Description"
}
[/block]
This plugin is designed to cause a graceful shutdown when reaching a particular block in a sequence of blocks produced by a specific block producer. It can be invoked to either shutdown on the **head block** or the **last irreversible block**.  

This is intended for testing, to determine exactly when a nodeos instance will shutdown.  
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
      "code": "# nodeos startup params\n--plugin eosio::test_control_plugin",
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
[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::chain_plugin\n\n# nodeos startup params\n--plugin eosio::chain_plugin",
      "language": "shell"
    }
  ]
}
[/block]