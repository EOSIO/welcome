---
title: "2.3 Understanding ABI Files"
excerpt: ""
---
[block:api-header]
{
  "title": "Introduction"
}
[/block]
Previously you deployed the `eosio.token` contract using the provided ABI file. This tutorial will overview how the ABI file correlates to the `eosio.token` contract. 

ABI files can be generated using the `eosio-cpp` utility provided by `eosio.cdt`. However, there are several situations that may cause ABI's generation to malfunction or fail altogether. Advanced C++ patterns can trip it up and custom types can sometimes cause issues for ABI generation. For this reason, it's **imperative** you understand how ABI files work, so you can debug and fix if and when necessary. 
[block:api-header]
{
  "title": "What is an ABI?"
}
[/block]
The Application Binary Interface (ABI) is a JSON-based description on how to convert user actions between their JSON and Binary representations. The ABI also describes how to convert the database state to/from JSON. Once you have described your contract via an ABI then developers and users will be able to interact with your contract seamlessly via JSON. 

[block:callout]
{
  "type": "danger",
  "body": "ABI can be bypassed when executing transactions. Messages and actions passed to a contract do not have to conform to the ABI. The ABI is a guide, not a gatekeeper.",
  "title": "Security Note"
}
[/block]

[block:api-header]
{
  "title": "Create an ABI File"
}
[/block]
Start with an empty ABI, name it `eosio.token.abi`
[block:code]
{
  "codes": [
    {
      "code": "\n{\n   \"version\": \"eosio::abi/1.0\",\n   \"types\": [],\n   \"structs\": [],\n   \"actions\": [],\n   \"tables\": [],\n   \"ricardian_clauses\": [],\n   \"abi_extensions\": [],\n   \"___comment\" : \"\"\n}",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Types"
}
[/block]
An ABI enables any client or interface to interpret and even generate a GUI for your contract. For this to work in a consistent manner, describe the custom types that are used as a parameter in any public action or struct that needs to be described in the ABI.  
[block:callout]
{
  "type": "info",
  "body": "EOSIO implements a number of custom built-ins. Built-in types don't need to be described in an ABI file. If you would like to familiarize yourself with EOSIO's built-ins, they are defined [here](https://github.com/EOSIO/eos/blob/master/libraries/chain/abi_serializer.cpp#L65-L103)",
  "title": "Built-in Types"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n   \"new_type_name\": \"name\",\n   \"type\": \"name\"\n}",
      "language": "json"
    }
  ]
}
[/block]
The ABI now looks like this: 
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"version\": \"eosio::abi/1.0\",\n   \"types\": [{\n     \"new_type_name\": \"name\",\n     \"type\": \"name\"\n\t }],\n   \"structs\": [],\n   \"actions\": [],\n   \"tables\": [],\n   \"ricardian_clauses\": [],\n   \"abi_extensions\": []\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Structs"
}
[/block]
Structs that are exposed to the ABI also need to be described. By looking at eosio.token.hpp, it can be quickly determined which structs are utilized by public actions. This is particularly important for the next step. 

A struct's object definition in JSON looks like the following:
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"name\": \"issue\", //The name \n   \"base\": \"\", \t\t\t//Inheritance, parent struct\n   \"fields\": []\t\t\t//Array of field objects describing the struct's fields. \n}",
      "language": "json"
    }
  ]
}
[/block]
## Fields
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"name\":\"\", // The field's name\n   \"type\":\"\"   // The field's type\n}    ",
      "language": "json"
    }
  ]
}
[/block]
In the `eosio.token` contract, there's a number of structs that require definition. Please note, not all of the structs are explicitly defined, some correspond to an actions' parameters. Here's a list of structs that require an ABI description for the `eosio.token` contract: 

## Implicit Structs

The following structs are implicit in that a struct was never explicitly defined in the contract. Looking at the [create](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L24) action, you'll find two parameters, `issuer` of type `name ` and `maximum_supply` of type `asset`. For brevity this tutorial won't break down every struct, but applying the same logic, you will end up with the following: 

### [create](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L25)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"create\",\n  \"base\": \"\",\n  \"fields\": [\n    {\n      \"name\":\"issuer\", \n      \"type\":\"name\"\n    },\n    {\n      \"name\":\"maximum_supply\", \n      \"type\":\"asset\"\n    }\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]
### [issue](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L29)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"issue\",\n  \"base\": \"\",\n  \"fields\": [\n    {\n      \"name\":\"to\", \n      \"type\":\"name\"\n    },\n    {\n      \"name\":\"quantity\", \n      \"type\":\"asset\"\n    },\n    {\n      \"name\":\"memo\", \n      \"type\":\"string\"\n    }\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]
### [retire](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L32)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"retire\",\n  \"base\": \"\",\n  \"fields\": [\n    {\n      \"name\":\"quantity\", \n      \"type\":\"asset\"\n    },\n    {\n      \"name\":\"memo\", \n      \"type\":\"string\"\n    }\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]
### [transfer](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L35-L38)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"transfer\",\n  \"base\": \"\",\n  \"fields\": [\n    {\n      \"name\":\"from\", \n      \"type\":\"name\"\n    },\n    {\n      \"name\":\"to\", \n      \"type\":\"name\"\n    },\n    {\n      \"name\":\"quantity\", \n      \"type\":\"asset\"\n    },\n    {\n      \"name\":\"memo\", \n      \"type\":\"string\"\n    }\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]
### [close](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L44)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"close\",\n  \"base\": \"\",\n  \"fields\": [\n    {\n      \"name\":\"owner\", \n      \"type\":\"name\"\n    },\n    {\n      \"name\":\"symbol\", \n      \"type\":\"symbol\"\n    }\n  ]\n }",
      "language": "json"
    }
  ]
}
[/block]
## Explicit Structs
These structs are explicitly defined, as they are a requirement to instantiate a multi-index table. Describing them is no different than defining the implicit structs as demonstrated above. 

### [account](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L61-L65)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"account\",\n  \"base\": \"\",\n  \"fields\": [\n    {\n      \"name\":\"balance\", \n      \"type\":\"asset\"\n    }\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]
### [currency_stats](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L67-L73)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"currency_stats\",\n  \"base\": \"\",\n  \"fields\": [\n    {\n      \"name\":\"supply\", \n      \"type\":\"asset\"\n    },\n    {\n      \"name\":\"max_supply\", \n      \"type\":\"asset\"\n    },\n    {\n      \"name\":\"issuer\", \n      \"type\":\"account_name\"\n    }\n  ]\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Actions"
}
[/block]
An action's JSON object definition looks like the following: 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"transfer\", \t\t\t//The name of the action as defined in the contract\n  \"type\": \"transfer\", \t\t\t//The name of the implicit struct as described in the ABI\n  \"ricardian_contract\": \"\" \t//An optional ricardian clause to associate to this action describing its intended functionality.\n}",
      "language": "json"
    }
  ]
}
[/block]
Describe the actions of the `eosio.token` contract by aggregating all the public functions described in the `eosio.token` contract's [header file](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L24-L36). 

Then describe each action's *type* according to its previously described struct. In most situations, the function name and the struct name will be equal, but are not required to be equal.

Below is a list of actions that link to their source code with example JSON provided for how each action would be described in an ABI.

##  [create](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L24-L25)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"create\",\n  \"type\": \"create\",\n  \"ricardian_contract\": \"\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## [issue](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L27)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"issue\",\n  \"type\": \"issue\",\n  \"ricardian_contract\": \"\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## [retire](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L31-L34)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"retire\",\n  \"type\": \"retire\",\n  \"ricardian_contract\": \"\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## [transfer](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L31-L34)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"transfer\",\n  \"type\": \"transfer\",\n  \"ricardian_contract\": \"\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## [close](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L36)
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"close\",\n  \"type\": \"close\",\n  \"ricardian_contract\": \"\"\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Tables"
}
[/block]
Describe the tables. Here's a table's JSON object definition: 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"\",       //The name of the table, determined during instantiation. \n  \"type\": \"\", \t\t\t//The table's corresponding struct\n  \"index_type\": \"\", //The type of primary index of this table\n  \"key_names\" : [], //An array of key names, length must equal length of key_types member\n  \"key_types\" : []  //An array of key types that correspond to key names array member, length of array must equal length of key names array.\n}",
      "language": "json"
    }
  ]
}
[/block]
The eosio.token contract instantiates two tables, [accounts](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L75) and [stats](https://github.com/EOSIO/eosio.contracts/blob/8b0d3fd8af1d786a4b3f600d6af895c2a853cadf/eosio.token/include/eosio.token/eosio.token.hpp#L76).

The accounts table is an i64 index, based on the [`account` struct](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L43-L47), has a [`uint64` as it's primary key](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L64)

Here's how the accounts table would be described in the ABI
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"accounts\",\n  \"type\": \"account\", // Corresponds to previously defined struct\n  \"index_type\": \"i64\",\n  \"key_names\" : [\"primary_key\"],\n  \"key_types\" : [\"uint64\"]\n}",
      "language": "json"
    }
  ]
}
[/block]
The stat table is an i64 index, based on the [`currency_stats` struct](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L49-L55), has a [`uint64` as it's primary key](https://github.com/EOSIO/eosio.contracts/blob/master/eosio.token/include/eosio.token/eosio.token.hpp#L54)

Here's how the stat table would be described in the ABI
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"stat\",\n  \"type\": \"currency_stats\",\n  \"index_type\": \"i64\",\n  \"key_names\" : [\"primary_key\"],\n  \"key_types\" : [\"uint64\"]\n}",
      "language": "json"
    }
  ]
}
[/block]
You'll notice the above tables have the same "key name." Naming your keys similar names is symbolic in that it can potentially suggest a subjective relationship. As with this implementation, implying that any given value can be used to query different tables.
[block:api-header]
{
  "title": "Putting it all Together"
}
[/block]
Finally, an ABI file that accurately describes the `eosio.token` contract. 
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"version\": \"eosio::abi/1.0\",\n  \"types\": [\n    {\n      \"new_type_name\": \"name\",\n      \"type\": \"name\"\n    }\n  ],\n  \"structs\": [\n    {\n      \"name\": \"create\",\n      \"base\": \"\",\n      \"fields\": [\n        {\n          \"name\":\"issuer\", \n          \"type\":\"name\"\n        },\n        {\n          \"name\":\"maximum_supply\", \n          \"type\":\"asset\"\n        }\n      ]\n    },\n    {\n       \"name\": \"issue\",\n       \"base\": \"\",\n       \"fields\": [\n          {\n            \"name\":\"to\", \n            \"type\":\"name\"\n          },\n          {\n            \"name\":\"quantity\", \n            \"type\":\"asset\"\n          },\n          {\n            \"name\":\"memo\", \n            \"type\":\"string\"\n          }\n       ]\n    },\n    {\n       \"name\": \"retire\",\n       \"base\": \"\",\n       \"fields\": [\n          {\n            \"name\":\"quantity\", \n            \"type\":\"asset\"\n          },\n          {\n            \"name\":\"memo\", \n            \"type\":\"string\"\n          }\n       ]\n    },\n    {\n       \"name\": \"close\",\n       \"base\": \"\",\n       \"fields\": [\n          {\n            \"name\":\"owner\", \n            \"type\":\"name\"\n          },\n          {\n            \"name\":\"symbol\", \n            \"type\":\"symbol\"\n          }\n       ]\n    },\n    {\n      \"name\": \"transfer\",\n      \"base\": \"\",\n      \"fields\": [\n        {\n          \"name\":\"from\", \n          \"type\":\"name\"\n        },\n        {\n          \"name\":\"to\", \n          \"type\":\"name\"\n        },\n        {\n          \"name\":\"quantity\", \n          \"type\":\"asset\"\n        },\n        {\n          \"name\":\"memo\", \n          \"type\":\"string\"\n        }\n      ]\n    },\n    {\n      \"name\": \"account\",\n      \"base\": \"\",\n      \"fields\": [\n        {\n          \"name\":\"balance\", \n          \"type\":\"asset\"\n        }\n      ]\n    },\n    {\n      \"name\": \"currency_stats\",\n      \"base\": \"\",\n      \"fields\": [\n        {\n          \"name\":\"supply\", \n          \"type\":\"asset\"\n        },\n        {\n          \"name\":\"max_supply\", \n          \"type\":\"asset\"\n        },\n        {\n          \"name\":\"issuer\", \n          \"type\":\"name\"\n        }\n      ]\n    }\n  ],\n  \"actions\": [\n    {\n      \"name\": \"transfer\",\n      \"type\": \"transfer\",\n      \"ricardian_contract\": \"\"\n    },\n    {\n      \"name\": \"issue\",\n      \"type\": \"issue\",\n      \"ricardian_contract\": \"\"\n    },\n    {\n      \"name\": \"retire\",\n      \"type\": \"retire\",\n      \"ricardian_contract\": \"\"\n    },\n    {\n      \"name\": \"create\",\n      \"type\": \"create\",\n      \"ricardian_contract\": \"\"\n    },\n    {\n      \"name\": \"close\",\n      \"type\": \"close\",\n      \"ricardian_contract\": \"\"\n    }\n  ],\n  \"tables\": [\n    {\n      \"name\": \"accounts\",\n      \"type\": \"account\",\n      \"index_type\": \"i64\",\n      \"key_names\" : [\"currency\"],\n      \"key_types\" : [\"uint64\"]\n    },\n    {\n      \"name\": \"stat\",\n      \"type\": \"currency_stats\",\n      \"index_type\": \"i64\",\n      \"key_names\" : [\"currency\"],\n      \"key_types\" : [\"uint64\"]\n    }\n  ],\n  \"ricardian_clauses\": [],\n  \"abi_extensions\": []\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Cases not Covered by Token Contract"
}
[/block]
## Vectors
When describing a vector in your ABI file, simply append the type with `[]`, so if you need to describe a vector of permission levels, you would describe it like so: `permission_level[]`

## Struct Base
It's a rarely used property worth mentioning. You can use the **base** ABI struct property to reference another struct for inheritance, as long as that struct is also described in the same ABI file. Base will do nothing or potentially throw an error if your smart contract logic does not support inheritance. 

You can see an example of base in use in the system contract [source code](https://github.com/EOSIO/eosio.contracts/blob/4e4a3ca86d5d3482dfac85182e69f33c49e62fa9/eosio.system/include/eosio.system/eosio.system.hpp#L46) and [ABI](https://github.com/EOSIO/eosio.contracts/blob/4e4a3ca86d5d3482dfac85182e69f33c49e62fa9/eosio.system/abi/eosio.system.abi#L262)
[block:api-header]
{
  "title": "Extra ABI Properties Not Covered Here"
}
[/block]
A few properties of the ABI specification were skipped here for brevity, however, there is a pending ABI specification that will outline every property of the ABI in its entirety. 

## Ricardian Clauses
Ricardian clauses describe the intended outcome of a particular actions. It may also be utilized to establish terms between the sender and the contract. 

## ABI Extensions
A generic "future proofing" layer that allows old clients to skip the parsing of "chunks" of extension data. For now, this property is unused. In the future each extension would have its own "chunk" in that vector so that older clients skip it and newer clients that understand how to interpret it.
[block:api-header]
{
  "title": "Maintenance"
}
[/block]
Every time you change a struct, add a table, add an action or add parameters to an action, use a new type, you will need to remember to update your ABI file. In many cases failure to update your ABI file will not produce any error. 
[block:api-header]
{
  "title": "Troubleshooting"
}
[/block]
## Table returns no rows

Check that your table is accurately described in the <<glossary:ABI>> file. For example, If you use `cleos` to add a table on a contract with a malformed <<glossary:ABI>> definition and then get rows from that table, you will recieve an empty result. `cleos` will not produce an error when adding a row nor reading a row when a contract has failed to properly describe its tables in its <<glossary:ABI>> File.