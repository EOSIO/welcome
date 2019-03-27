---
title: "get table"
excerpt: "Retrieves the contents of a database table."
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
`contract` _TEXT_ - The contract who owns the table
`scope` _TEXT_ - The scope within the contract in which the table is found
`table` _TEXT_ - The name of the table as specified by the contract abi
[block:api-header]
{
  "title": "Options"
}
[/block]
`-b,--binary` _UINT_ - Return the value as BINARY rather than using abi to interpret as JSON
`-l,--limit` _UINT_ - The maximum number of rows to return
`-k,--key` _TEXT_ - The name of the key to index by as defined by the abi, defaults to primary key
`-L,--lower` _TEXT_ - JSON representation of lower bound value of key, defaults to first
`-U,--upper` _TEXT_ - JSON representation of upper bound value value of key, defaults to last
[block:api-header]
{
  "title": "Example"
}
[/block]
Get the data from the accounts table for the eosio.token contract, for user eosio,
[block:code]
{
  "codes": [
    {
      "code": "$ cleos get table eosio.token eosio accounts\n{\n  \"rows\": [{\n      \"balance\": \"999999920.0000 SYS\"\n    }\n  ],\n  \"more\": false\n}\n",
      "language": "shell"
    }
  ]
}
[/block]