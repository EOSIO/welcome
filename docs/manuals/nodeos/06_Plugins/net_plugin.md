---
title: "net_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
**net_plugin** provides an authenticated p2p protocol to persistently synchronize nodes


[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  --p2p-listen-endpoint arg        (default=0.0.0.0:9876)\n                                   The actual host:port used to listen for\n                                   incoming p2p connections.\n  --p2p-server-address arg         An externally accessible host:port for\n                                   identifying this node. Defaults to\n                                   p2p-listen-endpoint.\n  --p2p-peer-address arg           The public endpoint of a peer node to connect                                    to. Use multiple p2p-peer-address options as\n                                   needed to compose a network.\n  --p2p-max-nodes-per-host arg     (default=1)     \n                                   Maximum number of client nodes from any single\n                                   IP address\n  --agent-name arg                 (default=\"EOS Test Agent\")  \n                                   The name supplied to identify this node     \n                                   amongst the peers.\n  --allowed-connection arg         (default=any)\n                                   Can be 'any' or 'producers' or 'specified' or\n                                   'none'. If 'specified', peer-key must be\n                                   specified at least once. If only 'producers',\n                                   peer-key is not required. 'producers' and\n                                   'specified' may be combined.\n  --peer-key arg                   Optional public key of peer allowed to\n                                   connect.  May be used multiple times.\n  --peer-private-key arg           Tuple of [PublicKey, WIF private key] (may\n                                   specify multiple times)\n  --max-clients arg                (default=25)\n                                   Maximum number of clients from which\n                                   connections are accepted, use 0 for no\n                                   limit\n  --connection-cleanup-period arg  (default=30) \n                                   Number of seconds to wait before cleaning up\n                                   dead connections\n  --max-cleanup-time-msec arg      (default=10)\n                                   Max connection cleanup time per cleanup call\n                                   in millisec\n  --network-version-match arg      (default=False)  \n                                   True to require exact match of peer network\n                                   version.\n  --sync-fetch-span arg            (default=100)\n                                   Number of blocks to retrieve in a chunk from\n                                   any individual peer during synchronization\n  --use-socket-read-watermark arg  (default=False)  \n                                   Enable expirimental socket read watermark\n                                   optimization\n  --peer-log-format arg            (default=[\"${_name}\" ${_ip}:${_port}])\n                                   The string used to format peers when logging\n                                   messages about them. Variables are escaped\n                                   with ${<variable name>}.\n                                   Available Variables:\n                                      _name  self-reported name\n                                      _id    self-reported ID (64 hex characters)\n                                      _sid   first 8 characters of_peer.id\n                                      _ip    remote IP address of peer\n                                      _port  remote port number of peer\n                                      _lip   local IP address connected to peer\n                                      _lport local port number connected to peer",
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
      "code": "# config.ini\nplugin = eosio::net_plugin\n\n# nodeos startup params\n-- plugin eosio::net_plugin\n",
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
 -