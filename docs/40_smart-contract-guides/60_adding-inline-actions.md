---
content_title: "Adding Inline Actions"
link_text: "Adding Inline Actions"
---
This tutorial shows how to call inline actions from a smart contract.

## Introduction
It was previously demonstrated by authoring the `addressbook` contract the basics of multi-index tables. In this part of the series you'll learn how to construct actions, and send those actions from within a contract.

## Step 1: Adding eosio.code to permissions

In order for the inline actions to be sent from `addressbook`, add the `eosio.code` permission to the contract's account's active permission. Open your terminal and run the following code
```shell
cleos set account permission addressbook active --add-code
```
The `eosio.code` authority is a pseudo authority implemented to enhance security, and enable contracts to execute inline actions.

## Step 2: Notify Action

If not still opened, open the `addressbook.cpp` contract authored in the last tutorial. Write an action that dispatches a "transaction receipt" whenever a transaction occurs. To do this, create a helper function in the `addressbook` class.
```cpp
[[eosio::action]]
void notify(name user, std::string msg) {}
```
This function is very simple, it just accepts a user account as a `name` type and a message as a `string` type. The user parameter dictates which user gets the message that is sent.

## Step 3: Copy action to sender using require_recipient

This transaction needs to be copied to the user so it can be considered as a receipt. To do this, use the [require_recipient](https://developers.eos.io/manuals/eosio.cdt/latest/group__action/#function-require_recipient) method.  Calling `require_recipient` adds an account to the require_recipient set and ensures that these accounts receive a notification of the action being executed. The notification is like sending a "carbon copy" of the action to the accounts in the require_recipient set.
```cpp
  [[eosio::action]]
  void notify(name user, std::string msg) {
   require_recipient(user);
  }
```
This action is very simple, however, as written, any user could call this function, and "fake" a receipt from this contract. This could be used in malicious ways, and should be seen as a vulnerability. To correct this, require that the authorization provided in the call to this action is from the contract itself, for this, use [get_self](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1contract#function-get_self)
```cpp
  [[eosio::action]]
  void notify(name user, std::string msg) {
    require_auth(get_self());
    require_recipient(user);
  }
```
Now if user `bob` calls this function directly, but passes the parameter `alice` the action will throw an exception.

## Step 4: Notify helper for sending inline transactions

Since this inline action will be called several times, write a quick helper for maximum code reuse. In the private region of your contract, define a new method.
```cpp
...
  private:
    void send_summary(name user, std::string message){}
```
Inside of this helper construct an action and send it.

## Step 5: The Action Constructor

Modify the `addressbook`  contract to send a receipt to the user every time they take an action on the contract.

To begin, address the "create record" case. This is the case that fires when a record is not found in the table, i.e., when `iterator == addresses.end()` is `true`.

Save this object to an `action` variable called `notification`
```cpp
...
  private:
    void send_summary(name user, std::string message){
      action(
        //permission_level,
        //code,
        //action,
        //data
      );   
    }


```
The action constructor requires a number of parameters.
- A [permission_level](https://developers.eos.io/manuals/eosio.cdt/latest/structeosio_1_1permission__level) struct
- The contract to call (initialised using `eosio::name` type)
- The action (initialised using `eosio::name` type)
- The data to pass to the action, a tuple of positionals that correlate to the actions being called.

## The Permission struct

In this contract the permission should be authorized by the `active` authority of the contract using `get_self()`. As a reminder, to use the 'active` authority inline you will need your contract's to give active authority to `eosio.code` pseudo-authority (instructions above)
```cpp
...
  private:
    void send_summary(name user, std::string message){
      action(
        permission_level{get_self(),"active"_n},
        //code,
        //action,
        //data
      );
    }
```

## The "code" AKA "account where contract is deployed"

Since the action called is in this contract, use  [get_self](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1contract/#function-get_self). `"addressbook"_n` would also work here, but if this contract were deployed under a different account name, it wouldn't work. Because of this, `get_self()` is the superior option.
```cpp
...
  private:
    void send_summary(name user, std::string message){
      action(
        permission_level{get_self(),"active"_n},
        get_self(),
        //action
        //data
      );
    }
```

## The action

The `notify` action was previously defined to be called from this inline action. Use the _n operator here.
```cpp
...
  private:
    void send_summary(name user, std::string message){
      action(
        permission_level{get_self(),"active"_n},
        get_self(),
        "notify"_n,
        //data
      );
    }
```

## The Data

Finally, define the data to pass to this action. The notify function accepts two parameters, an `name` and a `string`. The action constructor expects data as type `bytes`, so use `make_tuple`, a function available through `std` C++ library.  Data passed in the tuple is positional, and determined by the order of the parameters accepted by the action that being called.

- Pass the `user` variable that is provided as a parameter of the `upsert()` action.
- Concatenate a string that includes the name of the user, and include the `message` to pass to the `notify` action.
```cpp
...
  private:
    void send_summary(name user, std::string message){
      action(
        permission_level{get_self(),"active"_n},
        get_self(),
        "notify"_n,
        std::make_tuple(user, name{user}.to_string() + message)
      );
    }
```

## Send the action.

Finally, send the action using the `send` method of the action struct.
```cpp
...
  private:
    void send_summary(name user, std::string message) {
      action(
        permission_level{get_self(),"active"_n},
        get_self(),
        "notify"_n,
        std::make_tuple(user, name{user}.to_string() + message)
      ).send();
    }
```

## Step 6: Call the helper and inject relevant messages.
Now that the helper is defined, it should probably be called from the relevant locations. There's three specific places for the new `notify` helper to be called from:
- After the contract `emplaces` a new record: `send_summary(user, "successfully emplaced record to addressbook");`
- After the contract `modifies` an existing record: `send_summary(user, "successfully modified record in addressbook.");`
- After the contract `erases` an existing record: `send_summary(user, "successfully erased record from addressbook");`

## Step 7: Recompile and Regenerate the ABI File

Now that everything is in place, here's the current state of the `addressbook` contract:
```cpp
#include <eosio/eosio.hpp>
#include <eosio/print.hpp>

using namespace eosio;

class [[eosio::contract("addressbook")]] addressbook : public eosio::contract {

public:

  addressbook(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}

  [[eosio::action]]
  void upsert(name user, std::string first_name, std::string last_name, uint64_t age, std::string street, std::string city, std::string state) {
    require_auth(user);
    address_index addresses(get_first_receiver(), get_first_receiver().value);
    auto iterator = addresses.find(user.value);
    if( iterator == addresses.end() )
    {
      addresses.emplace(user, [&]( auto& row ) {
       row.key = user;
       row.first_name = first_name;
       row.last_name = last_name;
       row.age = age;
       row.street = street;
       row.city = city;
       row.state = state;
      });
      send_summary(user, " successfully emplaced record to addressbook");
    }
    else {
      addresses.modify(iterator, user, [&]( auto& row ) {
        row.key = user;
        row.first_name = first_name;
        row.last_name = last_name;
        row.street = street;
        row.city = city;
        row.state = state;
      });
      send_summary(user, " successfully modified record to addressbook");
    }
  }

  [[eosio::action]]
  void erase(name user) {
    require_auth(user);

    address_index addresses(get_first_receiver(), get_first_receiver().value);

    auto iterator = addresses.find(user.value);
    check(iterator != addresses.end(), "Record does not exist");
    addresses.erase(iterator);
    send_summary(user, " successfully erased record from addressbook");
  }

  [[eosio::action]]
  void notify(name user, std::string msg) {
    require_auth(get_self());
    require_recipient(user);
  }

private:
  struct [[eosio::table]] person {
    name key;
    std::string first_name;
    std::string last_name;
    uint64_t age;
    std::string street;
    std::string city;
    std::string state;

    uint64_t primary_key() const { return key.value; }
    uint64_t get_secondary_1() const { return age;}
  };

  void send_summary(name user, std::string message) {
    action(
      permission_level{get_self(),"active"_n},
      get_self(),
      "notify"_n,
      std::make_tuple(user, name{user}.to_string() + message)
    ).send();
  };

  typedef eosio::multi_index<"people"_n, person,
    indexed_by<"byage"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>
  > address_index;
};
```
Open your terminal, and navigate to `CONTRACTS_DIR/addressbook`
```shell
cd CONTRACTS_DIR/addressbook
```
Now, recompile the contract, including the `--abigen` flag since changes have been made to the contract that affects the ABI. If you've followed the instructions carefully, you shouldn't see any errors.
```shell
eosio-cpp -o addressbook.wasm addressbook.cpp --abigen
```
Smart contracts on EOSIO are upgradeable so the contract can be redeployed with changes.
```shell
cleos set contract addressbook CONTRACTS_DIR/addressbook
```

```shell
Publishing contract...
executed transaction: 1898d22d994c97824228b24a1741ca3bd5c7bc2eba9fea8e83446d78bfb264fd  7320 bytes  747 us
#         eosio <= eosio::setcode               {"account":"addressbook","vmtype":0,"vmversion":0,"code":"0061736d0100000001a6011a60027f7e0060077f7e...
#         eosio <= eosio::setabi                {"account":"addressbook","abi":"0e656f73696f3a3a6162692f312e30010c6163636f756e745f6e616d65046e616d65...
```
Success!

## Step 8: Testing it

Now that the contract has been modified and deployed, test it. In the previous tutorial, alice's addressbook record was deleted during the testing steps, so calling `upsert` will fire the inline action just written inside of the "create" case.

Run the following command in your terminal
```shell
cleos push action addressbook upsert '["alice", "alice", "liddell", 21, "123 drink me way", "wonderland", "amsterdam"]' -p alice@active
```
`cleos` will return some data, that includes all the actions executed in the transaction
```shell
executed transaction: e9e30524186bb6501cf490ceb744fe50654eb393ce0dd733f3bb6c68ff4b5622  160 bytes  9810 us
#   addressbook <= addressbook::upsert          {"user":"alice","first_name":"alice","last_name":"liddell","age":21,"street":"123 drink me way","cit...
#   addressbook <= addressbook::notify          {"user":"alice","msg":"alicesuccessfully emplaced record to addressbook"}
#         alice <= addressbook::notify          {"user":"alice","msg":"alicesuccessfully emplaced record to addressbook"}
```
The last entry in the previous log is an `addressbook::notify` action sent to `alice`. Use [cleos get actions](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/get/actions) to display actions executed and relevant to alice.
```shell
cleos get actions alice
```

```shell
#  seq  when                              contract::action => receiver      trx id...   args
================================================================================================================
#   62   2018-09-15T12:57:09.000       addressbook::notify => alice         685ecc09... {"user":"alice","msg":"alice successfully added record to ad...
```

## What's Next

- [Inline Actions to External Contracts](./70_inline-action-to-external-contract.md): Learn how to construct actions and send those actions to an external contract.
