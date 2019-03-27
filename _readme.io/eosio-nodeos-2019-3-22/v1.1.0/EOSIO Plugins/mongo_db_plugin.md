---
title: "mongo_db_plugin"
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
      "code": "  -q [ --mongodb-queue-size ] arg (=256)\n                                        The target queue size between nodeos\n                                        and MongoDB plugin thread.\n  --mongodb-wipe                        Required with --replay-blockchain,\n                                        --hard-replay-blockchain, or\n                                        --delete-all-blocks to wipe mongo\n                                        db.This option required to prevent\n                                        accidental wipe of mongo db.\n  --mongodb-block-start arg (=0)        If specified then only abi data pushed\n                                        to mongodb until specified block is\n                                        reached.\n  -m [ --mongodb-uri ] arg              MongoDB URI connection string, see:\n                                        https://docs.mongodb.com/master/referen\n                                        ce/connection-string/. If not specified\n                                        then plugin is disabled. Default\n                                        database 'EOS' is used if not specified\n                                        in URI. Example: mongodb://127.0.0.1:27\n                                        017/EOS\n",
      "language": "shell"
    }
  ]
}
[/block]