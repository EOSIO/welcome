---
title: "1.7 Create Test Accounts"
excerpt: ""
---
[block:api-header]
{
  "title": "What is an account?"
}
[/block]
An account is a collection of authorisations, stored on the blockchain, and used to identify a sender/recipient. It has a flexible authorisation structure that enables it to be owned either by an individual or group of individuals depending on **how** permissions have been configured. An account is required to send or receive a valid transaction to the blockchain

This tutorial series uses two "user" accounts, `bob` and `alice`, as well as the default `eosio` account for configuration. Additionally accounts are made for various contracts throughout this tutorial series.
[block:api-header]
{
  "title": "Step 1: Create Test Accounts"
}
[/block]

[block:html]
{
  "html": "<div class=\"no-your-public-key\">\n  In a previous step, you created a wallet and created a development key pair. You were asked to place that public key into a form, but either you skipped this step or have cookies disabled. You will need to replace YOUR_PUBLIC_KEY below with the public key you generated. \n</div>"
}
[/block]
Throughout these tutorials the accounts `bob` and `alice` are used. Create two accounts using [cleos create account](https://developers.eos.io/eosio-cleos/reference#cleos-create-account)
[block:code]
{
  "codes": [
    {
      "code": "cleos create account eosio bob YOUR_PUBLIC_KEY \ncleos create account eosio alice YOUR_PUBLIC_KEY",
      "language": "shell"
    }
  ]
}
[/block]
You should then see a confirmation message similar to the following for each command that confirms that the transaction has been broadcast.

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 40c605006de...  200 bytes  153 us\n#         eosio <= eosio::newaccount            {\"creator\":\"eosio\",\"name\":\"alice\",\"owner\":{\"threshold\":1,\"keys\":[{\"key\":\"EOS5rti4LTL53xptjgQBXv9HxyU...\nwarning: transaction executed locally, but may not be confirmed by the network yet    ]",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 2: Public Key"
}
[/block]
Note in `cleos` command a public key is associated with account `alice`. Each EOSIO account is associated with a public key.

Be aware that the account name is the only identifier for ownership. You can change the public key but it would not change the ownership of your EOSIO account.

Check which public key is associated with `alice` using [cleos get account](https://developers.eos.io/eosio-cleos/reference#cleos-get-account)
[block:code]
{
  "codes": [
    {
      "code": "cleos get account bob",
      "language": "shell"
    }
  ]
}
[/block]
You should see a message similar to the following:
[block:code]
{
  "codes": [
    {
      "code": "permissions:\n     owner     1:    1 EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\n        active     1:    1 EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV\nmemory:\n     quota:       unlimited  used:      2.66 KiB\n\nnet bandwidth:\n     used:               unlimited\n     available:          unlimited\n     limit:              unlimited\n\ncpu bandwidth:\n     used:               unlimited\n     available:          unlimited\n     limit:              unlimited",
      "language": "text"
    }
  ]
}
[/block]
Notice that actually `alice` has both `owner` and `active` public keys. EOSIO has a unique authorization structure that has added security for you account. You can minimize the exposure of your account by keeping the owner key cold, while using the key associated with your `active` permission. This way, if your `active` key were ever compromised, you could regain control over your account with your `owner` key. 

In term of authorization, if you have a `owner` permission you can change the private key of `active` permission. But you cannot do so other way around.
[block:callout]
{
  "type": "info",
  "body": "In this tutorial we are using the same public key for both `owner` and `active` for simplicity. In production network, two different keys are strongly recommended",
  "title": "Using Different Keys for Active/Owner on a PRODUCTION Network"
}
[/block]

[block:api-header]
{
  "title": "Troubleshooting"
}
[/block]
If you get an error while creating the account, make sure your wallet is unlocked
[block:code]
{
  "codes": [
    {
      "code": "cleos wallet list",
      "language": "shell"
    }
  ]
}
[/block]
You should see an asterisk (*) next to the wallet name, as seen below.
[block:code]
{
  "codes": [
    {
      "code": "Wallets:\n[\n  \"default *\"\n]",
      "language": "text"
    }
  ]
}
[/block]