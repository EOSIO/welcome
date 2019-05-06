---
title: "bnet_plugin"
excerpt: ""
---
[[info]]
|
The net plugin is the preferred plugin for connecting peers in the network.

## Description
**bnet_plugin** provides an p2p protocol to persistently synchronize two blockchains using a very simple algorithm:


## Options


```shell
  --bnet-endpoint arg (=0.0.0.0:4321)   The endpoint upon which to listen for
                                        incoming connections
  --bnet-follow-irreversible arg (=0)   This peer will request only
                                        irreversible blocks from other nodes
  --bnet-threads arg                    The number of threads to use to process
                                        network messages
  --bnet-connect arg                    Remote endpoint of other node to
                                        connect to; Use multiple bnet-connect
                                        options as needed to compose a network
  --bnet-no-trx                         This peer will request no pending
                                        transactions from other nodes
  --bnet-peer-log-format arg (=["${_name}" ${_ip}:${_port}])
                                        The string used to format peers when
                                        logging messages about them.  Variables
                                        are escaped with ${<variable name>}.
                                        Available Variables:
                                           _name  self-reported name
                                           _id    self-reported ID (Public Key)
                                           _ip    remote IP address of peer
                                           _port  remote port number of peer
                                           _lip   local IP address connected to
                                                  peer
                                           _lport local port number connected
                                                  to peer
```

## Usage


```shell
# config.ini
plugin = eosio::bnet_plugin

# nodeos startup params
--plugin eosio::bnet_plugin

#nodeos startup params with some config options
--plugin eosio::bnet_plugin --bnet-threads 2 --bnet-no-trx 
```

## Dependencies
None