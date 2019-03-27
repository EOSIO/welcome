---
title: "create account"
excerpt: "Creates a new account on the blockchain."
---
[block:callout]
{
  "type": "info",
  "body": "If the system contract is loaded, (for example a production network) then use [cleos system newaccount](#cleos-system-newaccount) instead"
}
[/block]

[block:api-header]
{
  "title": "Positionals"
}
[/block]
- ` creator` _TEXT_ - The name of the account creating the new account
- `name` _TEXT_ - The name of the new account
- `OwnerKey` _TEXT_ - The owner public key for the new account
- `ActiveKey` _TEXT_ - The active public key for the new account
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos create account inita tester PRIVATE_KEY_1 PRIVATE_KEY_2",
      "language": "shell"
    }
  ]
}
[/block]