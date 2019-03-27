---
title: "get currency stats"
excerpt: "Retrieve the stats of for a given currency"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
`contract` _TEXT_  - The contract that operates the currency
`symbol` _TEXT_ - The symbol for the currency if the contract operates multiple currencies
[block:api-header]
{
  "title": "Options"
}
[/block]
There are no options for this subcommand
[block:api-header]
{
  "title": "Usage"
}
[/block]
Get stats of the SYS token from the eosio.token contract. 
[block:code]
{
  "codes": [
    {
      "code": "$ cleos get currency stats eosio.token SYS\n{\n  \"SYS\": {\n    \"supply\": \"1000000000.0000 SYS\",\n    \"max_supply\": \"10000000000.0000 SYS\",\n    \"issuer\": \"eosio\"\n  }\n}",
      "language": "text"
    }
  ]
}
[/block]