---
title: "list"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Lists opened wallets, * = unlocked.
[block:api-header]
{
  "title": "Command"
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
  "title": "Output"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "Wallets:\n[\n  \"default *\",\n  \"second-wallet *\"\n]",
      "language": "shell"
    }
  ]
}
[/block]