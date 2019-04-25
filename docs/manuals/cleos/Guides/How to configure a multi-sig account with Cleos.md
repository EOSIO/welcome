---
title: "How to configure a multi-sig account with Cleos"
excerpt: ""
---
[block:callout]
{
  "type": "info",
  "body": "This tutorial assumes the following:\n1. You have `nodeos` built and running on localhost.\n2. You have already setup an account\n3. That account has some EOS allocated to it."
}
[/block]
``
[block:code]
{
  "codes": [
    {
      "code": "./cleos set account permission multisig active '{\"threshold\" : 1, \"accounts\" :  [{\"permission\":{\"actor\":\"eosio\",\"permission\":\"active\"},\"weight\":1},{\"permission\":{\"actor\":\"customera\",\"permission\":\"active\"},\"weight\":1}]}' owner -p multisig@owner",
      "language": "shell"
    }
  ]
}
[/block]