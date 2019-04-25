---
title: "2.9 Payable Actions"
excerpt: ""
---
[block:api-header]
{
  "title": "Step 1: the EOSIO_DISPATCH Macro"
}
[/block]
Up until now, we've been using a nifty little macro. 

[block:code]
{
  "codes": [
    {
      "code": "EOSIO_DISPATCH( myclass, (myaction1)(myaction2)(myacction3))",
      "language": "text"
    }
  ]
}
[/block]
The `EOSIO_DISPATCH` macro abstracts the dispatcher with a common pattern.
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
      "code": "#include <eosiolib/eosio.hpp>\n\nusing namespace eosio;\n\nCONTRACT hodl : public eosio::contract {\n  private:\n\n  public:\n  \n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
This contract will require some constant variables, to configure the contract. 
- When is the hodl over?
- What symbol does this contract accept?

Let us now define some constants:

- `the_party` constant sets the hodl is over at Tuesday, February 22, 2022 10:22:22 PM

- `symbol`: the symbol of tokens this contract is going to accept. In this case we use "SYS"

[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nCONTRACT hodl : public eosio::contract {\n  private:\n  \tstatic const uint64_t the_party = 1645568542;\n    static const uint64_t symbol = string_to_symbol(4, \"SYS\");\n  public:\n  \t\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
cleos push action hodl deposit '["han", "hodl", "1 SYS", "test"]' -p han@active
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n#include <eosiolib/asset.hpp>\n\nusing namespace eosio;\n\nCONTRACT hodl : public eosio::contract {\nprivate:\n  static const uint64_t the_party = 1645568542;\n  const symbol hodl_symbol;\n\npublic:\n  using contract::contract;\n\n  hodl(name receiver, name code, datastream<const char *> ds) : contract(receiver, code, ds),hodl_symbol(\"SYS\", 4)\n  {\n    eosio_assert(now() < the_party, \"Party should start after now, not before now.\");\n  }\n\n  ACTION deposit(name hodler, name to, eosio::asset quantity, std::string memo)\n  {\n\n    if (to != _self || hodler == _self)\n    {\n      print(\"These are not the droids you are looking for.\");\n      return;\n    }\n\n    eosio_assert(now() < the_party, \"You're way late\");\n    eosio_assert(quantity.amount > 0, \"When pigs fly\");\n    eosio_assert(quantity.symbol == hodl_symbol, \"These are not the droids you are looking for.\");\n\n    balance_table balance(_self, hodler.value);\n    auto hodl_it = balance.find(hodl_symbol.raw());\n\n    asset new_balance;\n    if (hodl_it != balance.end())\n      balance.modify(hodl_it, hodler, [&](auto &row) {\n        row.funds += quantity;\n        new_balance = row.funds;\n      });\n    else\n      balance.emplace(hodler, [&](auto &row) {\n        row.funds = quantity;\n        new_balance = row.funds;\n      });\n  }\n\n  ACTION party(name hodler)\n  {\n\n    require_auth(hodler);\n    eosio_assert(now() > the_party, \"Hold your horses\");\n\n    balance_table balance(_self, hodler.value);\n\n    auto hodl_it = balance.find(hodl_symbol.raw());\n\n    eosio_assert(hodl_it != balance.end(), \"You're not allowed to party\");\n\n    action{\n      permission_level{get_self(), \"active\"_n},\n      \"eosio.token\"_n,\n      \"transfer\"_n,\n      std::make_tuple(get_self(), hodler, hodl_it->funds, \"Party! Your hodl is free.\")\n    }\n    .send();\n\n    balance.erase(hodl_it);\n  }\n\nprivate:\n  TABLE balance\n  {\n    eosio::asset funds;\n    uint64_t primary_key() const { return funds.symbol.raw(); }\n  };\n\n  using balance_table = eosio::multi_index<\"balance\"_n, balance>;\n};\n\nextern \"C\"\n{\n  void apply(uint64_t receiver, uint64_t code, uint64_t action)\n  {\n\n    if (code == receiver && action == name(\"party\").value)\n    {\n      execute_action(name(receiver), name(code), &hodl::party);\n    }\n    else if (code == name(\"eosio.token\").value && action == name(\"transfer\").value)\n    {\n      execute_action(name(receiver), name(code), &hodl::deposit);\n    }\n  }\n};",
      "language": "cplusplus"
    }
  ]
}
[/block]