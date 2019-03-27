---
title: "producer_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The **producer_plugin** loads functionality required to for a node to produce blocks.
[block:callout]
{
  "type": "info",
  "body": "Additional configuration is required to produce blocks. Please reference the following: \n- [Configuring Block Producing Node](doc:producing-node)"
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
      "code": "# config.ini\nplugin = producer_plugin\n\n# nodeos startup params\n--plugin producer_plugin",
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
      "code": "# config.ini\nplugin = eosio::chain_plugin\n\n# nodeos startup params\n--plugin eosio::chain_plugin\n",
      "language": "shell"
    }
  ]
}
[/block]