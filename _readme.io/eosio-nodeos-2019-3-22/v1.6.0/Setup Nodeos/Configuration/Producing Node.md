---
title: "Producing Node"
excerpt: ""
---
[block:callout]
{
  "type": "info",
  "body": "These instructions assume you are attempting to launch a producing node on a network with **system contracts loaded.** These instructions will not work on a default development node using native functionality, or one without system contracts loaded."
}
[/block]

[block:api-header]
{
  "title": "Register your account as a producer"
}
[/block]
In order for your account to be eligible as a producer, you will need to register the account as a producer

## Example using `cleos system regproducer`

[block:code]
{
  "codes": [
    {
      "code": "cleos system regproducer accountname1 EOS1234534... http://producer.site Antarctica",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Set Producer Name"
}
[/block]
Set the `producer-name` option in config.ini to your account, like so
[block:code]
{
  "codes": [
    {
      "code": "# ID of producer controlled by this node (e.g. inita; may specify multiple times) (eosio::producer_plugin)\nproducer-name = youraccount",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Set the Producer's signature-provider"
}
[/block]
You will need to set the private key for your producer. The public key should have an authority for the producer account defined above. 

`signature-provider` is defined with a tuple
-  `public-key` - A valid EOSIO public key in form of a string.
- `provider-spec` - It's a string formatted like <provider-type>:<data>
- `provider-type` - KEY or KEOSD

## Using a Key
[block:code]
{
  "codes": [
    {
      "code": "signature-provider = PUBLIC_SIGNING_KEY=KEY:PRIVATE_SIGNING_KEY\n\n//Example\n//signature-provider = EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV=KEY:5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3\n",
      "language": "text"
    }
  ]
}
[/block]
## Using Keosd
You can also use Keosd instead of hard-defining keys. 
[block:code]
{
  "codes": [
    {
      "code": "signature-provider = KEOSD:<data>   \n\n//Example\n//EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV=KEOSD:https://127.0.0.1:8888",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Define a peers list"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# Default p2p port is 9876\np2p-peer-address = 123.255.78.9:9876",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Load the Required Plugins"
}
[/block]
In your [config.ini](doc:configuration-file), confirm the following plugins are loading or append them if necessary. 
[block:code]
{
  "codes": [
    {
      "code": "plugin = eosio::chain_plugin\nplugin = eosio::producer_plugin",
      "language": "text"
    }
  ]
}
[/block]