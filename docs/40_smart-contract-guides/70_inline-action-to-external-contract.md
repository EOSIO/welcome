---
content_title: "Inline Actions to External Contracts"
link_text: "Inline Actions to External Contracts"
---
This tutorial shows how to call inline actions from another smart contract.

## Introduction 
Previously, we sent an inline action to an action that was defined in the contract. In this part of the tutorial, we'll explore sending actions to an external contract. Since we've already gone over quite a bit of contract authoring, we'll keep this contract extremely simple. We'll author a contract that counts actions written by the contract. This contract has very little real-world use, but will demonstrate inline action calls to an external contract

## Step 1: The Addressbook Counter Contract

Navigate to `CONTRACTS_DIR` if not already there, create a directory called `abcounter` and then create a `abcounter.cpp` file

```shell
cd CONTRACTS_DIR
mkdir abcounter
cd abcounter
touch abcounter.cpp
```
Open the `abcounter.cpp` file in your favorite editor and paste the following code into the file. This contract is very basic, and for the most part does not cover much that we haven't already covered up until this point. There are a few exceptions though, and they are covered in full below.

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract("abcounter")]] abcounter : public eosio::contract {
  public:

    abcounter(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}

    [[eosio::action]]
    void count(name user, std::string type) {
      require_auth( name("addressbook"));
      count_index counts(get_first_receiver(), get_first_receiver().value);
      auto iterator = counts.find(user.value);

      if (iterator == counts.end()) {
        counts.emplace("addressbook"_n, [&]( auto& row ) {
          row.key = user;
          row.emplaced = (type == "emplace") ? 1 : 0;
          row.modified = (type == "modify") ? 1 : 0;
          row.erased = (type == "erase") ? 1 : 0;
        });
      }
      else {
        counts.modify(iterator, "addressbook"_n, [&]( auto& row ) {
          if(type == "emplace") { row.emplaced += 1; }
          if(type == "modify") { row.modified += 1; }
          if(type == "erase") { row.erased += 1; }
        });
      }
    }

    using count_action = action_wrapper<"count"_n, &abcounter::count>;

  private:
    struct [[eosio::table]] counter {
      name key;
      uint64_t emplaced;
      uint64_t modified;
      uint64_t erased;
      uint64_t primary_key() const { return key.value; }
    };

    using count_index = eosio::multi_index<"counts"_n, counter>;
};
```
The first new concept in the code above is that we are explicitly restricting calls to the one action to a **specific account** in this contract using [require_auth](https://developers.eos.io/manuals/eosio.cdt/latest/group__action/#function-require_auth) to the `addressbook` contract, as seen below.
```cpp
//Only the addressbook account/contract can authorize this command.
require_auth( name("addressbook"));
```
Previously, a dynamic value was used with `require_auth`.

Another new concept in the code above, is [action wrapper](https://developers.eos.io/manuals/eosio.cdt/latest/structeosio_1_1action__wrapper). As shown below the first template parameter is the 'action' we are going to call and the second one should point to the action function
```text
using count_action = action_wrapper<"count"_n, &abcounter::count>;
```

## Step 2: Create Account for abcounter Contract
Open your terminal and execute the following command to create the **abcounter** user.
```shell
cleos create account eosio abcounter YOUR_PUBLIC_KEY
```

## Step 3: Compile and Deploy

```shell
eosio-cpp abcounter.cpp -o abcounter.wasm
```

Finally, deploy the `abcounter` contract.

```shell
cleos set contract abcounter CONTRACTS_DIR/abcounter
```

## Step 4: Modify addressbook contract to send inline-action to abcounter
Navigate to your addressbook directory now.

```shell
cd CONTRACTS_DIR/addressbook
```

Open the `addressbook.cpp` file in your favorite editor if not already open.

In the last part of this series, we went over inline actions to our own contract. This time, we are going to send an inline action to another contract, our new `abcounter` contract.

Create another helper called `increment_counter` under the `private` declaration of the contract as below:
```cpp
void increment_counter(name user, std::string type) {
    abcounter::count_action count("abcounter"_n, {get_self(), "active"_n});
    count.send(user, type);
}
```
Let's go through the code listing above.

This time we use the [action wrapper](https://developers.eos.io/manuals/eosio.cdt/latest/structeosio_1_1action__wrapper) instead of calling a function. To do that, we firstly initialised the count_action object defined earlier. The first parameter we pass is the callee contract name, in this case `abcounter`. The second parameter is the permission struct.

- For the permission, [get_self()](https://developers.eos.io/manuals/eosio.cdt/latest/classeosio_1_1contract/#function-get_self)  returns the current `addressbook` contract. The `active` permission of `addressbook` is used.

Unlike the `Adding Inline Actions` tutorial, we won't need to specify the action because the action wrapper type incorporates the action when it is defined.

In line 3 we call the action with the data, namely `user` and `type` which are required by the `abcounter` contract.

Now, add the following calls to the helpers in their respective action scopes.

```text
//Emplace
increment_counter(user, "emplace");
//Modify
increment_counter(user, "modify");
//Erase
increment_counter(user, "erase");
```
Now your `addressbook.cpp` contract should look like this.
```cpp
#include <eosio/eosio.hpp>
#include "abcounter.cpp"

using namespace eosio;

class [[eosio::contract("addressbook")]] addressbook : public eosio::contract {

public:

  addressbook(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}

  [[eosio::action]]
  void upsert(name user, std::string first_name, std::string last_name,
      uint64_t age, std::string street, std::string city, std::string state) {
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
      increment_counter(user, "emplace");
    }
    else {
      std::string changes;
      addresses.modify(iterator, user, [&]( auto& row ) {
        row.key = user;
        row.first_name = first_name;
        row.last_name = last_name;
        row.age = age;
        row.street = street;
        row.city = city;
        row.state = state;
      });
      send_summary(user, " successfully modified record to addressbook");
      increment_counter(user, "modify");
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
    increment_counter(user, "erase");
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

  void increment_counter(name user, std::string type) {
    abcounter::count_action count("abcounter"_n, {get_self(), "active"_n});
    count.send(user, type);
  }

  typedef eosio::multi_index<"people"_n, person,
    indexed_by<"byage"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>
  > address_index;
};
```

## Step 5: Recompile and redeploy the addressbook contract
Recompile the `addressbook.cpp` contract, we don't need to regenerate the ABI, because none of our changes have affected the ABI. Note here we include the abcounter contract folder with the -I option.
```shell
eosio-cpp -o addressbook.wasm addressbook.cpp -I ../abcounter/
```
Redeploy the contract
```shell
cleos set contract addressbook CONTRACTS_DIR/addressbook
```

## Step 6: Test It.
Now that we have the `abcounter` deployed and `addressbook` redeployed, we're ready for some testing.
```shell
cleos push action addressbook upsert '["alice", "alice", "liddell", 19, "123 drink me way", "wonderland", "amsterdam"]' -p alice@active
```

```shell
executed transaction: cc46f20da7fc431124e418ecff90aa882d9ca017a703da78477b381a0246eaf7  152 bytes  1493 us
#   addressbook <= addressbook::upsert          {"user":"alice","first_name":"alice","last_name":"liddell","street":"123 drink me way","city":"wonde...
#   addressbook <= addressbook::notify          {"user":"alice","msg":"alice successfully modified record in addressbook"}
#         alice <= addressbook::notify          {"user":"alice","msg":"alice successfully modified record in addressbook"}
#     abcounter <= abcounter::count             {"user":"alice","type":"modify"}
```
As you can see, the counter was successfully notified. Let's check the table now.
```shell
cleos get table abcounter abcounter counts --lower alice --limit 1
```

```shell
{
  "rows": [{
      "key": "alice",
      "emplaced": 1,
      "modified": 0,
      "erased": 0
    }
  ],
  "more": false
}
```
Test each of the actions and check the counter. There's already a row for alice, so upsert _should_ **modify** the record.
```shell
cleos push action addressbook upsert '["alice", "alice", "liddell", 21,"1 there we go", "wonderland", "amsterdam"]' -p alice@active
```

```shell
executed transaction: c819ffeade670e3b44a40f09cf4462384d6359b5e44dd211f4367ac6d3ccbc70  152 bytes  909 us
#   addressbook <= addressbook::upsert          {"user":"alice","first_name":"alice","last_name":"liddell","street":"1 coming down","city":"normalla...
#   addressbook <= addressbook::notify          {"user":"alice","msg":"alice successfully emplaced record to addressbook"}
>> Notified
#         alice <= addressbook::notify          {"user":"alice","msg":"alice successfully emplaced record to addressbook"}
#     abcounter <= abcounter::count             {"user":"alice","type":"emplace"}
warning: transaction executed locally, but may not be confirmed by the network yet    ]
```
To erase:
```shell
cleos push action addressbook erase '["alice"]' -p alice@active
```

```shell
executed transaction: aa82577cb1efecf7f2871eac062913218385f6ab2597eaf31a4c0d25ef1bd7df  104 bytes  973 us
#   addressbook <= addressbook::erase           {"user":"alice"}
>> Erased
#   addressbook <= addressbook::notify          {"user":"alice","msg":"alice successfully erased record from addressbook"}
>> Notified
#         alice <= addressbook::notify          {"user":"alice","msg":"alice successfully erased record from addressbook"}
#     abcounter <= abcounter::count             {"user":"alice","type":"erase"}
warning: transaction executed locally, but may not be confirmed by the network yet    ]
Toaster:addressbook sandwich$
```
Next, we'll test if we can manipulate the data in `abcounter` contract by calling it directly.
```shell
cleos push action abcounter count '["alice", "erase"]' -p alice@active
```
Checking the table in `abcounter` we'll see the following:
```shell
cleos get table abcounter abcounter counts --lower alice
```

```shell
{
  "rows": [{
      "key": "alice",
      "emplaced": 1,
      "modified": 1,
      "erased": 1
    }
  ],
  "more": false
}
```
Wonderful! Since we require_auth for `name("addressbook")`, only the `addressbook` contract can successfully execute this action, the call by alice to fudge the numbers had no affect on the table.
## Extra Credit: More Verbose Receipts
The following modification sends custom receipts based on changes made, and if no changes are made during a modification, the receipt will reflect this situation.
```cpp
#include <eosio/eosio.hpp>
#include "abcounter.cpp"

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
      addresses.emplace(user, [&]( auto& row ){
       row.key = user;
       row.first_name = first_name;
       row.last_name = last_name;
       row.age = age;
       row.street = street;
       row.city = city;
       row.state = state;
       send_summary(user, " successfully emplaced record to addressbook");
       increment_counter(user, "emplace");
      });
    }
    else {
      std::string changes;
      addresses.modify(iterator, user, [&]( auto& row ) {

        if(row.first_name != first_name) {
          row.first_name = first_name;
          changes += "first name ";
        }

        if(row.last_name != last_name) {
          row.last_name = last_name;
          changes += "last name ";
        }

        if(row.age != age) {
          row.age = age;
          changes += "age ";
        }

        if(row.street != street) {
          row.street = street;
          changes += "street ";
        }

        if(row.city != city) {
          row.city = city;
          changes += "city ";
        }

        if(row.state != state) {
          row.state = state;
          changes += "state ";
        }
      });

      if(!changes.empty()) {
        send_summary(user, " successfully modified record in addressbook. Fields changed: " + changes);
        increment_counter(user, "modify");
      } else {
        send_summary(user, " called upsert, but request resulted in no changes.");
      }
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
    increment_counter(user, "erase");
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

  void increment_counter(name user, std::string type) {

    action counter = action(
      permission_level{get_self(),"active"_n},
      "abcounter"_n,
      "count"_n,
      std::make_tuple(user, type)
    );

    counter.send();
  }

  typedef eosio::multi_index<"people"_n, person, indexed_by<"byage"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>> address_index;
};
```

## What's Next

- [Linking Custom Permissions](80_linking-custom-permission.md): Learn how create a custom permission and how to link the permission to an action of a contract.
