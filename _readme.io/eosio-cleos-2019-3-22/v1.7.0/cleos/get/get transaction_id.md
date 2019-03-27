---
title: "get transaction_id"
excerpt: "Get transaction id given transaction object"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `transaction`  _TEXT_ - The JSON string or filename defining the transaction for which transaction id we want to retrieve (required). The JSON file must contain a packed transaction for it to function correctly.
[block:api-header]
{
  "title": "Options"
}
[/block]
- `-h,--help`  - Print this help message and exit
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos get transaction_id ./ptrx.json",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb",
      "language": "shell"
    }
  ]
}
[/block]