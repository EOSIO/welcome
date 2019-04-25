---
title: "import"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Imports private key into wallet.
[block:api-header]
{
  "title": "Info"
}
[/block]
**Command**
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos wallet import",
      "language": "shell"
    }
  ]
}
[/block]
**Output**
[block:code]
{
  "codes": [
    {
      "code": "ERROR: RequiredError: key\nImport private key into wallet\nUsage: ./cleos wallet import [OPTIONS] key\n\nPositionals:\n  key TEXT                    Private key in WIF format to import\n\nOptions:\n  -n,--name TEXT              The name of the wallet to import key into",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Command"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos wallet import 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3",
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
      "code": "imported private key for: EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
      "language": "shell"
    }
  ]
}
[/block]