---
title: "iterator_to"
excerpt: "**Member Access**"
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Returns a secondary index iterator to the given object in the Multi-Index table.
[block:api-header]
{
  "title": "Method"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "const_iterator iterator_to( const object_type& obj ) const",
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
An iterator to the given object.