---
title: "Understanding Accounts and Permissions"
excerpt: ""
---
# TL;DR

An **account** is a human-readable identifier that is stored on the blockchain. Every account has two default *named permissions*, owner and active. Developers can also introduce custom named permissions. Each named permission has a threshold that must be met for a transaction signed under that authority to be considered valid. Transactions are signed by utilizing a **client** that has a loaded and unlocked wallet. A wallet is software that protects and makes use of your keys. These keys may or may not be granted permission to an account authority on the blockchain.

# Wallets

Wallets are clients that store keys that may or may not be associated with the permissions of one or more accounts. Ideally, a wallet has a locked (encrypted) and unlocked (decrypted) state that is protected by a high entropy password. The EOSIO/eos repository comes bundled with a command line interface client called `cleos` that interfaces with a lite-client called `keosd` and together, they demonstrate this pattern.

# Accounts

An account is a human-readable name that is stored on the blockchain. It can be owned through authorization by an individual or group of individuals depending on permissions configuration. An account is required to transfer or push any valid transaction to the blockchain. 

# Authorization and Permissions

Permissions are arbitrary names used to define the requirements for a transaction sent on behalf of that permission. Permissions can be assigned for authority over specific contract actions by "linking authorization" or linkauth. 

Every account has two _native_ named permissions

- `owner` authority symbolizes ownership of an account. There are only a few transactions that require this authority, but most notably, are actions that make any kind of change to the owner authority. Generally, it is suggested that owner is kept in cold storage and not shared with anyone. `owner` can be used to recover another permission that may have been compromised.
- `active` authority is used for transferring funds, voting for producers and making other high-level account changes. 

Every permission name has a "parent." Parents possess the authority to change any of the permissions settings for any and all of their children. 

In addition to the _native_ permissions, an account can possess custom named permissions that are available to further extend account management. Custom permissions are incredibly flexible and address numerous possible use cases when implemented. Much of this is up to the developer community in how they are employed, and what conventions if any, are adopted.

Custom permissions are arbitrary and impotent until they have been linked to an action. 

Permission for any given authority can be assigned to one or multiple `public keys` or a valid `account name`. 

# Putting it all Together

Below is the combination of all the above concepts and some loose examples of how they might be practically employed. 

## Default Account Configuration (Single-Sig)

This is how an account is configured after it has been created, it has a single key for both the **owner** and **active** permissions, both keys with a weight of **1** and permissions both with a threshold of **1**. The default configuration requires a single signature to authorize a action for the native permissions.

### __*@bob account authorities*__

| Permission | Account                                               | Weight | Threshold |
|------------|-------------------------------------------------------|--------|-----------|
| owner      |                                                       |        | 1         |
|            | EOS5EzTZZQQxdrDaJAPD9pDzGJZ5bj34HaAb8yuvjFHGWzqV25Dch | 1      |           |
| active     |                                                       |        | 1         |
|            | EOS61chK8GbH4ukWcbom8HgK95AeUfP8MBPn7XRq8FeMBYYTgwmcX | 1      |           |

In the `@bob` account example, this table shows that @bob's owner key has a permissioned weight of 1, and the required threshold to push a transaction under that authority is 1. 

To push a transaction under the owner authority, only **@bob** needs to sign the transaction with his owner key for the transaction to be eligible for validation. This key would be stored in a _wallet_, and then processed using `cleos`.

## Multi-sig Account & Custom Permissions
[block:callout]
{
  "type": "info",
  "title": "Important Notice",
  "body": "While accounts are fully capable of being configured for multi-sig, for most situations the eosio.msig contract is preferred for emulating multi-signature functionality on an account."
}
[/block]
The below examples are authorities for a fictional account named `@multisig`. In this scenario, two users are authoritized to both the `owner` and `active` permissions of a fictional `@multisig` account, with three users permissioned to a custom `publish` permission with varying weight. 

### __*@multisig account authorities*__

| Permission | Account                                               | Weight | Threshold |
|------------|-------------------------------------------------------|--------|-----------|
| owner      |                                                       |        | 2         |
|            | bob@active                                                  | 1      |           |
|            | stacy@active 	                                              | 1      |           |
| active     |                                                       |        | 1         |
|            | bob@active                                                  | 1      |           |
|            | stacy@active 	                                              | 1      |           |
| publish    |                                                       |        | 2         |
|            | bob@active                                                  | 2      |           |
|            | stacy@active 	                                              | 2      |           |
|            | EOS7Hnv4iBWo1pcEpP8JyFYCJLRUzYcXSqt...                | 1      |           |

In this scenario, a weight threshold of 2 is required to make changes to the `owner` permission level, which means that because all parties have a weight of **1**, all users are required to sign the transaction for it to be fully authorized. 

To send a transaction which requires the *active* authority, the threshold is set to **1**. This implies that only 1 signature is required authorize a action from the *active* authority of the account. 

There's also a third *custom named permission* called *publish*. For the sake of this example, the *publish* permission is used to publish posts to the @multisig's blog using a theoretical blog dApp. The *publish* permission has a threshold of **2**, **@bob** and **@stacy** both have a weight of *2*, and a **public key** has a weight of **1**. This implies that both **@bob** and **@stacy** can publish without an additional signature, whereas the **public key** requires an additional signature in order for a action under the public permission to be authorized. 

Thus the above permissions table implies that **@bob** and **@stacy**, as owners of the account, have _elevated priviledges_ similar to a moderator or editor. While this primitive example has limitations particularly with scalability and is not necessarily a good design, it does adequately demonstrate the flexible nature of the EOSIO permissions system.

Also, notice in the above table, permissions are set using both an **account name** and a **key**. At first glance this may seem trivial, however it does suggest some added dimensions of flexibility. 

**Observations**

- @bob and @stacy can be explicitly identified as the owners of this account
- The public key cannot push an action under **publish** authority without an additional signature from @bob or @stacy
- @bob and @stacy can push an action under **publish** authority without any additional signatures.