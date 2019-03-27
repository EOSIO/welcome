---
title: "system listproducers"
excerpt: "Returns a list of producers"
---
Returns a list of producers in text or json format including
- Producer account name
- Producer key
- Producer URL
- Producer's scaled votes
[block:api-header]
{
  "title": "Positional Arguments"
}
[/block]
None
[block:api-header]
{
  "title": "Options"
}
[/block]
`-h,--help` - Print this help message and exit
`-j,--json` - Output in JSON format
` -l,--limit` _UINT_ - The maximum number of rows to return
`-L,--lower` _TEXT_ - Lower bound value of key, defaults to first
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos system listproducers",
      "language": "text"
    }
  ]
}
[/block]