---
title: "state_history_plugin"
excerpt: ""
---
## Description
The state_history_plugin caches blockchain data into files and is useful for obtaining historical data. The state_history listens on a socket for applications connecting to the state history plugin and send the blockchain data to the application.  

An example of an application which retrieves data from the state_history_plugin is [fill-postgresql](https://github.com/EOSIO/fill-postgresql)
## Options


```shell

  --state-history-dir arg       (default="state-history")
                                The location of the state-history directory
                                (absolute path or relative to application data
                                dir)
  --trace-history               Enable trace history
  --chain-state-history         Enable chain state history
  --state-history-endpoint arg  (default=0.0.0.0:8080)
                                The endpoint upon which to listen for incoming
                                connections
  --delete-state-history        Clear state history files

Requires the chain_plugin command

  --disable-replay-opts         Disable optimizations that specifically target
                                replay

```

## Usage


```shell
# config.ini
plugin = eosio::state_history_plugin

# nodeos startup program
--plugin eosio::state_history_plugin

```

## Dependencies
- [chain_plugin](doc:chain_plugin) 

## Load Dependency Examples

```shell
# config.ini
plugin = eosio::chain_plugin


# nodeos startup params
--plugin eosio::chain_plugin --disable-replay-opts
```
