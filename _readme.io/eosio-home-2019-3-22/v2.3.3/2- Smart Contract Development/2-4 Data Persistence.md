---
title: "2.4 Data Persistence"
excerpt: ""
---
To learn about data persistence, write a simple smart contract that functions as an address book. While this use case isn't very practical as a production smart contract for various reasons, it's a good contract to start with to learn how data persistence works on EOSIO without being distracted by business logic that does not pertain to eosio's `multi_index` functionality. 
[block:api-header]
{
  "title": "Step 1: Create a new directory"
}
[/block]
Earlier, you created a contract directory, navigate there now.
[block:code]
{
  "codes": [
    {
      "code": "cd CONTRACTS_DIR",
      "language": "shell"
    }
  ]
}
[/block]
Create a new directory for our contract and enter the directory
[block:code]
{
  "codes": [
    {
      "code": "mkdir addressbook\ncd addressbook",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 2: Create and open a new file"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "touch addressbook.cpp",
      "language": "cplusplus"
    }
  ]
}
[/block]
open the file in your favorite editor.
[block:api-header]
{
  "title": "Step 3: Write an Extended Standard Class and Include EOSIO"
}
[/block]
In a previous tutorial, you created a hello world contract and you learned the basics. You will be familiar with the structure below, the class has been named `addressbook`  respectively.
[block:code]
{
  "codes": [
    {
      "code": "#include <eosio/eosio.hpp>\n\nusing namespace eosio;\n\nclass [[eosio::contract(\"addressbook\")]] addressbook : public eosio::contract {\n  public:\n       \n  private: \n  \n};",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 4: Create The Data Structure for the Table"
}
[/block]
Before a table can be configured and instantiated, a struct that represents the data structure of the address book needs to be written. Since it's an address book, the table will contain people, so create a `struct` called "person"
[block:code]
{
  "codes": [
    {
      "code": "struct person {};",
      "language": "cplusplus"
    }
  ]
}
[/block]
When defining the structure of a multi_index table, you will require a unique value to use as the primary key. 

For this contract, use a field called "key" with type `name`. This contract will have one unique entry per user, so this key will be a consistent and guaranteed unique value based on the user's `name` 
[block:code]
{
  "codes": [
    {
      "code": "struct person {\n\tname key; \n};",
      "language": "cplusplus"
    }
  ]
}
[/block]
Since this contract is an address book it probably should store some relevant details for each entry or *person* 
[block:code]
{
  "codes": [
    {
      "code": "struct person {\n name key;\n std::string first_name;\n std::string last_name;\n std::string street;\n std::string city;\n std::string state;\n};",
      "language": "cplusplus"
    }
  ]
}
[/block]
Great. The basic data structure is now complete.

Next, define a `primary_key` method. Every multi_index struct requires a *primary key* to be set. Behind the scenes, this method is used according to the index specification of your multi_index instantiation. EOSIO wraps [boost::multi_index](https://www.boost.org/doc/libs/1_59_0/libs/multi_index/doc/index.html)

Create an method `primary_key()` and return a struct member, in this case, the `key` member as previously discussed. 
[block:code]
{
  "codes": [
    {
      "code": "struct person {\n name key;\n std::string first_name;\n std::string last_name;\n std::string street;\n std::string city;\n std::string state;\n \n uint64_t primary_key() const { return key.value;}\n};",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "A table's data structure cannot be modified while it has data in it. If you need to make changes to a table's data structure in any way, you first need to remove all its rows"
}
[/block]

[block:api-header]
{
  "title": "Step 5: Configure the Multi-Index Table"
}
[/block]
Now that the data structure of the table has been defined with a `struct` we need to configure the table. The [eosio::multi_index](https://eosio.github.io/eosio.cdt/classeosio_1_1multi__index.html) constructor needs to be named and configured to use the struct we previously defined.
[block:code]
{
  "codes": [
    {
      "code": "typedef eosio::multi_index<\"people\"_n, person> address_index;",
      "language": "cplusplus"
    }
  ]
}
[/block]
With the above `multi_index` configuration there is a table named **people**, that 

1. Uses the _n operator to define an eosio::name type and uses that to name the table. This table contains a number of different singular "persons", so name the table "people".
2. Pass in the singular `person` struct defined in the previous step.
3. Declare this table's type. This type will be used to instantiate this table later. 
4. There are some additional configurations, such as configuring indices, that will be covered further on.

So far, our file should look like this. 
[block:code]
{
  "codes": [
    {
      "code": "#include <eosio/eosio.hpp>\n\nusing namespace eosio;\n\nclass [[eosio::contract(\"addressbook\")]] addressbook : public eosio::contract {\n\n  public:\n\n  private:\n    struct [[eosio::table]] person {\n      name key;\n      std::string first_name;\n      std::string last_name;\n      std::string street;\n      std::string city;\n      std::string state;\n\n      uint64_t primary_key() const { return key.value;}\n    };\n  \n    typedef eosio::multi_index<\"people\"_n, person> address_index;\n};\n",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 6: The Constructor"
}
[/block]
When working with C++ classes, the first public method you should create is a constructor. 

Our constructor will be responsible for initially setting up the contract. 

EOSIO contracts extend the *contract* class. Initialize our parent *contract* class with the code name of the contract and the receiver. The important parameter here is the `code` parameter which is the account on the blockchain that the contract is being deployed to. 
[block:code]
{
  "codes": [
    {
      "code": "addressbook(name receiver, name code,  datastream<const char*> ds):contract(receiver, code, ds) {}",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 7: Adding a record to the table"
}
[/block]
Previously, the primary key of the multi-index table was defined to enforce that this contract will only store one record per user. To make it all work, some assumptions about the design need to be established. 

1. The only account authorized to modify the address book is the user. 
2. the **primary_key** of our table is unique, based on username
3. For usability, the contract should have the ability to both create and modify a table row with a single action.

In eosio a chain has unique accounts, so `name` is an ideal candidate as a **primary_key** in this specific use case. The [name](https://eosio.github.io/eosio.cdt/name_8hpp.html) type is a `uint64_t`. 

Next, define an action for the user to add or update a record. This action will need to accept any values that this action needs to be able to emplace (create) or modify. 

For user-experience and interface simplicity, have a single method be responsible for both creation and modification of rows. Because of this behavior, name it "upsert," a combination of "update" and "insert." 
[block:code]
{
  "codes": [
    {
      "code": "void upsert(\n  name user, \n  std::string first_name, \n  std::string last_name, \n  std::string street, \n  std::string city, \n  std::string state\n) {}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Earlier, it was mentioned that only the user has control over their own record, as this contract is opt-in. To do this, utilize the [require_auth](https://eosio.github.io/eosio.cdt/group__action.html#function-requireauth) method provided by the `eosio.cdt`. This method accepts an `name` type argument and asserts that the account executing the transaction equals the provided value. 
[block:code]
{
  "codes": [
    {
      "code": "void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {\n  require_auth( user );\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Previously, a multi_index table was configured, and declared as `address_index`. To instantiate a table, two required parameters are required: 

1. The "code", which represents the contract's account. Here we use the `get_self()` function which will pass the name of this contract.

2. The "scope" which can ensure the uniqueness of the table within this contract. In this case, since we only have one table we can use the value from `get_first_receiver()`. *`get_first_receiver` is the account name this contract is deployed to.* 
[block:code]
{
  "codes": [
    {
      "code": "void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {\n  require_auth( user );\n  address_index addresses(get_self(), get_first_receiver().value);\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Next, query the iterator, setting it to a variable since this iterator will be used several times
[block:code]
{
  "codes": [
    {
      "code": "void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {\n  require_auth( user );\n  address_index addresses(get_self(), get_first_receiver().value);\n  auto iterator = addresses.find(user.value);\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Security has been established and the table instantiated, great! 

Next up, write the logic for creating or modifying the table.  Detect whether or not the particular user already exists. 

To do this, use table's [find](https://eosio.github.io/eosio.cdt/classeosio_1_1multi__index.html#function-find) method by passing the `user` parameter. The find method will return an iterator. Use that iterator to test it against the [end](https://eosio.github.io/eosio.cdt/classeosio_1_1multi__index.html#function-end) method. The "end" method is an alias for "null". 
[block:code]
{
  "codes": [
    {
      "code": "void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {\n  require_auth( user );\n  address_index addresses(get_self(), get_first_receiver().value);\n  auto iterator = addresses.find(user.value);\n  if( iterator == addresses.end() )\n  {\n    //The user isn't in the table\n  }\n  else {\n    //The user is in the table\n  }\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Create a record in the table using the multi_index method [emplace](https://eosio.github.io/eosio.cdt/classeosio_1_1multi__index.html#function-emplace). This method accepts two arguments, the "payer" of this record who pays the storage usage and a callback function. 

The callback function for the emplace method must use a lamba to create a reference. Inside the body assign the row's values with the ones provided to `upsert`.
[block:code]
{
  "codes": [
    {
      "code": "void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {\n  require_auth( user );\n  address_index addresses(get_self(), get_first_receiver().value);\n  auto iterator = addresses.find(user.value);\n  if( iterator == addresses.end() )\n  {\n    addresses.emplace(user, [&]( auto& row ) {\n      row.key = user;\n      row.first_name = first_name;\n      row.last_name = last_name;\n      row.street = street;\n      row.city = city;\n      row.state = state;\n    });\n  }\n  else {\n    //The user is in the table\n  }\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Next, handle the modification, or update, case of the "upsert" function. Use the [modify](https://eosio.github.io/eosio.cdt/classeosio_1_1multi__index.html#function-modify-12) method, passing a few arguments:
- The iterator defined earlier, presently set to the user as declared when calling this action. 
- The "scope" or "ram payer", which in this case is the user, as previously decided when proposing the design for this contract. 
- The callback function to handle the modification of the table. 
[block:code]
{
  "codes": [
    {
      "code": "void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {\n  require_auth( user );\n  address_index addresses(get_self(), get_first_receiver().value);\n  auto iterator = addresses.find(user.value);\n  if( iterator == addresses.end() )\n  {\n    addresses.emplace(user, [&]( auto& row ) {\n      row.key = user;\n      row.first_name = first_name;\n      row.last_name = last_name;\n      row.street = street;\n      row.city = city;\n      row.state = state;\n    });\n  }\n  else {\n    std::string changes;\n    addresses.modify(iterator, user, [&]( auto& row ) {\n      row.key = user;\n      row.first_name = first_name;\n      row.last_name = last_name;\n      row.street = street;\n      row.city = city;\n      row.state = state;\n    });\n  }\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
The `addressbook` contract now has a functional action that will enable a user to create a row in the table if that record does not yet exist, and modify it if it already exists.

But what if the user wants to remove the record entirely? 
[block:api-header]
{
  "title": "Step 8: Remove record from the table"
}
[/block]
Similar to the previous steps, create a public method in the `addressbook`, making sure to include the ABI declarations and a [require_auth](https://eosio.github.io/eosio.cdt/group__action.html#function-requireauth) that tests against the action's argument `user` to verify only the owner of a record can modify their account. 
[block:code]
{
  "codes": [
    {
      "code": "    void erase(name user){\n      require_auth(user);\n    }\n",
      "language": "cplusplus"
    }
  ]
}
[/block]
Instantiate the table. In `addressbook` each account has only one record. Set `iterator` with [find](https://eosio.github.io/eosio.cdt/classeosio_1_1multi__index.html#function-find) 
[block:code]
{
  "codes": [
    {
      "code": "...\n    void erase(name user){\n      require_auth(user);\n      address_index addresses(get_self(), get_first_receiver().value);\n      auto iterator = addresses.find(user.value);\n    }\n...",
      "language": "cplusplus"
    }
  ]
}
[/block]
A contract *cannot* erase a record that doesn't exist, so check that the record indeed exists before proceeding.
[block:code]
{
  "codes": [
    {
      "code": "...\n    void erase(name user){\n      require_auth(user);\n      address_index addresses(get_self(), get_first_receiver().value);\n      auto iterator = addresses.find(user.value);\n      check(iterator != addresses.end(), \"Record does not exist\");\n    }\n...",
      "language": "cplusplus"
    }
  ]
}
[/block]
Finally, call the [erase](https://eosio.github.io/eosio.cdt/classeosio_1_1multi__index.html#function-erase-12) method, to erase the iterator.
[block:code]
{
  "codes": [
    {
      "code": "...\n  void erase(name user) {\n    require_auth(user);\n    address_index addresses(get_self(), get_first_receiver().value);\n    auto iterator = addresses.find(user.value);\n    check(iterator != addresses.end(), \"Record does not exist\");\n    addresses.erase(iterator);\n  }\n...",
      "language": "cplusplus"
    }
  ]
}
[/block]
The contract is now mostly complete. Users can create, modify and erase records. However, the contract is not quite ready to be compiled.
[block:api-header]
{
  "title": "Step 9: Preparing for the ABI"
}
[/block]
## 9.1 ABI Action Declarations
[eosio.cdt]() includes an ABI Generator, but for it to work will require some declarations

Above both the `upsert` and `erase` functions add the following C++11 declaration:
[block:code]
{
  "codes": [
    {
      "code": "[[eosio::action]]",
      "language": "cplusplus"
    }
  ]
}
[/block]
The above declaration will extract the arguments of the action and create necessary ABI *struct* descriptions in the generated ABI file. 

## 9.2 ABI Table Declarations
Add an ABI declaration to the table. Modify the following line defined in the private region of your contract:
[block:code]
{
  "codes": [
    {
      "code": "struct person {",
      "language": "cplusplus"
    }
  ]
}
[/block]
To this:
[block:code]
{
  "codes": [
    {
      "code": "struct [[eosio::table]] person {",
      "language": "cplusplus"
    }
  ]
}
[/block]
The `[[eosio.table]]` declaration will add the necessary descriptions to the ABI file. 

Now our contract is ready to be compiled.

Below is the final state of our `addressbook` contract:
[block:code]
{
  "codes": [
    {
      "code": "#include <eosio/eosio.hpp>\n\nusing namespace eosio;\n\nclass [[eosio::contract(\"addressbook\")]] addressbook : public eosio::contract {\n\npublic:\n  using contract::contract;\n  \n  addressbook(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}\n\n  [[eosio::action]]\n  void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {\n    require_auth( user );\n    address_index addresses( get_self(), get_first_receiver().value );\n    auto iterator = addresses.find(user.value);\n    if( iterator == addresses.end() )\n    {\n      addresses.emplace(user, [&]( auto& row ) {\n       row.key = user;\n       row.first_name = first_name;\n       row.last_name = last_name;\n       row.street = street;\n       row.city = city;\n       row.state = state;\n      });\n    }\n    else {\n      std::string changes;\n      addresses.modify(iterator, user, [&]( auto& row ) {\n        row.key = user;\n        row.first_name = first_name;\n        row.last_name = last_name;\n        row.street = street;\n        row.city = city;\n        row.state = state;\n      });\n    }\n  }\n\n  [[eosio::action]]\n  void erase(name user) {\n    require_auth(user);\n\n    address_index addresses( get_self(), get_first_receiver().value);\n\n    auto iterator = addresses.find(user.value);\n    check(iterator != addresses.end(), \"Record does not exist\");\n    addresses.erase(iterator);\n  }\n\nprivate:\n  struct [[eosio::table]] person {\n    name key;\n    std::string first_name;\n    std::string last_name;\n    std::string street;\n    std::string city;\n    std::string state;\n    uint64_t primary_key() const { return key.value; }\n  };\n  typedef eosio::multi_index<\"people\"_n, person> address_index;\n\n};    ",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 10: Compile the Contract"
}
[/block]
Execute the following command from your terminal.
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

[block:api-header]
{
  "title": "Step 11: Deploy the Contract"
}
[/block]
Create an account for the contract, execute the following shell command
[block:code]
{
  "codes": [
    {
      "code": "cleos create account eosio addressbook YOUR_PUBLIC_KEY YOUR_PUBLIC_KEY -p eosio@active",
      "language": "shell"
    }
  ]
}
[/block]
Deploy the `addressbook` contract
[block:code]
{
  "codes": [
    {
      "code": "cleos set contract addressbook CONTRACTS_DIR/addressbook -p addressbook@active",
      "language": "text"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "5f78f9aea400783342b41a989b1b4821ffca006cd76ead38ebdf97428559daa0  5152 bytes  727 us\n#         eosio <= eosio::setcode               {\"account\":\"addressbook\",\"vmtype\":0,\"vmversion\":0,\"code\":\"0061736d010000000191011760077f7e7f7f7f7f7f...\n#         eosio <= eosio::setabi                {\"account\":\"addressbook\",\"abi\":\"0e656f73696f3a3a6162692f312e30010c6163636f756e745f6e616d65046e616d65...\nwarning: transaction executed locally, but may not be confirmed by the network yet    ]",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 12: Test the Contract"
}
[/block]
Add a row to the table
[block:code]
{
  "codes": [
    {
      "code": "cleos push action addressbook upsert '[\"alice\", \"alice\", \"liddell\", \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p alice@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 003f787824c7823b2cc8210f34daed592c2cfa66cbbfd4b904308b0dfeb0c811  152 bytes  692 us\n#   addressbook <= addressbook::upsert          {\"user\":\"alice\",\"first_name\":\"alice\",\"last_name\":\"liddell\",\"street\":\"123 drink me way\",\"city\":\"wonde...",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Check that **alice** cannot add records for another user. 
[block:code]
{
  "codes": [
    {
      "code": "cleos push action addressbook upsert '[\"bob\", \"bob\", \"is a loser\", \"doesnt exist\", \"somewhere\", \"someplace\"]' -p alice@active",
      "language": "text"
    }
  ]
}
[/block]
As expected, the `require_auth` in our contract prevented alice from creating/modifying another user's row.
[block:code]
{
  "codes": [
    {
      "code": "Error 3090004: Missing required authority\nEnsure that you have the related authority inside your transaction!;\nIf you are currently using 'cleos push action' command, try to add the relevant authority using -p option.",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Retrieve alice's record.
[block:code]
{
  "codes": [
    {
      "code": "cleos get table addressbook addressbook people --lower alice --limit 1",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"rows\": [{\n      \"key\": \"3773036822876127232\",\n      \"first_name\": \"alice\",\n      \"last_name\": \"liddell\",\n      \"street\": \"123 drink me way\",\n      \"city\": \"wonderland\",\n      \"state\": \"amsterdam\"\n    }\n  ],\n  \"more\": false\n}",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Test to see that **alice** can remove the record.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action addressbook erase '[\"alice\"]' -p alice@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 0a690e21f259bb4e37242cdb57d768a49a95e39a83749a02bced652ac4b3f4ed  104 bytes  1623 us\n#   addressbook <= addressbook::erase           {\"user\":\"alice\"}\nwarning: transaction executed locally, but may not be confirmed by the network yet    ]",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Check that the record was removed:
[block:code]
{
  "codes": [
    {
      "code": "cleos get table addressbook addressbook people --lower alice --limit 1",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"rows\": [],\n  \"more\": false\n}",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Looking good!
[block:api-header]
{
  "title": "Wrapping Up"
}
[/block]
You've learned how to configure tables, instantiate tables, create new rows, modify existing rows and work with iterators. You've learned how to test against an empty iterator result. Congrats!