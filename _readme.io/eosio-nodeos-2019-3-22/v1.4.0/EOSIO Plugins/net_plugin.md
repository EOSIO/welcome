---
title: "net_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  --p2p-listen-endpoint arg (=0.0.0.0:9876)\n                                        The actual host:port used to listen for\n                                        incoming p2p connections.\n  --p2p-server-address arg              An externally accessible host:port for\n                                        identifying this node. Defaults to\n                                        p2p-listen-endpoint.\n  --p2p-peer-address arg                The public endpoint of a peer node to\n                                        connect to. Use multiple\n                                        p2p-peer-address options as needed to\n                                        compose a network.\n  --p2p-max-nodes-per-host arg (=1)     Maximum number of client nodes from any\n                                        single IP address\n  --agent-name arg (=\"EOS Test Agent\")  The name supplied to identify this node\n                                        amongst the peers.\n  --allowed-connection arg (=any)       Can be 'any' or 'producers' or\n                                        'specified' or 'none'. If 'specified',\n                                        peer-key must be specified at least\n                                        once. If only 'producers', peer-key is\n                                        not required. 'producers' and\n                                        'specified' may be combined.\n  --peer-key arg                        Optional public key of peer allowed to\n                                        connect.  May be used multiple times.\n  --peer-private-key arg                Tuple of [PublicKey, WIF private key]\n                                        (may specify multiple times)\n  --max-clients arg (=25)               Maximum number of clients from which\n                                        connections are accepted, use 0 for no\n                                        limit\n  --connection-cleanup-period arg (=30) number of seconds to wait before\n                                        cleaning up dead connections\n  --network-version-match arg (=0)      True to require exact match of peer\n                                        network version.\n  --sync-fetch-span arg (=100)          number of blocks to retrieve in a chunk\n                                        from any individual peer during\n                                        synchronization\n  --max-implicit-request arg (=1500)    maximum sizes of transaction or block\n                                        messages that are sent without first\n                                        sending a notice\n  --use-socket-read-watermark arg (=0)  Enable expirimental socket read\n                                        watermark optimization\n  --peer-log-format arg (=[\"${_name}\" ${_ip}:${_port}])\n                                        The string used to format peers when\n                                        logging messages about them.  Variables\n                                        are escaped with ${<variable name>}.\n                                        Available Variables:\n                                           _name  self-reported name\n\n                                           _id    self-reported ID (64 hex\n                                                  characters)\n\n                                           _sid   first 8 characters of\n                                                  _peer.id\n\n                                           _ip    remote IP address of peer\n\n                                           _port  remote port number of peer\n\n                                           _lip   local IP address connected to\n                                                  peer\n\n                                           _lport local port number connected\n                                                  to peer",
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