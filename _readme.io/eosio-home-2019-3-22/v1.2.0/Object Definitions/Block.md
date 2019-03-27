---
title: "Block"
excerpt: ""
---
[block:api-header]
{
  "title": "Content"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"previous\": \"00005e23b...0a1fe\",\n    \"timestamp\": \"2018-04-03T13:45:42.000\",\n    \"transaction_mroot\": \"a2e1...d1391d\",\n    \"action_mroot\": \"7486460...45e8b\",\n    \"block_mroot\": \"63f83ff315...f8f\",\n    \"producer\": \"eosio\",\n    \"schedule_version\": 0,\n    \"new_producers\": null,\n    \"producer_signature\": \"EOSKkp3t...LNqf8on92j\",\n    \"regions\": [{\n        \"region\": 0,\n        \"cycles_summary\": [\n            [{\n                \"read_locks\": [],\n                \"write_locks\": [],\n                \"transactions\": [{\n                    \"status\": \"executed\",\n                    \"id\": \"a2e1525a7...f6d1391d\"\n                }]\n            }]\n        ]\n    }],\n    \"input_transactions\": [],\n    \"id\": \"00005e240...d31ddb4e41d22\",\n    \"block_num\": 24100,\n    \"ref_block_prefix\": 89107424\n}",
      "language": "json",
      "name": ""
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Description"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Definition",
    "0-0": "`previous`",
    "0-1": "Checksum (SHA256) of the previous block.",
    "1-0": "`timestamp`",
    "1-1": "Scheduled time of this block.",
    "2-0": "`transaction_mroot`",
    "2-1": "Checksum (SHA256) representing a “commitment to all transactions scheduled / included or executed in this block”.",
    "3-0": "`action_mroot`",
    "3-1": "Checksum (SHA256) representing a “commitment to (some of) the side effects, outputs and outcomes of actions processed in this block”.",
    "4-0": "`block_mroot`",
    "4-1": "Root of the merkle tree of the entire blockchain, i.e. all blocks prior to this block.",
    "5-0": "`producer`",
    "5-1": "Account name of the block producer who produced this block.",
    "6-0": "`schedule_version`",
    "6-1": "Producer schedule version that should validate this block. This is used to \n indicate that the prior block, which included the new_producers->version, has been \n marked irreversible and that the new producer schedule takes effect this block.",
    "7-0": "`new_producers`",
    "7-1": "List of new block producers who have been elected.",
    "8-0": "`producer_signature`",
    "8-1": "Signature of the block producer who produced this block.",
    "9-0": "`regions`",
    "9-1": "`region` - An index that represents the shard of memory where this block is stored.\n`cycles_summary` - Processed activity during block production.",
    "10-0": "`input_transactions`",
    "10-1": "List of transaction ids associated with this block. (stored on disk but not sent over the wire to other nodes)",
    "11-0": "`id`",
    "11-1": "Calculated on the fly to identify this block. Not stored in the block.",
    "12-0": "`block_num`",
    "12-1": "Calculated on the fly to be an ordinal numeric identifier. Not stored in the block.",
    "13-0": "`ref_block_prefix`",
    "13-1": "Lower 32 bits of the calculated id. Not stored in the block."
  },
  "cols": 2,
  "rows": 14
}
[/block]

[block:api-header]
{
  "title": "Notes"
}
[/block]
`_mroot` - A merkle root is the top of a merkle tree.