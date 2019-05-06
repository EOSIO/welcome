---
title: "chain_api_plugin"
excerpt: ""
---
## Description
  * **chain_api_plugin** exposes functionality from the [chain_plugin](doc:chain_plugin) to the RPC API interface managed by the [http_plugin](doc:http_plugin) 
## Usage


```text
# config.ini
plugin = eosio::chain_api_plugin

# nodeos startup params
--plugin eosio::chain_api_plugin
```

## Dependencies
- [chain_plugin](doc:chain_plugin) 
- [http_plugin](doc:http_plugin) 

## Load Dependency Examples

```shell
# config.ini
plugin = eosio::chain_plugin
plugin = eosio::http_plugin

# nodeos startup params
--plugin eosio::chain_plugin --plugin eosio::http_plugin

```
