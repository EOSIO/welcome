---
title: "Permission"
excerpt: ""
---
[block:api-header]
{
  "title": "Content"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "[{\n\t\"name\": \"active\",\n\t\"parent\": \"owner\",\n\t\"required_auth\": {\n\t\t\"threshold\": 1,\n\t\t\"keys\": [{\n\t\t\t\"key\": \"EOS7d9A3uLe6As66jzN8j44TXJUqJSK3bFjjEEqR4oTvNAB3iM9SA\",\n\t\t\t\"weight\": 1\n\t\t}],\n\t\t\"accounts\": []\n\t}\n}]",
      "language": "json"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Description"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Definition",
    "0-0": "`name`",
    "1-0": "`parent`",
    "2-0": "`required_auth`",
    "3-0": "`threshold`",
    "4-0": "`keys`",
    "5-0": "`key`",
    "6-0": "`weight`",
    "8-0": "`name`",
    "7-0": "`accounts`",
    "9-0": "`parent`",
    "10-0": "`required_auth`",
    "11-0": "`threshold`",
    "12-0": "`keys`",
    "13-0": "`key`",
    "14-0": "`weight`",
    "15-0": "`accounts`",
    "0-1": "Name of the permission.",
    "1-1": "Parent of the permission",
    "2-1": "Required authorization to use permission",
    "3-1": "Threshold weight to pass authorization in order to use permission",
    "4-1": "Keys associates with the account",
    "5-1": "Public key for the account",
    "6-1": "Weight associated with the key",
    "7-1": "Accounts that have been authorized to use this permission"
  },
  "cols": 2,
  "rows": 8
}
[/block]

[block:api-header]
{
  "title": "Note"
}
[/block]
`owner` authority symbolizes ownership of an account. There are only a few transactions that require this authority, but most notably, are actions that make any kind of change to the `owner` authority. Generally, it is suggested that owner is kept in cold storage and not shared with anyone. `owner` can be used to recover another permission that may have been compromised.

`active` authority is used for transferring funds, voting for producers and making other high-level account changes.