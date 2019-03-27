---
title: "create key"
excerpt: "Creates a new keypair and prints the public and private keys."
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
- `--r1` - Generate a key using the R1 curve (iPhone), instead of the K1 curve (Bitcoin)
- `-f, --file` _TEXT_ - Name of file to write private/public key output to. (Must be set, unless "--to-console" is passed.
- `--to-console` - Print private/public keys to console.
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos create key -f myKey.txt\n$ ./cleos create key --to-console",
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
      "code": "\n\nPrivate key: 5KCkcSxYKZfh5Cr8CCunS2PiUKzNZLhtfBjudaUnad3PDargFQo\nPublic key: EOS5uHeBsURAT6bBXNtvwKtWaiDSDJSdSmc96rHVws5M1qqVCkAm6",
      "language": "shell"
    }
  ]
}
[/block]