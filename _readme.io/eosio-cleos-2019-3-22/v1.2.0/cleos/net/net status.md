---
title: "net status"
excerpt: "Returns status of a specific peer defined by url"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `host` _TEXT_ - The `hostname:port` to query status of connection (required)
[block:api-header]
{
  "title": "Options"
}
[/block]
None
[block:api-header]
{
  "title": "Example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos net status http://somepeer:1234\n#returns status of a configured peer",
      "language": "shell"
    }
  ]
}
[/block]