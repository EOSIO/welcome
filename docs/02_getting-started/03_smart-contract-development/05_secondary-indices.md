---
content_title: "2.5: Secondary Indices"
link_text: "2.5: Secondary Indices"
---
The following section, shows how to add another index to the `addressbook` contract, so you can iterate through the records in a different way besides using the primary index.

## Step 1: Remove existing data from table

As mentioned earlier, *a table's structure cannot be modified when it contains data.* This first step allows the removal of the data already added.

Remove all records of alice and bob that were added in previous tutorial.

```shell
cleos push action addressbook erase '["alice"]' -p alice@active
```

```shell
cleos push action addressbook erase '["bob"]' -p bob@active
```

## Step 2: Add secondary non-unique index to `kv_addresses_table` configuration

A non-unique index must be defined for at least two properties of the structure defining the `kv table` rows. The first one needs to be a property that stores unique values, because under the hood every `kv index` (non-unique or unique) is stored as a unique index, and by providing as the first property one that has unique values it ensures the uniques of the values combined (including non-unique ones). The rest of the properties defined for the non-unique index, next to the first one, are the ones indexed non-uniquely.

`KV API` provides the `non_unique` template type which is a clear way for developers to mark an index as non-unique.

For details about `KV API` indexes consult the `How-To Create KV API Indexes` section covering this subject.

Add the following `last_name_idx` non-unique index definition next to the already existing one `account_name_uidx`.

```cpp
  kv_table::index<name> account_name_uidx {"accnameuidx"_n, &person::account_name};
  kv_table::index<non_unique<eosio::name, string>> last_name_idx {"lastnameidx"_n, &person::last_name};
```

## Step 3: Use the new non-unique index

You can now use the newly created index. For that create a new action which will return all entries in the addressbook which share the same last name.

In the `addressbook.hpp` add the following:

```cpp
  // retrieves list of persons with the same last name
  [[eosio::action]]
  std::vector<person> getbylastname(string last_name);

  using get_by_last_name_action = action_wrapper<"getbylastname"_n, &kv_addr_book::getbylastname>;
```

And define the action in the `addressbook.cpp` as follows:

```cpp
// retrieves list of persons with the same last name
[[eosio::action]]
std::vector<person> addressbook::getbylastname(string last_name) {

   kv_address_table addresses{"kvaddrbook"_n};

   eosio::name min_account_name{0};
   eosio::name max_account_name{UINT_MAX};
   auto list_of_persons = addresses.last_name_idx.range(
      {min_account_name, last_name},
      {max_account_name, last_name});

   // return found list of person from action
   return list_of_persons;
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

```shell
cleos push action addressbook upsert '["mike", "mike", "liddell", 35, "345 drive", "somewhereelse", "seattle"]' -p bob@active
```

Retrieve all the persons in the addressbook by last name `liddell`.

```shell
cleos push action addressbook getbylastname '["liddell"]' -p alice@active
```

You should see something like the following:

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
    },
    {
      "key": "mike",
      "first_name": "mike",
      "last_name": "liddell",
      "age": 35,
      "street": "345 drive",
      "city": "somewhereelse",
      "state": "seattle"
    }
  ],
  "more": false,
  "next_key": ""
}
```

## Wrapping Up

The complete `addressbook` contract up to this point:

The `addressbook.hpp` file:

```cpp
#include <eosio/eosio.hpp>
using namespace std;
using namespace eosio;

struct person {
 eosio::name account_name;
 std::string first_name;
 eosio::non_unique<eosio::name, std::string> last_name;
 std::string street;
 std::string city;
 std::string state;
};

class [[eosio::contract]] addressbook : public eosio::contract {
   public:
      using contract::contract;

      addressbook(name receiver, name code, datastream<const char*> ds)
         : contract(receiver, code, ds) {}

      struct [[eosio::table]] kv_address_table : kv_table<person> {

         kv_table::index<name> account_name_uidx {"accnameuidx"_n, &person::account_name};
         kv_table::index<non_unique<eosio::name, string>> last_name_idx {"lastnameidx"_n, &person::last_name};

         kv_address_table(eosio::name contract_name) {
            init(contract_name,
               "kvaddrbook"_n,
               eosio::kv_ram,
               account_name_uidx,
               last_name_idx);
         }
      };

      // creates if not exists, or updates if already exists, a person
      [[eosio::action]]
      std::pair<int, std::string> upsert(
         eosio::name account_name,
         string first_name,
         string last_name,
         string street,
         string city,
         string state);

      // deletes a person based on primary key account_name
      [[eosio::action]]
      void del(name account_name);

      // retrieves list of persons with the same last name
      [[eosio::action]]
      std::vector<person> getbylastname(string last_name);

      using upsert_action = action_wrapper<"upsert"_n, &addressbook::upsert>;
      using del_action = action_wrapper<"del"_n, &addressbook::del>;
      using get_by_last_name_action = action_wrapper<"getbylastname"_n, &addressbook::getbylastname>;

   private:
      kv_address_table addresses{"kvaddrbook"_n};
};
```

The `addressbook.cpp` file:

```
#include <addressbook.hpp>

// creates if not exists, or updates if already exists, a person
[[eosio::action]]
std::pair<int, std::string> addressbook::upsert(
      eosio::name account_name,
      string first_name,
      string last_name,
      string street,
      string city,
      string state) {

   require_auth( account_name );
   kv_address_table addresses{"kvaddrbook"_n};

   std::pair<int, std::string> results = {0, "NOP"};

   // retrieves the person by account name
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
      eosio::print_f("Person was successfully added to addressbook.");
      results = {1, "New row created."};
   }
   else {
      eosio::print_f("Person was successfully updated in addressbook.");
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
      eosio::print_f("Person was successfully deleted from addressbook.");
   }
   else {
      eosio::print_f("Person not found in addressbook.");
   }
}

// retrieves list of persons with the same last name
[[eosio::action]]
std::vector<person> addressbook::getbylastname(string last_name) {

   kv_address_table addresses{"kvaddrbook"_n};

   eosio::name min_account_name{0};
   eosio::name max_account_name{UINT_MAX};
   auto list_of_persons = addresses.last_name_idx.range(
      {min_account_name, last_name},
      {max_account_name, last_name});

   // return found list of person from action
   return list_of_persons;
}
```

## What's Next?
- [Adding Inline Actions](./06_adding-inline-actions.md): Learn how to construct actions and send those actions from within a contract.
