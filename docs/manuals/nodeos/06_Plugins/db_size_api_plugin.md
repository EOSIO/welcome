---
title: "db_size_api_plugin"
excerpt: ""
---
## Description
Retrieve information about the blockchain

   - free_bytes
   - used_bytes
   - size
   - indices

## Options


```shell

```

## Usage


```shell
# Not available
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
