---
title: "Transaction"
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
      "code": "{\n\t\"ref_block_num\": \"100\",\n\t\"ref_block_prefix\": \"137469861\",\n\t\"expiration\": \"2017-09-25T06:28:49\",\n\t\"scope\": [\"initb\", \"initc\"],\n\t\"actions\": [{\n\t\t\"code\": \"currency\",\n\t\t\"type\": \"transfer\",\n\t\t\"recipients\": [\"initb\", \"initc\"],\n\t\t\"authorization\": [{\n\t\t\t\"account\": \"initb\",\n\t\t\t\"permission\": \"active\"\n\t\t}],\n\t\t\"data\": \"000000000041934b000000008041934be803000000000000\"\n\t}],\n\t\"signatures\": [],\n\t\"authorizations\": []\n}",
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
    "0-0": "`ref_block_num`",
    "1-0": "`ref_block_prefix`",
    "2-0": "`expiration`",
    "3-0": "`scope`",
    "4-0": "`actions`",
    "5-0": "`code`",
    "6-0": "`type`",
    "7-0": "`recipients`",
    "8-0": "`authorization`",
    "9-0": "`account`",
    "10-0": "`permission`",
    "11-0": "`data`",
    "12-0": "`signatures`",
    "13-0": "`authorizations`",
    "1-1": "Lower 32 bits of the calculated id of the last irreversible block.",
    "0-1": "Calculated block number of the last irreversible block.",
    "3-1": "Accounts who will be affect by the transaction.",
    "2-1": "Date and time of when the transaction will expire.",
    "5-1": "Contract name receiving the transaction.",
    "6-1": "Action name to be executed.",
    "7-1": "Accounts involved in the action execution.",
    "10-1": "Level of permission to be used on authorization.",
    "9-1": "Account giving authorization of action.",
    "8-1": "Authorization of action.",
    "4-1": "Action(s) to be executed in the transaction.",
    "11-1": "Data to be sent with action.",
    "12-1": "Signature(s) of account(s) pushing the transaction.",
    "13-1": "Authorization(s) of account(s) pushing the transaction."
  },
  "cols": 2,
  "rows": 14
}
[/block]