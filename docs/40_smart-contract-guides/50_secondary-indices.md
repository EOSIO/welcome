---
content_title: "Secondary Indices"
link_text: "Secondary Indices"
---
This tutorial shows how to persist data used by smart contracts and create many indexes to access that data.

## Introduction
EOSIO has the ability to sort tables by up to 16 indices. In the following section, we're going to add another index to the `addressbook` contract, so we can iterate through the records in a different way.

## Step 1: Remove existing data from table

As mentioned earlier, *a table's struct cannot be modified when it contains data.* This first step allows the removal of the data already added.

Remove all records of alice and bob that were added in previous tutorial.

```shell
cleos push action addressbook erase '["alice"]' -p alice@active
```

```shell
cleos push action addressbook erase '["bob"]' -p bob@active
```

## Step 2: Add new index member and getter

Add a new member variable and its getter to the `addressbook.cpp` contract. Since the secondary index needs to be numeric field, a `uint64_t` age variable is added.

```cpp
uint64_t age;
uint64_t get_secondary_1() const { return age;}
```

## Step 3: Add secondary index to `addresses` table configuration

A field has been defined as the secondary index, next the  `address_index` table needs to be reconfigured.

```cpp
using address_index = eosio::multi_index<"people"_n, person,
indexed_by<"byage"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>
>;
```

In the third parameter, we pass a `indexed_by` struct which is used to instantiate a index.

In that `indexed_by` struct, we specify the name of index as `"byage"` and the second type parameter as a function call operator which extracts a const value as an index key. In this case, we point it to the getter we created earlier so this multiple index table will index records by the `age` variable.

```cpp
indexed_by<"byage"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>

```

## Step 4: Modify code

With all the changes in previous steps, we can now update the `upsert` function. Change the function parameter list to the following:

```cpp
void upsert(name user, std::string first_name, std::string last_name, uint64_t age, std::string street, std::string city, std::string state)
```

Add additional lines to update `age` field in `upsert` function as the following:

```cpp
void upsert(name user, std::string first_name, std::string last_name, uint64_t age, std::string street, std::string city, std::string state) {
  require_auth( user );
  address_index addresses( get_first_receiver(), get_first_receiver().value);
  auto iterator = addresses.find(user.value);
  if( iterator == addresses.end() )
  {
    addresses.emplace(user, [&]( auto& row ) {
      row.key = user;
      row.first_name = first_name;
      row.last_name = last_name;
      // -- Add code below --
      row.age = age;
      row.street = street;
      row.city = city;
      row.state = state;
    });
  }
  else {
    addresses.modify(iterator, user, [&]( auto& row ) {
      row.key = user;
      row.first_name = first_name;
      row.last_name = last_name;
      // -- Add code below --
      row.age = age;
      row.street = street;
      row.city = city;
      row.state = state;
    });
  }
}
```

## Step 5: Compile and Deploy

Compile

```shell
eosio-cpp --abigen addressbook.cpp -o addressbook.wasm
```

Deploy

```shell
cleos set contract addressbook CONTRACTS_DIR/addressbook
```

## Step 6: Test it

Insert records

```shell
cleos push action addressbook upsert '["alice", "alice", "liddell", 9, "123 drink me way", "wonderland", "amsterdam"]' -p alice@active
```

```shell
cleos push action addressbook upsert '["bob", "bob", "is a guy", 49, "doesnt exist", "somewhere", "someplace"]' -p bob@active
```

Look up alice's address by the age index. Here the `--index 2` parameter is used to indicate that the query applies to the secondary index

```shell
cleos get table addressbook addressbook people --upper 10 \
--key-type i64 \
--index 2
```

You should see something like the following

```json
{
  "rows": [{
      "key": "alice",
      "first_name": "alice",
      "last_name": "liddell",
      "age": 9,
      "street": "123 drink me way",
      "city": "wonderland",
      "state": "amsterdam"
    }
  ],
  "more": false,
  "next_key": ""
}
```

Look it up by Bob's age

```shell
cleos get table addressbook addressbook people --upper 50 --key-type i64 --index 2
```

It should return

```json
{
  "rows": [{
      "key": "alice",
      "first_name": "alice",
      "last_name": "liddell",
      "age": 9,
      "street": "123 drink me way",
      "city": "wonderland",
      "state": "amsterdam"
    },{
      "key": "bob",
      "first_name": "bob",
      "last_name": "is a guy",
      "age": 49,
      "street": "doesnt exist",
      "city": "somewhere",
      "state": "someplace"
    }
  ],
  "more": false
}
```

## Wrapping Up

The complete `addressbook` contract up to this point:

```cpp
#include <eosio/eosio.hpp>
#include <eosio/print.hpp>

using namespace eosio;

class [[eosio::contract("addressbook")]] addressbook : public eosio::contract {

public:

  addressbook(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}

  [[eosio::action]]
  void upsert(name user, std::string first_name, std::string last_name, uint64_t age, std::string street, std::string city, std::string state) {
    require_auth( user );
    address_index addresses(get_first_receiver(),get_first_receiver().value);
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
    }
    else {
      addresses.modify(iterator, user, [&]( auto& row ) {
        row.key = user;
        row.first_name = first_name;
        row.last_name = last_name;
        row.age = age;
        row.street = street;
        row.city = city;
        row.state = state;
      });
    }
  }

  [[eosio::action]]
  void erase(name user) {
    require_auth(user);

    address_index addresses(get_self(), get_first_receiver().value);

    auto iterator = addresses.find(user.value);
    check(iterator != addresses.end(), "Record does not exist");
    addresses.erase(iterator);
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
    uint64_t get_secondary_1() const { return age; }

  };

  using address_index = eosio::multi_index<"people"_n, person, indexed_by<"byage"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>>;

};
```

## What's Next

- [Adding Inline Actions](./60_adding-inline-actions.md): Learn how to construct actions and send those actions from within a contract.
