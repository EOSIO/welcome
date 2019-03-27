---
title: "2.8 Secondary Indices"
excerpt: ""
---
EOSIO has the ability to sort tables by up to 16 indices. In the following section, we're going to add another index to the `addressbook` contract, so we can iterate through the records in a different way. 
[block:api-header]
{
  "title": "Step 1: Remove existing data from table"
}
[/block]
As mentioned earlier, **a table's struct cannot be modified when it has data in it.** The first step let us remove the data we've already added.

Remove records of alice and bob
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
      "code": "cleos push action addressbook erase '[\"bob\"]' -p bob@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 2: Add new index member and getter"
}
[/block]
First let us add a new member variable and its getter to the `addressbook.cpp` contract.

As the secondary index needs to be numeric field, so we choose to add an `uint64_t` age variable
[block:code]
{
  "codes": [
    {
      "code": "uint64_t age;\nuint64_t get_secondary_1() const { return age;}",
      "language": "cplusplus",
      "name": null
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "There are few other allowed types for a secondary index but we will cover them in a different tutorial"
}
[/block]

[block:api-header]
{
  "title": "Step 3: Add secondary index to `addresses` table configuration"
}
[/block]
Now we have a field that be used as the secondary index, we need to reconfigure the address_index table. 
[block:code]
{
  "codes": [
    {
      "code": "typedef eosio::multi_index<\"people\"_n, person, \nindexed_by<\"byage\"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>\n  > address_index;",
      "language": "cplusplus"
    }
  ]
}
[/block]
In the third parameter, we pass a `index_by` struct which is used to instantiate a index. 

In that `index_by` struct, we specify the name of index as `"byage"` and the second type parameter as a function call operator should extract a const value as an index key. In this case, we point it to the getter we created earlier so this multiple index table will index records by `age` variable.
[block:code]
{
  "codes": [
    {
      "code": "indexed_by<\"byage\"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 4: Compile and Deploy"
}
[/block]
Compile
[block:code]
{
  "codes": [
    {
      "code": "eosio-cpp -o addressbook.wasm addressbook.cpp --abigen\n",
      "language": "shell"
    }
  ]
}
[/block]
Deploy
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

[block:api-header]
{
  "title": "Step 5: Test it"
}
[/block]
Insert records
[block:code]
{
  "codes": [
    {
      "code": "cleos push action addressbook upsert '[\"alice\", \"alice\", \"liddell\", 9, \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p alice@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos push action addressbook upsert '[\"bob\", \"bob\", \"is a guy\", 49, \"doesnt exist\", \"somewhere\", \"someplace\"]' -p bob@active",
      "language": "shell"
    }
  ]
}
[/block]
Let us look up alice's address by the age index. Here we use the `--index 2` parameter to indicate which indices should be use
[block:code]
{
  "codes": [
    {
      "code": "cleos get table addressbook addressbook people --upper 10 \\\n--key-type i64 \\\n--index 2",
      "language": "shell"
    }
  ]
}
[/block]
You should see something like the following
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"rows\": [{\n      \"key\": \"alice\",\n      \"first_name\": \"alice\",\n      \"last_name\": \"liddell\",\n      \"age\": 9,\n      \"street\": \"123 drink me way\",\n      \"city\": \"wonderland\",\n      \"state\": \"amsterdam\"\n    }\n  ],\n  \"more\": false\n}",
      "language": "json"
    }
  ]
}
[/block]
Look it up by Bob's age
[block:code]
{
  "codes": [
    {
      "code": "cleos get table addressbook addressbook people --upper 50 \\\n--key-type i64 --index 2",
      "language": "shell"
    }
  ]
}
[/block]
It should return
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"rows\": [{\n      \"key\": \"alice\",\n      \"first_name\": \"alice\",\n      \"last_name\": \"liddell\",\n      \"age\": 9,\n      \"street\": \"123 drink me way\",\n      \"city\": \"wonderland\",\n      \"state\": \"amsterdam\"\n    },{\n      \"key\": \"bob\",\n      \"first_name\": \"bob\",\n      \"last_name\": \"is a loser\",\n      \"age\": 49,\n      \"street\": \"doesnt exist\",\n      \"city\": \"somewhere\",\n      \"state\": \"someplace\"\n    }\n  ],\n  \"more\": false\n}",
      "language": "json"
    }
  ]
}
[/block]

All good!

[block:api-header]
{
  "title": "Wrapping Up"
}
[/block]
The complete `addressbook` contract up to this point:
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass [[eosio::contract]] addressbook : public eosio::contract {\n\npublic:\n  using contract::contract;\n  \n  addressbook(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}\n\n  [[eosio::action]]\n  void upsert(name user, std::string first_name, std::string last_name, uint64_t age, std::string street, std::string city, std::string state) {\n    require_auth( user );\n    address_index addresses(_code, _code.value);\n    auto iterator = addresses.find(user.value);\n    if( iterator == addresses.end() )\n    {\n      addresses.emplace(user, [&]( auto& row ) {\n       row.key = user;\n       row.first_name = first_name;\n       row.last_name = last_name;\n       row.age = age;\n       row.street = street;\n       row.city = city;\n       row.state = state;\n      });\n    }\n    else {\n      std::string changes;\n      addresses.modify(iterator, user, [&]( auto& row ) {\n        row.key = user;\n        row.first_name = first_name;\n        row.last_name = last_name;\n        row.street = street;\n        row.city = city;\n        row.state = state;\n      });\n    }\n  }\n\n  [[eosio::action]]\n  void erase(name user) {\n    require_auth(user);\n\n    address_index addresses(_self, _code.value);\n\n    auto iterator = addresses.find(user.value);\n    eosio_assert(iterator != addresses.end(), \"Record does not exist\");\n    addresses.erase(iterator);\n  }\n\nprivate:\n  struct [[eosio::table]] person {\n    name key;\n    std::string first_name;\n    std::string last_name;\n    uint64_t age;\n    std::string street;\n    std::string city;\n    std::string state;\n  \n    uint64_t primary_key() const { return key.value; }\n    uint64_t get_secondary_1() const { return age;}\n  \n  };\n\n  typedef eosio::multi_index<\"people\"_n, person, indexed_by<\"byage\"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>> address_index;\n  \n};\n\nEOSIO_DISPATCH( addressbook, (upsert)(erase))",
      "language": "cplusplus"
    }
  ]
}
[/block]