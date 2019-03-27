---
title: "unlock"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Unlocks a wallet.
[block:api-header]
{
  "title": "Command"
}
[/block]
To unlock a wallet, specify the password provided when it was created.
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos wallet unlock -n second-wallet --password PW5Ji6JUrLjhKAVn68nmacLxwhvtqUAV18J7iycZppsPKeoGGgBEw",
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
      "code": "Unlocked: 'second-wallet'",
      "language": "shell"
    }
  ]
}
[/block]