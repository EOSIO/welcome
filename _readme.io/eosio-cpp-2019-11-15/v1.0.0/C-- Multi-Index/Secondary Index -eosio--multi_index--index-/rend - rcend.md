---
title: "rend & rcend"
excerpt: "**Iterator**"
---
[block:api-header]
{
  "title": "Methods"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "const_iterator rend()const",
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
      "code": "const_iterator rcend()const",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Returns"
}
[/block]
Returns a reverse iterator pointing to the virtual row representing just before the first row of the table (assuming one exists); cannot be dereferenced; can be advanced forward but not backward.