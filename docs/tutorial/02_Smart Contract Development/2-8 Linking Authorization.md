---
title: "2.8 Linking Authorization"
excerpt: ""
---
## Introduction
EOSIO enables for authorization of a particular action on a particular contract to be directly linked to a permission on an account. This enables all kinds of unique interactions, but the one we'll cover here is to permit a contract's action to execute without other permission than a specified one. This enable you to have segregation of control. 

With great power, comes great responsibility. This functionality poses some challenges for security, so please make sure you understand the concepts and steps below. 

Let's see how does that work exactly!
## Step 1. Create a Custom Permission
Firstly let us create a new permission level on alice's account

```shell
cleos set account permission alice upsert YOUR_PUBLIC_KEY -p alice@owner
```
Few things to note:

1. We created a new permission called `upsert`
2. The 'upsert' permission uses the development public key as the mean of authority verification
3. We create this permission on alice's account

Also good to know you can also specify other authorities than a public key for this permission. For example, a set of other accounts. Check [account permission](https://developers.eos.io/eosio-cleos/reference#cleos-set-account) for more details 
## Step 2. Link Authorization to Your Custom Permission
Link the authorization to invoke the upsert with the new permission we created:

```shell
cleos set action permission alice addressbook upsert upsert
```
In this example, we link the authorization to the upsert action we created earlier in the addressbook contract.
## Step 3. Test it
Firstly let us try to invoke the action with `active` permission:

```shell
cleos push action addressbook upsert '["alice", "alice", "liddel", 21, "Herengracht", "land", "dam"]' -p alice@active
```
You should see an error like the one below:

```text
Error 3090005: Irrelevant authority included
Please remove the unnecessary authority from your action!
Error Details:
action declares irrelevant authority '{"actor":"alice","permission":"active"}'; minimum authority is {"actor":"alice","permission":"upsert"}
```
Try with upsert permission again:

```text
cleos push action addressbook upsert '["alice", "alice", "liddel", 21, "Herengracht", "land", "dam"]' -p alice@upsert
```
It works now:

```text
cleos push action addressbook upsert '["alice", "alice", "liddel", 21, "Herengracht", "land", "dam"] -p alice@upsert
executed transaction:

2fe21b1a86ca2a1a72b48cee6bebce9a2c83d30b6c48b16352c70999e4c20983  144 bytes  9489 us
#   addressbook <= addressbook::upsert          {"user":"alice","first_name":"alice","last_name":"liddel","age":21,"street":"Herengracht","city":"land",...
#   addressbook <= addressbook::notify          {"user":"alice","msg":"alice successfully modified record to addressbook"}
#         eosio <= addressbook::notify          {"user":"alice","msg":"alice successfully modified record to addressbook"}
#     abcounter <= abcounter::count             {"user":"alice","type":"modify"}
```
