---
title: "unpack_action_data"
excerpt: "From packed to json action data form"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `account` _TEXT_ - The name of the account that hosts the contract
- `name` _TEXT_ - The name of the function that's called by this action
- `packed_action_data` _TEXT_ - The action data expressed as packed hex string 
[block:api-header]
{
  "title": "Options"
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
      "code": " cleos convert unpack_action_data eosio unlinkauth 000000008090b1ca000000000091b1ca000075982aea3055",
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
      "code": "{\n  \"account\": \"test1\",\n  \"code\": \"test2\",\n  \"type\": \"eosioeosio\"\n}",
      "language": "text"
    }
  ]
}
[/block]