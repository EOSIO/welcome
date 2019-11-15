---
title: "EOSLIB_SERIALIZE_DERIVED"
excerpt: "Defines serialization and deserialization for a class which inherits from other classes that have their serialization and deserialization defined"
---
[block:api-header]
{
  "title": "Parameters"
}
[/block]
* `TYPE` - the class to have its serialization and deserialization defined
* `BASE` - a sequence of base class names (basea)(baseb)(basec)
* `MEMBERS` - a sequence of member names.  (field1)(field2)(field3)

[block:api-header]
{
  "title": "Example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": " EOSLIB_SERIALIZE_DERIVED( token, (asset), (amount)(symbol)(contract))",
      "language": "cplusplus"
    }
  ]
}
[/block]