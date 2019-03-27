---
title: "2.9 Payable Actions"
excerpt: ""
---
[block:api-header]
{
  "title": "Step 1: the EOSIO_ABI Macro"
}
[/block]
Up until now, we've been using a nifty little macro. 

[block:code]
{
  "codes": [
    {
      "code": "EOSIO_ABI( myclass, (myaction1)(myaction2)(myacction3))",
      "language": "text"
    }
  ]
}
[/block]
The `EOSIO_ABI` macro abstracts the dispatcher with a common pattern.
- The base class is set, `myclass`
- The actions exposed are defined.
- A dispatched action's arguments are positional.
[block:api-header]
{
  "title": "Step 2: The HODL Contract"
}
[/block]
We're going to write a simple contract that accepts allows payment of a particular token, but will not allow the tokens to be withdrawn for a specific amount of time. 

First create a standard C++ class called "hodl" that extends `eosio::contract`.
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass hodl : public eosio::contract {\n  private:\n\n  public:\n  \n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
This contract will require some constant variables, to configure the contract. 
- When is the hodl over?
- What symbol does this contract accept?
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass hodl : public eosio::contract {\n  private:\n  \tstatic const uint64_t the_party = 1645568542;\n    static const uint64_t symbol = string_to_symbol(4, \"SYS\");\n  public:\n  \t\n}",
      "language": "text"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n#include <eosiolib/asset.hpp>\n\nusing namespace eosio;\n\nclass hodl : public eosio::contract {\n  private:\n    static const uint64_t the_party = 1645568542;\n    static const uint64_t symbol = string_to_symbol(4, \"SYS\");\n\n  public:\n    using contract::contract;\n\n    hodl(account_name self): contract(self) {\n      eosio_assert(now() < the_party, \"Party should start after now, not before now.\");\n    }\n\n    void deposit(account_name hodler, account_name to, eosio::asset quantity, std::string memo) {\n      if(to != _self || hodler == _self) {\n        print(\"These are not the droids you are looking for.\");\n        return;\n      }\n\n      eosio_assert(now() < the_party, \"You're way late\");\n      eosio_assert(quantity.amount > 0, \"When pigs fly\");\n      eosio_assert(quantity.symbol == symbol, \"These are not the droids you are looking for.\");\n\n      balance_table balance(_self, hodler);\n      auto hodl_it = balance.find(symbol);\n\n      asset new_balance;\n      if(hodl_it != balance.end())\n        balance.modify(hodl_it, hodler, [&](auto& row){\n            row.funds += quantity;\n            new_balance = row.funds;\n        });\n      else\n        balance.emplace(hodler, [&](auto& row){\n            row.funds = quantity;\n            new_balance  = row.funds;\n        });\n\n      send_receipt(hodler, message);\n    }\n\n    [[eosio::action]]\n    void party(account_name hodler){\n\n      require_auth(hodler);\n      eosio_assert(now() > the_party, \"Hold your horses\");\n\n      balance_table balance(_self, hodler);\n      auto hodl_it = balance.find(symbol);\n\n      eosio_assert(hodl_it != balance.end(), \"You're not allowed to party\");\n\n      action{\n          permission_level{get_self(), N(active)},\n          N(eosio.token),\n          N(transfer),\n          std::make_tuple(get_self(), hodler, hodl_it->funds, \"Party! Your hodl is free.\")\n      }.send();\n\n      balance.erase(hodl_it);\n    }\n\n    [[eosio::action]]\n    void receipt(account_name hodler, std::string msg){\n      require_auth(_self);\n      require_recipient(hodler);\n    }\n\n  private:\n    struct [[eosio::table]] balance {\n        eosio::asset funds;\n        uint64_t primary_key() const { return funds.symbol; }\n    };\n    using balance_table = eosio::multi_index<N(balance), balance>;\n\n    void send_receipt(account_name hodler, std::string message){\n      action(\n        permission_level{get_self(), N(active)},\n        get_self(),\n        N(receipt),\n        std::make_tuple(hodler, message)\n      ).send();\n    }\n\n};\n\nextern \"C\" {\n  void apply(uint64_t self, uint64_t code, uint64_t action) {\n    hodl _hodl(self);\n    if(code==self && action==N(party)) {\n      execute_action( &_hodl, &hodl::party );\n    }\n    else if(code==self && action==N(receipt)) {\n      execute_action( &_hodl, &hodl::receipt );\n    }\n    else if(code==N(eosio.token) && action==N(transfer)) {\n      execute_action( &_hodl, &hodl::deposit );\n    }\n  }\n};\n",
      "language": "cplusplus"
    }
  ]
}
[/block]