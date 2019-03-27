---
title: "2.7 Inline Action to External Contract"
excerpt: ""
---
Previously, an inline action was sent to an action that was defined within the same contract that was calling the inline action. In this part of the tutorial, the contract will be configured to send an inline action to an external contract. This contract has been kept extremely simple to avoid bloating it with irrelevant logic. The contract that will be deployed in this part of the series counts actions written by the `addressbook` contract. This contract has very little real-world use, but will demonstrate inline action calls to a specific external contract, and limit the ability to call the action on this contract from a single account. In this case, the `addressbook` contract. 
[block:api-header]
{
  "title": "Step 1: The Addressbook Counter Contract"
}
[/block]
Navigate to `CONTRACTS_DIR` if not already there, create a directory called `abcounter` and then create a `abcounter.cpp` file
[block:code]
{
  "codes": [
    {
      "code": "cd CONTRACTS_DIR\nmkdir abcounter\ntouch abcounter.cpp",
      "language": "shell"
    }
  ]
}
[/block]
Open and the `abcounter.cpp` file in your favorite editor and paste the following code into the file. This contract is very basic, and for the most part does not cover much that we haven't already covered up until this point. There is one exception, and it is covered in full below the provided code. 
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n\nusing namespace eosio;\n\nclass [[eosio::contract]] abcounter : public eosio::contract {\n  public:\n    using contract::contract;\n\n    abcounter(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}\n\n    [[eosio::action]]\n    void count(name user, std::string type) {\n      require_auth( name(\"addressbook\"));\n      count_index counts(name(_code), _code.value);\n      auto iterator = counts.find(user.value);\n      \n      if (iterator == counts.end()) {\n        counts.emplace(\"addressbook\"_n, [&]( auto& row ) {\n          row.key = user;\n          row.emplaced = (type == \"emplace\") ? 1 : 0;\n          row.modified = (type == \"modify\") ? 1 : 0;\n          row.erased = (type == \"erase\") ? 1 : 0;\n        });\n      }\n      else {\n        counts.modify(iterator, \"addressbook\"_n, [&]( auto& row ) {\n          if(type == \"emplace\") { row.emplaced += 1; }\n          if(type == \"modify\") { row.modified += 1; }\n          if(type == \"erase\") { row.erased += 1; }\n        });\n      }\n    }\n\n  private:\n    struct [[eosio::table]] counter {\n      name key;\n      uint64_t emplaced;\n      uint64_t modified;\n      uint64_t erased;\n      uint64_t primary_key() const { return key.value; }\n    };\n\n    using count_index = eosio::multi_index<\"counts\"_n, counter>;\n};\n\nEOSIO_DISPATCH( abcounter, (count));\n",
      "language": "cplusplus"
    }
  ]
}
[/block]
The only new concept in the code above, is that we are explicitly restricting calls to the one action to a **specific account** in this contract using [require_auth](https://eosio.github.io/eosio.cdt/group__action.html#function-requireauth) to the `addressbook` contract, as seen below. 
[block:code]
{
  "codes": [
    {
      "code": "//Only the addressbook account/contract can authorize this command. \nrequire_auth( name(\"addressbook\"));",
      "language": "cplusplus"
    }
  ]
}
[/block]
Previously, a dynamic value was used with `require_auth`
[block:api-header]
{
  "title": "Step 2: Create Account for abcounter Contract"
}
[/block]
Open your terminal and execute the following command to create the **abcounter** user.
[block:code]
{
  "codes": [
    {
      "code": "cleos create account eosio abcounter YOUR_PUBLIC_KEY",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 3: Compile and Deploy"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "eosio-cpp -o abcounter.wasm abcounter.cpp --abigen",
      "language": "shell"
    }
  ]
}
[/block]
Finally, deploy the `abcounter` contract.
[block:code]
{
  "codes": [
    {
      "code": "cleos set contract abcounter CONTRACTS_DIR/abcounter",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 4: Modify addressbook contract to send inline-action to abcounter"
}
[/block]
Navigate to your addressbook directory now.
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
Open the `addressbook.cpp` file in your favorite editor if not already open. 

In the last part of this series, we went over inline actions to our own contract. This time, send an inline action to another contract, our new `abcounter` contract. 

Create another helper called `increment_counter` in the `private` region of your contract.
[block:code]
{
  "codes": [
    {
      "code": "void increment_counter(name user, std::string type) {\n    \n  action counter = action(\n    permission_level{get_self(),\"active\"_n},\n    \"abcounter\"_n,\n    \"count\"_n,\n    std::make_tuple(user, type)\n  );\n\n  counter.send();\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
- For the permission, `get_self()` returns the current `addressbook` contract. The `active` permission is used.
- The `abcounter` contract account_name
- The action to call
- The data, `name user` and `string type`

Now, add the following calls to the helpers in their respective action scopes. 
[block:code]
{
  "codes": [
    {
      "code": "//Emplace\nincrement_counter(user, \"emplace\");\n//Modify\nincrement_counter(user, \"modify\");\n//Erase\nincrement_counter(user, \"erase\");",
      "language": "text"
    }
  ]
}
[/block]
Now your `addressbook.cpp` contract should look like this.
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\nclass [[eosio::contract]] addressbook : public eosio::contract {\n\npublic:\n  using contract::contract;\n  \n  addressbook(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}\n\n  [[eosio::action]]\n  void upsert(name user, std::string first_name, std::string last_name, uint64_t age, std::string street, std::string city, std::string state) {\n    require_auth(user);\n    address_index addresses(_code, _code.value);\n    auto iterator = addresses.find(user.value);\n    if( iterator == addresses.end() )\n    {\n      addresses.emplace(user, [&]( auto& row ) {\n       row.key = user;\n       row.first_name = first_name;\n       row.last_name = last_name;\n       row.age = age;\n       row.street = street;\n       row.city = city;\n       row.state = state;\n\n       send_summary(user, \" successfully emplaced record to addressbook\");\n       increment_counter(user, \"emplace\");\n      });\n    }\n    else {\n      std::string changes;\n      addresses.modify(iterator, user, [&]( auto& row ) {\n        row.key = user;\n        row.first_name = first_name;\n        row.last_name = last_name;\n        row.age = age;\n        row.street = street;\n        row.city = city;\n        row.state = state;\n\n        send_summary(user, \" successfully modified record to addressbook\");\n        increment_counter(user, \"modify\");\n      });\n\n    }\n  }\n\n  [[eosio::action]]\n  void erase(name user) {\n    require_auth(user);\n\n    address_index addresses(_code, _code.value);\n    auto iterator = addresses.find(user.value);\n    eosio_assert(iterator != addresses.end(), \"Record does not exist\");\n    addresses.erase(iterator);\n    send_summary(user, \" successfully erased record from addressbook\");\n    increment_counter(user, \"erase\");\n  }\n\n  [[eosio::action]]\n  void notify(name user, std::string msg) {\n    require_auth(get_self());\n    require_recipient(user);\n  }\n\nprivate:\n  struct [[eosio::table]] person {\n    name key;\n    std::string first_name;\n    std::string last_name;\n    uint64_t age;\n    std::string street;\n    std::string city;\n    std::string state;\n  \n    uint64_t primary_key() const { return key.value; }\n    uint64_t get_secondary_1() const { return age;}\n  \n  };\n\n  void send_summary(name user, std::string message) {\n    action(\n      permission_level{get_self(),\"active\"_n},\n      get_self(),\n      \"notify\"_n,\n      std::make_tuple(user, name{user}.to_string() + message)\n    ).send();\n  };\n\n  void increment_counter(name user, std::string type) {\n    \n    action counter = action(\n      permission_level{get_self(),\"active\"_n},\n      \"abcounter\"_n,\n      \"count\"_n,\n      std::make_tuple(user, type)\n    );\n\n    counter.send();\n  }\n\n  typedef eosio::multi_index<\"people\"_n, person, \n    indexed_by<\"byage\"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>\n  > address_index;\n  \n};\n\nEOSIO_DISPATCH( addressbook, (upsert)(notify)(erase))",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 5: Recompile and redeploy the addressbook contract"
}
[/block]
Recompile the `addressbook.cpp` contract, we don't need to regenerate the ABI, because none of our changes have affected the ABI.
[block:code]
{
  "codes": [
    {
      "code": "eosio-cpp -o addressbook.wasm addressbook.cpp",
      "language": "shell"
    }
  ]
}
[/block]
Redeploy the contract
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
  "title": "Step 6: Test It."
}
[/block]
Now that we have the `abcounter` deployed and `addressbook` redeployed, we're ready for some testing.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action addressbook upsert '[\"alice\", \"alice\", \"liddell\", 19, \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p alice@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: cc46f20da7fc431124e418ecff90aa882d9ca017a703da78477b381a0246eaf7  152 bytes  1493 us\n#   addressbook <= addressbook::upsert          {\"user\":\"alice\",\"first_name\":\"alice\",\"last_name\":\"liddell\",\"street\":\"123 drink me way\",\"city\":\"wonde...\n#   addressbook <= addressbook::notify          {\"user\":\"alice\",\"msg\":\"alice successfully modified record in addressbook\"}\n#         alice <= addressbook::notify          {\"user\":\"alice\",\"msg\":\"alice successfully modified record in addressbook\"}\n#     abcounter <= abcounter::count             {\"user\":\"alice\",\"type\":\"modify\"}",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
As you can see, the counter was successfully notified. Let's check the table now.
[block:code]
{
  "codes": [
    {
      "code": "cleos get table abcounter abcounter counts --lower alice --limit 1",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"rows\": [{\n      \"key\": \"alice\",\n      \"emplaced\": 1,\n      \"modified\": 0,\n      \"erased\": 0\n    }\n  ],\n  \"more\": false\n}",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Now let's test the remaining actions, just in case, we know there's a row for alice already, so upsert will *modify* the record.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action addressbook upsert '[\"alice\", \"alice\", \"liddell\", 21，\"1 there we go\", \"wonderland\", \"amsterdam\"]' -p alice@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: c819ffeade670e3b44a40f09cf4462384d6359b5e44dd211f4367ac6d3ccbc70  152 bytes  909 us\n#   addressbook <= addressbook::upsert          {\"user\":\"alice\",\"first_name\":\"alice\",\"last_name\":\"liddell\",\"street\":\"1 coming down\",\"city\":\"normalla...\n#   addressbook <= addressbook::notify          {\"user\":\"alice\",\"msg\":\"alice successfully emplaced record to addressbook\"}\n>> Notified\n#         alice <= addressbook::notify          {\"user\":\"alice\",\"msg\":\"alice successfully emplaced record to addressbook\"}\n#     abcounter <= abcounter::count             {\"user\":\"alice\",\"type\":\"emplace\"}\nwarning: transaction executed locally, but may not be confirmed by the network yet    ]",
      "language": "shell",
      "name": null
    }
  ]
}
[/block]
To erase:

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
      "code": "executed transaction: aa82577cb1efecf7f2871eac062913218385f6ab2597eaf31a4c0d25ef1bd7df  104 bytes  973 us\n#   addressbook <= addressbook::erase           {\"user\":\"alice\"}\n>> Erased\n#   addressbook <= addressbook::notify          {\"user\":\"alice\",\"msg\":\"alice successfully erased record from addressbook\"}\n>> Notified\n#         alice <= addressbook::notify          {\"user\":\"alice\",\"msg\":\"alice successfully erased record from addressbook\"}\n#     abcounter <= abcounter::count             {\"user\":\"alice\",\"type\":\"erase\"}\nwarning: transaction executed locally, but may not be confirmed by the network yet    ]\nToaster:addressbook sandwich$",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Next, we'll test if we can manipulate the data in `abcounter` contract by calling it directly.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action abcounter count '[\"alice\", \"erase\"]' -p alice@active",
      "language": "shell"
    }
  ]
}
[/block]
Checking the table in `abcounter` we'll see the following:
[block:code]
{
  "codes": [
    {
      "code": "cleos get table abcounter abcounter counts --lower alice --limit",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"rows\": [{\n      \"key\": \"alice\",\n      \"emplaced\": 1,\n      \"modified\": 1,\n      \"erased\": 1\n    }\n  ],\n  \"more\": false\n}",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Wonderful! Since we require_auth for `name(addressbook)`, only `addressbook` contract can successfully execute this action, the call by alice to fudge the numbers had no affect on the table.
[block:api-header]
{
  "title": "Extra Credit: More Verbose Receipts"
}
[/block]
The following modification sends custom receipts based on changes made, and if no changes are made during a modification, the receipt will reflect this situation. This code works, but is inefficient as written. Can you optimize it?
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/print.hpp>\n\nusing namespace eosio;\n\n\nclass [[eosio::contract]] addressbook : public eosio::contract {\n\npublic:\n  using contract::contract;\n  \n  addressbook(name receiver, name code,  datastream<const char*> ds): contract(receiver, code, ds) {}\n\n  [[eosio::action]]\n  void upsert(name user, std::string first_name, std::string last_name, uint64_t age, std::string street, std::string city, std::string state) {\n    require_auth(user);\n\n    address_index addresses(_code, _code.value);\n\n    auto iterator = addresses.find(user.value);\n    if( iterator == addresses.end() )\n    {\n      addresses.emplace(user, [&]( auto& row ){\n       row.key = user;\n       row.first_name = first_name;\n       row.last_name = last_name;\n       row.age = age;\n       row.street = street;\n       row.city = city;\n       row.state = state;\n       send_summary(user, \" successfully emplaced record to addressbook\");\n       increment_counter(user, \"emplace\");\n      });\n    }\n    else {\n      std::string changes;\n      addresses.modify(iterator, user, [&]( auto& row ) {\n        \n        if(row.first_name != first_name) {\n          row.first_name = first_name;\n          changes += \"first name \";\n        }\n        \n        if(row.last_name != last_name) {\n          row.last_name = last_name;\n          changes += \"last name \";\n        }\n\n        if(row.age != age) {\n          row.age = age;\n          changes += \"age \";\n        }\n\n        if(row.street != street) {\n          row.street = street;\n          changes += \"street \";\n        }\n        \n        if(row.city != city) {\n          row.city = city;\n          changes += \"city \";\n        }\n        \n        if(row.state != state) {\n          row.state = state;\n          changes += \"state \";\n        }\n      });\n\n      if(changes.length() > 0) {\n        send_summary(user, \" successfully modified record in addressbook. Fields changed: \" + changes);\n        increment_counter(user, \"modify\");\n      } else {\n        send_summary(user, \" called upsert, but request resulted in no changes.\");\n      }\n    }\n  }\n\n  [[eosio::action]]\n  void erase(name user) {\n    require_auth(user);\n    address_index addresses(_code, _code.value);\n    auto iterator = addresses.find(user.value);\n    eosio_assert(iterator != addresses.end(), \"Record does not exist\");\n    addresses.erase(iterator);\n    send_summary(user, \" successfully erased record from addressbook\");\n    increment_counter(user, \"erase\");\n  }\n\n  [[eosio::action]]\n  void notify(name user, std::string msg) {\n    require_auth(get_self());\n    require_recipient(user);\n  }\n\nprivate:\n  \n  struct [[eosio::table]] person {\n    name key;\n    std::string first_name;\n    std::string last_name;\n    uint64_t age;\n    std::string street;\n    std::string city;\n    std::string state;\n    uint64_t primary_key() const { return key.value; }\n    uint64_t get_secondary_1() const { return age;}\n  };\n\n  void send_summary(name user, std::string message) {\n    action(\n      permission_level{get_self(),\"active\"_n},\n      get_self(),\n      \"notify\"_n,\n      std::make_tuple(user, name{user}.to_string() + message)\n    ).send();\n  };\n\n  void increment_counter(name user, std::string type) {\n    \n    action counter = action(\n      permission_level{get_self(),\"active\"_n},\n      \"abcounter\"_n,\n      \"count\"_n,\n      std::make_tuple(user, type)\n    );\n\n    counter.send();\n  }\n\n  typedef eosio::multi_index<\"people\"_n, person, \n    indexed_by<\"byage\"_n, const_mem_fun<person, uint64_t, &person::get_secondary_1>>\n  > address_index;\n};\n\nEOSIO_DISPATCH( addressbook, (upsert)(notify)(erase))",
      "language": "cplusplus"
    }
  ]
}
[/block]