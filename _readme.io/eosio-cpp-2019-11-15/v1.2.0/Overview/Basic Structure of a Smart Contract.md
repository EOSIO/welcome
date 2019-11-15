---
title: "Basic Structure of a Smart Contract"
excerpt: ""
---
If you know how to create a C++ class, then you're already well on your way to writing EOSIO smart contracts. Below is a simple Hello World contract, that provides an action that will return your account name. While this contract doesn't utilize all of the possible functions provided by the C++ SDK (eosiolib), it's a start to understanding the fundamentals. 
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\nusing namespace eosio;\n\nclass hello : public eosio::contract {\n  public:\n      using contract::contract;\n\n      /// @abi action \n      void hi( account_name user ) {\n         print( \"Hello, \", name{user} );\n      }\n};\n\nEOSIO_ABI( hello, (hi) )",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Section by Section"
}
[/block]
## Includes 
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
The first step is to include any of the libraries you need in the contract. 

## Namespace
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
Utilizing namespaces when you can will help make your code more neat and ultimately improve your development experience. 

## Class Definition
1. The contract is named `hello`, and extends upon the `eosio::contract` class, made easier to reference by our previously defined namespace. 
2. A contract is likely to have public methods, so we continue here. 
3. The contract's methods are exposed to the public scope. 
[block:code]
{
  "codes": [
    {
      "code": "class hello : public eosio::contract {\n  public:\n      using contract::contract;\n  \n}",
      "language": "cplusplus"
    }
  ]
}
[/block]

## An Action with an Annotatation
[block:code]
{
  "codes": [
    {
      "code": "// @abi action \nvoid hi( account_name user ) {\n       print( \"Hello, \", name{user} );\n    }",
      "language": "cplusplus"
    }
  ]
}
[/block]
1 You will notice the annotation above the function definition. This tells the ABI generator that the method should be exposed via the ABI.