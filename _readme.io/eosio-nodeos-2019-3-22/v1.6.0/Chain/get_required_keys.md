---
title: "get_required_keys"
excerpt: "Returns the required keys needed to sign a transaction."
---
[block:api-header]
{
  "title": "Examples"
}
[/block]
Below is an example transaction object, you can provide any valid EOSIO transaction. 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"ref_block_num\": \"100\",\n  \"ref_block_prefix\": \"137469861\",\n  \"expiration\": \"2017-09-25T06:28:49\",\n  \"scope\": [\"initb\", \"initc\"],\n  \"actions\": [{\n    \"code\": \"eosio.token\",\n    \"type\": \"transfer\",\n    \"recipients\": [\"initb\", \"initc\"],\n    \"authorization\": [{\n      \"account\": \"initb\",\n      \"permission\": \"active\"\n    }],\n    \"data\": \"000000000041934b000000008041934be803000000000000\"\n  }],\n  \"signatures\": [],\n  \"authorizations\": []\n}",
      "language": "json",
      "name": "JSON"
    }
  ]
}
[/block]