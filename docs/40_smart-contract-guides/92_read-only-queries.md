---
content_title: "Read-Only Queries"
link_text: "Read-Only Queries"
---


External clients were limited to accessing chain state data through the get_tables APIs for chainbase or KV tables or through various history solutions. In version 2.2 of EOSIO there is now an API to invoke contract-defined read-only queries and return the results. Smart contracts can be written to include actions which are read-only queries using the `read-only` attribute. This tutorial will show you how to create a simple smart contract with a read-only query, and how to call this query from the cleos CLI. 

Once the tutorial is completed you should be able to create and call a read-only query.

## Before you begin
This tutorial requires the following:

* The EOSIO platform software, version 2.2. or greater, click on this link for instructions on [installing EOSIO](https://developers.eos.io/manuals/eos/latest/install/index)
* The EOSIO.CDT (Contract Development Toolkit), version 1.9. or greater, click on this link for instructions on [installing the EOSIO.CDT](https://developers.eos.io/manuals/eos/latest/install/index)
* Access to a running blockchain. Click on this link for instructions on [running a blockchain](01_before-you-begin/10_running-a-blockchain.md)
* An EOSIO account and access to the account keys. Click on this link for information on [Accounts and Permissions](01_before-you-begin/20_accounts-and-permissions.md)
* You understand how to build and deploy smart contracts. Follow this link for more information [hello world tutorial.](../30_getting-started-guide/25_hello-world.md)


## Run a Local Single-Node Blockchain
Run a local nodeos instance which produces blocks, creating a local single-node testnet, using these [instructions](https://developers.eos.io/manuals/eosio.cdt/latest/installation/index).
 

## Build a Smart Contract with a Read-Only Query 

Create a simple smart contract which contains three read-only actions: 
- `get` - Will return a value 
- `getComp` - Will return a complex value
- `getMore` - Will return a vector of values

Define the actions as read-only with the `eosio::read_only` attribute. Click on the follwing link for more information [ABI code generator attributes explained](https://developers.eos.io/manuals/eosio.cdt/latest/best-practices/abi/abi-code-generator-attributes-explained)   


```cpp
#include <eosio/eosio.hpp>
class [[eosio::contract]] hello : public eosio::contract {
  public:

     struct retVal {
         std::string name;
         uint32_t gender;
         uint32_t age;
      };
 
      using eosio::contract::contract;


      [[eosio::action, eosio::read_only]] std::string get() {
         return "Bob";
      }


      [[eosio::action, eosio::read_only]] retVal getComp() {
         retVal rv;

         rv.name = "Bob";
         rv.gender = 1;
         rv.age = 99;

         return rv;
      }


      [[eosio::action, eosio::read_only]] std::vector<retVal> getMore() {         
         std::vector<retVal> ret;
         
         retVal rv;
         
         rv.name = "Bob";
         rv.gender = 1;
         rv.age = 99;
         ret.push_back(rv);

         rv.name = "Alice";
         rv.gender = 0;
         rv.age = 19;
         ret.push_back(rv);

         return ret;
      }
};
```

Build the smart contract and deploy the smart contract to the local single-node testnet using [how to compile a smart contract via the CLI](https://developers.eos.io/manuals/eosio.cdt/latest/how-to-guides/compile/compile-a-contract-via-cli) and [how to deploy a smart contract.](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-deploy-a-smart-contract) 

## Call the Read-Only Query 
Once you have deployed the smart contract you can test it by calling the actions and seeing the data returned. Assuming the smart contract is deployed to an account called _scholder_ and that you have an account named _bob_ to authorise calling the actions. 

* Call get():

```shell
cleos push transaction --read-only -j '{"actions":[{"account":"scholder","name":"get","authorization":[{"actor":"bob","permission":"active"}],"data":""}]}' -p bob@active
```

The output should be similar to:

```json
{
  "head_block_num": 89230,
  "head_block_id": "00015c8e67e66b8bb1daeeb6452fefea22509d0ef99381f34ed4b1486036bdbd",
  "last_irreversible_block_num": 89229,
  "last_irreversible_block_id": "00015c8d117aa070cea8bbe8bae16d27cfa321d54deaa89b2125b5d2f5a4922b",
  "code_hash": "89959d556cf0a0863064269f93dbc69c3b1e3b278385d495fc59f3509f77a6fb",
  "pending_transactions": [],
  "result": {
    "id": "5394a83aebf2c43dd007473bd917ef4d7461c73395b1b504df6b853787f4967f",
    "block_num": 89231,
    "block_time": "2021-06-03T09:46:39.500",
    "producer_block_id": null,
    "receipt": {
      "status": "executed",
      "cpu_usage_us": 126,
      "net_usage_words": 12
    },
    "elapsed": 3562,
    "net_usage": 96,
    "scheduled": false,
    "action_traces": [{
        "action_ordinal": 1,
        "creator_action_ordinal": 0,
        "closest_unnotified_ancestor_action_ordinal": 0,
        "receipt": {
          "receiver": "scholder",
          "act_digest": "ffe396998865e412f71cb314f5b4fec9a05cb7a043f2bcc38e3e5bff70f6cfe7",
          "global_sequence": 89247,
          "recv_sequence": 6,
          "auth_sequence": [[
              "bob",
              6
            ]
          ],
          "code_sequence": 2,
          "abi_sequence": 2
        },
        "receiver": "scholder",
        "act": {
          "account": "scholder",
          "name": "get",
          "authorization": [{
              "actor": "bob",
              "permission": "active"
            }
          ],
          "hex_data": ""
        },
        "context_free": false,
        "elapsed": 3480,
        "console": "",
        "trx_id": "5394a83aebf2c43dd007473bd917ef4d7461c73395b1b504df6b853787f4967f",
        "block_num": 89231,
        "block_time": "2021-06-03T09:46:39.500",
        "producer_block_id": null,
        "account_ram_deltas": [],
        "account_disk_deltas": [],
        "except": null,
        "error_code": null,
        "return_value_hex_data": "045068696c0100000033000000",
        "return_value_data": "Bob"
      }
    ],
    "account_ram_delta": null,
    "except": null,
    "error_code": null
  }
}
```

* Call getComp():

```shell
cleos push transaction --read-only -j '{"actions":[{"account":"scholder","name":"getComp","authorization":[{"actor":"bob","permission":"active"}],"data":""}]}' -p bob@active
```

The output should be similar to:
 
```json
{
  "head_block_num": 89230,
  "head_block_id": "00015c8e67e66b8bb1daeeb6452fefea22509d0ef99381f34ed4b1486036bdbd",
  "last_irreversible_block_num": 89229,
  "last_irreversible_block_id": "00015c8d117aa070cea8bbe8bae16d27cfa321d54deaa89b2125b5d2f5a4922b",
  "code_hash": "89959d556cf0a0863064269f93dbc69c3b1e3b278385d495fc59f3509f77a6fb",
  "pending_transactions": [],
  "result": {
    "id": "5394a83aebf2c43dd007473bd917ef4d7461c73395b1b504df6b853787f4967f",
    "block_num": 89231,
    "block_time": "2021-06-03T09:46:39.500",
    "producer_block_id": null,
    "receipt": {
      "status": "executed",
      "cpu_usage_us": 126,
      "net_usage_words": 12
    },
    "elapsed": 3562,
    "net_usage": 96,
    "scheduled": false,
    "action_traces": [{
        "action_ordinal": 1,
        "creator_action_ordinal": 0,
        "closest_unnotified_ancestor_action_ordinal": 0,
        "receipt": {
          "receiver": "scholder",
          "act_digest": "ffe396998865e412f71cb314f5b4fec9a05cb7a043f2bcc38e3e5bff70f6cfe7",
          "global_sequence": 89247,
          "recv_sequence": 6,
          "auth_sequence": [[
              "bob",
              6
            ]
          ],
          "code_sequence": 2,
          "abi_sequence": 2
        },
        "receiver": "scholder",
        "act": {
          "account": "scholder",
          "name": "get",
          "authorization": [{
              "actor": "bob",
              "permission": "active"
            }
          ],
          "hex_data": ""
        },
        "context_free": false,
        "elapsed": 3480,
        "console": "",
        "trx_id": "5394a83aebf2c43dd007473bd917ef4d7461c73395b1b504df6b853787f4967f",
        "block_num": 89231,
        "block_time": "2021-06-03T09:46:39.500",
        "producer_block_id": null,
        "account_ram_deltas": [],
        "account_disk_deltas": [],
        "except": null,
        "error_code": null,
        "return_value_hex_data": "045068696c0100000033000000",
        "return_value_data":{
          "name": "Bob",
          "gender": 1,
          "age": 99
          }
      }
    ],
    "account_ram_delta": null,
    "except": null,
    "error_code": null
  }
}
```

* Call getMore():

```shell
cleos push transaction --read-only -j '{"actions":[{"account":"scholder","name":"getMore","authorization":[{"actor":"bob","permission":"active"}],"data":""}]}' -p bob@active
```

The output should be similar to:
 
```json
{
  "head_block_num": 89230,
  "head_block_id": "00015c8e67e66b8bb1daeeb6452fefea22509d0ef99381f34ed4b1486036bdbd",
  "last_irreversible_block_num": 89229,
  "last_irreversible_block_id": "00015c8d117aa070cea8bbe8bae16d27cfa321d54deaa89b2125b5d2f5a4922b",
  "code_hash": "89959d556cf0a0863064269f93dbc69c3b1e3b278385d495fc59f3509f77a6fb",
  "pending_transactions": [],
  "result": {
    "id": "5394a83aebf2c43dd007473bd917ef4d7461c73395b1b504df6b853787f4967f",
    "block_num": 89231,
    "block_time": "2021-06-03T09:46:39.500",
    "producer_block_id": null,
    "receipt": {
      "status": "executed",
      "cpu_usage_us": 126,
      "net_usage_words": 12
    },
    "elapsed": 3562,
    "net_usage": 96,
    "scheduled": false,
    "action_traces": [{
        "action_ordinal": 1,
        "creator_action_ordinal": 0,
        "closest_unnotified_ancestor_action_ordinal": 0,
        "receipt": {
          "receiver": "scholder",
          "act_digest": "ffe396998865e412f71cb314f5b4fec9a05cb7a043f2bcc38e3e5bff70f6cfe7",
          "global_sequence": 89247,
          "recv_sequence": 6,
          "auth_sequence": [[
              "bob",
              6
            ]
          ],
          "code_sequence": 2,
          "abi_sequence": 2
        },
        "receiver": "scholder",
        "act": {
          "account": "scholder",
          "name": "get",
          "authorization": [{
              "actor": "bob",
              "permission": "active"
            }
          ],
          "hex_data": ""
        },
        "context_free": false,
        "elapsed": 3480,
        "console": "",
        "trx_id": "5394a83aebf2c43dd007473bd917ef4d7461c73395b1b504df6b853787f4967f",
        "block_num": 89231,
        "block_time": "2021-06-03T09:46:39.500",
        "producer_block_id": null,
        "account_ram_deltas": [],
        "account_disk_deltas": [],
        "except": null,
        "error_code": null,
        "return_value_hex_data": "045068696c0100000033000000",
        "return_value_data": [{
          "name": "Bob",
          "gender": 1,
          "age": 99
          },{
          "name": "Alice",
          "gender": 0,
          "age": 19
         }
		]
      }
    ],
    "account_ram_delta": null,
    "except": null,
    "error_code": null
  }
}
```

## What's next?
Try using the [KV-API](https://developers.eos.io/manuals/eosio.cdt/latest/how-to-guides/key-value-api/index) or [Multi-Index-Tables API](https://developers.eos.io/manuals/eosio.cdt/latest/how-to-guides/multi-index/index) to store data then return this data in a read-only query.