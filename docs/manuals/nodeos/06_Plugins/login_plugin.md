---
title: "login_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
**login_plugin** supports the concept of applications authenticating with the EOSIO blockchain. The login_plugin API allows you to verify a user is able to sign to satisfy a specified [authority](https://developers.eos.io/eosio-nodeos/docs/accounts-and-permissions). 

[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  --max-login-requests arg          (default=1000000)   \n                                    The maximum number of pending login requests\n  --max-login-timeout arg           (default=60)\n                                    The maximum timeout for pending login\n                                    requests (in seconds)",
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
      "code": "# config.ini\nplugin = eosio::login_plugin\n\n# nodeos startup params\n--plugin eosio::login_plugin",
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