---
title: "get currency balance"
excerpt: "Retrieve the balance of an account for a given currency"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
`contract` _TEXT_ - The contract that operates the currency
`account` _TEXT_ - The account to query balances for
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
Get balance of eosio from eosio.token contract for SYS symbol. 
[block:code]
{
  "codes": [
    {
      "code": "$ cleos get currency balance eosio.token eosio SYS\n999999920.0000 SYS",
      "language": "text"
    }
  ]
}
[/block]