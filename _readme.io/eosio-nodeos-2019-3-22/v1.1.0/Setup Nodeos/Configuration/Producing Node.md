---
title: "Producing Node"
excerpt: ""
---
[block:callout]
{
  "type": "info",
  "body": "These instructions assume you already have an account on the network you are trying to produce blocks for.\n- [Create an account on node **without** system contracts](https://developers.eos.io/eosio-cleos/reference#cleos-create-account)\n- [Create an account on node/network **with** system contracts](https://developers.eos.io/eosio-cleos/reference#cleos-system-newaccount)"
}
[/block]

[block:api-header]
{
  "title": "Set the Producer's private keys used for signing blocks"
}
[/block]
You will need to set the private key for your producer. The public key should have an authority for the producer account defined above. 
[block:code]
{
  "codes": [
    {
      "code": "private-key = [\"PRODUCER_PUBLIC_KEY\",\"PRODUCER_PRIVATE_KEY\"]",
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
      "code": "# Default p2p port is 9876\np2p-peer-address = 123.456.78.9:9876",
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