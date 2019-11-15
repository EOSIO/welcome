---
title: "Debugging a Smart Contract"
excerpt: ""
---
In order to be able to debug your smart contract, you will need to setup local nodeos node. This local nodeos node can be run as separate private testnet or as an extension of public testnet.  This local node also needs to be run with the contracts-console option on, either `--contracts-console` via the command line or `contracts-console = true` via the config.ini

When you are creating your smart contract for the first time, it is recommended to test and debug your smart contract on a private testnet first, since you have full control of the whole blockchain. This enables you to have unlimited amount of eos needed and you can just reset the state of the blockchain whenever you want. When it is ready for production, debugging  on the public testnet (or official testnet) can be done by connecting your local nodeos to the public testnet (or official testnet) so you can see the log of the testnet in your local nodeos.

The concept is the same, so for the following guide, debugging on the private testnet will be covered.


If you haven't set up your own local nodeos, please follow the [setup guide](https://github.com/EOSIO/eos/wiki/Local-Environment). By default, your local nodeos will just run in a private testnet unless you modify the config.ini file to connect with public testnet (or official testnet) nodes as described in the following [guide](Testnet%3A%20Public).

## Method
The main method used to debug smart contract is **Caveman Debugging**, where we utilize the printing functionality to inspect the value of a variable and check the flow of the contract. Printing in smart contract can be done through the Print API ([C](https://github.com/EOSIO/eos/blob/master/contracts/eoslib/print.h) and [C++](https://github.com/EOSIO/eos/blob/master/contracts/eoslib/print.hpp)). The C++ API is the wrapper for C API, so most often we will just use the C++ API.

## Print
Print C API supports the following data type that you can print:
- prints - a null terminated char array (string)
- prints_l - any char array (string) with given size
- printi - 64-bit unsigned integer
- printi128 - 128-bit unsigned integer
- printd - double encoded as 64-bit unsigned integer
- printn - base32 string encoded as 64-bit unsigned integer
- printhex - hex given binary of data and its size 

While Print C++ API wraps some of the above C API by overriding the print() function so user doesn't need to determine which specific print function he needs to use. Print C++ API supports
- a null terminated char array (string)
- integer (128-bit unsigned, 64-bit unsigned, 32-bit unsigned, signed, unsigned)
- base32 string encoded as 64-bit unsigned integer
- struct that has print() method

## Example
Let's write a new contract as example for debugging

### debug.hpp
[block:code]
{
  "codes": [
    {
      "code": "#include <eoslib/eos.hpp>\n#include <eoslib/db.hpp>\n\nnamespace debug {\n    struct foo {\n        account_name from;\n        account_name to;\n        uint64_t amount;\n        void print() const {\n            eosio::print(\"Foo from \", eosio::name(from), \" to \",eosio::name(to), \" with amount \", amount, \"\\n\");\n        }\n    };\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
### debug.cpp
[block:code]
{
  "codes": [
    {
      "code": "#include <debug.hpp>\n\nextern \"C\" {\n\n    void apply( uint64_t code, uint64_t action ) {\n        if (code == N(debug)) {\n            eosio::print(\"Code is debug\\n\");\n            if (action == N(foo)) {\n                 eosio::print(\"Action is foo\\n\");\n                debug::foo f = eosio::unpack_action_data<debug::foo>();\n               if (f.amount >= 100) {\n                    eosio::print(\"Amount is larger or equal than 100\\n\");\n                } else {\n                    eosio::print(\"Amount is smaller than 100\\n\");\n                    eosio::print(\"Increase amount by 10\\n\");\n                    f.amount += 10;\n                    eosio::print(f);\n                }\n            }\n        }\n    }\n} // extern \"C\"",
      "language": "cplusplus"
    }
  ]
}
[/block]
### debug.abi
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"structs\": [{\n      \"name\": \"foo\",\n      \"base\": \"\",\n      \"fields\": {\n        \"from\": \"account_name\",\n        \"to\": \"account_name\",\n        \"amount\": \"uint64\"\n      }\n    }\n  ],\n  \"actions\": [{\n      \"action_name\": \"foo\",\n      \"type\": \"foo\"\n    }\n  ]\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Let's deploy it and send a message to it. Assume that you have `debug` account created and have its key in your wallet.

```bash
$ eosiocpp -o debug.wast debug.cpp
$ cleos set contract debug debug.wast debug.abi
$ cleos push action debug foo '{"from":"inita", "to":"initb", "amount":10}' --scope debug
```

When you check your local `nodeos` node log, you will see the following lines after the above message is sent.

```
Code is debug
Action is foo
Amount is smaller than 100
Increase amount by 10
Foo from inita to initb with amount 20
```

There, you can confirm that your message is going to the right control flow and the amount is updated correctly. You might see the above message at least 2 times and that's normal because each transaction is being applied during verification, block generation, and block application.