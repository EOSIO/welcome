---
title: "list"
excerpt: "Lists opened wallets, * = unlocked."
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
None
[block:api-header]
{
  "title": "Options"
}
[/block]
None
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos wallet list",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Outputs"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "Wallets:\n[\n  \"default *\",\n  \"second-wallet *\"\n]\n\nor when there are no wallets\nWallets:\n[\n]\n",
      "language": "shell"
    }
  ]
}
[/block]