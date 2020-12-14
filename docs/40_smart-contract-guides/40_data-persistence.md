---
content_title: "Data Persistence"
link_text: "Data Persistence"
---
This tutorial shows how to persist data used by smart contracts.

## Introduction
This section demonstrates data persistence and builds a simple addressbook smart contract. The implementation is not a full production smart contract, however it is a good smart contract to learn how data persistence works on EOSIO without being distracted by business logic not related to eosio's `multi_index API` functionality.

## Step 1: Create a new directory

In the previous [2.1: Hello World Contract](./10_hello-world.md) section, you created a contract directory, open a command shell and navigate there.

```shell
cd CONTRACTS_DIR
```

Create a new directory for the contract and enter the directory.

```shell
mkdir addressbook
cd addressbook
```

## Step 2: Create and open a new file

```shell
touch addressbook.cpp
```

Open the file in your favorite editor.

## Step 3: Write an Extended Standard Class and Include EOSIO

In the previous [2.1: Hello World Contract](./10_hello-world.md) section, you created a hello world contract and learned the basics. The code snippet below uses a similar pattern and creates a class named `addressbook`:

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract("addressbook")]] addressbook : public eosio::contract {
  public:

  private:

};
```

## Step 4: Create The Data Structure For The Address Book

Before a table can be configured and instantiated, we need to define a struct that represents the data structure of the address book. Since it is an address book, the table will contain people, so create a `struct` called "person"

```cpp
struct person {};
```

When defining the structure of a multi_index table, you use a unique value as the primary key.

For this contract, use a field called "key" with type `name` based on the user's `name`. This contract has one unique entry per user, so this key will be a consistent and guaranteed unique value.

```cpp
struct person {
 name key;
};
```

Since this contract is an address book it should store some relevant details for each entry or *person*

```cpp
struct person {
 name key;
 std::string first_name;
 std::string last_name;
 std::string street;
 std::string city;
 std::string state;
};
```

Great. The basic data structure is now complete.

Next, define a `primary_key` method. Every `multi_index` struct requires a *primary key* method. Behind the scenes, this method is used according to the index specification of your `multi_index` instantiation. EOSIO `multi_index` wraps [boost::multi_index](https://www.boost.org/doc/libs/1_59_0/libs/multi_index/doc/index.html)

Create a method `primary_key()` and return a struct member, in this case, the `key` member as previously discussed.

```cpp
struct person {
 name key;
 std::string first_name;
 std::string last_name;
 std::string street;
 std::string city;
 std::string state;

 uint64_t primary_key() const { return key.value;}
};
```

[[warning]]
| A table's data structure cannot be modified while it has data in it. If you need to make changes to a table's data structure in any way, you first need to remove all its rows

## Step 5: Configure the Multi-Index Table

Now that the data structure of the table has been defined with a `struct` we need to configure the table. The [eosio::multi_index](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1multi__index) constructor needs to be named and configured to use the struct we previously defined.

```cpp
using address_index = eosio::multi_index<"people"_n, person>;
```

With the above `multi_index` configuration there is a table named **people**, that

1. Uses the `_n` operator to define an eosio::name type and uses that to name the table. This table contains a number of different singular "persons", so name the table "people".
2. Pass in the singular `person` struct defined in the previous step.
3. Declare this table's type. This type will be used to instantiate this table later.

So far, our file should look like this.

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract("addressbook")]] addressbook : public eosio::contract {

  public:

  private:
    struct [[eosio::table]] person {
      name key;
      std::string first_name;
      std::string last_name;
      std::string street;
      std::string city;
      std::string state;

      uint64_t primary_key() const { return key.value;}
    };
    
  using address_index = eosio::multi_index<"people"_n, person>;
};
```

## Step 6: The Constructor

When working with C++ classes, the first public method you should create is a constructor.

Our constructor will be responsible for initially setting up the contract.

EOSIO contracts extend the *contract* class. Initialize our parent *contract* class with the code name of the contract and the receiver. The important parameter here is the `code` parameter which is the account on the blockchain that the contract is being deployed to.

```cpp
addressbook(name receiver, name code, datastream<const char*> ds):contract(receiver, code, ds) {}
```

## Step 7: Adding a record to the table

Previously, the primary key of the multi-index table was defined to enforce that this contract will only store one record per user. To make it all work, some rules about the design need to be established.

1. The only account authorized to modify the address book is the user.
2. The **primary_key** of our table is unique, based on username
3. For usability, the contract should have the ability to both create and modify a table row with a single action.

On a EOSIO blockchain an account name is unique, therefore the `name` type is an ideal candidate as a **primary_key**. Behind the scenes, the [name](https://developers.eos.io/manuals/eosio.cdt/latest/structeosio_1_1name) type is an `uint64_t` integer.

Next, define an action for the user to add or update a record. This action will need to accept any values that this action needs to be able to emplace (create) or modify.

For user-experience and interface simplicity, have a single method be responsible for both creation and modification of rows. Because of this behavior, name it "upsert," a combination of "update" and "insert."

```cpp
void upsert(
  name user,
  std::string first_name,
  std::string last_name,
  std::string street,
  std::string city,
  std::string state
) {}
```

Earlier, it was mentioned that only the user has control over their own record, as this contract is opt-in. To do this, utilize the [require_auth](https://developers.eos.io/manuals/eosio.cdt/latest/group__action/#function-require_auth) method provided by the `eosio.cdt`. This method accepts an `name` type argument and asserts that the account executing the transaction equals the provided value and has the proper permissions to do so.

```cpp
void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {
  require_auth( user );
}
```

Previously, a multi_index table was configured, and declared as `address_index`. To instantiate a table, two parameters are required:

1. The first parameter "code", which specifies the owner of this table. As the owner, the account will be charged for storage costs.  Also, only that account can modify or delete the data in this table unless another payer is specified. Here we use the `get_self()` function which will pass the name of this contract.

2. The second parameter "scope" which ensures the uniqueness of the table in the scope of this contract. In this case, since we only have one table we can use the value from `get_first_receiver()`. The value returned from the *`get_first_receiver` function is the account name on which this contract is deployed to.*

Note that scopes are used to logically separate tables within a multi-index (see the eosio.token contract multi-index for an example, which scopes the table on the token owner).  Scopes were originally intended to separate table state in order to allow for parallel computation on the individual sub-tables.  However, currently inter-blockchain communication has been prioritized over parallelism.  Because of this, scopes are currently only used to logically separate the tables as in the case of eosio.token.

```cpp
void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {
  require_auth( user );
  address_index addresses(get_self(), get_first_receiver().value);
}
```

Next, query the iterator, setting it to a variable since this iterator will be used several times

```cpp
void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {
  require_auth( user );
  address_index addresses(get_self(), get_first_receiver().value);
  auto iterator = addresses.find(user.value);
}
```

Security has been established and the table instantiated, great!  Next up, write the code for creating or modifying the table.  

First, detect whether a particular user already exists in the table. To do this, use table's [find](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1multi__index#function-find) method by passing the `user` parameter. The find method will return an iterator. Use that iterator to test it against the [end](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1multi__index#function-end) method. The "end" method is an alias for "null".

```cpp
void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {
  require_auth( user );
  address_index addresses(get_self(), get_first_receiver().value);
  auto iterator = addresses.find(user.value);
  if( iterator == addresses.end() )
  {
    //The user isn't in the table
  }
  else {
    //The user is in the table
  }
}
```

Create a record in the table using the multi_index method [emplace](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1multi__index/#function-emplace). This method accepts two arguments, the "payer" of this record who pays the storage usage and a callback function.

The callback function for the emplace method must use a lamba function to create a reference. Inside the body assign the row's values with the ones provided to `upsert`.

```cpp
void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {
  require_auth( user );
  address_index addresses(get_self(), get_first_receiver().value);
  auto iterator = addresses.find(user.value);
  if( iterator == addresses.end() )
  {
    addresses.emplace(user, [&]( auto& row ) {
      row.key = user;
      row.first_name = first_name;
      row.last_name = last_name;
      row.street = street;
      row.city = city;
      row.state = state;
    });
  }
  else {
    //The user is in the table
  }
}
```

Next, handle the modification, or update, case of the "upsert" function. Use the [modify](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1multi__index/#function-modify-12) method, passing a few arguments:

- The iterator defined earlier, presently set to the user as declared when calling this action.
- The "payer", who will pay for the storage cost of this row, in this case, the user.
- The callback function that actually modifies the row.

```cpp
void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {
  require_auth( user );
  address_index addresses(get_self(), get_first_receiver().value);
  auto iterator = addresses.find(user.value);
  if( iterator == addresses.end() )
  {
    addresses.emplace(user, [&]( auto& row ) {
      row.key = user;
      row.first_name = first_name;
      row.last_name = last_name;
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
      row.street = street;
      row.city = city;
      row.state = state;
    });
  }
}
```

The `addressbook` contract now has a functional action that will enable a user to create a row in the table if that record does not yet exist, and modify it if it already exists.

But what if the user wants to remove the record entirely?

## Step 8: Remove record from the table

Similar to the previous steps, create a public method in the `addressbook`, making sure to include the ABI declarations and a [require_auth](https://developers.eos.io/manuals/eosio.cdt/latest/group__action/#function-require_auth) that tests against the action's argument `user` to verify only the owner of a record can modify their account.

```cpp
    void erase(name user){
      require_auth(user);
    }

```

Instantiate the table. In `addressbook` each account has only one record. Set `iterator` with [find](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1multi__index/#function-find)

```cpp
...
    void erase(name user){
      require_auth(user);
      address_index addresses(get_self(), get_first_receiver().value);
      auto iterator = addresses.find(user.value);
    }
...
```

A contract *cannot* erase a record that doesn't exist, so check that the record indeed exists before proceeding.

```cpp
...
    void erase(name user){
      require_auth(user);
      address_index addresses(get_self(), get_first_receiver().value);
      auto iterator = addresses.find(user.value);
      check(iterator != addresses.end(), "Record does not exist");
    }
...
```

Finally, call the [erase](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1multi__index/#function-erase-12) method, to erase the iterator. Once the row is erased, the storage space will be free up for the original payer.

```cpp
...
  void erase(name user) {
    require_auth(user);
    address_index addresses(get_self(), get_first_receiver().value);
    auto iterator = addresses.find(user.value);
    check(iterator != addresses.end(), "Record does not exist");
    addresses.erase(iterator);
  }
...
```

The contract is now mostly complete. Users can create, modify and erase records. However, the contract is not quite ready to be compiled.

## Step 9: Preparing for the ABI

### 9.1 ABI Action Declarations

[eosio.cdt](https://developers.eos.io/manuals/eosio.cdt/latest) includes an ABI Generator, but for it to work will require some declarations.

Above both the `upsert` and `erase` functions add the following C++11 declaration:

```cpp
[[eosio::action]]
```

The above declaration will extract the arguments of the action and create necessary ABI *struct* descriptions in the generated ABI file.

### 9.2 ABI Table Declarations

Add an ABI declaration to the table. Modify the following line defined in the private region of your contract:

```cpp
struct person {
```

To this:

```cpp
struct [[eosio::table]] person {
```

The `[[eosio.table]]` declaration will add the necessary descriptions to the ABI file.

Now our contract is ready to be compiled.

Below is the final state of our `addressbook` contract:

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract("addressbook")]] addressbook : public eosio::contract {

public:

  addressbook(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}

  [[eosio::action]]
  void upsert(name user, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {
    require_auth( user );
    address_index addresses( get_self(), get_first_receiver().value );
    auto iterator = addresses.find(user.value);
    if( iterator == addresses.end() )
    {
      addresses.emplace(user, [&]( auto& row ) {
       row.key = user;
       row.first_name = first_name;
       row.last_name = last_name;
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
        row.street = street;
        row.city = city;
        row.state = state;
      });
    }
  }

  [[eosio::action]]
  void erase(name user) {
    require_auth(user);

    address_index addresses( get_self(), get_first_receiver().value);

    auto iterator = addresses.find(user.value);
    check(iterator != addresses.end(), "Record does not exist");
    addresses.erase(iterator);
  }

private:
  struct [[eosio::table]] person {
    name key;
    std::string first_name;
    std::string last_name;
    std::string street;
    std::string city;
    std::string state;
    uint64_t primary_key() const { return key.value; }
  };
  using address_index = eosio::multi_index<"people"_n, person>;
};
```

## Step 10 Prepare the Ricardian Contract [Optional]

Contracts compiled without a Ricardian contract will generate a compiler warning for each action missing an entry in the Ricardian clause.

```shell
Warning, action <upsert> does not have a ricardian contract
Warning, action <erase> does not have a ricardian contract
```

To define Ricardian contracts for this smart contract, create a new file called addressbook.contracts.md. Notice that the name of the Ricardian contracts must match the name of the smart contract.

```shell
touch addressbook.contracts.md
```

Add Ricardian Contract definitions to this file:

```yaml
<h1 class="contract">upsert</h1>
---
spec-version: 0.0.2
title: Upsert
summary: This action will either insert or update an entry in the address book. If an entry exists with the same name as the specified user parameter, the record is updated with the first_name, last_name, street, city, and state parameters. If a record does not exist, a new record is created. The data is stored in the multi index table. The ram costs are paid by the smart contract.
icon:

<h1 class="contract">erase</h1>
---
spec-version: 0.0.2
title: Erase
summary: This action will remove an entry from the address book if an entry in the multi index table exists with the specified name.
icon:
```

## Step 11 Prepare the Ricardian Clauses [Optional]
To define Ricardian clauses for this smart contract create and open a new file called addressbook.clauses.md. Notice again that the name of the Ricardian clauses must match the name of the smart contract.

```shell
touch addressbook.clauses.md
```

Add Ricardian clause definitions to this file:

```yaml
<h1 class="clause">Data Storage</h1>
---
spec-version: 0.0.1
title: General Data Storage
summary: This smart contract will store data added by the user. The user consents to the storage of this data by signing the transaction.
icon:


<h1 class="clause">Data Usage</h1>
---
spec-version: 0.0.1
title: General Data Use
summary: This smart contract will store user data. The smart contract will not use the stored data for any purpose outside store and delete.
icon:

<h1 class="clause">Data Ownership</h1>
---
spec-version: 0.0.1
title: Data Ownership
summary: The user of this smart contract verifies that the data is owned by the smart contract, and that the smart contract can use the data in accordance to the terms defined in the Ricardian Contract.
icon:

<h1 class="clause">Data Distirbution</h1>
---
spec-version: 0.0.1
title: Data Distirbution
summary: The smart contract promises to not actively share or distribute the address data. The user of the smart contract understands that data stored in a multi index table is not private data and can be accessed by any user of the blockchain.  
icon:


<h1 class="clause">Data Future</h1>
---
spec-version: 0.0.1
title: Data Future
summary: The smart contract promises to only use the data in accordance of the terms defined in the Ricardian Contract, now and at all future dates.
icon:
```

## Step 12: Compile the Contract

Execute the following command from your terminal.

```shell
eosio-cpp addressbook.cpp -o addressbook.wasm
```

If you created a Ricardian contract and Ricardian clauses, the definitions will appear in the .abi file. An example for the addressbook.cpp, built including the contract and clause definitions described above is shown below.

```json
{
    "____comment": "This file was generated with eosio-abigen. DO NOT EDIT ",
    "version": "eosio::abi/1.1",
    "types": [],
    "structs": [
        {
            "name": "erase",
            "base": "",
            "fields": [
                {
                    "name": "user",
                    "type": "name"
                }
            ]
        },
        {
            "name": "person",
            "base": "",
            "fields": [
                {
                    "name": "key",
                    "type": "name"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                },
                {
                    "name": "street",
                    "type": "string"
                },
                {
                    "name": "city",
                    "type": "string"
                },
                {
                    "name": "state",
                    "type": "string"
                }
            ]
        },
        {
            "name": "upsert",
            "base": "",
            "fields": [
                {
                    "name": "user",
                    "type": "name"
                },
                {
                    "name": "first_name",
                    "type": "string"
                },
                {
                    "name": "last_name",
                    "type": "string"
                },
                {
                    "name": "street",
                    "type": "string"
                },
                {
                    "name": "city",
                    "type": "string"
                },
                {
                    "name": "state",
                    "type": "string"
                }
            ]
        }
    ],
    "actions": [
        {
            "name": "erase",
            "type": "erase",
            "ricardian_contract": "---\nspec-version: 0.0.2\ntitle: Erase\nsummary: his action will remove an entry from the address book if an entry exists with the same name \nicon:"
        },
        {
            "name": "upsert",
            "type": "upsert",
            "ricardian_contract": "---\nspec-version: 0.0.2\ntitle: Upsert\nsummary: This action will either insert or update an entry in the address book. If an entry exists with the same name as the user parameter the record is updated with the first_name, last_name, street, city and state parameters. If a record does not exist a new record is created. The data is stored in the multi index table. The ram costs are paid by the smart contract.\nicon:"
        }
    ],
    "tables": [
        {
            "name": "people",
            "type": "person",
            "index_type": "i64",
            "key_names": [],
            "key_types": []
        }
    ],
    "ricardian_clauses": [
        {
            "id": "Data Storage",
            "body": "---\nspec-version: 0.0.1\ntitle: General data Storage\nsummary: This smart contract will store data added by the user. The user verifies they are happy for this data to be stored.\nicon:"
        },
        {
            "id": "Data Usage",
            "body": "---\nspec-version: 0.0.1\ntitle: General data Use\nsummary: This smart contract will store user data. The smart contract will not use the stored data for any purpose outside store and delete \nicon:"
        },
        {
            "id": "Data Ownership",
            "body": "---\nspec-version: 0.0.1\ntitle: Data Ownership\nsummary: The user of this smart contract verifies that the data is owned by the smart contract, and that the smart contract can use the data in accordance to the terms defined in the Ricardian Contract \nicon:"
        },
        {
            "id": "Data Distirbution",
            "body": "---\nspec-version: 0.0.1\ntitle: Data Ownership\nsummary: The smart contract promises to not actively share or distribute the address data. The user of the smart contract understands that data stored in a multi index table is not private data and can be accessed by any user of the blockchain.  \nicon:"
        },
        {
            "id": "Data Future",
            "body": "---\nspec-version: 0.0.1\ntitle: Data Ownership\nsummary: The smart contract promises to only use the data in accordance to the terms defined in the Ricardian Contract, now and at all future dates. \nicon:"
        }
    ],
    "variants": []
}
```

## Step 13: Deploy the Contract

Create an account for the contract, execute the following shell command

```shell
cleos create account eosio addressbook YOUR_PUBLIC_KEY -p eosio@active
```

Deploy the `addressbook` contract

```text
cleos set contract addressbook CONTRACTS_DIR/addressbook -p addressbook@active
```

```shell
5f78f9aea400783342b41a989b1b4821ffca006cd76ead38ebdf97428559daa0  5152 bytes  727 us
#         eosio <= eosio::setcode               {"account":"addressbook","vmtype":0,"vmversion":0,"code":"0061736d010000000191011760077f7e7f7f7f7f7f...
#         eosio <= eosio::setabi                {"account":"addressbook","abi":"0e656f73696f3a3a6162692f312e30010c6163636f756e745f6e616d65046e616d65...
warning: transaction executed locally, but may not be confirmed by the network yet    ]
```

## Step 14: Test the Contract

Add a row to the table

```shell
cleos push action addressbook upsert '["alice", "alice", "liddell", "123 drink me way", "wonderland", "amsterdam"]' -p alice@active
```

```shell
executed transaction: 003f787824c7823b2cc8210f34daed592c2cfa66cbbfd4b904308b0dfeb0c811  152 bytes  692 us
#   addressbook <= addressbook::upsert          {"user":"alice","first_name":"alice","last_name":"liddell","street":"123 drink me way","city":"wonde...
```

Check that **alice** cannot add records for another user.

```text
cleos push action addressbook upsert '["bob", "bob", "is a loser", "doesnt exist", "somewhere", "someplace"]' -p alice@active
```

As expected, the `require_auth` in our contract prevented alice from creating/modifying another user's row.

```shell
Error 3090004: Missing required authority
Ensure that you have the related authority inside your transaction!;
If you are currently using 'cleos push action' command, try to add the relevant authority using -p option.
Error Details:
missing authority of bob
```

Retrieve alice's record.

```shell
cleos get table addressbook addressbook people --lower alice --limit 1
```

```shell
{
  "rows": [{
      "key": "alice",
      "first_name": "alice",
      "last_name": "liddell",
      "street": "123 drink me way",
      "city": "wonderland",
      "state": "amsterdam"
    }
  ],
  "more": false,
  "next_key": ""
}
```

Test to see that **alice** can remove the record.

```shell
cleos push action addressbook erase '["alice"]' -p alice@active
```

```shell
executed transaction: 0a690e21f259bb4e37242cdb57d768a49a95e39a83749a02bced652ac4b3f4ed  104 bytes  1623 us
#   addressbook <= addressbook::erase           {"user":"alice"}
warning: transaction executed locally, but may not be confirmed by the network yet    ]
```

Check that the record was removed:

```shell
cleos get table addressbook addressbook people --lower alice --limit 1
```

```shell
{
  "rows": [],
  "more": false，
  "next_key": ""
}
```

Looking good!

## Wrapping Up

You've learned how to configure tables, instantiate tables, create new rows, modify existing rows and work with iterators. You've learned how to test against an empty iterator result. Congrats!

## What's Next

- [Secondary Indices](./50_secondary-indices.md): Learn how to add another index to the `addressbook` contract that you created in the preceding **Data Persistence** section.
