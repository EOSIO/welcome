---
title: "sign_transaction"
excerpt: "Signs a transaction."
---
[block:api-header]
{
  "title": "Example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "[{\n  \"ref_block_num\": 21453,\n  \"ref_block_prefix\": 3165644999,\n  \"expiration\": \"2017-12-08T10:28:49\",\n  \"scope\": [\"initb\", \"initc\"],\n  \"read_scope\": [],\n  \"messages\": [{\n    \"code\": \"currency\",\n    \"type\": \"transfer\",\n    \"authorization\": [{\n      \"account\": \"initb\",\n      \"permission\": \"active\"\n    }],\n    \"data\": \"000000008093dd74000000000094dd74e803000000000000\"\n  }],\n  \"signatures\": []\n},\n [\"EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\"], \"\"\n]",
      "language": "json"
    }
  ]
}
[/block]