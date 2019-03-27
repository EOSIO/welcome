---
title: "pack_transaction"
excerpt: "From plain signed json to packed form"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `transaction` _TEXT_ - The plain signed json (string)
[block:api-header]
{
  "title": "Options"
}
[/block]
- `--pack-action-data` - Pack all action data within transaction, needs interaction with nodeos
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos convert pack_transaction '{\n  \"expiration\": \"2018-08-02T20:24:36\",\n  \"ref_block_num\": 14207,\n  \"ref_block_prefix\": 1438248607,\n  \"max_net_usage_words\": 0,\n  \"max_cpu_usage_ms\": 0,\n  \"delay_sec\": 0,\n  \"context_free_actions\": [],\n  \"actions\": [{\n      \"account\": \"eosio\",\n      \"name\": \"newaccount\",\n      \"authorization\": [{\n          \"actor\": \"eosio\",\n          \"permission\": \"active\"\n        }\n      ],\n      \"data\": \"0000000000ea305500a6823403ea30550100000001000240cc0bf90a5656c8bb81f0eb86f49f89613c5cd988c018715d4646c6bd0ad3d8010000000100000001000240cc0bf90a5656c8bb81f0eb86f49f89613c5cd988c018715d4646c6bd0ad3d801000000\"\n    }\n  ],\n  \"transaction_extensions\": []\n}'",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Output"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"signatures\": [],\n  \"compression\": \"none\",\n  \"packed_context_free_data\": \"\",\n  \"packed_trx\": \"8468635b7f379feeb95500000000010000000000ea305500409e9a2264b89a010000000000ea305500000000a8ed3232660000000000ea305500a6823403ea30550100000001000240cc0bf90a5656c8bb81f0eb86f49f89613c5cd988c018715d4646c6bd0ad3d8010000000100000001000240cc0bf90a5656c8bb81f0eb86f49f89613c5cd988c018715d4646c6bd0ad3d80100000000\"\n}",
      "language": "text"
    }
  ]
}
[/block]