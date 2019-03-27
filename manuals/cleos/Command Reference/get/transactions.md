---
title: "transactions"
excerpt: "Retrieves all transactions with specific account name referenced in their scope."
---
[block:api-header]
{
  "title": "Positional Parameters"
}
[/block]
- `account_name` _TEXT_ - name of account to query on
- `skip_seq` _TEXT_ - Number of most recent transactions to skip (0 would start at most recent transaction)
- `num_seq` _TEXT_ - Number of transactions to return
[block:api-header]
{
  "title": "Examples"
}
[/block]
Get transactions belonging to eosio
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos get transactions eosio\n[\n  {\n    \"transaction_id\": \"eb4b94b72718a369af09eb2e7885b3f494dd1d8a20278a6634611d5edd76b703\",\n    ...\n  },\n  {\n    \"transaction_id\": \"6acd2ece68c4b86c1fa209c3989235063384020781f2c67bbb80bc8d540ca120\",\n    ...\n  },\n  ...\n]",
      "language": "shell"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "These transactions will not exist on your blockchain",
  "title": "Important Note"
}
[/block]