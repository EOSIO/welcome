---
content_title: "Creating and Linking Custom Permissions"
link_text: "Creating and Linking Custom Permissions"
---

EOSIO permissions control what an account is authorized to execute on an EOSIO blockchain. EOSIO permissions are powerful, flexible, and customizable. This tutorial explains custom permissions and illustrates how to use them. In the tutorial you will create a custom permission,  link a permission to an action, unlink a permission from an action, and delete a custom permission.
## Before You Begin

This tutorial requires the following:

* Access to a running blockchain. Click on this link for instructions on [running a blockchain](01_before-you-begin/10_running-a-blockchain.md)
* An EOSIO account and access to the account keys. Click on this link for information on [Accounts and Permissions](01_before-you-begin/20_accounts-and-permissions.md)
* Some knowledge of smart contracts. Follow this link for more information [hello world tutorial.](../30_getting-started-guide/25_hello-world.md)

## What is a Custom Permission
A custom permission is an arbitrarily named permission created and associated with an EOSIO account. When an account is created two permissions are created by default; `owner` and `active`. You can create a new permission, a custom permission, as a child permission of `owner`, `active` or another custom permission. Custom permissions require a public and private key pair. Custom permissions may be linked to smart contract actions to specify the permission required to execute that action. EOSIO accounts and permissions enable flexible and highly granular control over accounts and smart contract actions.

[[info]]
| The permission `eosio.code` is a special permission that allows smart contracts to call inline actions. The EOSIO blockchain performs an authorization check when an inline action is called from a smart contract. Smart contracts do not have access to account keys so cannot add authorization. Adding `eosio.code` to an account permission provides explicit permission for that account permission to execute an inline action. For information on how to add the `eosio.code` see [cleos set account permission](https://developers.eos.io/manuals/eos/v2.2/cleos/command-reference/set/set-account-permission).

## Why use a Custom Permission

Use custom permssions to improve the security on your account and for calling specific transactions. Use custom permissions to reduce the use of the `owner` and `active` keys and to limit the risk of the `owner` and `active` permissions being compromised.

[[info]]
| Custom permissions always have a parent permission. The parent permission has the authority to execute the same transactions as the custom permission. The parent permission also has the authority to recover the custom permission keys if the related custom permission is compromised.

## Using Custom Permissions
The following section explains in detail what you will do, what is required, and provides a simple smart contract you can use for testing.  

The following examples illustrate how to:

* [Create a Custom Permission](#create-custom-permissions)
* [Link a Custom Permission](#link-the-custom-permissions)
* [Unlink a Custom Permission](#unlink-the-permission)
* [Delete a Custom Permission](#delete-custom-permissions)

You will use:

* An account called _bob_, and the keys to control this account stored in a local wallet.
* An account called _scholder_, and the keys to control this account stored in a local wallet.
* A smart contract called _hello_ which has been deployed to the _scholder_ account. This smart contract has three actions:
  - _what(eosio::name user)_
  - _why(eosio::name user)_
  - _how(eosio::name user)_

You will create two custom permissions on the _bob_ account:

* A custom permission, _customp1_,  whose parent is `active`
* A custom permission, _customp2_, whose parent is _customp1_

You will link the custom permissions to smart contract actions:

* Link _customp1_ to _what(eosio::name user)_
* Link _customp2_ to _how(eosio::name user)_

You will see that the `active` permission can call all the actions.
You will see that the _customp1_  permission can call the _why_ and _how_ actions.
You will see that the _customp2_  permission can only call the _how_ action.

You will then unlink and delete the _customp2_ permission.

### The simple smart contract
The simple smart contract code used in the examples:

```c++

#include <eosio/eosio.hpp>
class [[eosio::contract]] hello : public eosio::contract {
  public:
      using eosio::contract::contract;
      [[eosio::action]] void what( eosio::name user ) {
         print( "hi, what do you want ", user);
      }

      [[eosio::action]] void why( eosio::name user ) {
         print( "why not ", user);
      }

      [[eosio::action]] void how( eosio::name user ) {
         print( "how are you ", user);
      }
};

```

Deploy this smart contract to your running blockchain.

[[info]]
| This simple sample  smart contract does not do any authorization checking, i.e. does not use  `require_auth`. This tutorial demonstrates **native authorization checking**. Click on this link for more information on [securing your contract.](https://developers.eos.io/manuals/eosio.cdt/latest/best-practices/securing_your_contract/#1-authorization-checks)

## Create Custom Permissions
To use a custom permission you need to create a custom permission. 

Create custom permission _customp1_, with the parent `active`, on the _bob_ account using the command [cleos set account permission](https://developers.eos.io/manuals/eos/v2.2/cleos/command-reference/set/set-account-permission):


```shell
cleos set account permission bob customp1 EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D active -p bob@active
```

The output should be similar to:

```console
executed transaction: 97e2af6966b40ea0b523402110c6a5592862c5ad2abbaad20c9bbf2f68017c98  160 bytes  145 us
#         eosio <= eosio::updateauth            {"account":"bob","permission":"customp1","parent":"active","auth":{"threshold":1,"keys":[{"key":"EOS...
```

Now create custom permission _customp2_, with the parent _customp1_, on the _bob_ account:

```shell
cleos set account permission bob customp2 EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D customp1 -p bob@active

```

The output should be similar to:

```console
executed transaction: 8b5e88d0d1cea6dd31a4967912d575d62391348345c58b6071aba7fb93d709b3  160 bytes  129 us
#         eosio <= eosio::updateauth            {"account":"bob","permission":"customp2","parent":"customp1","auth":{"threshold":1,"keys":[{"key":"E...
```

You can create a custom permission without specifying the parent, this will default to a parent of `active`:

```shell
cleos set account permission bob customp3 EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D -p bob@active
```

The output should be similar to:

```console
executed transaction: 42158f0a35bdce9e8374691285e12e5e517ab4d4831a68c8e3a2bb22e88fda7c  160 bytes  165 us
#         eosio <= eosio::updateauth            {"account":"bob","permission":"customp3","parent":"active","auth":{"threshold":1,"keys":[{"key":"EOS...
```

Let’s check the account:

```shell
cleos get account bob --json
```

The output will be similar to:

```json
{
  "account_name": "bob",
  "head_block_num": 23485,
  "head_block_time": "2021-05-06T07:46:19.000",
  "privileged": false,
  "last_code_update": "1970-01-01T00:00:00.000",
  "created": "2021-05-06T05:07:27.500",
  "ram_quota": -1,
  "net_weight": -1,
  "cpu_weight": -1,
  "net_limit": {
    "used": -1,
    "available": -1,
    "max": -1
  },
  "cpu_limit": {
    "used": -1,
    "available": -1,
    "max": -1
  },
  "ram_usage": 4414,
  "permissions": [{
      "perm_name": "active",
      "parent": "owner",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D",
            "weight": 1
          }
        ],
        "accounts": [],
        "waits": []
      }
    },{
      "perm_name": "customp1",
      "parent": "active",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D",
            "weight": 1
          }
        ],
        "accounts": [],
        "waits": []
      }
    },{
      "perm_name": "customp2",
      "parent": "customp1",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D",
            "weight": 1
          }
        ],
        "accounts": [],
        "waits": []
      }
    },,{
      "perm_name": "customp3",
      "parent": "active",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D",
            "weight": 1
          }
        ],
        "accounts": [],
        "waits": []
      }
    },{
      "perm_name": "owner",
      "parent": "",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D",
            "weight": 1
          }
        ],
        "accounts": [],
        "waits": []
      }
    }
  ],
  "total_resources": null,
  "self_delegated_bandwidth": null,
  "refund_request": null,
  "voter_info": null,
  "rex_info": null
}
```

[[info]]
| For simplicity we are using the same public/private key pair for each permission. For production systems we recommend that you create and use new key pairs for each permission.

## Link the Custom Permissions
Once you have a custom permission you can link this custom permission to a smart contract action, requiring that permission level authorization, or higher, to execute the action.

Link the custom permission _customp1_, to the _what_ action using the command [cleos set action permission](https://developers.eos.io/manuals/eos/v2.2/cleos/command-reference/set/set-action-permission):

```shell
cleos set action permission bob scholder what customp1 -p bob@active
```

The output should be similar to:

```console
executed transaction: 64198d1cc5f7dedf8809b86f22801eb004d50365ba72f8e2833ed191c6f6e30b  128 bytes  471 us
#         eosio <= eosio::linkauth              {"account":"bob","code":"scholder","type":"what","requirement":"customp1"}
```

Link the custom permission _customp2_, to the _how_ action using the command `cleos set action permission` (link)`:

```shell
cleos set action permission bob scholder how customp2 -p bob@active
```

The output should be similar to:

```console
executed transaction: 64198d1cc5f7dedf8809b86f22801eb004d50365ba72f8e2833ed191c6f6e30b  128 bytes  471 us
#         eosio <= eosio::linkauth              {"account":"bob","code":"scholder","type":"how","requirement":"customp2"}
```

### Test It
We now have linked two custom permissions, _customp1_, and _customp2_, to two actions, _what_, and _how_.

* `active` is able to call _why_, _what_, and _how_. The permission `active` is the parent of _customp1_ so is able to call anything that _customp1_ can call.
* _customp1_ is able to call _what_, and _how_.  The permission _customp1_ is the parent of _customp2_ so is able to call anything that _customp2_ can call.
* _customp2_ is able to call _how_ 

We can test this by using the permissions to call the smart contract actions.

#### Call the actions using the `active` permission

Call _why_ with bob@active:

```shell
cleos push action scholder why '["name"]' -p bob@active
```

The output should be similar to:

```console
executed transaction: 43b6ad4ce7a52d7281ccd2800caa02d5278ee714de36fefe9624bff621378402  104 bytes  129 us
#      scholder <= scholder::why               {"user":"name"}
>> why not name
```

Call _what_ with bob@active:

```shell
cleos push action scholder what '["name"]' -p bob@active
```
The output should be similar to:

```console
executed transaction: 43b6ad4ce7a52d7281ccd2800caa02d5278ee714de36fefe9624bff621378402  104 bytes  129 us
#      scholder <= scholder::what               {"user":"name"}
>> hi, what do you want name
```

Call _how_ with bob@active:


```shell
cleos push action scholder how '["name"]' -p bob@active
```

The output should be similar to:

```console
executed transaction: 43b6ad4ce7a52d7281ccd2800caa02d5278ee714de36fefe9624bff621378402  104 bytes  129 us
#      scholder <= scholder::how               {"user":"name"}
>> how are you name
```

We see that the `active` permission can sucessfully call all the actions.

#### Call the actions using the _customp1_ permission

Call _why_ with bob@customp1:

```shell
cleos push action scholder why '["name"]' -p bob@customp1
```

The output should be similar to:

```console
Error 3090005: Irrelevant authority included
Please remove the unnecessary authority from your action!
Error Details:
action declares irrelevant authority '{"actor":"bob","permission":"customp1"}'; minimum authority is {"actor":"bob","permission":"active"}
```

Call _what_ with bob@customp1:

```shell
cleos push action scholder what '["name"]' -p bob@customp1
```

The output should be similar to:

```console
executed transaction: 43b6ad4ce7a52d7281ccd2800caa02d5278ee714de36fefe9624bff621378402  104 bytes  129 us
#      scholder <= scholder::what               {"user":"name"}
>> why not name
```

Call _how_ with bob@customp1:

```shell
cleos push action scholder how '["name"]' -p bob@customp1
```
The output should be similar to:

```console
executed transaction: 43b6ad4ce7a52d7281ccd2800caa02d5278ee714de36fefe9624bff621378402  104 bytes  129 us
#      scholder <= scholder::how               {"user":"name"}
>> how are you name
```

We see that the _customp1_ permission can sucessfully call the _what_ and _how_ actions, but fails to call the _why_ action.

#### Call the actions using the _customp2_ permission

Call _why_ with bob@customp2:

```shell
cleos push action scholder why '["name"]' -p bob@customp2
```

The output should be similar to:

```console
Error 3090005: Irrelevant authority included
Please remove the unnecessary authority from your action!
Error Details:
action declares irrelevant authority '{"actor":"bob","permission":"customp2"}'; minimum authority is {"actor":"bob","permission":"active"}
```

Call _what_ with bob@customp2:

```shell
cleos push action scholder what '["name"]' -p bob@customp2
```

The output should be similar to:

```console
Error 3090005: Irrelevant authority included
Please remove the unnecessary authority from your action!
Error Details:
action declares irrelevant authority '{"actor":"bob","permission":"customp2"}'; minimum authority is {"actor":"bob","permission":"customp1"}
```

Call _how_ with bob@customp2:

```shell
cleos push action scholder how '["name"]' -p bob@customp2
```

The output should be similar to:

```shell
executed transaction: 43b6ad4ce7a52d7281ccd2800caa02d5278ee714de36fefe9624bff621378402  104 bytes  129 us
#      scholder <= scholder::how               {"user":"name"}
>> how are you name
```

We see that the _customp2_ permission can sucessfully call the _how_ action, but fails to call the _why_ and _what_ actions.

## Unlink The Permission
You can unlink permissions to a smart contract action.

Now we will unlink the _customp2_ permission from the _how_ action using the command [cleos set action permission](https://developers.eos.io/manuals/eos/v2.2/cleos/command-reference/set/set-action-permission):

```shell
cleos set action permission bob scholder how NULL -p bob@active

```
The output should be similar to:

```shell
executed transaction: 50fe754760a1b8bd0e56f57570290a3f5daa509c090deb54c81a721ee7048201  120 bytes  242 us
#         eosio <= eosio::unlinkauth            {"account":"bob","code":"scholder","type":"how"}

```

### Test It Again
We have unlinked the _customp2_ permission.

We now have one linked custom permission, _customp1_  which can call _what_. The _customp2_ permission is now unlinked so should not be able to call anything.

* `active` is able to call _why_, _what_, and _how_. The permission `active` is the parent of _customp1_ so is able to call anything that _customp1_ can call.
* _customp1_ is able to call _what_.
* _customp2_ is not linked to any action so should be unable to call an action.

#### Call the _how_ action using the all the permissions to show what permission has the authority to call the action

Call _how_ with bob@active:

```shell
cleos push action scholder how '["name"]' -p bob@active
```

The output should be similar to:

```console
executed transaction: 43b6ad4ce7a52d7281ccd2800caa02d5278ee714de36fefe9624bff621378402  104 bytes  129 us
#      scholder <= scholder::how               {"user":"name"}
>> how are you name
```

Call _how_ with bob@customp1:

```shell
cleos push action scholder how '["name"]' -p bob@customp1
```

The output should be similar to:

```console
Error 3090005: Irrelevant authority included
Please remove the unnecessary authority from your action!
Error Details:
action declares irrelevant authority '{"actor":"bob","permission":"customp1"}'; minimum authority is {"actor":"bob","permission":"active"}
```

Call _how_ with bob@customp2:

```shell
cleos push action scholder how '["name"]' -p bob@customp2
```

The output should be similar to:

```console
Error 3090005: Irrelevant authority included
Please remove the unnecessary authority from your action!
Error Details:
action declares irrelevant authority '{"actor":"bob","permission":"customp2"}'; minimum authority is {"actor":"bob","permission":"active"}
```

## Delete Custom Permissions
Now you have unlinked the _customp2_ permission you can delete this permission using the command [cleos set account permission](https://developers.eos.io/manuals/eos/v2.2/cleos/command-reference/set/set-account-permission):

```shell
cleos set account permission bob customp2 NULL active -p bob@active
```

The output should be similar to:

```console
executed transaction: 3f3e58707e5548ec34f5655327b1110c18d455c9ee0a6cffc102d7bc4e0a6cdb  112 bytes  472 us
#         eosio <= eosio::deleteauth            {"account":"bob","permission":"customp2"}
```
Let’s check the account:

```shell
cleos get account bob --json
```

The output will be similar to:

```json
{
  "account_name": "bob",
  "head_block_num": 23485,
  "head_block_time": "2021-05-06T07:46:19.000",
  "privileged": false,
  "last_code_update": "1970-01-01T00:00:00.000",
  "created": "2021-05-06T05:07:27.500",
  "ram_quota": -1,
  "net_weight": -1,
  "cpu_weight": -1,
  "net_limit": {
    "used": -1,
    "available": -1,
    "max": -1
  },
  "cpu_limit": {
    "used": -1,
    "available": -1,
    "max": -1
  },
  "ram_usage": 4414,
  "permissions": [{
      "perm_name": "active",
      "parent": "owner",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D",
            "weight": 1
          }
        ],
        "accounts": [],
        "waits": []
      }
    },{
      "perm_name": "customp1",
      "parent": "active",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D",
            "weight": 1
          }
        ],
        "accounts": [],
        "waits": []
      }
    },{
      "perm_name": "customp3",
      "parent": "active",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D",
            "weight": 1
          }
        ],
        "accounts": [],
        "waits": []
      }
    },{
      "perm_name": "owner",
      "parent": "",
      "required_auth": {
        "threshold": 1,
        "keys": [{
            "key": "EOS58wmANoBtT7RdPgMRCGDb37tcCQswfwVpj6NzC55D247tTMU9D",
            "weight": 1
          }
        ],
        "accounts": [],
        "waits": []
      }
    }
  ],
  "total_resources": null,
  "self_delegated_bandwidth": null,
  "refund_request": null,
  "voter_info": null,
  "rex_info": null
}
```

## Conclusion

This tutorial demonstrates how to create, link, and delete custom permissions. The tutorial shows you how to use these permissions to control which actions an account permission can perform.  

## Further Examples

Custom permissions can also be controlled directly using the JavaScript SDK. For examples follow these links:

* [How to create permissions](https://developers.eos.io/manuals/eosjs/latest/how-to-guides/how-to-create-permissions)
* [How to link permissions](https://developers.eos.io/manuals/eosjs/latest/how-to-guides/how-to-link-permissions)
* [How to unlink permissions](https://developers.eos.io/manuals/eosjs/latest/how-to-guides/how-to-unlink-permissions)
* [How to delete permissions](https://developers.eos.io/manuals/eosjs/latest/how-to-guides/how-to-delete-permissions)

## What's Next

* [Payable Actions](90_payable-actions.md): Learn how to write a smart contract that has payable actions.
