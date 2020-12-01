---
content_title: "Creating and Linking Custom Permissions"
link_text: "Creating and Linking Custom Permissions"
---
This tutorial shows how to creaet and use custom account permissions.

## Introduction
On an EOSIO blockchain, you can create various custom permissions for accounts.  A custom permission can later be linked to an action of a contract.  This permission system enables smart contracts to have a flexible authorization scheme.

This tutorial illustrates the creation of a custom permission, and subsequently, how to link the permission to an action. Upon completion of the steps, the contract's action will be prohibited from executing unless the authorization of the newly linked permission is provided. This allows you to have greater granularity of control over an account and its various actions.

With great power comes great responsibility. This functionality poses some challenges to the security of your contract and its users. Ensure you understand the concepts and steps prior to putting them to use.

[[info |Parent permission ]]
| When you create a custom permission, the permission will always be created under a parent permission.

If you have the authority of a parent permission which a custom permission was created under, you can always execute an action which requires that custom permission.

## Step 1. Create a Custom Permission
Firstly, let's create a new permission level on the `alice` account:

```shell
cleos set account permission alice upsert YOUR_PUBLIC_KEY owner -p alice@owner
```
A few things to note:

1. A new permission called **upsert** was created
2. The **upsert** permission uses the development public key as the proof of authority
3. This permission was created on the `alice` account

You can also specify authorities other than a public key for this permission, for example, a set of other accounts. Check [account permission](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/set/set-account) for more details.
## Step 2. Link Authorization to Your Custom Permission
Link the authorization to invoke the `upsert` action with the newly created permission:

```shell
cleos set action permission alice addressbook upsert upsert
```
In this example, we link the authorization to the `upsert` action created earlier in the addressbook contract.
## Step 3. Test it
Let's try to invoke the action with an `active` permission:

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
Now, try the **upsert** permission, this time, explicitly declaring the **upsert** permission we just created: (e.g. `-p alice@upsert`)

```text
cleos push action addressbook upsert '["alice", "alice", "liddel", 21, "Herengracht", "land", "dam"]' -p alice@upsert
```
Now it works:

```text
cleos push action addressbook upsert '["alice", "alice", "liddel", 21, "Herengracht", "land", "dam"] -p alice@upsert
executed transaction:

2fe21b1a86ca2a1a72b48cee6bebce9a2c83d30b6c48b16352c70999e4c20983  144 bytes  9489 us
#   addressbook <= addressbook::upsert          {"user":"alice","first_name":"alice","last_name":"liddel","age":21,"street":"Herengracht","city":"land",...
#   addressbook <= addressbook::notify          {"user":"alice","msg":"alice successfully modified record to addressbook"}
#         eosio <= addressbook::notify          {"user":"alice","msg":"alice successfully modified record to addressbook"}
#     abcounter <= abcounter::count             {"user":"alice","type":"modify"}
```

## What's Next

- [Payable Actions](90_payable-actions.md): Learn how write a smart contract that has payable actions. 
