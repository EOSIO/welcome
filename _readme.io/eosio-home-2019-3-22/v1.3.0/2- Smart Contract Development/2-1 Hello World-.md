---
title: "2.1 Hello World!"
excerpt: ""
---
Create a new directory called "hello" in the contracts directory you previously created, or through your system GUI or with cli and enter the directory.
[block:code]
{
  "codes": [
    {
      "code": "cd CONTRACTS_DIR\nmkdir hello\ncd hello",
      "language": "shell"
    }
  ]
}
[/block]
Create a new file, "hello.cpp" and open it in your favorite editor.
[block:code]
{
  "codes": [
    {
      "code": "touch hello.cpp",
      "language": "shell"
    }
  ]
}
[/block]
Include the required libraries into the file. 
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>",
      "language": "cplusplus"
    }
  ]
}
[/block]
To make things more concise in your contract use namespace `eosio`.
[block:code]
{
  "codes": [
    {
      "code": "using namespace eosio;",
      "language": "cplusplus"
    }
  ]
}
[/block]
- `eosiolib/eosio.hpp` loads the EOSIO C and C++ API into the scope of your contract, this is your new warchest.

Create a standard C++11 class. The contract class needs to extend `eosio::contract`.
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass hello : public contract {};",
      "language": "cplusplus"
    }
  ]
}
[/block]
An empty contract doesn't do much good. Add a public access specifier and a using-declaration. The `using` declaration will allow us to write more concise code. 
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass hello : public contract {\n  public:\n      using contract::contract;\n};",
      "language": "cplusplus"
    }
  ]
}
[/block]
This contract needs to do something. In the spirit of **hello world** write an action that accepts a "name" parameter, and then prints that parameter out.
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass hello : public contract {\n  public:\n      using contract::contract;\n      void hi( account_name user ) {\n         print( \"Hello, \", name{user} );\n      }\n};",
      "language": "cplusplus"
    }
  ]
}
[/block]
The above action accepts a parameter called `user` that's an `account_name` type. EOSIO comes with a number of typedefs, one of the most common typedefs you'll encounter is `account_name`. Using the `eosio::print` library previously included,  concatenate a string and print the `user` parameter. Use the braced initialization of `name{user}` to make the `user` parameter printable.

As is, the abi generator in `eosio.cdt` won't know about the `hi()` action without an attribute. Add a C++11 style attribute above the action, this way the abi generator can produce more reliable output. 
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass hello : public contract {\n  public:\n      using contract::contract;\n\n      [[eosio::action]]\n      void hi( account_name user ) {\n         print( \"Hello, \", name{user} );\n      }\n};",
      "language": "cplusplus"
    }
  ]
}
[/block]
Finally, add the `EOSIO_ABI` macro to handle the dispatching of actions for the `hello` contract.
[block:code]
{
  "codes": [
    {
      "code": "EOSIO_ABI( hello, (hi))",
      "language": "cplusplus"
    }
  ]
}
[/block]
Everything together, here's the completed hello world contract
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass hello : public contract {\n  public:\n      using contract::contract;\n\n      [[eosio::action]]\n      void hi( account_name user ) {\n         print( \"Hello, \", name{user} );\n      }\n};\nEOSIO_ABI( hello, (hi))",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "The ABI Generator in eosio.cdt supports several different style of attributes, see the ABI usage guide [here](https://github.com/EOSIO/eosio.cdt#difference-from-old-abi-generator)"
}
[/block]
You can compile your code to web assembly (.wasm) as follows:
[block:code]
{
  "codes": [
    {
      "code": "eosio-cpp -o hello.wasm hello.cpp --abigen",
      "language": "shell"
    }
  ]
}
[/block]
When a contract is deployed, it is deployed to an account, and the account becomes the interface for the contract. As mentioned earlier these tutorials use the same public key for all of the accounts to keep things more simple. 
[block:code]
{
  "codes": [
    {
      "code": "cleos wallet keys",
      "language": "shell"
    }
  ]
}
[/block]
Create an account for the contract using [cleos create account](), with the command provided below.
[block:code]
{
  "codes": [
    {
      "code": "cleos create account eosio hello YOUR_PUBLIC_KEY -p eosio@active",
      "language": "shell"
    }
  ]
}
[/block]
Broadcast the compiled `wasm` to the blockchain with [cleos set contract](https://developers.eos.io/eosio-cleos/reference#cleos-set-contract). 
[block:callout]
{
  "type": "info",
  "title": "Get an error?",
  "body": "Either your wallet needs to be unlocked, or you did not alias cleos as mentioned in step [1.3](https://developers.eos.io/eosio-home/docs/getting-the-software#section-step-4-aliasing-cleos)."
}
[/block]

[block:html]
{
  "html": "<div class=\"no-contracts-helper\">\n  In previous steps you should have created a `contracts` directory and obtained the absolute path and then saved it into a cookie. Replace \"CONTRACTS_DIR\" in the command below with the absolute path to your `contracts` directory.\n</div>"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos set contract hello CONTRACTS_DIR/hello -p hello@active\n",
      "language": "shell"
    }
  ]
}
[/block]
Great! Now the contract is set, push an action to it.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action hello hi '[\"bob\"]' -p bob@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 4c10c1426c16b1656e802f3302677594731b380b18a44851d38e8b5275072857  244 bytes  1000 cycles\n#    hello.code <= hello.code::hi               {\"user\":\"bob\"}\n>> Hello, bob",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
As written, the contract will allow any account to say hi to any user
[block:code]
{
  "codes": [
    {
      "code": "cleos push action hello hi '[\"bob\"]' -p alice@active\n",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 28d92256c8ffd8b0255be324e4596b7c745f50f85722d0c4400471bc184b9a16  244 bytes  1000 cycles\n#    hello.code <= hello.code::hi               {\"user\":\"bob\"}\n>> Hello, bob",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
As expected, the console output is "Hello, bob" 

In this case "alice" is the one who authorized it and `user` is just an argument. Modify the contract so that the authorizing user, "alice" in this case, must be the same as the user the contract is responding "hi" to. Use the `require_auth` method. This method takes an `account_name` as a parameter, and will check if the user executing the action matches the provided paramter. 


[block:code]
{
  "codes": [
    {
      "code": "void hi( account_name user ) {\n   require_auth( user );\n   print( \"Hello, \", name{user} );\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Recompile the contract
[block:code]
{
  "codes": [
    {
      "code": "eosio-cpp -o hello.wasm hello.cpp --abigen\n",
      "language": "shell"
    }
  ]
}
[/block]
And then update it
[block:code]
{
  "codes": [
    {
      "code": "cleos set contract hello CONTRACTS_DIR/hello -p hello@active",
      "language": "shell"
    }
  ]
}
[/block]
Try to execute the action again, but this time with mismatched authorization. 
[block:code]
{
  "codes": [
    {
      "code": "cleos push action hello hi '[\"bob\"]' -p alice@active",
      "language": "shell"
    }
  ]
}
[/block]
As expected, `require_auth` haulted the transaction and threw an error. 
[block:code]
{
  "codes": [
    {
      "code": "Error 3090004: Missing required authority\nEnsure that you have the related authority inside your transaction!;\nIf you are currently using 'cleos push action' command, try to add the [relevant](**http://google.com**) authority using -p option.",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
With our changes to the contract, verify the provided `account_name user` is the same as the authorizing user. Try it again, but this time, with the authority of the "alice" account. 
[block:code]
{
  "codes": [
    {
      "code": "cleos push action hello hi '[\"alice\"]' -p alice@active",
      "language": "text"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 235bd766c2097f4a698cfb948eb2e709532df8d18458b92c9c6aae74ed8e4518  244 bytes  1000 cycles\n#    hello <= hello::hi               {\"user\":\"alice\"}\n>> Hello, alice",
      "language": "text"
    }
  ]
}
[/block]