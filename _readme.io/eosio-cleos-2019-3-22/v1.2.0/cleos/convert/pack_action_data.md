---
title: "pack_action_data"
excerpt: "From json action data to packed form"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `account` _TEXT_ - The name of the account that hosts the contract
- `name` _TEXT_ - The name of the function that's called by this action
- `unpacked_action_data` _TEXT_ - The action data expressed as json
[block:api-header]
{
  "title": "Options"
}
[/block]
none
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": " cleos convert pack_action_data eosio unlinkauth '{\"account\":\"test1\", \"code\":\"test2\", \"type\":\"eosioeosio\"}'",
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
      "code": "000000008090b1ca000000000091b1ca000075982aea3055",
      "language": "text"
    }
  ]
}
[/block]