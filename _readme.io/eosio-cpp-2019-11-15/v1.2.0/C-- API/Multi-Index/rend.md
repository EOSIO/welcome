---
title: "rend"
excerpt: "Returns an iterator pointing to the `object_type` with the lowest primary key value in the Multi-Index table."
---
#### Returns
An iterator pointing to the `object_type` with the lowest primary key value in the Multi-Index table.

#### Example

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
      addresses.emplace(payer, [&](auto& address) {
        address.account_name = N(dan);
        address.first_name = "Daniel";
        address.last_name = "Larimer";
        address.street = "1 EOS Way";
        address.city = "Blacksburg";
        address.state = "VA";
      });
      addresses.emplace(payer, [&](auto& address) {
        address.account_name = N(brendan);
        address.first_name = "Brendan";
        address.last_name = "Blumer";
        address.street = "1 EOS Way";
        address.city = "Hong Kong";
        address.state = "HK";
      });
      auto itr = addresses.rend();
      itr--;
      eosio_assert(itr->account_name == N(brendan), "Incorrect First Record ");
      itr--;
      eosio_assert(itr->account_name == N(dan), "Incorrect Second Record");
    }
}
EOSIO_ABI( addressbook, (myaction) )
```