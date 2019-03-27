---
title: "lock"
excerpt: "Locks a wallet."
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
- `-n, --name` _TEXT_ - The name of the wallet to lock
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet lock\nor\n$ ./cleos wallet lock -n second-wallet",
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
      "code": "Locked: 'default'\nor\nLocked: 'second-wallet'",
      "language": "shell"
    }
  ]
}
[/block]