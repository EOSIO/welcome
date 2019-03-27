---
title: "get code"
excerpt: "Retrieves the code and ABI for an account."
---
[block:api-header]
{
  "title": "Positional Parameters"
}
[/block]
- `name` _TEXT_ - The name of the account whose code should be retrieved
[block:api-header]
{
  "title": "Options"
}
[/block]
- `-c,--code` _TEXT_ - The name of the file to save the contract _.wast_ to
- `-a,--abi` _TEXT_ - The name of the file to save the contract _.abi_ to
[block:api-header]
{
  "title": "Examples"
}
[/block]
Simply output the hash of eosio.token contract 
[block:code]
{
  "codes": [
    {
      "code": "$ cleos get code eosio.token\ncode hash: f675e7aeffbf562c033acfaf33eadff255dacb90d002db51c7ad7cbf057eb791",
      "language": "shell"
    }
  ]
}
[/block]
Retrieve and save abi for eosio.token contract
[block:code]
{
  "codes": [
    {
      "code": "$ cleos get code eosio.token -a eosio.token.abi\ncode hash: f675e7aeffbf562c033acfaf33eadff255dacb90d002db51c7ad7cbf057eb791\nsaving abi to eosio.token.abi",
      "language": "shell"
    }
  ]
}
[/block]
Retrieve and save wast code for eosio.token contract
[block:code]
{
  "codes": [
    {
      "code": "$ cleos get code eosio.token -c eosio.token.wast\ncode hash: f675e7aeffbf562c033acfaf33eadff255dacb90d002db51c7ad7cbf057eb791\nsaving wast to eosio.token.wast",
      "language": "shell"
    }
  ]
}
[/block]