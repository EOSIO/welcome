---
title: "history_plugin"
excerpt: ""
---
[[warning]]
|Deprecation Notice
The history plugin is deprecated and will no longer be maintained, please use the [state history plugin](doc:state_history_plugin) instead

## Description
The **history_plugin** provides a cache layer for blockchain objects that are useful for obtaining historical data. It depends on [chain_plugin](doc:chain_plugin) for the data. The history_api_plugin uses this to provide read-only access to blockchain data.
## Options


```shell
  -f [ --filter-on ] arg                Track actions which match
                                        receiver:action:actor. Actor may be
                                        blank to include all. Receiver and
                                        Action may not be blank.
                                        
  -f [ --filter-out ] arg               Do not track actions which match
                                        receiver:action:actor. Action and Actor
                                        both blank excludes all from Reciever.
                                        Actor blank excludes all from
                                        reciever:action. Receiver may not be
                                        blank.                                      

```

## Usage


```text
# config.ini
plugin = eosio::history_plugin

# nodeos startup params
--plugin eosio::history_plugin
```

## Dependencies
- [chain_plugin](doc:chain_plugin) 

## Load Dependency Examples

```shell
# config.ini
plugin = eosio::chain_plugin


# nodeos startup params
--plugin eosio::chain_plugin

```
