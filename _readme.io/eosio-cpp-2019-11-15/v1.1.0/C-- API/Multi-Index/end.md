---
title: "end"
excerpt: "Returns an iterator pointing to the `object_type` with the highest primary key value in the Multi-Index table."
---
Returns an iterator pointing to the `object_type` with the highest primary key value in the Multi-Index table. 
#### Returns
An iterator pointing to the `object_type` with the highest primary key value in the Multi-Index table.

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
      address_index addresses(_self, _self);  // code, scope
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
      eosio_assert(itr != addresses.end(), "Address for account doesn't exist");
    }
}
EOSIO_ABI( addressbook, (myaction) )
```