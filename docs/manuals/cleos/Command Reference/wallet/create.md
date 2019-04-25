---
title: "create"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Creates a wallet with the specified name. If no name is given, the wallet will be created with the name 'default'.
[block:api-header]
{
  "title": "Commands"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos wallet create\nor\n$ ./cleos wallet create -n second-wallet",
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