---
title: "2.6 Adding Inline Actions"
excerpt: ""
---
[block:api-header]
{
  "title": "Introduction"
}
[/block]
It was previously demonstrated by authoring the `addressbook` contract the basics of multi-index tables. In this part of the series you'll learn how to construct actions, and send those actions from within a contract. 
[block:api-header]
{
  "title": "Step 1: Adding eosio.code to permissions"
}
[/block]
In order for the inline actions to be sent from `addressbook`, add the `eosio.code` permission to the contract's account's active permission. Open your terminal and run the following code
[block:code]
{
  "codes": [
    {
      "code": "cleos set account permission addressbook active --add-code",
      "language": "shell"
    }
  ]
}
[/block]
The `eosio.code` authority is a pseudo authority implemented to enhance security, and enable contracts to execute inline actions.
[block:api-header]
{
  "title": "Step 2: Notify Action"
}
[/block]
If not still opened, open the `addressbook.cpp` contract authored in the last tutorial. Write an action that will behave as a "transaction receipt". To do this, create a helper function in the `addressbook` class.
[block:code]
{
  "codes": [
    {
      "code": "[[eosio::action]]\nvoid notify(name user, std::string msg) {}",
      "language": "cplusplus"
    }
  ]
}
[/block]
This function is very simple, it just accepts an `name` and a `string`. 
[block:api-header]
{
  "title": "Step 3: Copy action to sender using require_recipient"
}
[/block]
This transaction needs to be copied to the user so it can be considered as a receipt. To do this, use the [require_recipient](https://eosio.github.io/eosio.cdt/1.5.0/group__action.html#function-requirerecipient) method.  Calling `require_recipient` adds an account to the require_recipient set and ensures that these accounts receive a notification of the action being executed. The notification is like sending a "carbon copy" of the action to the accounts in the require_recipient set.
[block:code]
{
  "codes": [
    {
      "code": "  [[eosio::action]]\n  void notify(name user, std::string msg) {\n   require_recipient(user);\n  }",
      "language": "cplusplus"
    }
  ]
}
[/block]
This action is very simple, it will copy the given action to the provided user. However, as written, any user could call this function, and "fake" a receipt from this contract. This could be use in malicious ways, and should be seen as a vulnerability. To correct this, require that the authorities provided in the call to this action is from the contract, for this, use [get_self](https://developers.eos.io/eosio-cpp/v1.3.0/reference#get_self)
[block:code]
{
  "codes": [
    {
      "code": "  [[eosio::action]]\n  void notify(name user, std::string msg) {\n    require_auth(get_self());\n    require_recipient(user);\n  }",
      "language": "cplusplus"
    }
  ]
}
[/block]
Now if user `bob` calls this function directly, but passes the parameter `alice` the action will throw an exception.
[block:api-header]
{
  "title": "Step 4: Notify helper for sending inline transactions"
}
[/block]
Since this inline action will be called several times, write a quick helper for maximum code reuse. In the private region of your contract, define a new method.
[block:code]
{
  "codes": [
    {
      "code": "...\n  private:\n    void send_summary(name user, std::string message){}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Inside of this helper construct an action and send it.
[block:api-header]
{
  "title": "Step 5: The Action Constructor"
}
[/block]
Modify the `addressbook`  contract to send a receipt to the user every time they have taken an action on the contract.

To begin, address the "create record" case. This is the case that fires when a record is not found in the table, when `iterator == addresses.end()` is `true`

Save this object to an `action` variable called `notification`
[block:code]
{
  "codes": [
    {
      "code": "...\n  private: \n    void send_summary(name user, std::string message){\n      action(\n        //permission_level,\n        //code,\n        //action,\n        //data\n      );   \n    }\n\n",
      "language": "cplusplus"
    }
  ]
}
[/block]
The action constructor requires a number of parameters.
- A [permission_level](https://eosio.github.io/eosio.cdt/structeosio_1_1permission__level.html) struct
- The contract to call (initialised using `eosio::name` type)
- The action (initialised using `eosio::name` type)
- The data to pass to the action, a tuple of positionals that correlate to the actions being called.

## The Permission struct
In this contract the permission should be authorized by the `active` authority of the contract using `get_self()`. As a reminder, to use the 'active` authority inline you will need your contract's to give active authority to `eosio.code` pseudo-authority (instructions above)
[block:code]
{
  "codes": [
    {
      "code": "...\n  private: \n    void send_summary(name user, std::string message){\n      action(\n        permission_level{get_self(),\"active\"_n},\n      );\n    }",
      "language": "cplusplus"
    }
  ]
}
[/block]
## The "code" AKA "account where contract is deployed"
Since the action called is in this contract, use  [get_self](https://eosio.github.io/eosio.cdt/classeosio_1_1contract.html#function-getself). `"addressbook"_n` would also work here, but if this contract were deployed under a different account name, it wouldn't work. Because of this, `get_self()` is the superior option.
[block:code]
{
  "codes": [
    {
      "code": "...\n  private: \n    void send_summary(name user, std::string message){\n      action(\n        permission_level{get_self(),\"active\"_n},\n        get_self(),\n        //action\n        //data\n      );\n    }",
      "language": "cplusplus"
    }
  ]
}
[/block]
## The action
The `notify` action was previously defined to be called from this inline action. Use the _n operator here.
[block:code]
{
  "codes": [
    {
      "code": "...\n  private: \n    void send_summary(name user, std::string message){\n      action(\n        permission_level{get_self(),\"active\"_n},\n        get_self(),\n        \"notify\"_n,\n        //data\n      );\n    }",
      "language": "cplusplus"
    }
  ]
}
[/block]
## The Data
Finally, define the data to pass to this action. The notify function accepts two parameters, an `name` and a `string`. The action constructor expects data as type `bytes`, so use `make_tuple`, a function available through `std` C++ library.  Data passed in the tuple is positional, and determined by the order of the parameters accepted by the action that being called. 

- Pass the `user` variable that is provided as a parameter of the `upsert()` action. 
- Concatenate a string that includes the name of the user, and include the `message` to pass to the `notify` action. 
[block:code]
{
  "codes": [
    {
      "code": "...\n  private: \n    void send_summary(name user, std::string message){\n      action(\n        permission_level{get_self(),\"active\"_n},\n        get_self(),\n        \"notify\"_n,\n        std::make_tuple(user, name{user}.to_string() + message)\n      );\n    }",
      "language": "cplusplus"
    }
  ]
}
[/block]
## Send the action.
Finally, send the action using the `send` method of the action struct. 
[block:code]
{
  "codes": [
    {
      "code": "...\n  private: \n    void send_summary(name user, std::string message){\n      action(\n        permission_level{get_self(),\"active\"_n},\n        get_self(),\n        \"notify\"_n,\n        std::make_tuple(user, name{user}.to_string() + message)\n      ).send();\n    }",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 6: Call the helper and inject relevant messages."
}
[/block]
Now that the helper is defined, it should probably be called from the relevant locations. There's three specific places for the new `notify` helper to be called from:
- After the contract `emplaces` a new record: `send_summary(user, "successfully emplaced record to addressbook");`
- After the contract `modifies` an existing record: `send_summary(user, "successfully modified record in addressbook.");` 
- After the contract `erases` an existing record: `send_summary(user, "successfully erased record from addressbook");`
[block:api-header]
{
  "title": "Step 7: Updating the EOSIO_DISPATCH macro"
}
[/block]
The new action `notify` has been added to the contract, so update the `EOSIO_DISPATCH` macro at the bottom of the file to include the new `notify` action. This ensures that the `notify` action is not scrubbed by `eosio.cdt`'s optimizer.
[block:code]
{
  "codes": [
    {
      "code": "  EOSIO_DISPATCH( addressbook, (upsert)(erase)(notify) )",
      "language": "cplusplus"
    }
  ]
}
[/block]
Now that everything is in place, here's the current state of the `addressbook` contract:
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass [[eosio::contract]] addressbook : public eosio::contract {\n\npublic:\n  using contract::contract;\n  \n  addressbook(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}\n\n  [[eosio::action]]\n  void upsert(name user, std::string first_name, std::string last_name, uint64_t age, std::string street, std::string city, std::string state) {\n    require_auth(user);\n    address_index addresses(_code, _code.value);\n    auto iterator = addresses.find(user.value);\n    if( iterator == addresses.end() )\n    {\n      addresses.emplace(user, [&]( auto& row ) {\n       row.key = user;\n       row.first_name = first_name;\n       row.last_name = last_name;\n       row.age = age;\n       row.street = street;\n       row.city = city;\n       row.state = state;\n      });\n      send_summary(user, \" successfully emplaced record to addressbook\");\n    }\n    else {\n      std::string changes;\n      addresses.modify(iterator, user, [&]( auto& row ) {\n        row.key = user;\n        row.first_name = first_name;\n        row.last_name = last_name;\n        row.street = street;\n        row.city = city;\n        row.state = state;\n      });\n      send_summary(user, \" successfully modified record to addressbook\");\n    }\n  }\n\n\n\n  [[eosio::action]]\n  void erase(name user) {\n    require_auth(user);\n\n    address_index addresses(_self, _code.value);\n\n    auto iterator = addresses.find(user.value);\n    eosio_assert(iterator != addresses.end(), \"Record does not exist\");\n    addresses.erase(iterator);\n    send_summary(user, \" successfully erased record from addressbook\");\n  }\n\n  [[eosio::action]]\n  void notify(name user, std::string msg) {\n    require_auth(get_self());\n    require_recipient(user);\n  }\n\nprivate:\n  struct [[eosio::table]] person {\n    name key;\n    std::string first_name;\n    std::string last_name;\n    uint64_t age;\n    std::string street;\n    std::string city;\n    std::string state;\n  \n    uint64_t primary_key() const { return key.value; }\n    uint64_t get_secondary_1() const { return age;}\n  \n  };\n\n  void send_summary(name user, std::string message) {\n    action(\n      permission_level{get_self(),\"active\"_n},\n      get_self(),\n      \"notify\"_n,\n      std::make_tuple(user, name{user}.to_string() + message)\n    ).send();\n  };\n\n\n  typedef eosio::multi_index<\"people\"_n, person, \n    indexed_by<\"byage\"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>\n  > address_index;\n  \n};\n\nEOSIO_DISPATCH( addressbook, (upsert)(notify)(erase))",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 8: Recompile and Regenerate the ABI File"
}
[/block]
Open your terminal, and navigate to `CONTRACTS_DIR/addressbook` 
[block:code]
{
  "codes": [
    {
      "code": "cd CONTRACTS_DIR/addressbook",
      "language": "shell"
    }
  ]
}
[/block]
Now, recompile the contract, including the `--abigen` flag since changes have bene made to the contract that affects the ABI. If you've followed the instructions carefully, you shouldn't see any errors.
[block:code]
{
  "codes": [
    {
      "code": "eosio-cpp -o addressbook.wasm addressbook.cpp --abigen",
      "language": "shell"
    }
  ]
}
[/block]
Smart contracts on EOSIO are upgradeable so the contract can be redeployed with changes.
[block:code]
{
  "codes": [
    {
      "code": "cleos set contract addressbook CONTRACTS_DIR/addressbook",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "Publishing contract...\nexecuted transaction: 1898d22d994c97824228b24a1741ca3bd5c7bc2eba9fea8e83446d78bfb264fd  7320 bytes  747 us\n#         eosio <= eosio::setcode               {\"account\":\"addressbook\",\"vmtype\":0,\"vmversion\":0,\"code\":\"0061736d0100000001a6011a60027f7e0060077f7e...\n#         eosio <= eosio::setabi                {\"account\":\"addressbook\",\"abi\":\"0e656f73696f3a3a6162692f312e30010c6163636f756e745f6e616d65046e616d65...",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Success!
[block:api-header]
{
  "title": "Step 9: Testing it"
}
[/block]
Now that the contract has been modified and deployed, test it. In the previous tutorial,  alice's addressbook record was deleted during the testing steps, so calling `upsert` will fire the inline action just written inside of the "create" case.

Run the following command in your terminal
[block:code]
{
  "codes": [
    {
      "code": "cleos push action addressbook upsert '[\"alice\", \"alice\", \"liddell\", 21, \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p alice@active",
      "language": "shell"
    }
  ]
}
[/block]
`cleos` will return some data, that includes all the actions executed in the transaction
[block:code]
{
  "codes": [
    {
      "code": "executed transaction: e9e30524186bb6501cf490ceb744fe50654eb393ce0dd733f3bb6c68ff4b5622  160 bytes  9810 us\n#   addressbook <= addressbook::upsert          {\"user\":\"alice\",\"first_name\":\"alice\",\"last_name\":\"liddell\",\"age\":21,\"street\":\"123 drink me way\",\"cit...\n#   addressbook <= addressbook::notify          {\"user\":\"alice\",\"msg\":\"alicesuccessfully emplaced record to addressbook\"}\n#         alice <= addressbook::notify          {\"user\":\"alice\",\"msg\":\"alicesuccessfully emplaced record to addressbook\"}",
      "language": "shell"
    }
  ]
}
[/block]
At the bottom you'll notice that `addressbook::notify` copied `alice` with some information about this transaction. Use [cleos get actions](https://developers.eos.io/eosio-cleos/reference#cleos-get-transactions) to show us actions executed and relevant to alice.
[block:code]
{
  "codes": [
    {
      "code": "cleos get actions alice",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "#  seq  when                              contract::action => receiver      trx id...   args\n================================================================================================================\n#   62   2018-09-15T12:57:09.000       addressbook::notify => alice         685ecc09... {\"user\":\"alice\",\"msg\":\"alice successfully added record to ad...",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]