---
title: "Account"
excerpt: ""
---
An account a unique identifier and a requirement to interact with an EOSIO blockchain. Unlike most other cryptocurrencies, transfers are sent to a human readable account name instead of a public key, while keys attributed to the account are used to sign transactions. 

[block:api-header]
{
  "title": "Anatomy"
}
[/block]
Every account has two native permissions, `owner` and `active,` respectively. The `owner` permission enables account recovery and high-level operations against an account. While the `active` permission is used for anything related to value, for example: staking, voting and token transfers. 

Accounts can also have custom permissions, which are created through a transaction authorized by the `active` permission. 
[block:api-header]
{
  "title": "Authorization"
}
[/block]
Each permission is authorized by one or more keys.