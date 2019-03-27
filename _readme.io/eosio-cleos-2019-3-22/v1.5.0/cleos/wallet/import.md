---
title: "import"
excerpt: "Imports private key into wallet."
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
- `-n, --name` _TEXT_ - The name of the wallet to import key into.
- `--private-key` _TEXT_ - Private key in WIF format to import.
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos wallet import --private-key 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3",
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
      "code": "imported private key for: EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
      "language": "shell"
    }
  ]
}
[/block]