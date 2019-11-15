---
title: "Multi Index Tables Example"
excerpt: ""
---
# Description

In this tutorial we will go through the steps to create and use Multi Index Tables in your smart contract.

# Notes

Multi Index Tables are a way to cache state and/or data in RAM for fast access. Multi index tables support create, read, update and delete (CRUD) operations, something which the blockchain doesn't (it only supports create and read.) 

Multi Index Tables provide a fast to access data store and are a practical way to store data for use in your smart contract. The blockchain records the transactions, but you should use Multi Index Tables to store application data.

They are multi index tables because they support using multiple indexes on the data, the primary index type must be uint64_t and must be unique, but the other, secondary, indexes can have duplicates. You can have up to 16 additional indexes and the field types can be uint64_t, uint128_t, uint256_t, double or long double

If you want to index on a string you will need to convert this to an integer type, and store the results in a field that you then index.

# 1. Create a struct

Create a struct which can be stored in the multi index table, and define getters on the fields you want to index. 

Remember that one of these getters must be named "primary_key()", if you don't have this the compiler ([eosio-cpp](https://github.com/EOSIO/eosio.cdt#eosio-cpp)) will generate an error ... it can't find the field to use as the primary key. 

If you want to have more than one index, (up to 16 are allowed) then define a getter for any field you want to index, at this point the name is less important as you will pass the getter name into the typedef.
[block:code]
{
  "codes": [
    {
      "code": "      struct [[eosio::table]] mystruct \n      {\n         uint64_t     key; \n         uint64_t     secondid;\n         std::string  name; \n         std::string  account; \n\n         uint64_t primary_key() const { return key; } // getter for primary key\n         uint64_t by_id() const {return secondid; } // getter for additional key\n      };",
      "language": "cplusplus"
    }
  ]
}
[/block]
     
Two additional things to note here:

1. The attribute `[[eosio::table]]` is required for the ABI generator, [eosio-cpp](https://github.com/EOSIO/eosio.cdt#eosio-cpp), to recognise that you want to expose this table via the ABI and make it visible outside the smart contract.

2. The struct name is less than 12 characters and all in lower case.

# 2. typedef the multi index table and the define the indexes

Define the multi index table which will use mystruct, tell it what to index, and how to get the data which is being indexed. A primary key will automatically be created, so using the struct above if I want a multi index table with only a primary key I would define it as :

[block:code]
{
  "codes": [
    {
      "code": "typedef eosio::multi_index<name(mystruct), mystruct> datastore;",
      "language": "cplusplus"
    }
  ]
}
[/block]
This defines the multi index passing in the tablename "name(mystruct)" and the struct name "mystruct". name(mystruct) performs a compile conversion of the struct name to a uint64_t and this uint64_t is used to identify data belonging to the multi index table.  

To add additional or secondary indexes use the indexed_by template as a parameter, so the definition becomes
[block:code]
{
  "codes": [
    {
      "code": "typedef eosio::multi_index<name(mystruct), mystruct, indexed_by<name(secondid), const_mem_fun<mystruct, uint64_t, &mystruct::by_id>>> datastore;",
      "language": "cplusplus"
    }
  ]
}
[/block]
where

`indexed_by<name(secondid), const_mem_fun<mystruct, uint64_t, &mystruct::by_id>>`

the parameters 

- the name of the field converted to an integer, name(secondid)
- a user defined key extractor, const_mem_fun<mystruct, uint64_t, &mystruct::by_id>

To have three indexes
[block:code]
{
  "codes": [
    {
      "code": "      struct [[eosio::table]] mystruct \n      {\n         uint64_t     key; \n         uint64_t     secondid;\n         uint64_t\t\t\tanotherid;\n         std::string  name; \n         std::string  account; \n\n         uint64_t primary_key() const { return key; }\n         uint64_t by_id() const {return secondid; }\n         uint64_t by_anotherid() const {return anotherid; }\n      };\n      \ntypedef eosio::multi_index<name(mystruct), mystruct, indexed_by<name(secondid), const_mem_fun<mystruct, uint64_t, &mystruct::by_id>>, indexed_by<name(anotherid), const_mem_fun<mystruct, uint64_t, &mystruct::by_anotherid>>> datastore;\n      \n      \n      ",
      "language": "cplusplus"
    }
  ]
}
[/block]
and so on.

An important thing to note here is that struct name matches the table name, and that the the names that will appear in the abi file follow the rules (12 characters and all in lower case.) If they don't then the tables are not visible via the abi (you can get around this by editing the abi file.)

# 3. create local variables which are of the defined type

```
      // local instances of the multi indexes
      pollstable _polls;
      votes _votes;
```

Now I have defined a multi index table with two indexes and I can use this in my smart contract.

An example working smart contract using two multi index tables is shown below. Here you can see how to iterate over the tables and how to use two tables in the same contract.
[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n\nusing namespace eosio;\n\nclass youvote : public contract\n{\n  public:\n      youvote(eosio::name s):contract(s), _polls(s, s), _votes(s, s)\n      {}\n\n      // public methods exposed via the ABI\n      // on pollsTable\n\n      [[eosio::action]]\n      void version()\n      {\n          print(\"YouVote version  0.01\"); \n\n      };\n      \n      [[eosio::action]]\n      void addpoll(eosio::name s, std::string pollName)\n      {\n          //require_auth(s);\n\n          print(\"Add poll \", pollName); \n              \n          // update the table to include a new poll\n          _polls.emplace(get_self(), [&](auto& p)\n                                      {\n                                        p.key = _polls.available_primary_key();\n                                        p.pollId = _polls.available_primary_key();\n                                        p.pollName = pollName;\n                                        p.pollStatus = 0;\n                                        p.option = \"\";\n                                        p.count = 0;\n                                      });\n      };\n\n\n      [[eosio::action]]\n      void rmpoll(eosio::name s, std::string pollName)\n      {\n          //require_auth(s);\n\n          print(\"Remove poll \", pollName); \n              \n          std::vector<uint64_t> keysForDeletion;\n          // find items which are for the named poll\n          for(auto& item : _polls)\n          {\n              if (item.pollName == pollName)\n              {\n                  keysForDeletion.push_back(item.key);   \n              }\n          }\n          \n          // now delete each item for that poll\n          for (uint64_t key : keysForDeletion)\n          {\n              print(\"remove from _polls \", key);\n              auto itr = _polls.find(key);\n              if (itr != _polls.end())\n              {\n                _polls.erase(itr);\n              }\n          }\n\n\n          // add remove votes ... don't need it the actions are permanently stored on the block chain\n\n          std::vector<uint64_t> keysForDeletionFromVotes;\n          // find items which are for the named poll\n          for(auto& item : _votes)\n          {\n              if (item.pollName == pollName)\n              {\n                  keysForDeletionFromVotes.push_back(item.key);   \n              }\n          }\n          \n          // now delete each item for that poll\n          for (uint64_t key : keysForDeletionFromVotes)\n          {\n              print(\"remove from _votes \", key);\n              auto itr = _votes.find(key);\n              if (itr != _votes.end())\n              {\n                _votes.erase(itr);\n              }\n          }\n\n\n      };\n\n      [[eosio::action]]\n      void status(std::string pollName)\n      {\n          print(\"Change poll status \", pollName);\n\n          std::vector<uint64_t> keysForModify;\n          // find items which are for the named poll\n          for(auto& item : _polls)\n          {\n              if (item.pollName == pollName)\n              {\n                  keysForModify.push_back(item.key);   \n              }\n          }\n          \n          // now get each item and modify the status\n          for (uint64_t key : keysForModify)\n          {\n\n            print(\"modify _polls status\", key);\n            auto itr = _polls.find(key);\n            if (itr != _polls.end())\n            {\n              _polls.modify(itr, get_self(), [&](auto& p)\n                                              {\n                                                p.pollStatus = p.pollStatus + 1;\n                                              });\n            }\n          }\n      };\n\n      [[eosio::action]]\n      void statusreset(std::string pollName)\n      {\n          print(\"Reset poll status \", pollName); \n              \n          std::vector<uint64_t> keysForModify;\n          // find all poll items\n          for(auto& item : _polls)\n          {\n              if (item.pollName == pollName)\n              {\n                  keysForModify.push_back(item.key);   \n              }\n          }\n          \n          // update the status in each poll item\n          for (uint64_t key : keysForModify)\n          {\n              print(\"modify _polls status\", key);\n              auto itr = _polls.find(key);\n              if (itr != _polls.end())\n              {\n                _polls.modify(itr, get_self(), [&](auto& p)\n                                                {\n                                                  p.pollStatus = 0;\n                                                });\n              }\n          }\n      };\n\n\n      [[eosio::action]]\n      void addpollopt(std::string pollName, std::string option)\n      {\n          print(\"Add poll option \", pollName, \"option \", option); \n\n          // find the pollId, from _polls, use this to update the _polls with a new option\n          for(auto& item : _polls)\n          {\n              if (item.pollName == pollName)\n              {\n                    // can only add if the poll is not started or finished\n                    if(item.pollStatus == 0)\n                    {\n                        _polls.emplace(get_self(), [&](auto& p)\n                                          {\n                                            p.key = _polls.available_primary_key();\n                                            p.pollId = item.pollId;\n                                            p.pollName = item.pollName;\n                                            p.pollStatus = 0;\n                                            p.option = option;\n                                            p.count = 0;\n                                          });\n                    }\n                    else\n                    {\n                        print(\"Can not add poll option \", pollName, \"option \", option, \" Poll has started or is finished.\");\n                    }\n\n                    break; // so you only add it once\n              }\n          }\n      };\n\n      [[eosio::action]]\n      void rmpollopt(std::string pollName, std::string option)\n      {\n          print(\"Remove poll option \", pollName, \"option \", option); \n              \n          std::vector<uint64_t> keysForDeletion;\n          // find and remove the named poll\n          for(auto& item : _polls)\n          {\n              if (item.pollName == pollName)\n              {\n                  keysForDeletion.push_back(item.key);   \n              }\n          }\n          \n          \n          for (uint64_t key : keysForDeletion)\n          {\n              print(\"remove from _polls \", key);\n              auto itr = _polls.find(key);\n              if (itr != _polls.end())\n              {\n                  if (itr->option == option)\n                  {\n                      _polls.erase(itr);\n                  }\n              }\n          }\n      };\n\n\n      [[eosio::abi]]\n      void vote(std::string pollName, std::string option, std::string accountName)\n      {\n          print(\"vote for \", option, \" in poll \", pollName, \" by \", accountName); \n\n          // is the poll open\n          for(auto& item : _polls)\n          {\n              if (item.pollName == pollName)\n              {\n                  if (item.pollStatus != 1)\n                  {\n                      print(\"Poll \",pollName,  \" is not open\");\n                      return;\n                  }\n\n                  break; // only need to check status once\n              }\n          }\n\n          // has account name already voted?  \n          for(auto& vote : _votes)\n          {\n              if (vote.pollName == pollName && vote.account == accountName)\n              {\n                  print(accountName, \" has already voted in poll \", pollName);\n                  //eosio_assert(true, \"Already Voted\");\n                  return;\n              }\n          }\n\n          uint64_t pollId =99999; // get the pollId for the _votes table\n\n          // find the poll and the option and increment the count\n          for(auto& item : _polls)\n          {\n              if (item.pollName == pollName && item.option == option)\n              {\n                  pollId = item.pollId; // for recording vote in this poll\n\n                  _polls.modify(item, get_self(), [&](auto& p)\n                                                {\n                                                    p.count = p.count + 1;\n                                                });\n              }\n          }\n\n          // record that accountName has voted\n          _votes.emplace(get_self(), [&](auto& pv)\n                                      {\n                                        pv.key = _votes.available_primary_key();\n                                        pv.pollId = pollId;\n                                        pv.pollName = pollName;\n                                        pv.account = accountName;\n                                      });        \n      };\n\n  private:    \n\n    // create the multi index tables to store the data\n      struct [[eosio::table]] poll \n      {\n        uint64_t      key; // primary key\n        uint64_t      pollId; // second key, non-unique, this table will have dup rows for each poll because of option\n        std::string   pollName; // name of poll\n        uint8_t      pollStatus =0; // staus where 0 = closed, 1 = open, 2 = finished\n        std::string  option; // the item you can vote for\n        uint32_t    count =0; // the number of votes for each itme -- this to be pulled out to separte table.\n\n        uint64_t primary_key() const { return key; }\n        uint64_t by_pollId() const {return pollId; }\n      };\n      typedef eosio::multi_index<N(poll), poll, indexed_by<N(pollId), const_mem_fun<poll, uint64_t, &poll::by_pollId>>> pollstable;\n\n      struct [[eosio::table]] pollvotes \n      {\n         uint64_t     key; \n         uint64_t     pollId;\n         std::string  pollName; // name of poll\n         std::string  account; //this account has voted, use this to make sure noone votes > 1\n\n         uint64_t primary_key() const { return key; }\n         uint64_t by_pollId() const {return pollId; }\n      };\n      typedef eosio::multi_index<name(pollvotes), pollvotes, indexed_by<name(pollId), const_mem_fun<pollvotes, uint64_t, &pollvotes::by_pollId>>> votes;\n\n      // local instances of the multi indexes\n      pollstable _polls;\n      votes _votes;\n};\n\nEOSIO_DISPATCH( youvote, (version)(addpoll)(rmpoll)(status)(statusreset)(addpollopt)(rmpollopt)(vote))\n",
      "language": "cplusplus"
    }
  ]
}
[/block]
Note the EOSIO_ABI call, this exposes the functions via the abi, it's important the function names match the abi function name rules.