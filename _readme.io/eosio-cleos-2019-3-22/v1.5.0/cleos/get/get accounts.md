---
title: "get accounts"
excerpt: "Retrieves all accounts associated with a defined public key."
---
[block:callout]
{
  "type": "info",
  "body": "This command will not return privileged accounts."
}
[/block]

[block:api-header]
{
  "title": "Positionals"
}
[/block]
`public_key` _TEXT_  - The public key to retrieve accounts for
[block:api-header]
{
  "title": "Options"
}
[/block]
There are no options for this command 
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ cleos get accounts EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt\n{\n  \"account_names\": [\n    \"testaccount\"\n  ]\n}",
      "language": "shell"
    }
  ]
}
[/block]