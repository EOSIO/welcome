---
title: "test_control_api_plugin"
excerpt: "This plugin is designed for testing nodeos"
---
## Description
This allows you to send a control message to the [test_control_plugin](doc:test_control_plugin) telling the test_control_plugin to shut down a nodeos instance when reaching a particular block.

It is intended for testing.
## Options


```shell
curl %s/v1/test_control/kill_node_on_producer -d '{ \"producer\":\"%s\", \"where_in_sequence\":%d, \"based_on_lib\":\"%s\" }' -X POST -H \"Content-Type: application/json\"" % \
            
```

## Usage


```shell
# nodeos startup params
--plugin eosio::test_control_api_plugin
```

## Dependencies
- [test_control_plugin](doc:test_control_plugin) 
- [chain_plugin](doc:chain_plugin) 
- [http_plugin](doc:http_plugin)
## Load Dependancy Examples


```shell
# config.ini
plugin = eosio::chain_plugin
plugin = eosio::http_plugin

# nodeos startup params
--plugin eosio::test_control_plugin 


# nodeos startup params
--plugin eosio::test_control_plugin --plugin eosio::chain_plugin --plugin eosio::http_plugin
```
