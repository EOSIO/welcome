---
title: "Permission"
excerpt: ""
---
A weighted security mechanism that determines whether or not a message is properly authorized by evaluating its signature(s) authority

[block:api-header]
{
  "title": "Overview"
}
[/block]
  * A permission is authorized by one or two keys
  * A key has weight (default:1) 
  * Permissions have thresholds (default:1) 
  * Thresholds determine if the weight of a transaction's signature is equal to or greater than the threshold of the permission. 
[block:api-header]
{
  "title": "Permission Types"
}
[/block]
- native permissions are the `owner` and `active` authorities. 
- custom named permissions that are available to further extend account management.
[block:api-header]
{
  "title": "Authority"
}
[/block]
- `owner` (native permission) symbolizes ownership of an account. There are only a few transactions that require this authority, but most notably, are actions that make any kind of change to the owner authority.  Generally, it is suggested that owner is kept in cold storage and not shared with anyone. `owner` can be used to recover another permission that may have been compromised.
- `active` (native permission) authority is used for transferring funds, voting for producers and making other high-level account changes. 
- `foo` (custom permission) configurable arbitrary collections of keys and authorization requirements. 

Custom permissions arwe flexible and can be used address numerous possible use cases when implemented. Much of this is up to the developer community in how they are employed, and what conventions if any, are adopted.

Permission for any given authority can be assigned to one or multiple `public keys` or a valid `account name`.
[block:api-header]
{
  "title": "Examples"
}
[/block]
## Default Account Configuration (Single-Sig)

This is how an account is configured after it has been created, it has a single key for both the **owner** and **active** permissions, both keys with a weight of **1** and permissions both with a threshold of **1**. The default configuration requires a single signature to authorize a action for the native permissions.

### @bob account authorities

| Permission | Account                                               | Weight | Threshold |
|------------|-------------------------------------------------------|--------|-----------|
| owner      |                                                       |        | 1         |
|            | EOS5EzTZZQQxdrDaJAPD9pDzGJZ5bj34H...                  | 1      |           |
| active     |                                                       |        | 1         |
|            | EOS61chK8GbH4ukWcbom8HgK95AeUfP8M...                  | 1      |           |

In the `@bob` account example @bob's owner key has a weight of 1, and the required threshold to push a transaction under that authority is 1. 

To push a transaction under the owner authority, only **@bob** needs to sign the transaction with his owner key for the transaction to be eligible for validation. This key would be stored in a _wallet_, and then processed using `eosc`.

## Multi-sig Account & Custom Permissions

The below examples are authorities for a fictional account named `@multisig`. In this scenario, two users are authoritized to both the `owner` and `active` permissions of a fictional `@multisig` account, with three users permissioned to a custom `publish` permission with varying weight. 

### @multisig account authorities

| Permission | Account                                               | Weight | Threshold |
|------------|-------------------------------------------------------|--------|-----------|
| owner      |                                                       |        | 2         |
|            | @bob                                                  | 1      |           |
|            | @stacy 	                                              | 1      |           |
| active     |                                                       |        | 1         |
|            | @bob                                                  | 1      |           |
|            | @stacy 	                                              | 1      |           |
| publish    |                                                       |        | 2         |
|            | @bob                                                  | 2      |           |
|            | @stacy 	                                              | 2      |           |
|            | EOS7Hnv4iBWo1pcEpP8JyFYCJLRUzYcXSqt...                | 1      |           |

In this scenario, a weight threshold of 2 is required to make changes to the `owner` permission level, which means that because all parties have a weight of **1**, all users are required to sign the transaction for it to be fully authorized. 

To send a transaction which requires the *active* authority, the threshold is set to **1**. This implies that only 1 signature is required authorize a action from the *active* authority of the account. 

There's also a third *custom named permission* called *publish*. For the sake of this example, the *publish* permission is used to publish posts to the @multisig's blog using a theoretical blog dApp. The *publish* permission has a threshold of **2**, **@bob** and **@stacy** both have a weight of *2*, and a **public key** has a weight of **1**. This implies that both **@bob** and **@stacy** can publish without an additional signature, whereas the **public key** requires an additional signature in order for a action under the public permission to be authorized. 

Thus the above permissions table implies that **@bob** and **@stacy**, as owners of the account, have _elevated priviledges_ similar to a moderator or editor. While this primitive example has limitations particularly with scalability and is not necessarily a good design, it does adequately demonstrate the flexible nature of the EOS permissions system.

Also, notice in the above table, permissions are set using both an **account name** and a **key**. At first glance this may seem trivial, however it does suggest some added dimensions of flexibility. 

### Observations

- @bob and @stacy can be explicitly identified as the owners of this account
- The public key cannot push a action under **publish** authority without an additional signature from @bob or @stacy
- @bob and @stacy can push a action under **publish** authority without any additional signatures.