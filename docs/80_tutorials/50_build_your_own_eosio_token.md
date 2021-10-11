---
content_title: Build Your Own EOSIO Token Tutorial
link_text: Build Your Own EOSIO Token Tutorial
---

This tutorial provides explanations and a step-by-step procedure to create and deploy an EOSIO blockchain token starting with the *sample* EOSIO token smart contract. It is recommended, for understanding the *sample* EOSIO token smart contract,  to read the “EOSIO Token Tutorial”.

## Introduction

An EOSIO-based blockchain allows you to create tokens. There are many ways in which you can create tokens. One way is to leverage the existing `eosio.token` sample smart contract and build on top of it a token that meets your requirements.

## Learning Objectives

The learning objectives for this tutorial are:

* Application
    * Create a new token starting with the `eosio.token` sample smart contract
    * Customize the `eosio.token` sample smart contract
    * Build and deploy a smart contract to a blockchain that uses EOSIO tokens
    * Create, issue, and transfer EOSIO tokens
    * Create and use the airgrab action

## Create A New Token

To create a new token, create the smart contract that manages that token. A token can take many forms and have various features. 

Select of the following techniques to create a smart contract that manages a token:
* Develop the smart contract from scratch
* Use the existing ‘eosio.token’ sample smart contract as is
* Use the existing ‘eosio.token’ sample smart contract and customize it to meet your requirements

This tutorial demonstrates the steps to customize, build and deploy a new token smart contract, which manages a token with symbol *NEWT*, starting with the `eosio.token` sample smart contract.

### Procedure

This procedure shows you how to implement the following five steps to extend or change the ‘eosio.token’ smart contract:

1. [Duplicate the original `eosio.token` smart contract ](#step-1-duplicate-the-eosiotoken-sources)
2. [Specialize the new token according to its requirements](#step-2-specialize-the-newt-smart-contract)
3. [Extend the new token functionality with an `airgrab` action](#step-3-extend-the-newt-smart-contract)
4. [Compile and deploy the new token](#step-4-compile-and-deploy-newt-token-to-the-blockchain)
5. [Thoroughly test your token to behave correctly in all cases](#step-5-test-newt-token)

#### Prerequisites

Make sure the following prerequisites are met before starting this procedure.

##### Nodeos and Wallet Prerequisites

* There is a local *nodeos* started with the default connection port. Refer to instructions on how to start one in this [how to](https://developers.eos.io/manuals/eos/latest/nodeos/usage/development-environment/local-single-node-testnet).
* Your public and private key pair are in your [wallet](https://developers.eos.io/welcome/latest/getting-started-guide/local-development-environment/development-wallet) and the wallet is opened before executing the commands presented in the following sections.

##### Test Accounts Prerequisites

Make sure you have test accounts ready in your development environment for testing purposes. The tutorial uses *newt* and *ama* accounts. You can create them, or use the ones you already have and substitute them accordingly.

You can learn [here](https://developers.eos.io/welcome/latest/getting-started/development-environment/create-test-accounts) how to create accounts with the *cleos* command line tool. Or you can execute the following commands and replace the public key with your own:

```sh
cleos create account eosio newt EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
cleos create account eosio ama EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
```

#### New Token Smart Contract Requirements

* Your smart contract creates and manages only one token with symbol *NEWT*
* The *NEWT* token can be created only by the smart contract account owner
* The maximum amount of *NEWT* tokens is 21 million
* The *NEWT* token can be airgrabed by a particular set of accounts. Only the account names that start with a vowel will be able to grab your token, with a first come first served rule

**Note**: Whenever you find the *EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV* public key is part of the shell commands, you will have to substitute it with your own public key.

#### Step 1: Duplicate The *eosio.token* Sources

Clone the [eosio.token repo](https://github.com/eosio/eosio.token) from GitHub and copy its sources to a new folder *newt*.

```sh
cd ~
git clone https://github.com/EOSIO/eosio.token.git
mkdir newt
cp eosio.token/contracts/eosio.token/include/eosio.token/eosio.token.hpp newt
cp eosio.token/contracts/eosio.token/src/eosio.token.cpp newt
cd newt
```

Rename the files to suit the `newt` token name.

```sh
mv eosio.token.hpp newt.hpp
mv eosio.token.cpp newt.cpp
```

Change this line from newt.hpp 

```cpp
class [[eosio::contract("eosio.token")]] token : public contract {
```

to

```cpp
class [[eosio::contract("newt")]] token : public contract {
```

This change tells the compiler that the customized smart contract name is `newt`. The attribute `[[eosio::contract]]`, if it has no parameter specified, uses by default the contract `token` *class name*. The EOSIO framework uses the name of the contract to logically connect actions, tables and notification handlers to a specific compiled smart contract. The contract name if specified in the `[[eosio::contract]]` attribute must meet the [restrictions of an EOSIO account name](https://developers.eos.io/welcome/latest/glossary/index/#account-name) whereas the contract *class name* is free of those constraints.

Change this line from newt.cpp

```cpp
#include <eosio.token/eosio.token.hpp>
```

to 

```cpp
#include "newt.hpp"
```

###### Build And Deploy The *newt* Smart Contract

As a quick verification step build and deployed your new token to the blockchain.

To build the *newt* token run the following commands from command shell:

```sh
cd ~/newt
eosio-cpp -abigen -abigen_output=newt.abi -o newt.wasm newt.cpp
ls -al
```

If you executed every step correctly and no error occurs the last command prints all the files in the current directory and the list of files looks like this:

```sh
.  ..  newt.abi  newt.cpp  newt.hpp  newt.wasm
```

You can now deploy the *newt.wasm* on the blockchain. To do so run the following command:

```sh
cleos set contract newt . --abi newt.abi newt.wasm -p newt@active
```

#### Step 2. Specialize The *newt* Smart Contract

The `eosio.token` smart contract is generic and it can deal with multiple tokens created by different accounts. Therefore the newly created token you have at this time has the exact same properties as the `eosio.token`. However, one of the requirements for your token is to be specialized, that is, to deal with only one token and thus only one account token owner. To realize this restriction you have to make the following changes.

##### Update The *create* Action

Update the `create` action with the code below:

```cpp
  void token::create() {
     require_auth(get_self());

     auto sym = symbol("NEWT", 4); // NEWT is the token symbol with precision 4
     auto maximum_supply = asset(210000000000, sym);

     stats statstable(get_self(), sym.code().raw());
     auto existing = statstable.find(sym.code().raw());
     check(existing == statstable.end(), "token with symbol already created");

     statstable.emplace(get_self(), [&](auto &s) {
        s.supply.symbol = sym;
        s.max_supply = maximum_supply;
        s.issuer = get_self();
     });
  }
```

**Note**: The create action now does not need input parameters, because the only token that can be created is the *NEWT* token and can only be created by the smart contract owner.

Also the `create` action mints 21 million tokens. Note how the 21 million is specified in the code as ``210000000000``, that is 21 million followed by 4 zeros. Because the precision was defined one line above as 4, you have to add 4 zeros at the end of the 21 million.

##### Update The *issue* Action

Update the `issue` action with the code below:

```cpp
  void token::issue(const asset &quantity, const string &memo) {
     require_auth(get_self());

     auto sym = quantity.symbol;
     auto newtsym_code = symbol("NEWT", 4); // NEWT is the token symbol with precision 4
     check(sym.code() == newtsym_code.code(), "This contract can handle NEWT tokens only.");
     check(sym.is_valid(), "invalid symbol name");
     check(memo.size() <= 256, "memo has more than 256 bytes");

     stats statstable(get_self(), sym.code().raw());
     auto existing = statstable.find(sym.code().raw());
     check(existing != statstable.end(), "token with symbol does not exist, create token before issue");

     const auto& existing_token = *existing;
     require_auth( existing_token.issuer );

     check(quantity.is_valid(), "invalid quantity");
     check(quantity.amount > 0, "must issue positive quantity");
     check(quantity.symbol == existing_token.supply.symbol, "symbol precision mismatch");
     check(quantity.amount <= existing_token.max_supply.amount - existing_token.supply.amount,
                                "quantity exceeds available supply");

     statstable.modify(existing_token, same_payer, [&](auto &s) {
        s.supply += quantity;
     });

     add_balance(existing_token.issuer, quantity, existing_token.issuer);
  }
```

The `issue` action does not need the `to` parameter anymore because the issuing of new tokens can only be done for *NEWT* token symbol and for only one account, the smart contract owner account.

There are also two new lines of code introduced which check if the `asset` received as parameter matches the *NEWT* token symbol.

```cpp
     auto newtsym_code = symbol("NEWT", 4); // NEWT is the token symbol with precision 4
     check(sym.code() == newtsym_code.code(), "This contract can handle NEWT tokens only.");
```

##### Update The *retire* Action

Update the `retire` action with the code below:

```cpp
  void token::retire(const asset &quantity, const string &memo) {
     auto sym = quantity.symbol;
     check(sym.is_valid(), "invalid symbol name");
     check(memo.size() <= 256, "memo has more than 256 bytes");
     auto newtsym_code = symbol("NEWT", 4); // NEWT is the token symbol with precision 4
     check(sym.code() == newtsym_code.code(), "This contract can handle NEWT tokens only.");

     stats statstable(get_self(), sym.code().raw());
     auto existing = statstable.find(sym.code().raw());
     check(existing != statstable.end(), "token with symbol does not exist");
     const auto &st = *existing;

     require_auth(st.issuer);
     check(quantity.is_valid(), "invalid quantity");
     check(quantity.amount > 0, "must retire positive quantity");

     check(quantity.symbol == st.supply.symbol, "symbol precision mismatch");

     statstable.modify(st, same_payer, [&](auto &s) {
        s.supply -= quantity;
     });

     sub_balance(st.issuer, quantity);
  }
```

The only addition to this action is the check to make sure that the `asset` received as input parameter matches the *NEWT* token symbol.

```cpp
     auto newtsym_code = symbol("NEWT", 4); // NEWT is the token symbol with precision 4
     check(sym.code() == newtsym_code.code(), "This contract can handle NEWT tokens only.");
```

##### Update The *transfer* Action

Update the `transfer` action with the code below:


```cpp
  void token::transfer(const name &from,
                       const name &to,
                       const asset &quantity,
                       const string &memo) {
     check(from != to, "cannot transfer to self");
     require_auth(from);
     check(is_account(to), "to account does not exist");
     auto sym = quantity.symbol.code();

     auto newtsym_code = symbol("NEWT", 4); // NEWT is the token symbol with precision 4
     check(sym == newtsym_code.code(), "This contract can handle NEWT tokens only.");
     stats statstable(get_self(), sym.raw());
     const auto &st = statstable.get(sym.raw());

     require_recipient(from);
     require_recipient(to);

     check(quantity.is_valid(), "invalid quantity");
     check(quantity.amount > 0, "must transfer positive quantity");
     check(quantity.symbol == st.supply.symbol, "symbol precision mismatch");
     check(memo.size() <= 256, "memo has more than 256 bytes");

     auto payer = has_auth(to) ? to : from;

     sub_balance(from, quantity);
     add_balance(to, quantity, payer);
  }
```

As with the previous action, the only addition to this action is the check to make sure that the `asset` received as input parameter matches the *NEWT* token symbol.

```cpp
     auto newtsym_code = symbol("NEWT", 4); // NEWT is the token symbol with precision 4
     check(sym.code() == newtsym_code.code(), "This contract can handle NEWT tokens only.");
```

#### Step 3. Extend The *newt* Smart Contract

Another requirement for your token is to be able to be airgrabbed by accounts which start with a vowel. To realize this, extend the `newt` smart contract with an `airgrab` action. The `airgrab` action allows an account which starts with a vowel to receive 100 *NEWT* tokens only once.

In _newt.hpp_, right after the `close` action, add a declaration for the `airgrab` action like below:

```cpp
[[eosio::action]]
void airgrab(const name &owner);
```

Create an action wrapper next to the already existing ones:

```cpp
using airgrab_action = eosio::action_wrapper<"airgrab"_n, &token::airgrab>;
```

Finally, create a new table that stores all accounts that airgrabbed tokens. Include the following structure and type definition:

```cpp
struct [[eosio::table]] airgrab_list {
    name account;

    uint64_t primary_key()const { return account.value; }
};

typedef eosio::multi_index< "airgrabs"_n, airgrab_list > airgrabs;
```

Add in the private methods declaration section the `starts_with_vowel` which checks if an account name starts with a vowel:

```cpp
int starts_with_vowel(string account_name);
```

Move to *newt.cpp* and add the `airgrab` action and `starts_with_vowel` implementations at the end of the contract:

```cpp
  void token::airgrab(const name &owner) {
     check(starts_with_vowel(owner.to_string()) == 0,
           "Account is not qualified, it must start with a vowel.");
     check(_self != owner, "Cannot airgrab from NEWT owner account.");

     require_auth(owner);
     require_recipient(_self); // from
     require_recipient(owner); // to

     auto sym = symbol("NEWT", 4); // NEWT is the token symbol with precision 4
     asset airgrabbed_asset(1000000, sym);    // allow 100 tokens to be airgrabbed

     // Check if the user have airgrabbed their tokens
     airgrabs airgrab_table(get_self(), sym.raw());

     auto it = airgrab_table.find(owner.value);
     check(it == airgrab_table.end(), "You have already airgrabbed your tokens");

     sub_balance(_self, airgrabbed_asset);
     add_balance(owner, airgrabbed_asset, owner);

     // Register the airgrab so it will not be able to do it the second time
     airgrab_table.emplace(owner, [&](auto &row) {
        row.account = owner;
     });
  }

  int token::starts_with_vowel(string account_name) {
     if (!(account_name[0] == 'A' || account_name[0] == 'a' || account_name[0] == 'E'
           || account_name[0] == 'e' || account_name[0] == 'I' || account_name[0] == 'i'
           || account_name[0] == 'O' || account_name[0] == 'o' || account_name[0] == 'U'
           || account_name[0] == 'u'))
        return 1;
     else
        return 0;
  }
```

Go through the airgrab action implementation. You should be familiar with most of the checks. This section will focus on the new parts of the code.

The first check is for the account name to start with a vowel.

Then it checks for the account which does the airgrab to not be the smart contract owner.

In the next lines of code, you initialize the table that you will use to keep track of all accounts that claimed their free tokens. You also have a check that prevents accounts from claiming tokens twice.

Finally, if the account airgrabs the tokens for the first time, the code updates the account’s balance, transfers the tokens and updates the airgrab table. The same steps are done by the `transfer` action as well. The difference this time is that the account which receives the airgrabbed tokens pays for the used resources. Note the `owner` account which is sent as payer (last parameter) to the `add_balance` method invocation:

```cpp
 add_balance(owner, airgrabbed_asset, owner);
```

#### Step 4: Compile And Deploy NEWT Token To The Blockchain

Compile and deploy your newly created token smart contract to the blockchain.

##### Compile

Compile the smart contract:

```sh
eosio-cpp -abigen -abigen_output=newt.abi -o newt.wasm newt.cpp
```

##### Deploy

Deploy the smart contract with the *newt* account:

```sh
cleos set contract newt . --abi newt.abi newt.wasm -p newt@active
```

#### Step 5: Test NEWT Token

To test the NEWT token execute the following actions using the `cleos` command line tool.

##### Create a new token

To create the *NEWT* token use the following command:

```sh
cleos push action newt create '[]' -p newt@active
```

Output:

```text
	executed transaction: 098fb8b4089d86f36acf21c47a6f62946a5af162c14ad6a876e7aba06a7c5505  96 bytes  233 us
	#          newt <= newt::create                 ""
	warning: transaction executed locally, but may not be confirmed by the network yet         ]
```

Try to execute the same command again. You will see it failed with the below error message:

```text
Error 3050003: eosio_assert_message assertion failure
Error Details:
assertion failure with message: token with symbol already created
pending console output: 
```

Execute the following command to verify that `newt` account owns the NEWT tokens:

```sh
cleos get table newt NEWT stat
```

Output:

```json
{
  "rows": [{
      "supply": "0.0000 NEWT",
      "max_supply": "21000000.0000 NEWT",
      "issuer": "newt"
    }
  ],
  "more": false,
  "next_key": "",
  "next_key_bytes": ""
}
```

A similar command to the one above is the following:

```sh
cleos get currency stats newt NEWT
```

##### Issue New Tokens

Issue 1000 NEWT tokens. To execute the action, use the following command:

```sh
cleos push action newt issue '["1000.0000 NEWT", "issue 1000 NEWT"]' -p newt@active
```

Output:

```text
executed transaction: 56e205345a6cf397b8ba0684f375996daff5e2865f424bd0261c4747b740c755  128 bytes  176 us
	#          newt <= newt::issue                  {"quantity":"1000.0000 NEWT","memo":"issue 1000 NEWT"}
	warning: transaction executed locally, but may not be confirmed by the network yet         ] 
```

You can check again with the same command from above that the supply for the NEWT token changed:

```sh
cleos get table newt NEWT stat
```

Output:

```json
{
  "rows": [{
      "supply": "1000.0000 NEWT",
      "max_supply": "21000000.0000 NEWT",
      "issuer": "newt"
    }
  ],
  "more": false,
  "next_key": "",
  "next_key_bytes": ""
}
```

##### Transfer Tokens

Now that you have issued tokens, you can transfer *NEWT* tokens to the `ama` test account you created earlier in the tutorial. To transfer 100 *NEWT* tokens use the following command:

```sh
cleos push action newt transfer '[ "newt", "ama", "100.0000 NEWT", "enjoy the NEWT tokens, spend them wisely" ]' -p newt@active
```

Output:

```text
executed transaction: 6fd8c626658ca4aaca1f255ef31b58bd3de507055be440c6214391ae34737ea6  168 bytes  333 us
	#          newt <= newt::transfer               {"from":"newt","to":"ama","quantity":"100.0000 NEWT","memo":"enjoy the NEWT tokens, spend them wisel...
	#           ama <= newt::transfer               {"from":"newt","to":"ama","quantity":"100.0000 NEWT","memo":"enjoy the NEWT tokens, spend them wisel...
	warning: transaction executed locally, but may not be confirmed by the network yet         ] 
```


A similar command to the one above is the following:

```sh
cleos transfer newt ama "100.0000 NEWT" "enjoy the NEWT tokens, spend them wisely" -c newt -p newt
```

Check the balances have updated on the two accounts:

```sh
cleos get currency balance newt newt NEWT
```

Output:

```text
900.0000 NEWT
```

```sh
cleos get currency balance newt ama NEWT
```

Output:

```text
100.0000 NEWT
```

##### Airgrab tokens

Finally, test the airgrab action. To execute it use the command below: 

```sh
cleos push action newt airgrab '[ "ama", "100.0000 NEWT"]' -p ama@active
```

Output:

```text
executed transaction: 9310694a185896c4706ce1db94f15e8139a73a921ad301919ba63498d03e36b1  104 bytes  257 us
	#          newt <= newt::airgrab                {"owner":"ama"}
	#           ama <= newt::airgrab                {"owner":"ama"}
	warning: transaction executed locally, but may not be confirmed by the network yet         ] 
```

If you try to airgrab again for `ama` account you will see the error below:

```text
Error 3050003: eosio_assert_message assertion failure
	Error Details:
	assertion failure with message: You have already airgrabbed your tokens
	pending console output: 
```

You can check now the `ama` account balance:

```sh
cleos get currency balance newt ama NEWT
```

And the output is:

```text
200.0000 NEWT
```

You can also verify that the airgrab was successful if you check the `airgrabs` table with the following command:

```sh
cleos get table newt NEWT airgrabs
```

Output:

```json
{
  "rows": [{
      "account": "ama"
    }
  ],
  "more": false,
  "next_key": "",
  "next_key_bytes": ""
}
```

## Summary

This tutorial demonstrated:
* How the `eosio.token` smart contract works
* How to create a new token based on the `eosio.token` smart contract
* How to customize your new token
* How to *airgrab* your new token
* How to deploy and test your new token


## Acknowledgements

_Thank you Dimo (**@ddzhurenov**) for your assistance with this tutorial._

## Next Steps

If you want to learn more, check the [tic-tac-toe game](20_tic-tac-toe-game-smart-contract-single-node.md) smart contract tutorial.
