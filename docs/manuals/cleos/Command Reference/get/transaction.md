---
title: "transaction"
excerpt: "Retrieves a transaction from the blockchain."
---
[block:api-header]
{
  "title": "Positional Parameters"
}
[/block]
`id`` _TEXT_ - ID of the transaction to retrieve
[block:api-header]
{
  "title": "Options"
}
[/block]
There are no options for this command
[block:api-header]
{
  "title": "Info"
}
[/block]
**Command**
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos get transaction",
      "language": "shell"
    }
  ]
}
[/block]
**Output**
[block:api-header]
{
  "title": "Example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos get transaction eb4b94b72718a369af09eb2e7885b3f494dd1d8a20278a6634611d5edd76b703\n{\n  \"transaction_id\": \"eb4b94b72718a369af09eb2e7885b3f494dd1d8a20278a6634611d5edd76b703\",\n  \"processed\": {\n    \"refBlockNum\": 2206,\n    \"refBlockPrefix\": 221394282,\n    \"expiration\": \"2017-09-05T08:03:58\",\n    \"scope\": [\n      \"inita\",\n      \"tester\"\n    ],\n    \"signatures\": [\n      \"1f22e64240e1e479eee6ccbbd79a29f1a6eb6020384b4cca1a958e7c708d3e562009ae6e60afac96f9a3b89d729a50cd5a7b5a7a647540ba1678831bf970e83312\"\n    ],\n    \"messages\": [{\n        \"code\": \"eos\",\n        \"type\": \"transfer\",\n        \"authorization\": [{\n            \"account\": \"inita\",\n            \"permission\": \"active\"\n          }\n        ],\n        \"data\": {\n          \"from\": \"inita\",\n          \"to\": \"tester\",\n          \"amount\": 1000,\n          \"memo\": \"\"\n        },\n        \"hex_data\": \"000000008040934b00000000c84267a1e80300000000000000\"\n      }\n    ],\n    \"output\": [{\n        \"notify\": [{\n            \"name\": \"tester\",\n            \"output\": {\n              \"notify\": [],\n              \"sync_transactions\": [],\n              \"async_transactions\": []\n            }\n          },{\n            \"name\": \"inita\",\n            \"output\": {\n              \"notify\": [],\n              \"sync_transactions\": [],\n              \"async_transactions\": []\n            }\n          }\n        ],\n        \"sync_transactions\": [],\n        \"async_transactions\": []\n      }\n    ]\n  }\n}",
      "language": "shell"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "Important Note",
  "body": "The above transaction id will not exist on your blockchain"
}
[/block]