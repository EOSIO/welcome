---
title: "Multi Index Table Usage Guide"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Below is a usage guide for the multi index table.
[block:callout]
{
  "type": "info",
  "body": "In the interest of being thorough and providing clarity, sections of the final .cpp file will be broken out and discussed in further detail. Note that the complete .cpp file can be found at the bottom of this page."
}
[/block]

[block:api-header]
{
  "title": "Glossary"
}
[/block]
- `code` - Refers to an `account_name` where a contract has been published.
- `scope` - An `account_name` that the data in question belongs to. 
- `table_name` - The name of the table that is stored in memory. 
[block:api-header]
{
  "title": "Code Break Down"
}
[/block]
##Struct to be stored##
The data to be stored in the multi index table is the `limit_order` struct. The functions `primary_key()`, `get_expiration()`, `get_price()` are used to return the table. The returned table will be sorted based on which function was called.
[block:code]
{
  "codes": [
    {
      "code": "struct limit_order {\n  uint64_t     id;\n  uint128_t    price;\n  uint64_t     expiration;\n  account_name owner;\n\n  auto primary_key() const { return id; }\n  uint64_t get_expiration() const { return expiration; }\n  uint128_t get_price() const { return price; }\n\n  EOSLIB_SERIALIZE( limit_order, ( id )( price )( expiration )( owner ) )\n};",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Different from other RDBs, primary key cannot be defined from multiple columns. Only one columns can be a primary key. If you want to implement it, use secondary index and implement the logic manually."
}
[/block]
##Creating the multi index table##
[block:code]
{
  "codes": [
    {
      "code": "auto payer = ilm.get_account();\n...",
      "language": "cplusplus"
    }
  ]
}
[/block]
`payer` is the variable that holds the account who will be "billed" for adding elements to the multi index table and modifying elements already in the multi index table.


[block:code]
{
  "codes": [
    {
      "code": "...\neosio::multi_index< N( orders ), limit_order, \n...",
      "language": "cplusplus"
    }
  ]
}
[/block]
`N( orders )` is the name of the multi index table and `limit_orders` is the data to be stored in the table.
[block:code]
{
  "codes": [
    {
      "code": "...  \nindexed_by< N( byexp ), const_mem_fun< limit_order, uint64_t, \n&limit_order::get_expiration> >,\n...",
      "language": "cplusplus"
    }
  ]
}
[/block]
`indexed_by< N( byexp ), const_mem_fun< limit_order, uint64_t, &limit_order::get_expiration> >` is the definition of a way the `orders` multi index table can be indexed. `N( byexp )` is the name of this index. The `const_mem_fun` indicates the data type being retrieved, `limit_order`, the type of variable being sorted by, `uint64_t`, and the function that will be used get the variable, `get_expiration`.
[block:code]
{
  "codes": [
    {
      "code": "...\n  indexed_by< N( byprice ), const_mem_fun< limit_order, uint128_t, &limit_order::get_price> >\n...",
      "language": "cplusplus"
    }
  ]
}
[/block]
`indexed_by< N( byprice ), const_mem_fun< limit_order, uint128_t, &limit_order::get_price> >` is the definition of a way the `orders` multi index table can be indexed. `N( byprice )` is the name of this index. The `const_mem_fun` indicates the data type being retrieved, `limit_order`, the type of variable being sorted by, `uint128_t`, and the function that will be used get the variable, `get_price`.
[block:code]
{
  "codes": [
    {
      "code": "orders( N( limitorders ), N( limitorders )",
      "language": "cplusplus"
    }
  ]
}
[/block]
`orders` is the multi index table.
[block:code]
{
  "codes": [
    {
      "code": "auto payer = ilm.get_account();\n\nprint(\"Creating multi index table 'orders'.\\n\");\neosio::multi_index< N( orders ), limit_order, \n  indexed_by< N( byexp ),   const_mem_fun< limit_order, uint64_t, &limit_order::get_expiration> >,\n  indexed_by< N( byprice ), const_mem_fun< limit_order, uint128_t, &limit_order::get_price> >\n    > orders( N( limitorders ), N( limitorders ) );",
      "language": "cplusplus"
    }
  ]
}
[/block]
##Adding to the multi index table##
Below, two `limit_order`s are added to the `orders` table. Note that `payer` is the account that is being "billed" for the modification to the `orders` table.
[block:code]
{
  "codes": [
    {
      "code": "orders.emplace( payer, [&]( auto& o ) {\n  o.id = 1;\n  o.expiration = 300;\n  o.owner = N(dan);\n});\n\nauto order2 = orders.emplace( payer, [&]( auto& o ) {\n  o.id = 2;\n  o.expiration = 200;\n  o.owner = N(thomas);\n});",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "If you want to use auto-increment feature, use [available_primary_key()](https://developers.eos.io/eosio-cpp/v1.2.0/reference#available_primary_key)."
}
[/block]
##Sorted by primary key##
By default, the `orders` table is sorted by primary key.
[block:code]
{
  "codes": [
    {
      "code": "print(\"Items sorted by primary key:\\n\");\nfor( const auto& item : orders ) {\n  print(\" ID=\", item.id, \", expiration=\", item.expiration, \", owner=\", name{item.owner}, \"\\n\");\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
##Sorted by secondary index - expiration##
The `orders` table gets sorted by expiration and assigned to `expidx`.
[block:code]
{
  "codes": [
    {
      "code": "auto expidx = orders.get_index<N(byexp)>();\n\nprint(\"Items sorted by expiration:\\n\");\nfor( const auto& item : expidx ) {\n  print(\" ID=\", item.id, \", expiration=\", item.expiration, \", owner=\", name{item.owner}, \"\\n\");\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
##Sorted by secondary index - price##
The `orders` table gets sorted by price and assigned to `pridx`.
[block:code]
{
  "codes": [
    {
      "code": "auto pridx = orders.get_index<N(byprice)>();\n\nprint(\"Items sorted by price:\\n\");\nfor( const auto& item : pridx ) {\n  print(\" ID=\", item.id, \", expiration=\", item.expiration, \", owner=\", name{item.owner}, \"\\n\");\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
##Modify an entry##
Below, the entry with "ID=2" gets modified. Note that `payer` is the account that is being "billed" for the modification to the `orders` table.
[block:code]
{
  "codes": [
    {
      "code": "print(\"Modifying expiration of order with ID=2 to 400.\\n\");\norders.modify( order2, payer, [&]( auto& o ) {\n  o.expiration = 400;\n});",
      "language": "cplusplus"
    }
  ]
}
[/block]
##Getting the lower bound##
[block:code]
{
  "codes": [
    {
      "code": "auto lower = expidx.lower_bound(100);\n\nprint(\"First order with an expiration of at least 100 has ID=\", lower->id, \" and expiration=\", lower->get_expiration(), \"\\n\");",
      "language": "cplusplus"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Complete .cpp file"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "#include <eosiolib/eosio.hpp>\n#include <eosiolib/dispatcher.hpp>\n#include <eosiolib/multi_index.hpp>\n\nusing namespace eosio;\n\nnamespace limit_order_table {\n\n    struct limit_order {\n        uint64_t     id;\n        uint128_t    price;\n        uint64_t     expiration;\n        account_name owner;\n\n        auto primary_key() const { return id; }\n        uint64_t get_expiration() const { return expiration; }\n        uint128_t get_price() const { return price; }\n\n        EOSLIB_SERIALIZE( limit_order, ( id )( price )( expiration )( owner ) )\n    };\n\n    class limit_order_table {\n        public:\n\n        ACTION( N( limitorders ), issue_limit_order ) {\n            EOSLIB_SERIALIZE( issue_limit_order )\n        };\n\n        static void on( const issue_limit_order& ilm ) {\n            auto payer = ilm.get_account();\n\n            print(\"Creating multi index table 'orders'.\\n\");\n            eosio::multi_index< N( orders ), limit_order, \n                indexed_by< N( byexp ),   const_mem_fun< limit_order, uint64_t, &limit_order::get_expiration> >,\n                indexed_by< N( byprice ), const_mem_fun< limit_order, uint128_t, &limit_order::get_price> >\n                > orders( N( limitorders ), N( limitorders ) );\n\n            orders.emplace( payer, [&]( auto& o ) {\n                o.id = 1;\n                o.expiration = 300;\n                o.owner = N(dan);\n            });\n\n            auto order2 = orders.emplace( payer, [&]( auto& o ) {\n                o.id = 2;\n                o.expiration = 200;\n                o.owner = N(thomas);\n            });\n\n            print(\"Items sorted by primary key:\\n\");\n            for( const auto& item : orders ) {\n                print(\" ID=\", item.id, \", expiration=\", item.expiration, \", owner=\", name{item.owner}, \"\\n\");\n            }\n\n            auto expidx = orders.get_index<N(byexp)>();\n\n            print(\"Items sorted by expiration:\\n\");\n            for( const auto& item : expidx ) {\n                print(\" ID=\", item.id, \", expiration=\", item.expiration, \", owner=\", name{item.owner}, \"\\n\");\n            }\n\n            auto pridx = orders.get_index<N(byprice)>();\n\n            print(\"Items sorted by price:\\n\");\n            for( const auto& item : pridx ) {\n                print(\" ID=\", item.id, \", expiration=\", item.expiration, \", owner=\", name{item.owner}, \"\\n\");\n            }\n\n            print(\"Modifying expiration of order with ID=2 to 400.\\n\");\n            orders.modify( order2, payer, [&]( auto& o ) {\n                o.expiration = 400;\n            });\n\n            auto lower = expidx.lower_bound(100);\n\n            print(\"First order with an expiration of at least 100 has ID=\", lower->id, \" and expiration=\", lower->get_expiration(), \"\\n\");\n   };\n\n} /// limit_order_table\n\nnamespace limit_order_table {\n   extern \"C\" {\n      /// The apply method implements the dispatch of events to this contract\n      void apply( uint64_t code, uint64_t action ) {\n         require_auth( code );\n         eosio_assert( eosio::dispatch< limit_order_table, limit_order_table::issue_limit_order >( code, action ), \"Could not dispatch\" );\n      }\n   }\n}",
      "language": "cplusplus",
      "name": null
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Deleting a Table"
}
[/block]
Tables cannot be directly deleted, however, a table will delete itself automatically after all rows have been deleted.
[block:api-header]
{
  "title": "Modifying a Table"
}
[/block]
Table cannot be directly modified. If you want to do this, follow this step.

#### 1. Create another table
[block:code]
{
  "codes": [
    {
      "code": "    struct limit_order { // Old table\n        uint64_t     id;\n        uint128_t    price;\n        uint64_t     expiration;\n        account_name owner;\n\n        auto primary_key() const { return id; }\n    };\n    typedef eosio::multi_index< N( orders ), limit_order> _limit_order;\n\n    struct limit_order2 { // New table\n        uint64_t     id;\n        uint128_t    price;\n        uint64_t     expiration;\n        account_name owner;\n        asset        byeos; // added column\n\n        auto primary_key() const { return id; }       \n    };\n    typedef eosio::multi_index< N( orders2 ), limit_order2> _limit_order2;",
      "language": "cplusplus"
    }
  ]
}
[/block]
#### 2. Implement migration function
[block:code]
{
  "codes": [
    {
      "code": "void sth::migrate(){\n    require_auth(_self);\n  \n    _limit_order old_table(_self, _self);\n    _limit_order2 new_table(_self, _self);\n    auto itr = old_table.begin();\n    while ( itr != old_table.end() ){\n      new_table.emplace( _self, [&]( auto& o ) {\n        o.id = itr.id;\n        o.price = itr.price;\n        o.expiration = itr.expiration;\n        o.owner = itr.owner;\n        o.byeos = itr.price / 3; // implement yourself\n      });\n      \n      itr++;\n    }\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
#### 3. After migration, you may delete records of the old table