---
title: "unlock"
excerpt: "Unlocks a wallet."
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
- `-n, --name` _TEXT_ - The name of the wallet to unlock.
- `--password` _TEXT_ - The password returned by wallet create.
[block:api-header]
{
  "title": "Usage"
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
  "title": "Outputs"
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