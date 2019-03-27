---
title: "create_key"
excerpt: "Create a key pair within the wallet"
---
[block:api-header]
{
  "title": "Positional Parameters"
}
[/block]
`key_type` _TEXT_ - "K1" or "R1" Key type to create
[block:api-header]
{
  "title": "Options"
}
[/block]
-n,--name TEXT=default The name of the wallet to create key into
[block:api-header]
{
  "title": "Description"
}
[/block]
Creates a key pair within the wallet so that you don't need to manually import it like you would with `cleos create key`. By default this will create a key with the type "favored" by the wallet, which is a K1 key. But this command also lets you create a key in R1 format.
[block:api-header]
{
  "title": "Commands"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet create_key K1",
      "language": "shell"
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
      "code": "Created new private key with a public key of: \"EOS67xHKzQArkWZN6rKLCq7NLvaj8kurwxzRxoTVz6cgDJkiWdGug\"",
      "language": "shell"
    }
  ]
}
[/block]