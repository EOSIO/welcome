---
title: "wallet_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
**wallet_plugin** adds wallet functionality to a node
[block:callout]
{
  "type": "warning",
  "body": "**wallet_plugin** is not designed to be loaded as a plugin on a publicly accessible node without further security measures. This is particularly true when also loading the **wallet_api_plugin**, which should not under any conditions be loaded on a publicly accessible node."
}
[/block]

[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  --wallet-dir arg (=\".\")               The path of the wallet files (absolute\n                                        path or relative to application data\n                                        dir)\n  --unlock-timeout arg (=900)           Timeout for unlocked wallet in seconds\n                                        (default 900 (15 minutes)). Wallets\n                                        will automatically lock after specified\n                                        number of seconds of inactivity.\n                                        Activity is defined as any wallet\n                                        command e.g. list-wallets.\n  --yubihsm-url URL                     Override default URL of\n                                        http://localhost:12345 for connecting\n                                        to yubihsm-connector\n  --yubihsm-authkey key_num             Enables YubiHSM support using given\n                                        Authkey",
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
      "code": "# config.ini\nplugin = eosio::wallet_plugin\n\n# nodeos startup params\n--plugin eosio::wallet_plugin",
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
None