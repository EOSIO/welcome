---
title: "test_control_plugin"
excerpt: "This plugin is designed for testing nodeos"
---
## Description
This plugin is designed to cause a graceful shutdown when reaching a particular block in a sequence of blocks produced by a specific block producer. It can be invoked to either shutdown on the **head block** or the **last irreversible block**.  

This is intended for testing, to determine exactly when a nodeos instance will shutdown.  
## Options


```shell

```

## Usage


```shell
# nodeos startup params
--plugin eosio::test_control_plugin
```

## Dependencies
- [chain_plugin](doc:chain_plugin) 

```shell
# config.ini
plugin = eosio::chain_plugin

# nodeos startup params
--plugin eosio::chain_plugin
```
