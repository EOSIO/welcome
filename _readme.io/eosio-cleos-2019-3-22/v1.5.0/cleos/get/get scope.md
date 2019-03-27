---
title: "get scope"
excerpt: "Retrieve a list of scopes and tables owned by a contract"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `contract` _TEXT_ -  The contract who owns the table (required)
[block:api-header]
{
  "title": "Options"
}
[/block]
- `-t,--table` _TEXT_ -  The name of the table as a filter
- `-l,--limit` _UINT_ -  The maximum number of rows to return
- `-L,--lower` _TEXT_ -  Lower bound of scope
- `-U,--upper` _TEXT_ -  Upper bound of scope
- `-r,--reverse` - Iterate in reverse order
[block:api-header]
{
  "title": "Example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos get scope eosio",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"rows\": [{\n      \"code\": \"eosio\",\n      \"scope\": \"...........e\",\n      \"table\": \"userres\",\n      \"payer\": \"...........e\",\n      \"count\": 1\n    },{\n      \"code\": \"eosio\",\n      \"scope\": \"..........e\",\n      \"table\": \"userres\",\n      \"payer\": \"..........e\",\n      \"count\": 1\n    },{\n      \"code\": \"eosio\",\n      \"scope\": \".........a.e\",\n      \"table\": \"userres\",\n      \"payer\": \".........a.e\",\n      \"count\": 1\n    },{\n      \"code\": \"eosio\",\n      \"scope\": \".........e\",\n      \"table\": \"userres\",\n      \"payer\": \".........e\",\n      \"count\": 1\n    },{\n      \"code\": \"eosio\",\n      \"scope\": \".........e.e\",\n      \"table\": \"userres\",\n      \"payer\": \".........e.e\",\n      \"count\": 1\n    },{\n      \"code\": \"eosio\",\n      \"scope\": \"........e\",\n      \"table\": \"userres\",\n      \"payer\": \"........e\",\n      \"count\": 1\n    },{\n      \"code\": \"eosio\",\n      \"scope\": \".......e\",\n      \"table\": \"userres\",\n      \"payer\": \".......e\",\n      \"count\": 1\n    },{\n      \"code\": \"eosio\",\n      \"scope\": \".......e.e\",\n      \"table\": \"userres\",\n      \"payer\": \".......e.e\",\n      \"count\": 1\n    },{\n      \"code\": \"eosio\",\n      \"scope\": \"......bank\",\n      \"table\": \"userres\",\n      \"payer\": \"......bank\",\n      \"count\": 1\n    },{\n      \"code\": \"eosio\",\n      \"scope\": \"......e\",\n      \"table\": \"userres\",\n      \"payer\": \"......e\",\n      \"count\": 1\n    }\n  ],\n  \"more\": \".....e.....e\"\n}\n",
      "language": "shell"
    }
  ]
}
[/block]