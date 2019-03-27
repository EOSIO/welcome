---
title: "get info"
excerpt: "Gets current blockchain state JSON"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
This command does not accept any parameters. 
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
      "code": "$ ./cleos get info\n\n{\n  \"server_version\": \"7451e092\",\n  \"head_block_num\": 6980,\n  \"last_irreversible_block_num\": 6963,\n  \"head_block_id\": \"00001b4490e32b84861230871bb1c25fb8ee777153f4f82c5f3e4ca2b9877712\",\n  \"head_block_time\": \"2017-12-07T09:18:48\",\n  \"head_block_producer\": \"initp\",\n  \"recent_slots\": \"1111111111111111111111111111111111111111111111111111111111111111\",\n  \"participation_rate\": \"1.00000000000000000\"\n}",
      "language": "shell"
    }
  ]
}
[/block]