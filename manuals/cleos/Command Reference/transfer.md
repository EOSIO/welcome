---
title: "transfer"
excerpt: "Creates a new account on the blockchain."
---
[block:api-header]
{
  "title": "Positional Parameters"
}
[/block]
- `sender` _TEXT_ - The account sending EOS
- `recipient` _TEXT_ - The account receiving EOS
- `amount` _UINT_ - The amount of EOS to send
- `memo` _TEXT_ - The memo for the transfer

[block:api-header]
{
  "title": "Example"
}
[/block]
Transfer 1000 SYS from **inita** to **tester**
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos transfer inita tester 1000",
      "language": "shell"
    }
  ]
}
[/block]
The response will look something like this
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"transaction_id\": \"eb4b94b72718a369af09eb2e7885b3f494dd1d8a20278a6634611d5edd76b703\",\n  \"processed\": {\n    \"refBlockNum\": 2206,\n    \"refBlockPrefix\": 221394282,\n    \"expiration\": \"2017-09-05T08:03:58\",\n    \"scope\": [\n      \"inita\",\n      \"tester\"\n    ],\n    \"signatures\": [\n      \"1f22e64240e1e479eee6ccbbd79a29f1a6eb6020384b4cca1a958e7c708d3e562009ae6e60afac96f9a3b89d729a50cd5a7b5a7a647540ba1678831bf970e83312\"\n    ],\n    \"messages\": [{\n        \"code\": \"eos\",\n        \"type\": \"transfer\",\n        \"authorization\": [{\n            \"account\": \"inita\",\n            \"permission\": \"active\"\n          }\n        ],\n        \"data\": {\n          \"from\": \"inita\",\n          \"to\": \"tester\",\n          \"amount\": 1000,\n          \"memo\": \"\"\n        },\n        \"hex_data\": \"000000008040934b00000000c84267a1e80300000000000000\"\n      }\n    ],\n    \"output\": [{\n        \"notify\": [{\n            \"name\": \"tester\",\n            \"output\": { ... }\n          },{\n            \"name\": \"inita\",\n            \"output\": { ... }\n          }\n        ],\n        \"sync_transactions\": [],\n        \"async_transactions\": []\n      }\n    ]\n  }\n}",
      "language": "shell"
    }
  ]
}
[/block]