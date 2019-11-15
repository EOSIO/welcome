---
title: "upper_bound"
excerpt: "Searches for the `object_type` with the highest primary key that is less than or equal to a given primary key."
---
Searches for the `object_type` with the highest primary key that is less than or equal to a given primary key.

#### Parameters
* `primary` - Primary key that establishes the target value for the upper bound search

#### Returns
An iterator pointing to the `object_type` that has the highest primary key that is less than or equal to `primary`. If an object could not be found, it will return the `end` iterator. If the table does not exist** it will return `-1`.

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
     uint32_t zip = 0;
     uint64_t liked = 0;
     uint64_t primary_key() const { return account_name; }
     uint64_t by_zip() const { return zip; }
     EOSLIB_SERIALIZE( address, (account_name)(first_name)(last_name)(street)(city)(state)(zip) )
  };
  public:
    addressbook(account_name self):contract(self) {}
    typedef eosio::multi_index< N(address), address, indexed_by< N(zip), const_mem_fun<address, uint64_t, &address::by_zip> > address_index;
    void myaction() {
      address_index addresses(_self, _self);  // code, scope
      // add to table, first argument is account to bill for storage
      addresses.emplace(payer, [&](auto& address) {
        address.account_name = N(dan);
        address.first_name = "Daniel";
        address.last_name = "Larimer";
        address.street = "1 EOS Way";
        address.city = "Blacksburg";
        address.state = "VA";
        address.zip = 93446;
      });
      addresses.emplace(payer, [&](auto& address) {
        address.account_name = N(brendan);
        address.first_name = "Brendan";
        address.last_name = "Blumer";
        address.street = "1 EOS Way";
        address.city = "Hong Kong";
        address.state = "HK";
        address.zip = 93445;
      });
      uint32_t zipnumb = 93445;
      auto zip_index = addresses.get_index<N(zip)>();
      auto itr = zip_index.upper_bound(zipnumb);
      eosio_assert(itr->account_name == N(dan), "Incorrect First Upper Bound Record ");
      itr++;
      eosio_assert(itr == zip_index.end(), "Incorrect End of Iterator");
    }
}
EOSIO_ABI( addressbook, (myaction) )
```