---
title: "wallet_api_plugin"
excerpt: ""
---
## Description
**wallet_api_plugin** exposes functionality from the [wallet_plugin](doc:wallet_plugin) to the RPC API interface managed by the [http_plugin](doc:http_plugin)
[[danger]]
|
This plugin exposes wallets and so running this plugin on a publicly accessible node is not recommended. As of 1.2.0 Nodeos will no longer allow **wallet_api_plugin**.

## Options

## Usage


```text
# config.ini
plugin = eosio::wallet_api_plugin

# nodeos startup params
--plugin eosio::wallet_api_plugin
```

## Dependencies
- [wallet_plugin](doc:wallet_plugin) 
- [http_plugin](doc:http_plugin) 

## Load Dependency Examples

```shell
# config.ini
plugin = eosio::wallet_plugin
plugin = eosio::http_plugin

# nodeos startup params
--plugin eosio::wallet_plugin --plugin eosio::http_plugin

```
