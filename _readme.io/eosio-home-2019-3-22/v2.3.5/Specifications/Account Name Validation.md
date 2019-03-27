---
title: "Account Name Validation"
excerpt: ""
---
[block:api-header]
{
  "title": "Rules"
}
[/block]
Below are rules regarding the creation of an `account name`.
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Rule",
    "0-0": "**length**",
    "0-1": "`<= 12 characters`\n`>= 1 character`",
    "1-0": "**available characters**",
    "1-1": "`.12345abcdefghijklmnopqrstuvwxyz`",
    "2-0": "***can* start / end with**",
    "2-1": "`12345abcdefghijklmnopqrstuvwxyz`",
    "3-0": "***cannot* start / end with**",
    "3-1": "`.`"
  },
  "cols": 2,
  "rows": 4
}
[/block]

[block:api-header]
{
  "title": "Regex"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "(^[a-z1-5.]{1,11}[a-z1-5]$)|(^[a-z1-5.]{12}[a-j1-5]$)",
      "language": "text",
      "name": "Regex"
    },
    {
      "code": "",
      "language": "javascript"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Examples"
}
[/block]
##Rejected
```#Invalid
.
aa.
booleanjulien
tbcox456
tbCOX```

## Accepted
```#Valid
abc
a.b
.a
booleanjulie
tbcox123
1.3.5
```