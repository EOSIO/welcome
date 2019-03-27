---
title: "get_required_keys"
excerpt: "Returns the required keys needed to sign a transaction."
---
[block:api-header]
{
  "title": "Examples"
}
[/block]
`transaction`
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"ref_block_num\": \"100\",\n  \"ref_block_prefix\": \"137469861\",\n  \"expiration\": \"2017-09-25T06:28:49\",\n  \"scope\": [\"initb\", \"initc\"],\n  \"actions\": [{\n    \"code\": \"currency\",\n    \"type\": \"transfer\",\n    \"recipients\": [\"initb\", \"initc\"],\n    \"authorization\": [{\n      \"account\": \"initb\",\n      \"permission\": \"active\"\n    }],\n    \"data\": \"000000000041934b000000008041934be803000000000000\"\n  }],\n  \"signatures\": [],\n  \"authorizations\": []\n}",
      "language": "json",
      "name": "JSON"
    }
  ]
}
[/block]
`available_keys`
[block:code]
{
  "codes": [
    {
      "code": "[\"EOS4toFS3YXEQCkuuw1aqDLrtHim86Gz9u3hBdcBw5KNPZcursVHq\",\n \"EOS7d9A3uLe6As66jzN8j44TXJUqJSK3bFjjEEqR4oTvNAB3iM9SA\",\n \"EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\"]",
      "language": "javascript",
      "name": "array of strings"
    }
  ]
}
[/block]