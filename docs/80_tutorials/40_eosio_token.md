---
content_title: EOSIO Token Tutorial
link_text: EOSIO Token Tutorial
---

This tutorial explores the *sample* EOSIO token smart contract and it helps you acquire the basic knowledge needed to build your own EOSIO token. To learn how to create and manage your own token please read the “Build Your Own EOSIO Token Tutorial” after you have completed the current tutorial.

## Introduction

An EOSIO-based blockchain allows you to create tokens. Tokens serve various purposes which you will learn about later in this tutorial.

## Learning Objectives

The learning objectives for this tutorial are:

* Knowledge
    * What is a token?
    * What is a coin or a system token?
    * What is airdrop?
    * What is airgrab?
* Understanding
    * How does the ‘eosio.token’ smart contract code behaves?

## Concepts

This section introduces basic concepts related to tokens and coins and how they specifically relate to the EOSIO platform.

### Token

A token is a digital representation of stored value that enables you to exchange value. Tokens represent assets of all types. They are typically stored and exchanged for other tokens that represent other types of assets. Tokens are minted, issued, transferred, or burned.

### Digital Coin

A digital coin, or coin, is a special** token** of a blockchain. It is special because it is used to pay for the system resources of that blockchain and it is also named **system token**. A blockchain can have one system token, that is, one digital coin. There are very rare occasions when a blockchain has more than one system token. 

An EOSIO-based blockchain can be configured to have no system token, or one system token. Once you configured the system token you can not change it, that is, you can not change its symbol or name. The following table provides examples of EOSIO-based blockchains and their system tokens:


<table>
  <tr>
   <td><strong>EOSIO-Based Blockchain</strong>
   </td>
   <td><strong>System Token Name</strong>
   </td>
  </tr>
  <tr>
   <td>EOS
   </td>
   <td>EOS
   </td>
  </tr>
  <tr>
   <td>TELOS
   </td>
   <td>TLOS
   </td>
  </tr>
  <tr>
   <td>WAX
   </td>
   <td>WAX
   </td>
  </tr>
</table>



### Airdrop and Airgrab

Many times a token issuer needs to distribute their tokens to a discrete number of users. These users can vary from being a very restricted group based on certain criteria, or they can be a very wide group, such as all users of a blockchain. 

Airdrop and airgrab are the distribution processes that disperse tokens to users.

#### Airdrop

Airdrop is a process that distributes tokens to a list of users. Users do not pay for the tokens. Users receive the tokens for free. 

Use an airdrop when you want to raise your user’s interest in a project proposal or solution. Use an airdrop when you are motivated to reach as many users as possible or a particular set of users. For example, a token issuer airdrops tokens as a promotional tool. When a company sends tokens, users typically receive a notification about the token transfer that just took place, or they discover new tokens in their wallet. Once they have the tokens in their possession they can check the sender and get to learn about their project and/or business. 

The airdrop process requires resources (RAM, CPU, NET) for its execution. The token issuer pays for the resources to transfer the tokens. For example, when token issuer A uses the action `transfer` to send tokens to user B, token issuer A pays for the required resources necessary to execute the `transfer` action. The token issuer that executes the airdrop has to cover the cost of resources for all the token `transfer` actions for all targeted accounts. Therefore, a ‘transfer’ action can result in a significant cost, which is paid for by the token issuer.

#### Airgrab

Airgrab is a process that allows the users to claim (grab) issued tokens. The token issuer is not required to pay for the resources of executing the token transfer. For example, a token issuer uses the airgrab process when they have a small budget, such as startups and small businesses.

With airgrab, the token issuer gives away tokens to a targeted audience at no cost to them. The resources for the transfer operation come from the user executing the airgrab (claim) action. In this case the token issuer needs to use other marketing tools for the promotion or their project or solution to persuade users to claim their tokens and pay the associated costs.

Users airgrab (claim) tokens for several reasons:

* Special benefits of owning the tokens
* Future price increase (speculation)
* As a collectible

Therefore they have the incentive to go and `grab` them.

## Prerequisites

The following knowledge and tools are required to develop and run this tutorial:

* Medium knowledge of the C++ programming language
* Basic knowledge of the EOSIO platform
* C++ editor already installed
* EOSIO development environment including nodeos

If you need to set up your environment, follow the steps in the [Getting Started Guide](https://developers.eos.io/welcome/latest/getting-started-guide/local-development-environment/index). This guide provides instructions on how to start a local node with nodeos that produces blocks, creates a wallet that keeps your keys, and creates test accounts used later in this tutorial.

## EOSIO Token Smart Contract Reference

The EOSIO platform provides the ‘eosio.token’ smart contract, also known as the reference token smart contract. This smart contract implementation provides guidelines for a minimum set of basic mandatory and optional items that make up a token contract. Use this smart contract as it is provided or as a starting point for the implementation of your own token that contains customized business logic that meets your requirements.

**Note**: For more information, consult the [Proposed EOSIO Token Standard](https://github.com/EOSIO/EEPs/blob/master/EEPS/eep-3.md) in the EOSIO EEP system.


The `eosio.token` is implemented in two files:
* Eosio.token.hpp (header file)
* Eosio.token.cpp (implementation file)

In C++ these files are typically referred to as header and implementation files.

### The eosio.token.hpp File

The header file contains the smart contract  C++ class definition. The class definition consists of its public and private methods and attributes. The eosio.token.hpp file defines the two structures used by the smart contract to store information about the accounts and tokens:

* ‘Currency_stats’ - the table that stores the created token symbols and their account owners
* ‘Account’ - the table that stores accounts and the token balances for each account

These structures are the underlying data structures for two multi-index tables used by the smart contract to store information about the tokens.

Both tables are uniquely indexed by the token symbol therefore two entries with the same token symbol cannot exist in any of the two tables.

**Note**: Refer to the [Mullti-Index How Tos](https://developers.eos.io/manuals/eosio.cdt/latest/how-to-guides/multi-index/index) section for details on how to define and instantiate a multi-index table with code and scope and how to define indexes for multi-index tables.

### The eosio.token.cpp File

The  eosio.token.cpp file is the source file that contains public and private methods implementation. The actions of the smart contract are the public methods marked by the EOSIO `[[eosio::action]]` specific attribute.

The `eosio.token` smart contract contains the following actions and private methods:

<table>
  <tr>
   <td><strong>ACTION</strong>
   </td>
   <td><strong>DESCRIPTION</strong>
   </td>
  </tr>
  <tr>
   <td><strong><em>

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: undefined internal link (link text: "create"). Did you generate a TOC? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

<a href="#heading=h.4b8ujw9dhwd9">create</a></em></strong>
   </td>
   <td><em>This action creates a new token with a specified symbol and maximum supply</em>
   </td>
  </tr>
  <tr>
   <td><strong><em>

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: undefined internal link (link text: "issue"). Did you generate a TOC? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

<a href="#heading=h.sveb91tt7jle">issue</a></em></strong>
   </td>
   <td><em>This action issues N amount of tokens to the issuer</em>
   </td>
  </tr>
  <tr>
   <td><strong><em>

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: undefined internal link (link text: "retire"). Did you generate a TOC? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

<a href="#heading=h.nn9jkvvzpbkm">retire</a></em></strong>
   </td>
   <td><em>This action retires the token (opposite action of create)</em>
   </td>
  </tr>
  <tr>
   <td><strong><em>

<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: undefined internal link (link text: "transfer"). Did you generate a TOC? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

<a href="#heading=h.ardlzcwr99m1">transfer</a></em></strong>
   </td>
   <td><em>This action transfers tokens from account A to account B</em>
   </td>
  </tr>
  <tr>
   <td><strong><em>

<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: undefined internal link (link text: "sub_balance"). Did you generate a TOC? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

<a href="#heading=h.lotiwhixpiau">sub_balance</a></em></strong>
   </td>
   <td><em>This private method subtracts the balance of the account sending the tokens</em>
   </td>
  </tr>
  <tr>
   <td><strong><em>

<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: undefined internal link (link text: "add_balance"). Did you generate a TOC? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

<a href="#heading=h.b0wsbj4121bv">add_balance</a></em></strong>
   </td>
   <td><em>This private method adds to the balance of the account receiving the tokens</em>
   </td>
  </tr>
  <tr>
   <td><strong><em>

<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: undefined internal link (link text: "open"). Did you generate a TOC? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

<a href="#heading=h.cqktejzgcbv">open</a></em></strong>
   </td>
   <td><em>This action allows the <strong>ram_payer</strong> account to create an account <strong>owner</strong> with zero balance at the expense of <strong>ram_payer</strong> for specified token symbol</em>
   </td>
  </tr>
  <tr>
   <td><strong><em>

<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: undefined internal link (link text: "close"). Did you generate a TOC? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

<a href="#heading=h.q8qs718h8obx">close</a></em></strong>
   </td>
   <td><em>This action closes the account owner (opposite action of open)</em>
   </td>
  </tr>
</table>

### Create Action

The `create` action creates a new token with a specified symbol and maximum supply. This  action constructs a new record in the `statstable` table that contains the data for the token.

The code block below implements the business logic for the `create` action:

```cpp
void token::create( const name&   issuer, const asset&  maximum_supply )
{
   require_auth( get_self() );

   auto sym = maximum_supply.symbol;
   check( sym.is_valid(), "invalid symbol name" );
   check( maximum_supply.is_valid(), "invalid supply");
   check( maximum_supply.amount > 0, "max-supply must be positive");

   stats statstable( get_self(), sym.code().raw() );
   auto existing = statstable.find( sym.code().raw() );
   check( existing == statstable.end(), "token with symbol already exists" );

   statstable.emplace( get_self(), [&]( auto& s ) {
      s.supply.symbol = maximum_supply.symbol;
      s.max_supply    = maximum_supply;
      s.issuer        = issuer;
   });
}
```

#### Parameters

The `create` action takes two parameters:
* `issuer`: the account who is the token creator and owner
* `maximum_supply`: the maximum number of tokens of type `asset`. 
    * Specify the maximum supply amount and the token ‘symbol’ through the ‘asset’ type
    * The token `symbol` is a unique identifier for the token in the blockchain namespace and consists of `precision` and `name`. The token `name` must include only uppercase alphabet letters.

#### Implementation Notes

The action implementation does the following:

1. To authorize execution of the current action: calls the `require_auth` authorization method to check whether the smart contract account owner has signed the action currently processed
    **Note**: The smart contract account owner is obtained by the `get_self()` method call or a higher authority,

    Refer to these guidelines for more details to authorize the execution of a current action:
        * [How to implement authorization checks](https://developers.eos.io/manuals/eosio.cdt/v1.7/best-practices/securing_your_contract/#1-authorization-checks)
        * [Permissions](https://developers.eos.io/welcome/latest/smart-contract-guides/linking-custom-permission) tutorial for more details on how permissions work
2. Checks for the maximum supply amount and the token symbol
3. Determines whether the token already exists
4. Instantiates the `statstable` with the `code` parameter as the contract owner and the `scope` parameter as the token symbol; an important consequence is that there is *one instante table* created for each pair defined by a contract owner and a token symbol.

### Issue Action

The ‘issue’ action issues N amount of tokens to the account that created the tokens. Use an ‘issue’ action after token(s) are created to bring tokens into existence.

The code block below implements the business logic for the `issue` action:

```cpp
void token::issue( const name& to, const asset& quantity, const string& memo )
{
   auto sym = quantity.symbol;
   check( sym.is_valid(), "invalid symbol name" );
   check( memo.size() <= 256, "memo has more than 256 bytes" );

   stats statstable( get_self(), sym.code().raw() );
   auto existing = statstable.find( sym.code().raw() );
   check( existing != statstable.end(), "token with symbol does not exist, create token before issue" );
   const auto& st = *existing;
   check( to == st.issuer, "tokens can only be issued to issuer account" );

   require_auth( st.issuer );
   check( quantity.is_valid(), "invalid quantity" );
   check( quantity.amount > 0, "must issue positive quantity" );

   check( quantity.symbol == st.supply.symbol, "symbol precision mismatch" );
   check( quantity.amount <= st.max_supply.amount - st.supply.amount, "quantity exceeds available supply");

   statstable.modify( st, same_payer, [&]( auto& s ) {
      s.supply += quantity;
   });

   add_balance( st.issuer, quantity, st.issuer );
}
```

#### Parameters

The issue action takes three parameters:

* `to`: the token issuer account designated in the ‘issuer’ parameter of the ‘create’ action; only the issuer can issue new tokens
* `quantity`: the amount of tokens to be issued
* `memo`: optional message to be persisted on the blockchain with the transaction that executes the action. 


#### Implementation Notes

1. Check any conditions that must be met.
    For example: The following two lines show that the action allows only the token creator to issue tokens:

    ```cpp
        check( to == st.issuer, "tokens can only be issued to issuer account" );
        require_auth( st.issuer );
    ```

    The authorization method `require_auth` ensures that action is authorized only by the token issuer or a higher authority.

2. The code modifies the supply for the newly issued token which is recorded in the `statstable` instance
3. The modify method accepts two parameters `st` and `same_payer`:
    - `st` is the existing updated table entry
    - `same_payer` is a constant expression defined by the EOSIO framework in the `multi_index.hpp` file.
    
    **Note**: When used, if the new stored value requires more RAM, the extra needed RAM is paid by the same account that originally paid for the table entry. If the new value requires less RAM, a new fee is not incurred.

4. The private *add_balance* method modifies the token balance for the issuer account as explained later in the [“Add Balance Method”](#add-balance-method) section of the tutorial.
5. The code modifies the balance of the token issuer by using the private *add_balance* method which is explained later in the tutorial. 

### Retire Action

The ‘retire’ action is the opposite action of `create` action.

#### Implementation Notes

The code block below implements the business logic for the `retire` action:

```cpp
void token::retire( const asset& quantity, const string& memo )
{
   auto sym = quantity.symbol;
   check( sym.is_valid(), "invalid symbol name" );
   check( memo.size() <= 256, "memo has more than 256 bytes" );

   stats statstable( get_self(), sym.code().raw() );
   auto existing = statstable.find( sym.code().raw() );
   check( existing != statstable.end(), "token with symbol does not exist" );
   const auto& st = *existing;

   require_auth( st.issuer );
   check( quantity.is_valid(), "invalid quantity" );
   check( quantity.amount > 0, "must retire positive quantity" );

   check( quantity.symbol == st.supply.symbol, "symbol precision mismatch" );

   statstable.modify( st, same_payer, [&]( auto& s ) {
      s.supply -= quantity;
   });

   sub_balance( st.issuer, quantity );
}
```

The ‘retire’ action’s code validates the asset, the amount of tokens, and the memo.

The ‘retire’ action uses the authorization method to validate the token issuer. Only the token issuer can retire the token. 

```cpp
require_auth( st.issuer );
```

If all validations pass, the retire action debits the`supply` quantity for the current `statstable` table entry. The `sub_balance` method updates the balance of the issuer account.

### Transfer Action

The `transfer` action transfers tokens from account A to account B. Use this action to execute the transfer of tokens from one account to another in the ‘eosio.token’ sample smart contract.

#### Parameters

Each transfer requires four parameters:
* `from`: the account transferring the tokens
* `to`: the account to receive the tokens
* `quantity`: the number of tokens to be transferred
* `memo`: optional message

#### Implementation Notes

The code block below implements the business logic for the `transfer` action:

```cpp
void token::transfer( const name&    from,
                     const name&    to,
                     const asset&   quantity,
                     const string&  memo )
{
   check( from != to, "cannot transfer to self" );
   require_auth( from );
   check( is_account( to ), "to account does not exist");
   auto sym = quantity.symbol.code();
   stats statstable( get_self(), sym.raw() );
   const auto& st = statstable.get( sym.raw() );

   require_recipient( from );
   require_recipient( to );

   check( quantity.is_valid(), "invalid quantity" );
   check( quantity.amount > 0, "must transfer positive quantity" );
   check( quantity.symbol == st.supply.symbol, "symbol precision mismatch" );
   check( memo.size() <= 256, "memo has more than 256 bytes" );

   auto payer = has_auth( to ) ? to : from;

   sub_balance( from, quantity );
   add_balance( to, quantity, payer );
}
```

The `require_recipient` method is a receipt for the transaction.

```cpp
  require_recipient( from );
   require_recipient( to );
```

The `require_recipient` method ensures the end-user is notified of this transfer. A copy of the ‘transfer’ action is sent to the `require_recipient` account as an input parameter. Therefore, the receiving account can monitor and respond to token transfers, such as to log the transfer or send another token.

When all validations pass at the end of the action, the code updates the balances of the two participants in the transfer using `sub_balance` and `add_balance` methods:


```cpp
   sub_balance( from, quantity );
   add_balance( to, quantity, payer );
```

### Subtract Balance Method

The `sub_balance` method updates the token balance of an account by subtracting a specified amount of tokens from the current account balance.

#### Parameters

The `sub_balance` method requires two parameters:

* `owner`: the account for which the balance is updated
* `value`: the token amount subtracted from the balance

#### Implementation Notes

The code block below shows the `sub_balance` method implementation:

```cpp
void token::sub_balance(const name &owner, const asset &value)
  {
     accounts from_acnts(get_self(), owner.value);

     const auto &from = from_acnts.get(value.symbol.code().raw(), "no balance object found");
     check(from.balance.amount >= value.amount, "overdrawn balance");

     from_acnts.modify(from, owner, [&](auto &a) {
        a.balance -= value;
     });
  }
```

The `sub_balance` method instantiates an `accounts` table and makes it accessible through the `from_acnts` variable. 

**Note**: The `accounts` table instance initializes with the `code` parameter as the contract owner account, `get_self()`, and with the `scope` parameter as the `owner.value` account, for which the `sub_balance` method is called. This table instance is created to hold all the tokens the account owns.

The `sub_balance` method checks whether the sender owns the token they want to send and for a valid balance amount. The balance amount is valid when it is higher or equal to the amount transferred out of the account. The account sending the tokens can not spend more than what they own.

If both pass, the `sub_balance` method updates the sender’s balance with the new value.

### Add Balance Method

The `add_balance` method updates the token balance of an account by adding a specified amount of tokens to the current account balance.

#### Parameters

The `add_balance` method requires two parameters:
* `owner`: the account for which the balance is updated
* `value`: the token amount added to the balance

#### Implementation Notes

The code block below shows the `add_balance` method implementation:

```cpp
void token::add_balance(const name &owner, const asset &value, const name &ram_payer)
  {
     accounts to_acnts(get_self(), owner.value);
     auto to = to_acnts.find(value.symbol.code().raw());
     if (to == to_acnts.end())
     {
        to_acnts.emplace(ram_payer, [&](auto &a) {
           a.balance = value;
        });
     }
     else
     {
        to_acnts.modify(to, same_payer, [&](auto &a) {
           a.balance += value;
        });
     }
  }
```

The `add_balance` method instantiates an `accounts` table and makes it accessible through the `to_acnts` variable. 

**Note: **The `accounts` table instance is initialized with the `code` parameter as the contract owner account, `get_self()`, and with the `scope` parameter as the `owner.value` account for which the `add_balance` method is called. This table instance is created to hold all the tokens the account owns.

The code adds an entry to the `to_acnts` table if the account does not yet own the token. The payer for the RAM is specified with the `ram_payer` parameter. 

If the receiver owns the token, the balance is updated with the received amount and instructs the method to use the `same_payer` as the payer. If the new value to be stored requires more RAM, the extra needed RAM is paid by the same account that originally paid for the table entry. If the new value requires less RAM, a new fee is not incurred. 

### Open Action

The `open` action allows a payer account to register an account as a token holder for a given symbol with the token balance as zero. It allows the action signer to pay for the RAM needed to create a new entry in the table that holds the record of all tokens for a user and set the balance for that token to zero.

#### Parameters

The `open` action requires three parameters:
* `owner`: the account to be registered as the token holder
* `symbol`: the token symbol for which the account is registered
* `ram_payer`: the account that pays for the RAM resource needed for the new account


#### Implementation Notes

The code block below implements the business logic for the `open` action:

```cpp
void token::open(const name &owner, const symbol &symbol, const name &ram_payer)
  {
     require_auth(ram_payer);

     check(is_account(owner), "owner account does not exist");

     auto sym_code_raw = symbol.code().raw();
     stats statstable(get_self(), sym_code_raw);
     const auto &st = statstable.get(sym_code_raw, "symbol does not exist");
     check(st.supply.symbol == symbol, "symbol precision mismatch");

     accounts acnts(get_self(), owner.value);
     auto it = acnts.find(sym_code_raw);
     if (it == acnts.end())
     {
        acnts.emplace(ram_payer, [&](auto &a) {
           a.balance = asset{0, symbol};
        });
     }
  }
```

The `open` action requires a valid authorization of the `ram_payer` and checks if the `owner` is a valid EOSIO account. The code checks for a valid symbol.

If all checks pass, the ‘open’ action creates a new zero balance record in the `acnts` table for the `owner` account. If a record already exists for the `owner`, the action does nothing.

The `open` action complements the `close` action. For more details consult these two github entries:
* [Github issue #61](https://github.com/EOSIO/eosio.contracts/issues/61)
* [Github issue #62](https://github.com/EOSIO/eosio.contracts/issues/62)

### Close Action

The `close` action is the opposite of the `open` action.

#### Parameters

The `close` action requires two parameters:
* `owner`: the account to be unregistered as the token holder
* `symbol`: the token symbol for which the account is unregistered

#### Implementation Notes

The code block below implements the business logic for the `close` action:

```cpp
void token::close(const name &owner, const symbol &symbol)
  {
     require_auth(owner);
     accounts acnts(get_self(), owner.value);
     auto it = acnts.find(symbol.code().raw());
     check(it != acnts.end(), "Balance row already deleted or never existed. Action won't have any effect.");
     check(it->balance.amount == 0, "Cannot close because the balance is not zero.");
     acnts.erase(it);
  }
```

The `close` action is the opposite of the `open` action. It deletes the table entry previously created in the open action. The `close` action requires the authorization of the `owner` account. Only they can delete the data from the `acnts` table. The balance amount must be equal to zero before data is deleted.

The next section of the tutorial shows how to create a new token. It uses the `eosio.token` sample smart contract code as a starting point, it will customize it, add an `airgrab` action and test it.


## Summary

This tutorial demonstrated:
* The main concept revolving around EOSIO coin and tokens
* How the `eosio.token` smart contract code is structured
* How the `eosio.token` smart contract works


## Acknowledgements

_Thank you Dimo (**@ddzhurenov**) for your assistance with this tutorial._

## Next Steps

If you want to learn more, check the [tic-tac-toe game](https://developers.eos.io/welcome/latest/tutorials/tic-tac-toe-game-smart-contract-single-node) smart contract tutorial.
