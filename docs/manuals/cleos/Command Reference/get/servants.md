---
title: "servants"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]

[block:api-header]
{
  "title": "Info"
}
[/block]
**Command**
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos get servants",
      "language": "shell"
    }
  ]
}
[/block]
**Output**
[block:code]
{
  "codes": [
    {
      "code": "ERROR: RequiredError: account\nRetrieve accounts which are servants of a given account \nUsage: ./cleos get servants account\n\nPositionals:\n  account TEXT                The name of the controlling account",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Command"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos get servants inita",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Output"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"controlled_accounts\": [\n    \"tester\"\n  ]\n}",
      "language": "shell"
    }
  ]
}
[/block]