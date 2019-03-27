---
title: "sign"
excerpt: "Arbitrarily sign a string, such as sJSON or a filename."
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `transaction` _TEXT_ - The JSON string or filename defining the transaction to sign (required)

[block:api-header]
{
  "title": "Options"
}
[/block]
* `-k,--private-key` _TEXT_ - The private key that will be used to sign the transaction
*`-c,--chain-id` _TEXT_ - The chain id that will be used to sign the transaction
* `-p,--push-transaction` - Push transaction after signing