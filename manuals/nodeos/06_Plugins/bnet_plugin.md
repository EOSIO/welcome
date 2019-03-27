---
title: "bnet_plugin"
excerpt: ""
---
[block:callout]
{
  "type": "info",
  "body": "The net plugin is the preferred plugin for connecting peers in the network."
}
[/block]

[block:api-header]
{
  "title": "Description"
}
[/block]
**bnet_plugin** provides an p2p protocol to persistently synchronize two blockchains using a very simple algorithm:


[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  --bnet-endpoint arg (=0.0.0.0:4321)   The endpoint upon which to listen for\n                                        incoming connections\n  --bnet-follow-irreversible arg (=0)   This peer will request only\n                                        irreversible blocks from other nodes\n  --bnet-threads arg                    The number of threads to use to process\n                                        network messages\n  --bnet-connect arg                    Remote endpoint of other node to\n                                        connect to; Use multiple bnet-connect\n                                        options as needed to compose a network\n  --bnet-no-trx                         This peer will request no pending\n                                        transactions from other nodes\n  --bnet-peer-log-format arg (=[\"${_name}\" ${_ip}:${_port}])\n                                        The string used to format peers when\n                                        logging messages about them.  Variables\n                                        are escaped with ${<variable name>}.\n                                        Available Variables:\n                                           _name  self-reported name\n                                           _id    self-reported ID (Public Key)\n                                           _ip    remote IP address of peer\n                                           _port  remote port number of peer\n                                           _lip   local IP address connected to\n                                                  peer\n                                           _lport local port number connected\n                                                  to peer",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::bnet_plugin\n\n# nodeos startup params\n--plugin eosio::bnet_plugin\n\n#nodeos startup params with some config options\n--plugin eosio::bnet_plugin --bnet-threads 2 --bnet-no-trx ",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Dependencies"
}
[/block]
None