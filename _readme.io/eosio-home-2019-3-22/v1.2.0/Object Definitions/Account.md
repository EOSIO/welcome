---
title: "Account"
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
      "code": "{\n\t\"name\": \"tester\",\n\t\"eos_balance\": 0,\n\t\"staked_balance\": 1,\n\t\"unstaking_balance\": 0,\n\t\"last_unstaking_time\": \"1969-12-31T23:59:59\",\n\t\"permissions\": [{\n\t\t\"name\": \"active\",\n\t\t\"parent\": \"owner\",\n\t\t\"required_auth\": {\n\t\t\t\"threshold\": 1,\n\t\t\t\"keys\": [{\n\t\t\t\t\"key\": \"EOS7d9A3uLe6As66jzN8j44TXJUqJSK3bFjjEEqR4oTvNAB3iM9SA\",\n\t\t\t\t\"weight\": 1\n\t\t\t}],\n\t\t\t\"accounts\": []\n\t\t}\n\t}",
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
    "1-0": "`eos_balance`",
    "2-0": "`staked_balance`",
    "3-0": "`unstaking_balance`",
    "4-0": "`last_unstaking_time`",
    "5-0": "`permissions`",
    "6-0": "`name`",
    "7-0": "`parent`",
    "8-0": "`required_auth`",
    "9-0": "`threshold`",
    "10-0": "`keys`",
    "11-0": "`key`",
    "12-0": "`weight`",
    "13-0": "`accounts`",
    "0-1": "Name of the account",
    "1-1": "Total balance, the sum of staked and unstaked tokens.",
    "2-1": "Balance of account's tokens that have been staked.",
    "3-1": "Balance of account's tokens that are \"unstaked\" or liquid.",
    "4-1": "Unix timestamp representing the last time tokens were unstaked",
    "5-1": "See \"[Permission](/docs/permission)\"",
    "6-1": "Name of the permission",
    "7-1": "Parent of the permission",
    "8-1": "Required authorization to use permission",
    "9-1": "Threshold weight to pass authorization in order to use permission"
  },
  "cols": 2,
  "rows": 6
}
[/block]