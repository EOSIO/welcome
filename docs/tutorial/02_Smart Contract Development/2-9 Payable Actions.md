---
title: "2.9 Payable Actions"
excerpt: ""
---
## Step 1: the EOSIO_DISPATCH Macro
Up until now, we've been using a nifty little macro. 


```text
EOSIO_DISPATCH( myclass, (myaction1)(myaction2)(myacction3))
```
The `EOSIO_DISPATCH` macro abstracts the dispatcher with a common pattern.
- The base class is set, `myclass`
- The actions exposed are defined.
- A dispatched action's arguments are positional.
## Step 2: The HODL Contract
We're going to write a simple contract that accepts allows payment of a particular token, but will not allow the tokens to be withdrawn for a specific amount of time. 

First create a standard C++ class called "hodl" that extends `eosio::contract`.

```cpp
#include <eosiolib/eosio.hpp>

using namespace eosio;

CONTRACT hodl : public eosio::contract {
  private:

  public:
  
}
```
This contract will require some constant variables, to configure the contract. 
- When is the hodl over?
- What symbol does this contract accept?

Let us now define some constants:

- `the_party` constant sets the hodl is over at Tuesday, February 22, 2022 10:22:22 PM

- `symbol`: the symbol of tokens this contract is going to accept. In this case we use "SYS"


```cpp
#include <eosiolib/eosio.hpp>
#include <eosiolib/print.hpp>

using namespace eosio;

CONTRACT hodl : public eosio::contract {
  private:
  	static const uint64_t the_party = 1645568542;
    static const uint64_t symbol = string_to_symbol(4, "SYS");
  public:
  	
}
```
cleos push action hodl deposit '["han", "hodl", "1 SYS", "test"]' -p han@active

```cpp
#include <eosiolib/eosio.hpp>
#include <eosiolib/print.hpp>
#include <eosiolib/asset.hpp>

using namespace eosio;

CONTRACT hodl : public eosio::contract {
private:
  static const uint64_t the_party = 1645568542;
  const symbol hodl_symbol;

public:
  using contract::contract;

  hodl(name receiver, name code, datastream<const char *> ds) : contract(receiver, code, ds),hodl_symbol("SYS", 4)
  {
    eosio_assert(now() < the_party, "Party should start after now, not before now.");
  }

  ACTION deposit(name hodler, name to, eosio::asset quantity, std::string memo)
  {

    if (to != _self || hodler == _self)
    {
      print("These are not the droids you are looking for.");
      return;
    }

    eosio_assert(now() < the_party, "You're way late");
    eosio_assert(quantity.amount > 0, "When pigs fly");
    eosio_assert(quantity.symbol == hodl_symbol, "These are not the droids you are looking for.");

    balance_table balance(_self, hodler.value);
    auto hodl_it = balance.find(hodl_symbol.raw());

    asset new_balance;
    if (hodl_it != balance.end())
      balance.modify(hodl_it, hodler, [&](auto &row) {
        row.funds += quantity;
        new_balance = row.funds;
      });
    else
      balance.emplace(hodler, [&](auto &row) {
        row.funds = quantity;
        new_balance = row.funds;
      });
  }

  ACTION party(name hodler)
  {

    require_auth(hodler);
    eosio_assert(now() > the_party, "Hold your horses");

    balance_table balance(_self, hodler.value);

    auto hodl_it = balance.find(hodl_symbol.raw());

    eosio_assert(hodl_it != balance.end(), "You're not allowed to party");

    action{
      permission_level{get_self(), "active"_n},
      "eosio.token"_n,
      "transfer"_n,
      std::make_tuple(get_self(), hodler, hodl_it->funds, "Party! Your hodl is free.")
    }
    .send();

    balance.erase(hodl_it);
  }

private:
  TABLE balance
  {
    eosio::asset funds;
    uint64_t primary_key() const { return funds.symbol.raw(); }
  };

  using balance_table = eosio::multi_index<"balance"_n, balance>;
};

extern "C"
{
  void apply(uint64_t receiver, uint64_t code, uint64_t action)
  {

    if (code == receiver && action == name("party").value)
    {
      execute_action(name(receiver), name(code), &hodl::party);
    }
    else if (code == name("eosio.token").value && action == name("transfer").value)
    {
      execute_action(name(receiver), name(code), &hodl::deposit);
    }
  }
};
```
