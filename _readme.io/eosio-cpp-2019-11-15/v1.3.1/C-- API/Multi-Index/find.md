---
title: "find"
excerpt: "Search for an existing object in a table using its primary key."
---
Search for an existing object in a table using its primary key.

#### Parameters
* `primary` - Primary key value of the object

#### Returns
An iterator to the found object which has a primary key equal to `primary` OR the `end` iterator of the referenced table if an object with primary key `primary` is not found.
[block:callout]
{
  "type": "info",
  "body": "`find` or `get` can actually be used to look up objects using secondary indexes by first using `get_index` and then calling `find` or `get` on that new multi_index instance."
}
[/block]
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
      // add to table, first argument is account to bill for storage
      addresses.emplace(_self, [&](auto& address) {
        address.account_name = N(dan);
        address.first_name = "Daniel";
        address.last_name = "Larimer";
        address.street = "1 EOS Way";
        address.city = "Blacksburg";
        address.state = "VA";
      });
      auto itr = addresses.find(N(dan));
      eosio_assert(itr != addresses.end(), "Couldn't get him.");
    }
}
EOSIO_ABI( addressbook, (myaction) )
```