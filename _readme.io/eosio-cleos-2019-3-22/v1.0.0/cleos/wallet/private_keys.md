---
title: "private_keys"
excerpt: ""
---
It is possible to query for the public and private key pairs of an individual wallet. The wallet must already be unlocked and you must give the password again.
[block:api-header]
{
  "title": "Options"
}
[/block]
`-n,--name` _TEXT_ - The name of the wallet to list keys from, otherwise - default
`--password` _TEXT_ - The password returned by wallet create
[block:code]
{
  "codes": [
    {
      "code": "./cleos wallet private_keys",
      "language": "javascript"
    }
  ]
}
[/block]