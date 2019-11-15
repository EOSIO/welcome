---
title: "Multi-Index"
excerpt: "Defines EOSIO Multi Index Table."
---
EOSIO Multi-Index API provides a C++ interface to the EOSIO database. It is patterned after Boost Multi Index Container. EOSIO Multi-Index table requires exactly a uint64_t primary key. For the table to be able to retrieve the primary key, the object stored inside the table is required to have a const member function called primary_key() that returns uint64_t. EOSIO Multi-Index table also supports up to 16 secondary indices. The type of the secondary indices could be any of:

* uint64_t

* uint128_t

* uint256_t

* double

* long double

#### Parameters
* `TableName` - name of the table 

* `T` - type of the data stored inside the table 

* `Indices` - secondary indices for the table, up to 16 indices is supported here

Example:

```cpp
#include <eosiolib/eosio.hpp>
using namespace eosio;
class mycontract: contract {
  struct record {
    uint64_t    primary;
    uint64_t    secondary_1;
    uint128_t   secondary_2;
    uint256_t   secondary_3;
    double      secondary_4;
    long double secondary_5;
    uint64_t primary_key() const { return primary; }
    uint64_t get_secondary_1() const { return secondary_1; }
    uint128_t get_secondary_2() const { return secondary_2; }
    uint256_t get_secondary_3() const { return secondary_3; }
    double get_secondary_4() const { return secondary_4; }
    long double get_secondary_5() const { return secondary_5; }
    EOSLIB_SERIALIZE( record, (primary)(secondary_1)(secondary_2)(secondary_3)(secondary_4)(secondary_5) )
  };
  public:
    mycontract( account_name self ):contract(self){}
    void myaction() {
      auto code = _self;
      auto scope = _self;
      multi_index<N(mytable), record,
        indexed_by< N(bysecondary1), const_mem_fun<record, uint64_t, &record::get_secondary_1> >,
        indexed_by< N(bysecondary2), const_mem_fun<record, uint128_t, &record::get_secondary_2> >,
        indexed_by< N(bysecondary3), const_mem_fun<record, uint256_t, &record::get_secondary_3> >,
        indexed_by< N(bysecondary4), const_mem_fun<record, double, &record::get_secondary_4> >,
        indexed_by< N(bysecondary5), const_mem_fun<record, long double, &record::get_secondary_5> >
      > table( code, scope);
    }
}
EOSIO_ABI( mycontract, (myaction) )
```

### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`class` [`eosio::multi_index`](docs2/multiindex.md#classeosio_1_1multi__index) | 



## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public inline` [`multi_index`](#multi_index)`(uint64_t code,uint64_t scope)` | load_object_by_primary_iterator
`public inline uint64_t` [`get_code`](#get_code)`() const` | Returns the `code` member property.
`public inline uint64_t `[`get_scope`](#get_scope)`() const` | Returns the `scope` member property.
`public inline` [`const_iterator`](#const_iterator) [`cbegin`](#cbegin)`() const` | Returns an iterator pointing to the object_type with the lowest primary key value in the Multi-Index table.
`public inline` [`const_iterator`](#const_iterator) [`begin`](#begin)`() const` | Returns an iterator pointing to the object_type with the lowest primary key value in the Multi-Index table.
`public inline` [`const_iterator`](#const_iterator) [`cend`](#cend)`() const` | Returns an iterator pointing to the `object_type` with the highest primary key value in the Multi-Index table.
`public inline` [`const_iterator`](#const_iterator) [`end`](#end)`() const` | Returns an iterator pointing to the `object_type` with the highest primary key value in the Multi-Index table.
`public inline` [`const_reverse_iterator`](#const_reverse_iterator) [`crbegin`](#crbegin)`() const` | Returns a reverse iterator pointing to the `object_type` with the highest primary key value in the Multi-Index table.
`public inline` [`const_reverse_iterator`](#const_reverse_iterator) [`rbegin`](#rbegin)`() const` | Returns a reverse iterator pointing to the `object_type` with the highest primary key value in the Multi-Index table.
`public inline` [`const_reverse_iterator`](#const_reverse_iterator) [`crend`](#crend)`() const` | Returns an iterator pointing to the `object_type` with the lowest primary key value in the Multi-Index table.
`public inline` [`const_reverse_iterator`](#const_reverse_iterator) `[`rend`](#rend)`() const` | Returns an iterator pointing to the `object_type` with the lowest primary key value in the Multi-Index table.
`public inline` [`const_iterator`](#const_iterator) [`lower_bound`](#lower_bound) `(uint64_t primary) const` | Searches for the `object_type` with the lowest primary key that is greater than or equal to a given primary key.
`public inline` [`const_iterator`](#const_iterator) [`upper_bound`](#upper_bound) `(uint64_t primary) const` | Searches for the `object_type` with the highest primary key that is less than or equal to a given primary key.
`public inline uint64_t` [`available_primary_key`](#available_primary_key)`() const` | Returns an available primary key.
`public template<>`  <br/> `inline auto` [`get_index`](#get_index)`()` | Returns an appropriately typed Secondary Index.
`public template<>`  <br/> `inline auto` [`get_index`](#get_index)`() const` | Returns an appropriately typed Secondary Index.
`public inline` [`const_iterator`](#const_iterator) [`iterator_to`](#iterator_to)`(const T & obj) const` | Returns an iterator to the given object in a Multi-Index table.
`public template<>`  <br/> `inline` [`const_iterator`](#const_iterator)` `[`emplace`](#emplace)`(uint64_t payer,Lambda && constructor)` | Adds a new object (i.e., row) to the table.
`public template<>`  <br/> `inline void` [`modify`](#modify)`(`[`const_iterator`](#const_iterator)` itr,uint64_t payer,Lambda && updater)` | Modifies an existing object in a table.
`public template<>`  <br/> `inline void` [`modify`](#modify)`(const T & obj,uint64_t payer,Lambda && updater)` | Modifies an existing object in a table.
`public inline const T &` [`get`](#get)`(uint64_t primary,const char * error_msg) const` | Retrieves an existing object from a table using its primary key.
`public inline` [`const_iterator`](#const_iterator)` `[`find`](#find)`(uint64_t primary) const` | Search for an existing object in a table using its primary key.
`public inline` [`const_iterator`](#const_iterator)` `[`erase`](#erase)`(`[`const_iterator`](#const_iterator)` itr)` | Remove an existing object from a table using its primary key.
`public inline void` [`erase`](#erase)`(const T & obj)` | Remove an existing object from a table using its primary key.
`typedef` [`const_reverse_iterator`](#const_reverse_iterator) | struct [multi_index::const_iterator](#multi_index::const_iterator)

## Members

### `public inline` [`multi_index`](#multi_index)`(uint64_t code,uint64_t scope)` 

load_object_by_primary_iterator

Constructs an instance of a Multi-Index table. Constructs an instance of a Multi-Index table.

#### Parameters
* `code` - Account that owns table 

* `scope` - Scope identifier within the code hierarchy

#### Precondition
code and scope member properties are initialized 

#### Post Condition
each secondary index table initialized 

#### Post Condition
Secondary indices are updated to refer to the newly added object. If the secondary index tables do not exist, they are created. 

#### Post Condition
The payer is charged for the storage usage of the new object and, if the table (and secondary index tables) must be created, for the overhead of the table creation.

Notes The `[eosio::multi_index](#eosio::multi_index)` template has template parameters `<uint64_t TableName, typename T, typename... Indices>`, where:

* `TableName` is the name of the table, maximum 12 characters long, characters in the name from the set of lowercase letters, digits 1 to 5, and the "." (period) character;

* `T` is the object type (i.e., row definition);

* `Indices` is a list of up to 16 secondary indices.

* Each must be a default constructable class or struct

* Each must have a function call operator that takes a const reference to the table object type and returns either a secondary key type or a reference to a secondary key type

* It is recommended to use the eosio::const_mem_fun template, which is a type alias to the boost::multi_index::const_mem_fun. See the documentation for the Boost const_mem_fun key extractor for more details.

Example:

```cpp
#include <eosiolib/eosio.hpp>
using namespace eosio;
using namespace std;
class addressbook: contract {
  struct address {
     uint64_t account_name;
     string first_name;
     string last_name;
     string street;
     string city;
     string state;
     uint64_t primary_key() const { return account_name; }
     EOSLIB_SERIALIZE( address, (account_name)(first_name)(last_name)(street)(city)(state) )
  };
  public:
    addressbook(account_name self):contract(self) {}
    typedef eosio::multi_index< N(address), address > address_index;
    void myaction() {
      address_index addresses(_self, _self); // code, scope
    }
}
EOSIO_ABI( addressbook, (myaction) )
```