---
content_title: "1.6: Create Test Accounts"
link_text: "1.6: Create Test Accounts"
---
## What is an account?
An account is a collection of authorisations, stored on the blockchain, and used to identify a sender/recipient. It has a flexible authorisation structure that enables it to be owned either by an individual or group of individuals depending on **how** permissions have been configured. An account is required to send or receive a valid transaction to the blockchain

This tutorial series uses two "user" accounts, `bob` and `alice`, as well as the default `eosio` account for configuration. Additionally accounts are made for various contracts throughout this tutorial series.
## Step 1: Create Test Accounts

[[caution | Noy your public key]]
| In a previous step, you created a wallet and created a development key pair. You were asked to place that public key into a form, but either you skipped this step or have cookies disabled. You will need to replace YOUR_PUBLIC_KEY below with the public key you generated.

Throughout these tutorials the accounts `bob` and `alice` are used. Create two accounts using [cleos create account](https://developers.eos.io/eosio-cleos/reference#cleos-create-account)

```shell
cleos create account eosio bob YOUR_PUBLIC_KEY
cleos create account eosio alice YOUR_PUBLIC_KEY
```
You should then see a confirmation message similar to the following for each command that confirms that the transaction has been broadcast.

Result
```shell
executed transaction: 40c605006de...  200 bytes  153 us
#         eosio <= eosio::newaccount            {"creator":"eosio","name":"alice","owner":{"threshold":1,"keys":[{"key":"EOS5rti4LTL53xptjgQBXv9HxyU...
warning: transaction executed locally, but may not be confirmed by the network yet    ]
```

## Step 2: Public Key
Note in `cleos` command a public key is associated with account `alice`. Each EOSIO account is associated with a public key.

Be aware that the account name is the only identifier for ownership. You can change the public key but it would not change the ownership of your EOSIO account.

Check which public key is associated with `alice` using [cleos get account](https://developers.eos.io/eosio-cleos/reference#cleos-get-account)

```shell
cleos get account alice
```
You should see a message similar to the following:

```text
permissions:
     owner     1:    1 EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
        active     1:    1 EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
memory:
     quota:       unlimited  used:      2.66 KiB

net bandwidth:
     used:               unlimited
     available:          unlimited
     limit:              unlimited

cpu bandwidth:
     used:               unlimited
     available:          unlimited
     limit:              unlimited
```
Notice that actually `alice` has both `owner` and `active` public keys. EOSIO has a unique authorization structure that has added security for your account. You can minimize the exposure of your account by keeping the owner key cold, while using the key associated with your `active` permission. This way, if your `active` key were ever compromised, you could regain control over your account with your `owner` key.

In term of authorization, if you have a `owner` permission you can change the private key of `active` permission. But you cannot do so other way around.
[[info]]
| Using Different Keys for Active/Owner on a PRODUCTION Network
In this tutorial we are using the same public key for both `owner` and `active` for simplicity. In production network, two different keys are strongly recommended

## Troubleshooting
If you get an error while creating the account, make sure your wallet is unlocked

```shell
cleos wallet list
```
You should see an asterisk (*) next to the wallet name, as seen below.

```text
Wallets:
[
  "default *"
]
```
