---
title: "Debugging a Smart Contract"
excerpt: ""
---
In order to be able to debug your smart contract, you will need to setup local nodeos node. This local nodeos node can be run as separate private testnet or as an extension of public testnet.  This local node also needs to be run with the contracts-console option on, either `--contracts-console` via the command line or `contracts-console = true` via the config.ini and/or by setting up logging on your running nodeos node and checking the output logs. See below for details on logging.

When you are creating your smart contract for the first time, it is recommended to test and debug your smart contract on a private testnet first, since you have full control of the whole blockchain and can easily add suitable logging. This enables you to have unlimited amount of eos needed and you can just reset the state of the blockchain whenever you want. When it is ready for production, debugging  on the public testnet (or official testnet) can be done by connecting your local nodeos to the public testnet (or official testnet) so you can see the log of the testnet in your local nodeos.

The concept is the same, so for the following guide, debugging on the private testnet will be covered.

If you haven't set up your own local nodeos, please follow the [setup guide](https://developers.eos.io/eosio-home/docs/getting-the-software). By default, your local nodeos will just run in a private testnet unless you modify the config.ini file to connect with public testnet (or official testnet) nodes. 

## Method
The main method used to debug smart contract is **Caveman Debugging**, where we utilize the printing functionality to inspect the value of a variable and check the flow of the contract. Printing in smart contract can be done through the Print API. The C++ API is the wrapper for C API, so most often we will just use the C++ API.

## Print
Print C API supports the following data type that you can print:
- prints - a null terminated char array (string)
- prints_l - any char array (string) with given size
- printi - 64-bit signed integer
- printui - 64-bit unsigned integer 
- printi128 - 128-bit signed integer
- printui128 - 128-bit unsigned integer
- printsf - single-precision floating point number
- printdf - double encoded as 64-bit unsigned integer
- printqf - quadruple encoded as 64-bit unsigned integer
- printn - 64 bit names as base32 encoded string
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
$ eosio-cpp -abigen debug.cpp -o debug.wasm
$ cleos set contract debug CONTRACT_DIR/debug -p youraccount@active
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
[block:api-header]
{
  "title": "Logging"
}
[/block]
Logging for Nodeos is controlled by the logging.json file. The logging.json file is usually located in the --config-dir, the same directory as the config.ini file. This path can be explicitly defined using the -l or --logconf options when starting nodeos.
 
 ```sh
 ./nodeos --help
  ...
  Application Command Line Options:
  ...
  --config-dir arg                      Directory containing configuration files such as config.ini
  -l [ --logconf ] arg (=logging.json)  Logging configuration file name/path for library users
                                        
```

The logging.json file can be used to define appenders and loggers. The json configuration is used to define and tie appenders to loggers and logging levels.

### Appenders

The logging library built into EOSIO supports three appender types:

#### console 

This will output log message to the screen. The configuration options are:

 - name - arbitrary name to identify instance for use in loggers
 - type - "console"
 - stream - "std_out" or "std_err"
 - level_colors - maps a log level to a colour.
   -- level - see logging levels below.
   -- color - may be one of ("red", "green", "brown", "blue", "magenta", "cyan", "white", "console_default")
 - enabled - bool value to enabling/disabling the appender.

Example:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"name\": \"consoleout\",\n     \"type\": \"console\",\n     \"args\": {\n       \"stream\": \"std_out\",\n\n       \"level_colors\": [{\n           \"level\": \"debug\",\n           \"color\": \"green\"\n         },{\n           \"level\": \"warn\",\n           \"color\": \"brown\"\n         },{\n           \"level\": \"error\",\n           \"color\": \"red\"\n         }\n       ]\n     },\n     \"enabled\": true\n   }",
      "language": "json"
    }
  ]
}
[/block]
#### gelf

This sends the log messages to Graylog. Graylog is a fully integrated platform for collecting, indexing, and analyzing log messages. The configuration options are:

 - name - arbitrary name to identify instance for use in loggers
 - type - "gelf"
 - endpoint - ip address and port number
 - host - Graylog hostname, identifies you to Graylog.
 - enabled - bool value to enabling/disabling the appender.

Example:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"name\": \"net\",\n     \"type\": \"gelf\",\n     \"args\": {\n       \"endpoint\": \"104.198.210.18:12202”,\n       \"host\": <YOURNAMEHERE IN QUOTES>\n     },\n     \"enabled\": true\n}",
      "language": "json"
    }
  ]
}
[/block]
#### file

The file appender is currently disabled 

### Loggers

The logging library built into EOSIO currently supports five loggers:

- default, the default logger, always enabled.
- net_plugin_impl, detailed logging for the net plugin.
- bnet_plugin, detailed logging for the net plugin.
- producer_plugin, detailed logging for the producer plugin.
- transaction_tracing, detailed log that emits verdicts from relay nodes on the P2P network.

The configuration options are:

 - `name` - must match one of the names described above.
 - `level` - see logging levels below.
 - `enabled` - bool value to enabling/disabling the logger.
 - `additivity` - true or flase
 - `appenders`
  -- list of appenders by name (name in the appender configuration)

Example:
[block:code]
{
  "codes": [
    {
      "code": "{\n     \"name\": \"net_plugin_impl\",\n     \"level\": \"debug\",\n     \"enabled\": true,\n     \"additivity\": false,\n     \"appenders\": [\n       \"net\"\n     ]\n}\n\n",
      "language": "json"
    }
  ]
}
[/block]
`net_plugin_impl`, `bnet_plugin`, `producer_plugin`, `transaction_tracing` are not enabled unless explicitly enabled in the `logging.json`

### Logging Levels

There are six available logging levels:
- all, 
- debug
- info
- warn
- error
- off  


Sample logging.json
[block:code]
{
  "codes": [
    {
      "code": "{\n \"includes\": [],\n \"appenders\": [{\n     \"name\": \"consoleout\", \n     \"type\": \"console\",\n     \"args\": {\n       \"stream\": \"std_out\",\n       \"level_colors\": [{\n           \"level\": \"debug\",\n           \"color\": \"green\"\n         },{\n           \"level\": \"warn\",\n           \"color\": \"brown\"\n         },{\n           \"level\": \"error\",\n           \"color\": \"red\"\n         }\n       ]\n     },\n     \"enabled\": true\n   },{\n     \"name\": \"net\",\n     \"type\": \"gelf\",\n     \"args\": {\n       \"endpoint\": \"10.10.10.10\",\n       \"host\": \"test\"\n     },\n     \"enabled\": true\n   }\n ],\n \"loggers\": [{\n     \"name\": \"default\",\n     \"level\": \"info\",\n     \"enabled\": true,\n     \"additivity\": false,\n     \"appenders\": [\n       \"consoleout\",\n       \"net\"\n     ]\n   },{\n     \"name\": \"net_plugin_impl\",\n     \"level\": \"debug\",\n     \"enabled\": true,\n     \"additivity\": false,\n     \"appenders\": [\n       \"net\"\n     ]\n   }\n ]\n}",
      "language": "json",
      "name": "logging.json"
    }
  ]
}
[/block]