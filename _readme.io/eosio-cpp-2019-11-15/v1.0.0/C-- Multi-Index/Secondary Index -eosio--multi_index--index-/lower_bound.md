---
title: "lower_bound"
excerpt: "**Member Access**"
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Searches for the object_type with the lowest secondary key that is greater than or equal to a given secondary key.
[block:api-header]
{
  "title": "Methods"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "const_iterator lower_bound( secondary_key_type&& secondary )const",
      "language": "cplusplus"
    }
  ]
}
[/block]
or
[block:code]
{
  "codes": [
    {
      "code": "const_iterator lower_bound( const secondary_key_type&& secondary )const",
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
`secondary` - Secondary key that establishes the target value for the lower bound search
[block:api-header]
{
  "title": "Returns"
}
[/block]
- an iterator pointing to the object in the secondary index that has the lowest secondary key that is greater than or equal to `secondary`

**OR**

- the `end` iterator if an object could not be found, including if the table does not exist