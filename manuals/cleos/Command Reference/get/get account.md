---
title: "get account"
excerpt: "Retrieves an account from the blockchain."
---
[block:api-header]
{
  "title": "Positional Parameters"
}
[/block]
- `name` _TEXT_ - The name of the account to retrieve
[block:api-header]
{
  "title": "Options"
}
[/block]
- `-j,--json` - Output in JSON format
[block:api-header]
{
  "title": "Example"
}
[/block]
## Get formatted data for user **eosio**
[block:code]
{
  "codes": [
    {
      "code": "$ cleos get account eosio\nprivileged: true\npermissions: \n     owner     1:    1 EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\n        active     1:    1 EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\nmemory: \n     quota:        -1 bytes  used:      1.22 Mb   \n\nnet bandwidth: (averaged over 3 days)\n     used:                -1 bytes\n     available:           -1 bytes\n     limit:               -1 bytes\n\ncpu bandwidth: (averaged over 3 days)\n     used:                -1 us   \n     available:           -1 us   \n     limit:               -1 us   \n\nproducers:     <not voted>",
      "language": "shell"
    }
  ]
}
[/block]
## Get JSON data for user **eosio**
[block:code]
{
  "codes": [
    {
      "code": "$ cleos get account eosio --json\n{\n  \"account_name\": \"eosio\",\n  \"privileged\": true,\n  \"last_code_update\": \"2018-05-23T18:00:25.500\",\n  \"created\": \"2018-03-02T12:00:00.000\",\n  \"ram_quota\": -1,\n  \"net_weight\": -1,\n  \"cpu_weight\": -1,\n  \"net_limit\": {\n    \"used\": -1,\n    \"available\": -1,\n    \"max\": -1\n  },\n  \"cpu_limit\": {\n    \"used\": -1,\n    \"available\": -1,\n    \"max\": -1\n  },\n  \"ram_usage\": 1279625,\n  \"permissions\": [{\n      \"perm_name\": \"active\",\n      \"parent\": \"owner\",\n      \"required_auth\": {\n        \"threshold\": 1,\n        \"keys\": [{\n            \"key\": \"EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\",\n            \"weight\": 1\n          }\n        ],\n        \"accounts\": [],\n        \"waits\": []\n      }\n    },{\n      \"perm_name\": \"owner\",\n      \"parent\": \"\",\n      \"required_auth\": {\n        \"threshold\": 1,\n        \"keys\": [{\n            \"key\": \"EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\",\n            \"weight\": 1\n          }\n        ],\n        \"accounts\": [],\n        \"waits\": []\n      }\n    }\n  ],\n  \"total_resources\": null,\n  \"delegated_bandwidth\": null,\n  \"voter_info\": {\n    \"owner\": \"eosio\",\n    \"proxy\": \"\",\n    \"producers\": [],\n    \"staked\": 0,\n    \"last_vote_weight\": \"0.00000000000000000\",\n    \"proxied_vote_weight\": \"0.00000000000000000\",\n    \"is_proxy\": 0,\n    \"deferred_trx_id\": 0,\n    \"last_unstake_time\": \"1970-01-01T00:00:00\",\n    \"unstaking\": \"0.0000 SYS\"\n  }\n}\n",
      "language": "shell"
    }
  ]
}
[/block]