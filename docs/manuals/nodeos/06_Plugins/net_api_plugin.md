---
title: "net_api_plugin"
excerpt: ""
---
## Description
**net_api_plugin** exposes functionality from the [net_plugin](doc:net_plugin) to the RPC API interface managed by the [http_plugin](doc:http_plugin)

Provides four RPC API endpoints:
 - connect
 - disconnect
 - connections
 - status

See [Net section of ROC API] (https://developers.eos.io/eosio-nodeos/reference)
[[danger]]
|
This plugin exposes endpoints that allow management of p2p connections, running this plugin on a publicly accessible node is not recommended as it can be exploited.

## Options


```shell

```

## Usage


```text
# config.ini
plugin = eosio::net_api_plugin

# nodeos startup params
--plugin eosio::net_api_plugin
```

## Dependencies
- [net_plugin](doc:net_plugin) 
- [http_plugin](doc:http_plugin) 

## Load Dependency Examples

```shell
# config.ini
plugin = eosio::net_plugin
plugin = eosio::http_plugin

# nodeos startup params
--plugin eosio::net_plugin --plugin eosio::http_plugin

```
