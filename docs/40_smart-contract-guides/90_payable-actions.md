---
content_title: "Payable actions"
link_text: "Payable actions"
---
This tutorial shows how to write a smart contract that has payable actions. 

## Introduction
Payable actions are actions that require you to transfer some tokens to actions prior to use other functionality of the smart contract. Also, the EOSIO `asset` type is covered in this tutorial.

As for the logic of this smart contract, we're going to write a contract that accepts a particular token but will not allow the tokens to be withdrawn for a specific amount of time.

## The token to HODL
First create a standard C++ class called "hodl" that extends `eosio::contract`.
```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract("hodl")]] hodl : public eosio::contract{
  private:
  public:
}
```
This contract needs to set up a few constraints:

- What symbol/token does this contract accept?
- When is the hodl over?

Let us now define these constraints as constants:

- `hodl_symbol`: the symbol of tokens this contract accepts. In this case, we use the "SYS" symbol.
- `the_party` constant sets the hodl to end on Tuesday, February 22, 2022 10:22:22 PM.
```cpp
#include <eosiolib/eosio.hpp>

using namespace eosio;

class [[eosio::contract("hodl")]] hodl : public eosio::contract {
  private:
    static const uint32_t the_party = 1645525342;
    const symbol hodl_symbol;
  public:

}
```
Next, let's define a table to track the number of tokens the `hodl` contract has received.
```cpp
struct [[eosio::table]] balance
{
  eosio::asset funds;
  uint64_t primary_key() const { return funds.symbol.raw(); }
};
```
In this multiple index table declaration, a new type called `asset` is used.  An `asset` is a type designed to represent a digital token asset. See more details in the [asset reference documentation](https://developers.eos.io/manuals/eosio.cdt/latest/structeosio_1_1asset).

The `symbol` member of an asset instance will be used as the primary key.  By calling the `raw()` function the `symbol` variable will be converted into an unsigned integer so it can be used as a primary key.

## Constructor
The constructor initializes the hodl_symbol as “SYS”, which is a token created in the [Deploy, Issue and Transfer Tokens](./20_deploy-issue-and-transfer-tokens.md#step-5-create-the-token) section.
```cpp
public:
  using contract::contract;
  hodl(name receiver, name code, datastream<const char *> ds):contract(receiver, code, ds), hodl_symbol("SYS", 4){}
```

## Get current UTC time
In order to get time in UTC timezone throughout the code, create a function to easily access the current UTC time.
```cpp
uint32_t now() {
  return current_time_point().sec_since_epoch();
}
```
Next, we'll write the actions of the contract.
## Deposit
To accept a transfer we need to have a deposit action.
```cpp
[[eosio::on_notify("eosio.token::transfer")]]
void deposit(name hodler, name to, eosio::asset quantity, std::string memo)
{
  if (to != get_self() || hodler == get_self())
  {
    print("These are not the droids you are looking for.");
    return;
  }

  check(now() < the_party, "You're way late");
  check(quantity.amount > 0, "When pigs fly");
  check(quantity.symbol == hodl_symbol, "These are not the droids you are looking for.");

  balance_table balance(get_self(), hodler.value);
  auto hodl_it = balance.find(hodl_symbol.raw());

  if (hodl_it != balance.end())
    balance.modify(hodl_it, get_self(), [&](auto &row) {
      row.funds += quantity;
    });
  else
    balance.emplace(get_self(), [&](auto &row) {
      row.funds = quantity;
    });
}
```
This action should not introduce many new concepts if you have followed this tutorial from the beginning.

Firstly, the action checks that the contract is not transferring to itself:
```cpp
if (to != get_self() || hodler == get_self()) {
  print("These are not the droids you are looking for.");
  return;
}
```
The contract needs to do so because transferring to the contract account itself would create an invalid booking situation in which an account could have more tokens than the account has in the `eosio.token` contract.

Then this action checks a few other conditions:

* The time to withdraw has not already passed
* The incoming transfer has a valid amount of tokens
* The incoming transfer uses the token we specify in the constructor
```cpp
check(now() < the_party, "You're way late");
check(quantity.amount > 0, "When pigs fly");
check(quantity.symbol == hodl_symbol, "These are not the droids you are looking for.");
```
If all constraints are passed, the action updates the balances accordingly:
```cpp
balance_table balance(get_self(), hodler.value);
auto hodl_it = balance.find(hodl_symbol.raw());

if (hodl_it != balance.end())
  balance.modify(hodl_it, get_self(), [&](auto &row) {
    row.funds += quantity;
  });
else
  balance.emplace(get_self(), [&](auto &row) {
    row.funds = quantity;
  });
```
The important thing to note is the deposit function will actually be triggered by the `eosio.token` contract. To understand this behaviour we need to understand the `on_notify` attribute.
## The on_notify attribute

```cpp
[[eosio::on_notify("eosio.token::transfer")]]
```
The `on_notify` attribute is one of the EOSIO.CDT [attributes](https://developers.eos.io/manuals/eosio.cdt/latest/best-practices/abi/abi-code-generator-attributes-explained) that annotates a smart contract action.

Annotating an action with an [`on_notify`](https://developers.eos.io/manuals/eosio.cdt/latest/best-practices/abi/abi-code-generator-attributes-explained/#eosioon_notifyvalid_eosio_account_namevalid_eosio_action_name) attribute ensures any incoming notification is forwarded to the annotated action if and only if the notification is dispatched from a specified contract and from a specified action.

In this case, the `on_notify` attribute ensures the incoming notification is forward to the deposit action only if the notification comes from the `eosio.token` contract and is from the `eosio.token`'s `transfer` action.

This is also why we don't need to check if the hodler actually has the appropriate amount of tokens he or she claimed, as the `eosio.token` contract would have done this check prior to the transfer notification reaching the `hodl` `deposit` action.
## Party!
The party action will only allow withdrawals after the configured `the_party` time has elapsed. The party action has a similar construct as the deposit action with the following conditions:

* check the withdrawing account is the account which made the deposit initially
* find the locked balance
* transfer the token from the `hodl` contract to the account itself
```cpp
[[eosio::action]]
void party(name hodler)
{
  //Check the authority of hodler
  require_auth(hodler);

  //Check the current time has passed the the_party time
  check(now() > the_party, "Hold your horses");

  balance_table balance(get_self(), hodler.value);
  auto hodl_it = balance.find(hodl_symbol.raw());

  //Make sure the holder is in the table
  check(hodl_it != balance.end(), "You're not allowed to party");

  action{
    permission_level{get_self(), "active"_n},
    "eosio.token"_n,
    "transfer"_n,
    std::make_tuple(get_self(), hodler, hodl_it->funds, std::string("Party! Your hodl is free."))
  }.send();

  balance.erase(hodl_it);
}
```
The complete code listing is the following:
```cpp
#include <eosio/eosio.hpp>
#include <eosio/print.hpp>
#include <eosio/asset.hpp>
#include <eosio/system.hpp>

using namespace eosio;

class [[eosio::contract("hodl")]] hodl : public eosio::contract {
  private:
    static const uint32_t the_party = 1645525342;
    const symbol hodl_symbol;

    struct [[eosio::table]] balance
    {
      eosio::asset funds;
      uint64_t primary_key() const { return funds.symbol.raw(); }
    };

    using balance_table = eosio::multi_index<"balance"_n, balance>;

    uint32_t now() {
      return current_time_point().sec_since_epoch();
    }

  public:
    using contract::contract;

    hodl(name receiver, name code, datastream<const char *> ds) : contract(receiver, code, ds),hodl_symbol("SYS", 4){}

    [[eosio::on_notify("eosio.token::transfer")]]
    void deposit(name hodler, name to, eosio::asset quantity, std::string memo) {
      if (hodler == get_self() || to != get_self())
      {
        return;
      }

      check(now() < the_party, "You're way late");
      check(quantity.amount > 0, "When pigs fly");
      check(quantity.symbol == hodl_symbol, "These are not the droids you are looking for.");

      balance_table balance(get_self(), hodler.value);
      auto hodl_it = balance.find(hodl_symbol.raw());

      if (hodl_it != balance.end())
        balance.modify(hodl_it, get_self(), [&](auto &row) {
          row.funds += quantity;
        });
      else
        balance.emplace(get_self(), [&](auto &row) {
          row.funds = quantity;
        });
    }

    [[eosio::action]]
    void party(name hodler)
    {
      //Check the authority of hodlder
      require_auth(hodler);

      // //Check the current time has pass the the party time
      check(now() > the_party, "Hold your horses");

      balance_table balance(get_self(), hodler.value);
      auto hodl_it = balance.find(hodl_symbol.raw());

      // //Make sure the holder is in the table
      check(hodl_it != balance.end(), "You're not allowed to party");

      action{
        permission_level{get_self(), "active"_n},
        "eosio.token"_n,
        "transfer"_n,
        std::make_tuple(get_self(), hodler, hodl_it->funds, std::string("Party! Your hodl is free."))
      }.send();

      balance.erase(hodl_it);
    }
};
```
Great, let's deploy it.
## Test deposit
First, create an account and deploy to it:
```shell
cleos create account eosio hodl YOUR_PUBLIC_KEY
eosio-cpp hodl.cpp -o hodl.wasm
cleos set contract hodl ./ -p hodl@active
```
As mentioned in a previous tutorial, this contract needs an eosio.code permission:
```shell
cleos set account permission hodl active --add-code
```
Next, create a testing account:
```shell
cleos create account eosio han YOUR_PUBLIC_KEY
```
Let's transfer some SYS tokens issued in the previous section to `han`:
```shell
cleos push action eosio.token transfer '[ "alice", "han", "100.0000 SYS", "Slecht geld verdrijft goed" ]' -p alice@active
```
Finally, transfer some SYS tokens to the `hodl` contract from `han`'s account.
```shell
cleos transfer han hodl '0.0001 SYS' 'Hodl!' -p han@active
```

## Test withdraw
To test the withdrawal feature, the `the_party` variable needs to be updated. Update the `the_party` variable to a point in time in the past so the withdrawal functionality can be tested.
```cpp

CONTRACT hodl : public eosio::contract {
  private:
    // 9 June 2018 01:00:00
    static const uint32_t the_party = 1528549200;
```
Withdrawing the funds:
```text
cleos push action hodl party '["han"]' -p han@active
```
Should produce the following response:
```shell
executed transaction: 62b1e6848c8c5e6458b9a0f7600e65574eaf60445be114d224adccc5a962a09a  104 bytes  383 us
#          hodl <= hodl::party                  {"hodler":"han"}
#   eosio.token <= eosio.token::transfer        {"from":"hodl","to":"han","quantity":"0.0001 SYS","memo":"Party! Your hodl is free."}
#          hodl <= eosio.token::transfer        {"from":"hodl","to":"han","quantity":"0.0001 SYS","memo":"Party! Your hodl is free."}
#           han <= eosio.token::transfer        {"from":"hodl","to":"han","quantity":"0.0001 SYS","memo":"Party! Your hodl is free."}
```

Party time!

## What's Next

- [Elemental Battles](https://battles.eos.io): Build a blockchain game based on EOSIO and continue building your EOSIO knowledge!
