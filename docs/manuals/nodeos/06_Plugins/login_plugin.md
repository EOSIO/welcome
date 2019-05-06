---
title: "login_plugin"
excerpt: ""
---
## Description
**login_plugin** supports the concept of applications authenticating with the EOSIO blockchain. The login_plugin API allows you to verify a user is able to sign to satisfy a specified [authority](https://developers.eos.io/eosio-nodeos/docs/accounts-and-permissions). 

## Options


```shell
  --max-login-requests arg          (default=1000000)   
                                    The maximum number of pending login requests
  --max-login-timeout arg           (default=60)
                                    The maximum timeout for pending login
                                    requests (in seconds)
```

## Usage


```shell
# config.ini
plugin = eosio::login_plugin

# nodeos startup params
--plugin eosio::login_plugin
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
