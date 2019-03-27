---
title: "bnet_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
**bnet_plugin** provides an p2p protocol to persistently synchronize two blockchains using a very simple algorithm:

1. find the last block id on our local chain that the remote peer knows about
2. if we have the next block send it to them
3. if we don't have the next block send them a the oldest unexpired transaction
 *
There are several input events:
 *
1. new block accepted by local chain
2. block deemed irreversible by local chain
3. new block header accepted by local chain
4. transaction accepted by local chain
5. block received from remote peer
6. transaction received from remote peer
7. socket ready for next write
[block:api-header]
{
  "title": "Each session is responsible for maintaining the following"
}
[/block]
1. the most recent block on our current best chain which we know with certainty that the remote peer has.
- this could be the peers last irreversible block
- a block ID after the LIB that the peer has notified us of
- a block which we have sent to the remote peer
- a block which the peer has sent us
2. the block IDs we have received from the remote peer so that we can disconnect peer if one of those blocks is deemed invalid
- we can clear these IDs once the block becomes reversible
3. the transactions we have received from the remote peer so that we do not send them something that they already know.
- this includes transactions sent as part of blocks
- we clear this cache after we have applied a block that includes the transactions because we know the controller  should not notify us again (they would be dupe)

[block:api-header]
{
  "title": "Assumptions"
}
[/block]
1. All blocks we send the peer are valid and will be held in the peers fork database until they become irreversible or are replaced by an irreversible alternative. 
2. We don't care what fork the peer is on, so long as we know they have the block prior to the one we want to send. The peer will sort it out with its fork database and hopfully come to our conclusion.
3. The peer will send us blocks on the same basis

[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  --bnet-endpoint arg (=0.0.0.0:4321)   the endpoint upon which to listen for\n                                        incoming connections\n  --bnet-follow-irreversible arg (=0)   this peer will request only\n                                        irreversible blocks from other nodes\n  --bnet-threads arg                    the number of threads to use to process\n                                        network messages\n  --bnet-connect arg                    remote endpoint of other node to\n                                        connect to; Use multiple bnet-connect\n                                        options as needed to compose a network\n  --bnet-no-trx                         this peer will request no pending\n                                        transactions from other nodes\n  --bnet-peer-log-format arg (=[\"${_name}\" ${_ip}:${_port}])\n                                        The string used to format peers when\n                                        logging messages about them.  Variables\n                                        are escaped with ${<variable name>}.\n                                        Available Variables:\n                                           _name  self-reported name\n\n                                           _id    self-reported ID (Public Key)\n\n                                           _ip    remote IP address of peer\n\n                                           _port  remote port number of peer\n\n                                           _lip   local IP address connected to\n                                                  peer\n\n                                           _lport local port number connected\n                                                  to peer",
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
      "code": "# config.ini\nplugin = eosio::bnet_plugin\n\n# nodeos startup params\n--plugin eosio::bnet_plugin",
      "language": "shell"
    }
  ]
}
[/block]