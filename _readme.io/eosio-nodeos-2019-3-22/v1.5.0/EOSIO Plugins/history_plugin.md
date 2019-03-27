---
title: "history_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The **history_plugin** provides a cache layer for blockchain objects that are useful for obtaining historical data. It depends on [chain_plugin](doc:chain_plugin) for the data
[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  -f [ --filter-on ] arg                Track actions which match\n                                        receiver:action:actor. Actor may be\n                                        blank to include all. Receiver and\n                                        Action may not be blank.\n                                        \n  -f [ --filter-out ] arg               Do not track actions which match\n                                        receiver:action:actor. Action and Actor\n                                        both blank excludes all from Reciever.\n                                        Actor blank excludes all from\n                                        reciever:action. Receiver may not be\n                                        blank.                                      \n\nConfig Options for eosio::http_client_plugin:\n  --https-client-root-cert arg          PEM encoded trusted root certificate\n                                        (or path to file containing one) used\n                                        to validate any TLS connections made.\n                                        (may specify multiple times)\n\n  --https-client-validate-peers arg (=1)\n                                        true: validate that the peer\n                                        certificates are valid and trusted,\n                                        false: ignore cert errors",
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