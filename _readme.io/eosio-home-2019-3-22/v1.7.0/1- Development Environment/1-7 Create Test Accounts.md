---
title: "1.7 Create Test Accounts"
excerpt: ""
---
[block:api-header]
{
  "title": "What is an account?"
}
[/block]
An account is a collection of authorizations, stored on the blockchain, and used to identify a sender/recipient. It has a flexible authorization structure that enables it to be owned either by an individual or group of individuals depending on **how** permissions have been configured. An account is required to send or receive a valid transaction to the blockchain

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
Throughout these tutorials the users `bob` and `alice` are used. Create two accounts using [cleos create account](https://developers.eos.io/eosio-cleos/reference#cleos-create-account)
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

[block:callout]
{
  "type": "info",
  "body": "EOSIO has a unique authorization structure that has added security for you account. You can minimize the exposure of your account by keeping the owner key cold, while using the key associated with your `active` permission. This way, if your `active` key were every compromised, you could regain control over your account with your `owner` key.",
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