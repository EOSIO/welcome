---
title: "system listbw"
excerpt: "List bandwidth delegated from an account"
---
Returns list of delegated bandwidth from an account in either text or json. 
[block:api-header]
{
  "title": "Positional Arguments"
}
[/block]
- `account` _TEXT_ - The account delegated bandwidth
[block:api-header]
{
  "title": "Options"
}
[/block]
`-h,--help` - Print this help message and exit
`-j,--json` - Output in JSON format
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos system listbw someaccount1",
      "language": "shell"
    }
  ]
}
[/block]