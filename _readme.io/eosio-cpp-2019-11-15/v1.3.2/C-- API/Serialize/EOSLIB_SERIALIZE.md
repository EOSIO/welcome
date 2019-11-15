---
title: "EOSLIB_SERIALIZE"
excerpt: "Defines serialization and deserialization for a class"
---
[block:api-header]
{
  "title": "Parameters"
}
[/block]
* `TYPE` - the class to have its serialization and deserialization defined
* `MEMBERS` - a sequence of member names to be serialized  (field1)(field2)(field3)
[block:api-header]
{
  "title": "Example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": " EOSLIB_SERIALIZE( address, (account_name)(first_name)(last_name)(street)(city)(state) )",
      "language": "cplusplus"
    }
  ]
}
[/block]