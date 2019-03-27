---
title: "create"
excerpt: "Creates a wallet with the specified name. If no name is given, the wallet will be created with the name 'default'."
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
- `-n, --name` _TEXT_ - The name of the new wallet
- `-f, --file` _TEXT_ - Name of file to write wallet password output to. (Must be set, unless "--to-console" is passed
- `--to-console` - Print password to console
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos wallet create --to-console\nor\n$ ./cleos wallet create -n second-wallet --to-console\nor\n$ ./cleos wallet create --name my-new-wallet --file my-new-wallet.txt",
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
      "code": "Creating wallet: default\nSave password to use in the future to unlock this wallet.\nWithout password imported keys will not be retrievable.\n\"PW5JD9cw9YY288AXPvnbwUk5JK4Cy6YyZ83wzHcshu8F2akU9rRWE\"\nor\nCreating wallet: second-wallet\nSave password to use in the future to unlock this wallet.\nWithout password imported keys will not be retrievable.\n\"PW5Ji6JUrLjhKAVn68nmacLxwhvtqUAV18J7iycZppsPKeoGGgBEw\"",
      "language": "shell"
    }
  ]
}
[/block]