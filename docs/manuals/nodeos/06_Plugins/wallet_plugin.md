---
title: "wallet_plugin"
excerpt: ""
---
## Description
**wallet_plugin** adds wallet functionality to a node
[[warning]]
|
**wallet_plugin** is not designed to be loaded as a plugin on a publicly accessible node without further security measures. This is particularly true when also loading the **wallet_api_plugin**, which should not under any conditions be loaded on a publicly accessible node.

## Options


```shell
  --wallet-dir arg (=".")               The path of the wallet files (absolute
                                        path or relative to application data
                                        dir)
  --unlock-timeout arg (=900)           Timeout for unlocked wallet in seconds
                                        (default 900 (15 minutes)). Wallets
                                        will automatically lock after specified
                                        number of seconds of inactivity.
                                        Activity is defined as any wallet
                                        command e.g. list-wallets.
  --yubihsm-url URL                     Override default URL of
                                        http://localhost:12345 for connecting
                                        to yubihsm-connector
  --yubihsm-authkey key_num             Enables YubiHSM support using given
                                        Authkey
```

## Usage


```shell
# config.ini
plugin = eosio::wallet_plugin

# nodeos startup params
--plugin eosio::wallet_plugin
```

## Dependencies
None