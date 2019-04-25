---
title: "open"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Opens an existing wallet.
[block:api-header]
{
  "title": "Commands"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos wallet open\nor\n$ ./cleos wallet open -n second-wallet",
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
      "code": "Wallets: [\n  \"default\"\n]\nor\nWallets: [\n  \"default\",\n  \"second-wallet\"\n]",
      "language": "shell"
    }
  ]
}
[/block]