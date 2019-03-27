---
title: "get block"
excerpt: "Retrieves a full block from the blockchain."
---
[block:api-header]
{
  "title": "Positional Parameters"
}
[/block]
- `block` _TEXT_ - The number **or** ID of the block to retrieve
[block:api-header]
{
  "title": "Options"
}
[/block]
This command has no options
[block:api-header]
{
  "title": "Example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos get block 1\n$ ./cleos get block 0000000130d70e94e0022fd2fa035cabb9e542c34ea27f572ac90b5a7aa3d891",
      "language": "shell"
    }
  ]
}
[/block]
This will output a block object similar to the following
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"timestamp\": \"2018-03-02T12:00:00.000\",\n  \"producer\": \"\",\n  \"confirmed\": 1,\n  \"previous\": \"0000000000000000000000000000000000000000000000000000000000000000\",\n  \"transaction_mroot\": \"0000000000000000000000000000000000000000000000000000000000000000\",\n  \"action_mroot\": \"0000000000000000000000000000000000000000000000000000000000000000\",\n  \"schedule_version\": 0,\n  \"new_producers\": null,\n  \"header_extensions\": [],\n  \"producer_signature\": \"SIG_K1_111111111111111111111111111111111111111111111111111111111111111116uk5ne\",\n  \"transactions\": [],\n  \"block_extensions\": [],\n  \"id\": \"0000000130d70e94e0022fd2fa035cabb9e542c34ea27f572ac90b5a7aa3d891\",\n  \"block_num\": 1,\n  \"ref_block_prefix\": 3526296288\n}",
      "language": "json"
    }
  ]
}
[/block]