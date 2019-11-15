---
title: "get_index"
excerpt: "Returns an appropriately typed Secondary Index."
---
Returns an appropriately typed Secondary Index.

#### Parameters
* `IndexName` - the ID of the desired secondary index

#### Returns
An index of the appropriate type: Primitive 64-bit unsigned integer key (idx64), Primitive 128-bit unsigned integer key (idx128), 128-bit fixed-size lexicographical key (idx128), 256-bit fixed-size lexicographical key (idx256), Floating point key, Double precision floating point key, Long Double (quadruple) precision floating point key

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
      uint32_t zipnumb = 93446;
      auto zip_index = addresses.get_index<N(zip)>();
      auto itr = zip_index.find(zipnumb);
      eosio_assert(itr->account_name == N(dan), "Incorrect Record ");
    }
}
EOSIO_ABI( addressbook, (myaction) )
```