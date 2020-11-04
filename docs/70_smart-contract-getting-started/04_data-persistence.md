---
content_title: "Data Persistence"
link_text: "Data Persistence"
---

This section demonstrates data persistence and builds a simple addressbook smart contract. The implementation is not a full production smart contract, however it is a good smart contract to learn how data persistence works on EOSIO without being distracted by business logic not related to eosio's `Key-Value API` functionality.

## Step 1: Create a new directory

In the previous [2.1: Hello World Contract](./01_hello-world.md) section, you created a contract directory, open a command shell and navigate there.

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

In the previous [2.1: Hello World Contract](./01_hello-world.md) section, you created a hello world contract and learned the basics. The code snippet below uses a similar pattern and creates a class named `addressbook`:

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract]] addressbook : public eosio::contract {
  public:

  private:

};
```

## Step 4: Create The Data Structure For The Address Book

In this step you will create the following:

1. the C++ `person` structure which defines the structure of the objects stored in `addressbook` underlying `kv table`,
2. the `kv_address_table` type which defines the `kv table` where the `person` objects are stored.

### Step 4.1: Define The Person Structure

The `addressbook` smart contract stores person records in a `key-value table` also referred to as `kv table`.  A `kv table` is an on-chain storage location which is organized as a table of rows where each row stores objects of the same type.

Define a C++ structure which represents the `person` stored in the `addressbook`.

```cpp
struct person {
};
```

The object stored in a `kv table` row must have defined a property which stores unique values. To accomplish this, for the `person` structure, define a property named `account_name` of type `eosio::name`. A unique index, called `primary index`, will be defined later based on this property.

```cpp
struct person {
 eosio::name account_name;
};
```

Since this contract is an addressbook it should store some relevant details for each `person`.

```cpp
struct person {
 eosio::name account_name;
 std::string first_name;
 std::string last_name;
 std::string street;
 std::string city;
 std::string state;
};
```

The underlying `kv table` row data structure is now complete.

### Step 4.2: Define The Key-Value Table Type

To define a `kv table` extend the parameterized class `kv::table` provided by the `KV API` and use the `person` structure defined earlier for its parameter.

Next, define the required `primary index` by the `kv::table` based on the `account_name` property. To accomplish this declare and initialize a data member `account_name_uidx` of type `kv::table::index`. For initialization use `accname` as its name and `person::account_name` as the underlying property which is indexed.

Call the `kv::table::init()` method from the constructor of the `kv_address_table` struct. Pass as parameters the `contract_name`, the name of the table, and the unique index data member defined and initialized in the previous step.

For the last step, instantiate a data member of type `kv_address_table` and initialize its name which must be an `eosio::name` type, let's say `kvaddrbook`.

```hpp
class [[eosio::contract]] addressbook : public contract {
   public:
      using contract::contract;

      addressbook(name receiver, name code, datastream<const char*> ds)
         : contract(receiver, code, ds) {}

      struct [[eosio::table]] kv_address_table : eosio::kv::table<person, "kvaddrbook"_n> {

      index<name> account_name_uidx {
         name{"accname"_n},
         &person::account_name };
      index<non_unique<name, string>> last_name_idx {
         name{"lastnameidx"_n},
         &person::last_name };

         kv_address_table(name contract_name) {
            init(contract_name,
               account_name_uidx,
               last_name_idx);
         }
      };

   private:
      kv_address_table addresses{"kvaddrbook"_n};
};
```

The `addressbook` underlying `kv table` data structure is now complete.

[[warning]]
| If you add or remove a property to the underlying data structure for a `kv table`, attempting to read the old rows fails.

If you need to modify the underlying data structure, your only options are:

* Add `binary_extension` fields at the end of the structure.
* Define separate structures for the old and new layouts, e.g. `person_v0` and `person_v1`, and define `person` as a variant:  using `person = std::variant<person_v0, person_v1>`.

The same restrictions apply to the multi index tables, except that upgrading from a non-variant to a variant is allowed.

## Step 5: Adding a record to the table

Previously, a unique key was defined to enforce that this contract stores only one record per user. To make it all work, a few rules about the design need to be established.

1. The only account authorized to modify the addressbook is the user.
2. The `primary_key` of the `kv table` is unique, based on `account_name` property.
3. For usability, the contract should have the ability to both create and modify a table row with a single action.

On a EOSIO blockchain an account name is unique, therefore the `account_name` property is an ideal candidate as a **primary_key**. Behind the scenes, the [eosio::name](https://developers.eos.io/manuals/eosio.cdt/latest/structeosio_1_1name) type is an `uint64_t` integer.

Next, define an action for the user to add or update a record in the `kv table`. This action must accept as input parameters the values it needs to create or modify a record.

For user-experience and interface simplicity, write a single method be responsible for both creation and modification of rows. Because of this behavior, name it "upsert," a combination of "update" and "insert."

```cpp
void addressbook::upsert(
  eosio::name account_name,
  std::string first_name,
  std::string last_name,
  std::string street,
  std::string city,
  std::string state
) {}
```

Earlier, it was mentioned that only the user has control over their own record, as this contract is opt-in. To do this, utilize the [require_auth](https://developers.eos.io/manuals/eosio.cdt/latest/group__action/#function-require_auth) method provided by the `eosio.cdt`. This method accepts an `eosio::name` type argument and asserts that the account executing the transaction matches the provided value and has the proper permissions to do so.

```cpp
void upsert(eosio::name account_name, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {

  require_auth( account_name );
}
```

To access the previously defined `kv_address_table`, declare a variable of its type and pass its name as parameter:

```cpp
void upsert(name account_name, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {

  require_auth( account_name );
  kv_address_table addresses{"kvaddrbook"_n};
}
```

To create a new record or update it, if it already exists, call the `put` method defined by the `kv::table` class.

```cpp
void upsert(name account_name, std::string first_name, std::string last_name, std::string street, std::string city, std::string state) {

  require_auth( account_name );
  addresses.put({account_name, first_name, last_name, street, city, state}, get_self());
}
```

### Step 5.1: Return values from action

Starting from EOSIO version 2.1 you can return values from actions. Because the `upsert` action has two outcomes, one that creates a new row in the table and another that updates the row if it already exists, you can take advantage of this new feature and return two different results, one for each case. The returned results can be of any C++ standard type or any standard library type as well as any user defined types. For exemplification they are defined as a `std::pair<int, std::string>` consisting of an integer and a string detailing the result. Also change the return type of the function that implements the `upsert` action to be of type `std::pair<int, std::string>`.

```cpp
// creates if not exists, or updates if already exists, a person
pair<int, string> addressbook::upsert(
      name account_name,
      string first_name,
      string last_name,
      string street,
      string city,
      string state) {

   require_auth( account_name );
   kv_address_table addresses{"kvaddrbook"_n};

   pair<int, string> results = {0, "NOP"};

   // retrieve the person by account name
   auto itr = addresses.account_name_uidx.find(account_name);

   // upsert into kv_table
   addresses.put({
         account_name,
         first_name,
         {account_name, last_name},
         street,
         city,
         state},
      get_self());

   // print customized message for insert vs update
   if (itr == addresses.account_name_uidx.end()) {
      print_f("Person was successfully added to addressbook.");
      results = {1, "New row created."};
   }
   else {
      print_f("Person was successfully updated in addressbook.");
      results = {2, "Existing row updated."};
   }
   return results;
}
```

The `addressbook` contract has an action which enables a user to create a row in the table, if that record does not yet exist, or modify it if it already exists. And for each case it returns a different result.

But what if the user wants to remove the record entirely?

## Step 6: Remove record from the table

Similar to the previous steps, create a public method in the `addressbook` contract and make sure to include the ABI declarations and a [require_auth](https://developers.eos.io/manuals/eosio.cdt/latest/group__action/#function-require_auth). The `require_auth` tests against the action's argument `account_name` to verify that only the owner of a record can modify their account.

```cpp
    void del(name account_name){
        require_auth(account_name);
    }
```

In `addressbook` each account has only one record. Add an iterator and use the `find` method, of the `kv::table::index` class, to search for a `person` by the primary key account name.

```cpp
...
    // deletes a person based on primary key account_name
    void addressbook::del(name account_name) {

        require_auth(account_name);
        kv_address_table addresses{"kvaddrbook"_n};

        // search for person by primary key account_name
        auto itr = addresses.account_name_uidx.find(account_name);
    }
...
```

A contract *cannot* erase a record that doesn't exist, so check that the record indeed exists before proceeding.

```cpp
...
    // deletes a person based on primary key account_name
    void addressbook::del(name account_name) {

        require_auth(account_name);
        kv_address_table addresses{"kvaddrbook"_n};

        // search for person by primary key account_name
        auto itr = addresses.account_name_uidx.find(account_name);

        // check if person was found
        if (itr != addresses.account_name_uidx.end()) {
        }
        else {
        }
    }
...
```

Finally, call the `erase` method in case the person already exists. Once the row is erased, the storage space is freed for the original payer.

```cpp
...
// deletes a person based on primary key account_name
    void addressbook::del(name account_name) {

        require_auth(account_name);
        kv_address_table addresses{"kvaddrbook"_n};

        // search for person by primary key account_name
        auto itr = addresses.account_name_uidx.find(account_name);

        // check if person was found
        if (itr != addresses.account_name_uidx.end()) {
            // extract person from iterator and delete it
            const auto& person_found = itr.value();

            // delete it from kv_table
            addresses.erase(person_found);
            print_f("Person was successfully deleted from addressbook.");
        }
        else {
            print_f("Person not found in addressbook.");
        }
    }
...
```

The contract is now mostly complete. Users can create, modify and erase records. However, the contract is not quite ready to be compiled.

## Step 7: Preparing for the ABI

### 7.1 ABI Action Declarations

[eosio.cdt](https://developers.eos.io/manuals/eosio.cdt/latest) includes an ABI Generator, with requires some specific declarations related to EOSIO smart contracts and actions definitions.

Above both the `upsert` and `del` functions add the following C++11 declaration:

```cpp
[[eosio::action]]
```

The above declaration extracts the arguments of the action and creates necessary ABI *struct* descriptions in the generated ABI file.

### 7.2 ABI Table Declarations

Add an ABI declaration to the table. Modify the following line defined in the private region of your contract:

```cpp
struct person {
```

To this:

```cpp
struct [[eosio::table]] person {
```

The `[[eosio.table]]` declaration adds the necessary descriptions to the ABI file.

The `addressbook` smart contract is ready to be compiled now. Below is the final version of the source code files:

The `addressbook.hpp` header file:

```hpp
#include <eosio/eosio.hpp>
using namespace std;
using namespace eosio;

struct person {
 name account_name;
 string first_name;
 non_unique<name, string> last_name;
 string street;
 string city;
 string state;
};

class [[eosio::contract]] addressbook : public contract {
   public:
      using contract::contract;

      addressbook(name receiver, name code, datastream<const char*> ds)
         : contract(receiver, code, ds) {}

      struct [[eosio::table]] kv_address_table : eosio::kv::table<person, "kvaddrbook"_n> {

        index<name> account_name_uidx {
            name{"accname"_n},
            &person::account_name };

        kv_address_table(name contract_name) {
            init(contract_name,
               account_name_uidx,
               last_name_idx);
        }
      };

      // creates if not exists, or updates if already exists, a person
      [[eosio::action]]
      pair<int, string> upsert(
         name account_name,
         string first_name,
         string last_name,
         string street,
         string city,
         string state);

      // deletes a person based on primary key account_name
      [[eosio::action]]
      void del(name account_name);

      using upsert_action = action_wrapper<"upsert"_n, &addressbook::upsert>;
      using del_action = action_wrapper<"del"_n, &addressbook::del>;

   private:
      kv_address_table addresses{"kvaddrbook"_n};
};
```

The `addressbook.cpp` file:

```cpp
#include <addressbook.hpp>

// creates if not exists, or updates if already exists, a person
[[eosio::action]]
pair<int, string> addressbook::upsert(
      name account_name,
      string first_name,
      string last_name,
      string street,
      string city,
      string state) {

   require_auth( account_name );
   kv_address_table addresses{"kvaddrbook"_n};

   pair<int, string> results = {0, "NOP"};

   // retrieve the person by account name
   auto itr = addresses.account_name_uidx.find(account_name);

   // upsert into kv_table
   addresses.put({
         account_name,
         first_name,
         {account_name, last_name},
         street,
         city,
         state},
      get_self());

   // print customized message for insert vs update
   if (itr == addresses.account_name_uidx.end()) {
      print_f("Person was successfully added to addressbook.");
      results = {1, "New row created."};
   }
   else {
      print_f("Person was successfully updated in addressbook.");
      results = {2, "Existing row updated."};
   }
   return results;
}

// deletes a person based on primary key account_name
[[eosio::action]]
void addressbook::del(name account_name) {

   require_auth(account_name);
   kv_address_table addresses{"kvaddrbook"_n};

   // search for person by primary key account_name
   auto itr = addresses.account_name_uidx.find(account_name);

   // check if person was found
   if (itr != addresses.account_name_uidx.end()) {
      // extract person from iterator and delete it
      const auto& person_found = itr.value();

      // delete it from kv_table
      addresses.erase(person_found);
      print_f("Person was successfully deleted from addressbook.");
   }
   else {
      print_f("Person not found in addressbook.");
   }
}
```

## Step 8 Prepare the Ricardian Contract [Optional]

Contracts compiled without a Ricardian contract generate a compiler warning for each action missing an entry in the Ricardian clause.

```shell
Warning, action <upsert> does not have a ricardian contract
Warning, action <del> does not have a ricardian contract
```

To define Ricardian contracts for this smart contract, create a new file called `addressbook.contracts.md`. Notice that the name of the Ricardian contracts must match the name of the smart contract.

```shell
touch addressbook.contracts.md
```

Add Ricardian Contract definitions to this file:

```yaml
<h1 class="contract">upsert</h1>
---
spec-version: 0.0.2
title: Upsert
summary: This action inserts or updates an entry in the `addressbook`. If an entry exists with the same name as the specified account_name parameter, the record is updated with the first_name, last_name, street, city, and state parameters. If a record does not exist, a new record is created. The data is stored in the key-value table. The ram costs are paid by the smart contract.
icon:

<h1 class="contract">del</h1>
---
spec-version: 0.0.2
title: Del
summary: This action removes an entry from the `addressbook` if an entry in the key-value table exists with the specified name.
icon:
```

## Step 9 Prepare the Ricardian Clauses [Optional]

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
summary: This smart contract stores data added by the user. The user consents to the storage of this data by signing the transaction.
icon:


<h1 class="clause">Data Usage</h1>
---
spec-version: 0.0.1
title: General Data Use
summary: This smart contract stores user data. The smart contract does not use the stored data for any purpose outside store and delete.
icon:

<h1 class="clause">Data Ownership</h1>
---
spec-version: 0.0.1
title: Data Ownership
summary: The user of this smart contract verifies that the data is owned by the smart contract, and that the smart contract can use the data in accordance to the terms defined in the Ricardian Contract.
icon:

<h1 class="clause">Data Distribution</h1>
---
spec-version: 0.0.1
title: Data Distribution
summary: The smart contract promises to not actively share or distribute the address data. The user of the smart contract understands that data stored in a key-value table is not private data and can be accessed by any user of the blockchain.  
icon:


<h1 class="clause">Data Future</h1>
---
spec-version: 0.0.1
title: Data Future
summary: The smart contract promises to only use the data in accordance of the terms defined in the Ricardian Contract, now and at all future dates.
icon:

```

## Step 10: Compile the Contract

Execute the following command from your terminal.

```shell
eosio-cpp addressbook.cpp -o addressbook.wasm
```

If you created a Ricardian contract with Ricardian clauses, the definitions appear in the .abi file. An example for the addressbook.cpp, built including the contract and clause definitions described above, is shown below.

```json
{
    "____comment": "This file was generated with eosio-abigen. DO NOT EDIT ",
    "version": "eosio::abi/1.1",
    "types": [],
    "structs": [
        {
            "name": "del",
            "base": "",
            "fields": [
                {
                    "name": "account_name",
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
                    "name": "account_name",
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
            "name": "del",
            "type": "del",
            "ricardian_contract": "---\nspec-version: 0.0.2\ntitle: Erase\nsummary: this action removes an entry from the `addressbook` if an entry exists with the same name \nicon:"
        },
        {
            "name": "upsert",
            "type": "upsert",
            "ricardian_contract": "---\nspec-version: 0.0.2\ntitle: Upsert\nsummary: This action either inserts or updates an entry in the `addressbook`. If an entry exists with the same name as the account_name parameter the record is updated with the first_name, last_name, street, city and state parameters. If a record does not exist a new record is created. The data is stored in the key-value table. The ram costs are paid by the smart contract.\nicon:"
        }
    ],
    "tables": [
        {
            "name": "kvaddrbook",
            "type": "person",
            "index_type": "i64",
            "key_names": [],
            "key_types": []
        }
    ],
    "ricardian_clauses": [
        {
            "id": "Data Storage",
            "body": "---\nspec-version: 0.0.1\ntitle: General data Storage\nsummary: This smart contract stores data added by the user. The user verifies they are happy for this data to be stored.\nicon:"
        },
        {
            "id": "Data Usage",
            "body": "---\nspec-version: 0.0.1\ntitle: General data Use\nsummary: This smart contract stores user data. The smart contract does not use the stored data for any purpose outside store and delete \nicon:"
        },
        {
            "id": "Data Ownership",
            "body": "---\nspec-version: 0.0.1\ntitle: Data Ownership\nsummary: The user of this smart contract verifies that the data is owned by the smart contract, and that the smart contract can use the data in accordance to the terms defined in the Ricardian Contract \nicon:"
        },
        {
            "id": "Data Distribution",
            "body": "---\nspec-version: 0.0.1\ntitle: Data Ownership\nsummary: The smart contract promises to not actively share or distribute the address data. The user of the smart contract understands that data stored in a key-value table is not private data and can be accessed by any user of the blockchain.  \nicon:"
        },
        {
            "id": "Data Future",
            "body": "---\nspec-version: 0.0.1\ntitle: Data Ownership\nsummary: The smart contract promises to only use the data in accordance to the terms defined in the Ricardian Contract, now and at all future dates. \nicon:"
        }
    ],
    "variants": []
}
```

## Step 11: Deploy the Contract

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

## Step 12: Test the Contract

Add a row to the table

```shell
cleos push action addressbook upsert '["alice", "alice", "liddell", "123 drink me way", "wonderland", "amsterdam"]' -p alice@active
```

```shell
executed transaction: 003f787824c7823b2cc8210f34daed592c2cfa66cbbfd4b904308b0dfeb0c811  152 bytes  692 us
#   addressbook <= addressbook::upsert          {"account_name":"alice","first_name":"alice","last_name":"liddell","street":"123 drink me way","city":"wonde...
```

Check that `alice` cannot add records for another user.

```text
cleos push action addressbook upsert '["bob", "bob", "is a loser", "doesnt exist", "somewhere", "someplace"]' -p alice@active
```

As expected, the `require_auth` function used in the action method prevented `alice` from creating/modifying another user's row.

```shell
Error 3090004: Missing required authority
Ensure that you have the related authority inside your transaction!;
If you are currently using 'cleos push action' command, try to add the relevant authority using -p option.
Error Details:
missing authority of bob
```

Retrieve alice's record.

```shell
cleos get table addressbook addressbook kvaddrbook --lower alice --limit 1
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

Test to see that `alice` can remove the record.

```shell
cleos push action addressbook del '["alice"]' -p alice@active
```

```shell
executed transaction: 0a690e21f259bb4e37242cdb57d768a49a95e39a83749a02bced652ac4b3f4ed  104 bytes  1623 us
#   addressbook <= addressbook::del           {"account_name":"alice"}
warning: transaction executed locally, but may not be confirmed by the network yet    ]
```

Check that the record was removed:

```shell
cleos get table addressbook addressbook kvaddrbook --lower alice --limit 1
```

```shell
{
  "rows": [],
  "more": false，
  "next_key": ""
}
```

## Wrapping Up

You've learned how to configure tables, instantiate tables, create new rows, modify existing rows and work with iterators. You've learned how to test against an empty iterator result. Congrats!

## What's Next?

- [Secondary Indices](./05_secondary-indices.md): Learn how to add another index to the `addressbook` contract that you created in the preceding **Data Persistence** section.
