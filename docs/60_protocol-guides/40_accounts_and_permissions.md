---
content_title: Accounts and Permissions
---


# 1. Overview

An account identifies a participant in an EOSIO blockchain. A participant can be an individual or a group depending on the assigned permissions within the account. Accounts also represent the smart contract actors that push and receive actions to and from other accounts in the blockchain. Actions are always contained within transactions. A transaction can be one or more atomic actions.

Permissions associated with an account are used to authorize actions and transactions to other accounts. Each permission is linked to an authority table which contains a threshold that must be reached in order to allow the action associated with the given permission to be authorized for execution. The following diagram illustrates the relationship between accounts, permissions, and authorities.

```dot-svg

#accounts, permissions, authorities - accts_perms_auths.dot
#
#notes: * to see image copy/paste to https://dreampuf.github.io/GraphvizOnline
#       * image will be rendered by gatsby-remark-graphviz plugin in eosio docs.

digraph {
    rankdir=LR  #sets rank direction (left to right)
    newrank=true  #allows ranks inside subgraphs (important!)
    compound=true  #allows edges connecting nodes with subgraphs

    graph [style=dashed, nodesep=.2, ranksep=.8, splines=ortho]
    node [shape=box, height=.25]
    edge [arrowsize=.5]

    subgraph cluster_accts {
        label=Accounts
        rank=same
        "@alice", "@bob"
        more_accts [label="...", color=invis]
    }

    subgraph cluster_perms {
        label=Permissions
        rank=same
        subgraph cluster_alice_perm {
            label="@alice\npermissions"
            graph [style=solid]
            active -> owner
            family -> active
            friends -> family
            lawyer -> active  #disable permission sibling lawyer (w.r.t. family) for now
        }
        more_perms [label="...", color=invis]
    }

    "@alice" -> owner [lhead=cluster_alice_perm]

    subgraph cluster_auths {
        label=Authorities
        rank=same
        active_auth [
            shape=plaintext
            label=<
                <table border='0' cellborder='1' cellspacing='0'>
                    <tr><td colspan='2'>@alice active authority</td></tr>
                    <tr><td bgcolor='lightgray' colspan='2'>threshold</td></tr>
                    <tr><td colspan='2'>2</td></tr>
                    <tr><td bgcolor='lightgray'>accounts/keys</td><td bgcolor='lightgray'>weights</td></tr>
                    <tr><td>bob@active</td><td>2</td></tr>
                    <tr><td>stacy@active</td><td>2</td></tr>
                    <tr><td>EOS7Hnv4...</td><td>1</td></tr>
                    <tr><td>EOS3Wo1p...</td><td>1</td></tr>
                </table>
            >
        ]
        more_auths [label="...", color=invis]
    }

    active -> active_auth
}

```

The example above depicts `alice`'s account, her named permissions along with their hierarchical dependencies, and her linked `active` authority table. It also shows that a weight threshold of two must be reached in `alice`'s `active` authority in order to allow an action associated with the active permission to be executed by or on behalf of `alice`.


# 2. Accounts

Each account is identified by a human readable name between 1 and 12 characters in length. The characters can include a-z, 1-5, and optional dots (.) except the last character. This allows exactly one exa ($2^{60}$) accounts minus one:

$$
31^{1} \cdot \sum_{n=0}^{n=11} 32^{n} = 2^{60}-1 = 1,152,921,504,606,846,975
$$

which is in the order of $1 \times 10^{18}$.

Ownership of each account on an EOSIO blockchain is solely determined by the account name. Therefore, an account can update its keys without having to redistribute them to other parties.


## 2.1. Account Schema

Besides the account name, the blockchain associates other fields with each account instance stored in the chain database, such as ram quota/usage, cpu/net limits/weights, voter info, etc. (see `account` schema below). More importantly, each account holds the list of named permissions assigned to it. This allows a flexible permission structure that makes single or multi-user authorizations possible (see [3. Permissions](#3-permissions)).

### account schema

Name | Type | Description
-|-|-
`account_name` | `name` | encoded 13-char account name
`head_block_num` | `uint32_t` | last block account was referenced
`head_block_time` | `time_point` | last time account was referenced
`privileged` | `bool` | True, if privileged account, False otherwise
`last_code_update` | `time_point` | time account code was set/updated
`created` | `time_point` | time account was created
`core_liquid_balance` | `asset` | current balance of token asset
`ram_quota` | `int64_t` | maximum RAM amount for account
`net_weight` | `int64_t` | weight for net limit percentage (weight/total)
`cpu_weight` | `int64_t` | weight for cpu limit percentage (weight/total)
`net_limit` | `account_resource_limit` | total net used, available, and max
`cpu_limit` | `account_resource_limit` | total cpu used, available, and max
`ram_usage` | `int64_t` | amount of RAM in bytes used by account
`permissions` | array of `permission` | list of named [permissions](#3-permissions)
`total_resources` | `variant` | total cpu/net weights for all accounts
`self_delegated_bandwidth` | `variant` | cpu/net stake delegated from self
`refund_request` | `variant` | cpu/net refund amounts for token unstaking
`voter_info` | `variant` | name of voter, proxy or producers, vote stake
`rex_info` | `variant` | vote stake and rex balance if applicable

The `name` type consists of a 64-bit value that encodes alphanumeric characters into 5-bit chunks, except the last character, if any, which uses a 4-bit chunk. The `name` type is used to encode account names, action names, etc. The `time_point` type stores timestamps in microseconds. The `asset` type associates a currency or token symbol with a given amount. The `account_resource_limit` type keeps track of the amount used, available, and maximum that can be used in a given window for the given resource (NET or CPU). The `permission` type holds the list of permission levels associated with the account (see [3. Permissions](#3-permissions)).


## 2.2. Actions and Transactions

Besides identifying participants in an EOSIO blockchain, actions and transactions are the other reason for accounts to exist. An action requires one or more actors to push or send the action, and a receiver account to whom the action is directed. A receiver account is also needed when leaving proof, in an action receipt, that the action was pushed to the intended recipient.

In contrast, transactions are agnostic to accounts, although there is an indirect link to them through their associated keys. Transactions are signed using one or more signing keys belonging to the one or more actors involved in the actions that form the transaction. This can be the receiving account itself or other authorized actors specified on the authority table from the receiving account's permission.


# 3. Permissions

Permissions control what EOSIO accounts can do and how actions are authorized. This is accomplished through a flexible permission structure that links each account to a list of hierarchical named permissions, and each named permission to an authority table (see `permission` schema below).

## permission schema

Name | Type | Description
-|-|-
`perm_name` | `name` | named permission
`parent` | `name` | parent's named permission
`required_auth` | `authority` | associated [authority](#32-authority-table) table

The `parent` field links the named permission level to its parent permission. This is what allows hierarchical permission levels in EOSIO.


## 3.1. Permission Levels

A named permission may be created under another permission, thereby allowing a hierarchical parent-children permission structure. This makes implicit action authorizations possible by allowing a given `actor:child-permission` authorization within an action to be implicitly satisfied if the `actor:parent-permission` is also satisfied. An authorization quorum or "threshold" must still be met for the action to be authorized for execution (see [3.2.2. Authority Threshold](#322-authority-threshold)).

[[info | Contract-level Permissions]]
| It is also possible to create an implicit link between two accounts with the same named permission (for authorization satisfaction purposes). This can be achieved by associating an explicit named permission to the smart contract (different from the "minimum permission" for that `contract[::action]`). However, defining explicit `actor:permission` authorizations within actions is preferred versus associating permissions to the whole contract.

Every account has two default named permissions when created, owner and active. They have a parent-child relationship by default, although this can be customized by adding other permission levels and hierarchies.


### 3.1.1. Owner permission

The owner permission sits at the root of the permission hierarchy for every account. It is therefore the highest relative permission an account can have within its permission structure. Although the owner permission can do anything a lower level permission can, it is typically used for recovery purposes when a lower permission has been compromised. As such, keys associated with the owner permission are typically kept in cold storage, not used for signing regular operations.


### 3.1.2. Active permission

In the current EOSIO implementation, the implicit default permission linked to all actions is `active`, which sits one level below the `owner` permission within the hierarchy structure. As a result, the `active` permission can do anything the `owner` permission can, except changing the keys associated with the owner. The `active` permission is typically used for voting, transferring funds, and other account operations. For more specific actions, custom permissions are typically created below the `active` permission and mapped to specific contracts or actions. Refer to the [Creating and Linking Custom Permissions](../../40_smart-contract-guides/80_linking-custom-permission.md) for more details.

[[info | Custom Permissions]]
| EOSIO allows to create custom hierarchical permissions that stem from the owner permission. This allows finer control over action authorizations. It also strengthens security in case the `active` permission gets compromised.


## 3.2. Authority Table

Each account's permission can be linked to an authority table used to determine whether a given action authorization can be satisfied. The authority table contains the applicable permission name and threshold, the "factors" and their weights, all of which are used in the evaluation to determine whether the authorization can be satisfied. The permission threshold is the target numerical value that must be reached to satisfy the action authorization (see `authority` schema below).

### authority schema

Name | Type | Description
-|-|-
`threshold` | `uint32_t` | threshold value to satisfy authorization
`keys` | array of `key_weight` | list of public keys and weights
`accounts` | array of `permission_level_weight` | list of `account@permission` levels and weights
`waits` | array of `wait_weight` | list of time waits and weights

The `key_weight` type contains the actor's public key and associated weight. The `permission_level_weight` type consists of the actor's `account@permission` level and associated weight. The `wait_weight` contains the time wait and associated weight (used to satisfy action authorizations in delayed user transactions (see [Transactions Protocol: 3.6.3. Delayed User Transactions](20_transactions_protocol.md#363-delayed-user-transactions)). All of these types allow to define lists of authority factors that are used for satisfaction of action authorizations (see [3.2.1. Authority factors](#321-authority-factors) below).

### 3.2.1. Authority Factors

Every authority table linked to a given permission lists potential "factors" explicitly used in the evaluation of the action authorization. A factor type can be one of the following:

*   Actor's account name and permission level
*   Actor's public key
*   Time wait

The potential actors who may execute the action are specified by either public key or account name in the authority table. Time waits are special factors which are satisfied by publishing a transaction with a delay in excess of the defined time. These carry weights as well that may contribute to satisfy the threshold.


### 3.2.2. Authority Threshold

Authorization over a given action is determined by satisfying all explicit authorizations specified in the action instance (see [Transactions Protocol: 3.4.3. Action Instance](20_transactions_protocol.md#343-action-instance)). Those are in turn individually satisfied by evaluating each "factor" (account, public key, wait) for satisfaction (potentially recursively) and summing the weights of those that are satisfied. If the sum equals or exceeds the weight threshold, the action is authorized.


### 3.2.3. Authority Example

The authority table for `alice`'s `publish` named permission is shown below. According to its contents, in order to authorize an action under that permission, a threshold of two must be reached. Since both `bob@active` and `stacy@active` factors have a weight of two, either one can satisfy the action authorization. This means that either `bob` or `stacy` with a permission level of `active` or higher can independently execute any action under `alice`'s `publish` permission.


<table>
  <tr>
   <th> Permission
   </th>
   <th> Account / Public Key
   </th>
   <th> Weight
   </th>
   <th> Threshold
   </th>
  </tr>
  <tr>
   <td rowspan="4"> publish
   </td>
   <td> bob@active
   </td>
   <td> 2
   </td>
   <td rowspan="4"> 2
   </td>
  </tr>
  <tr>
   <td> stacy@active
   </td>
   <td> 2
   </td>
  </tr>
  <tr>
   <td> EOS7Hnv4iBfcw2...
   </td>
   <td> 1
   </td>
  </tr>
  <tr>
   <td> EOS3Wo1p9er7fh...
   </td>
   <td> 1
   </td>
  </tr>
</table>


Alternatively, it would require two acounts with public keys `EOS7Hnv4iBfcw2...` and `EOS3Wo1p9er7fh...` to satisfy the action authorization. This is because each public key has a weight of 1 in the authority table.


## 3.3. Permission Mapping

Any given account can define a mapping between any of its named permissions and a smart contract or action within that contract. This sets the "minimum permission" required for that `contract[::action]`. It does not afford, however, any other account any access or authority to execute that `contract[::action]`. This is by design and the process is controlled by a permission evaluation mechanism, described next.


## 3.4. Permission Evaluation

When determining whether an action is authorized to be executed, the EOSIO software first checks whether the signatures provided in the transaction are valid (see [3.4.2. Signature Validation](#342-signature-validation)). Then it proceeds to check the authorization of all the actions included in the transaction. This is where permissions are evaluated. If there is at least one action that fails to be authorized (by not meeting the authority threshold (see [3.2.2. Authority Threshold](#322-authority-threshold)), the transaction fails.


### 3.4.1. Custom Permissions

By default every account on the EOSIO blockchain is linked to the `active` permission. Again, this can be customized by creating children permissions under `active` or by creating alternate permissions under `owner` (see [3.1. Permission Levels](#31-permission-levels)). Creating custom permissions under `owner` (separate from `active`) is recommended. This is because if the keys associated with the `active` permission are compromised, the security of the account will not be compromised.

[[info | Use Case: Social Media]]
| Say we have a `publish` permission created for message posting on a social media application. However, we do not want to associate that permission with sensitive actions, such as transferring or withdrawing funds. Under this scenario, it makes sense to link the `social::post` action to the `publish` permission. This allows to define an authority structure which can authorize `post`, but cannot satisfy the default `active` permission for all other actions. That authority structure could delegate itself to a different account at any named permission level. If it did so to another `publish` permission on another account, that would be purely coincidental.


### 3.4.2. Signature Validation

Satisfying authorities linked to permissions involves first and foremost the validation/recovery of the public keys that signed the transaction. After a signed transaction is received by a node, the set of signatures is extracted from the transaction instance. The set of public keys are then recovered from the signatures. Then for all actions included in the transaction, the node checks that each `actor:permission` meets or exceeds the minimum permission as defined by the per-account permission links.

Once validated, the set of recovered keys are provided to the authorization manager instance along with the amount of time "waited". The authorization manager then proceeds to check whether the provided "factors" satisfy the authorities, potentially recursing into other linked permission levels/authorities (see [3.2. Authority Table](#32-authority-table) and [Transactions Protocol: 3.4. Verify Transaction](20_transactions_protocol.md#34-verify-transaction) for more information).
