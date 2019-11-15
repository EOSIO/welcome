---
title: "extract_secondary_key"
excerpt: "**Utilities**"
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Returns the secondary key value for an object from a secondary index.
[block:api-header]
{
  "title": "Method"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "static auto extract_secondary_key(const object_type& obj)",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Parameters"
}
[/block]
`obj` - a const reference to the desired object
[block:api-header]
{
  "title": "Returns"
}
[/block]
A key value for the given object, for that index.