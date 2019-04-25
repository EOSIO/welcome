---
title: "faucet_testnet_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
This plugin provides an interface that assists in the automation of distributing tokens on an EOSIO testnet
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::faucet_testnet_plugin\n\n# nodeos startup params\n--plugin eosio::faucet_testnet_plugin",
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
[http_plugin](doc:http_plugin)
[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::http_plugin\n\n# nodeos startup params\n--plugin eosio::http_plugin",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{}
[/block]