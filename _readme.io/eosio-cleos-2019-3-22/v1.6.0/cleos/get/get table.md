---
title: "get table"
excerpt: "Retrieves the contents of a database table."
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
`contract` _TEXT_ - The contract who owns the table
`scope` _TEXT_ - The scope within the contract in which the table is found
`table` _TEXT_ - The name of the table as specified by the contract abi
[block:api-header]
{
  "title": "Options"
}
[/block]
`-b,--binary` _UINT_ - Return the value as BINARY rather than using abi to interpret as JSON
`-l,--limit` _UINT_ - The maximum number of rows to return
`-L,--lower` _TEXT_ - JSON representation of lower bound value of key, defaults to first
`--show-payer` _BOOLEAN_ - show RAM payer (default: false)
`-r,--reverse` _BOOLEAN_ - Iterate in reverse order (default: false)
`-U,--upper` _TEXT_ - JSON representation of upper bound value value of key, defaults to last
`--index` _TEXT_ - Index number, 1 - primary (first), 2 - secondary index (in order defined by multi_index), 3 - third index, etc. Number or name of index can be specified, e.g. 'secondary' or '2'.
`--key-type` _TEXT_ - The key type of --index, primary only supports (i64), all others support (i64, i128, i256, float64, float128, sha256). Special type 'name' indicates an account name.
[block:api-header]
{
  "title": "Usage"
}
[/block]
Find the bid name with the lowest bid
[block:code]
{
  "codes": [
    {
      "code": "cleos get table eosio eosio namebids --key-type i64 --index 2 -r -l 1",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"rows\": [{\n      \"newname\": \"com\",\n      \"high_bidder\": \"a123\",\n      \"high_bid\": 100000,\n      \"last_bid_time\": \"1541667021500000\"\n    }\n  ],\n  \"more\": true\n}",
      "language": "json",
      "name": "Result"
    }
  ]
}
[/block]
Or to show all name bids from high to low, including the RAM payer information
[block:code]
{
  "codes": [
    {
      "code": "cleos get table eosio eosio namebids --key-type i64 --index 2 -r --show-payer",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"rows\": [{\n      \"data\": {\n        \"newname\": \"com\",\n        \"high_bidder\": \"a123\",\n        \"high_bid\": 100000,\n        \"last_bid_time\": \"1541667021500000\"\n      },\n      \"payer\": \"a123\"\n    },{\n      \"data\": {\n        \"newname\": \"abc\",\n        \"high_bidder\": \"a123\",\n        \"high_bid\": 110000,\n        \"last_bid_time\": \"1541667021500000\"\n      },\n      \"payer\": \"a123\"\n    },{\n      \"data\": {\n        \"newname\": \"ddd\",\n        \"high_bidder\": \"a123\",\n        \"high_bid\": 120000,\n        \"last_bid_time\": \"1541667021500000\"\n      },\n      \"payer\": \"a123\"\n    },{\n      \"data\": {\n        \"newname\": \"zoo\",\n        \"high_bidder\": \"a123\",\n        \"high_bid\": 9990000,\n        \"last_bid_time\": \"1541667022000000\"\n      },\n      \"payer\": \"a123\"\n    }\n  ],\n  \"more\": false\n}",
      "language": "json",
      "name": "Result"
    }
  ]
}
[/block]