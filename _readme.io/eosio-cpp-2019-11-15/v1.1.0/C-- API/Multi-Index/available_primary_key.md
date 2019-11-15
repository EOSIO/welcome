---
title: "available_primary_key"
excerpt: "Returns an available primary key."
---
#### Returns
An available (unused) primary key value.

Notes: Intended to be used in tables in which the primary keys of the table are strictly intended to be auto-incrementing, and thus will never be set to custom values by the contract. Violating this expectation could result in the table appearing to be full due to inability to allocate an available primary key. Ideally this method would only be used to determine the appropriate primary key to use within new objects added to a table in which the primary keys of the table are strictly intended from the beginning to be autoincrementing and thus will not ever be set to custom arbitrary values by the contract. Violating this agreement could result in the table appearing full when in reality there is plenty of space left.

Example:

```cpp
#include <eosiolib/eosio.hpp>
using namespace eosio;
using namespace std;
class addressbook: contract {
  struct address {
     uint64_t key;
     string first_name;
     string last_name;
     string street;
     string city;
     string state;
     uint64_t primary_key() const { return key; }
     EOSLIB_SERIALIZE( address, (key)(first_name)(last_name)(street)(city)(state) )
  };
  public:
    addressbook(account_name self):contract(self) {}
    typedef eosio::multi_index< N(address), address > address_index;
    void myaction() {
      address_index addresses(_self, _self);  // code, scope
      // add to table, first argument is account to bill for storage
      addresses.emplace(payer, [&](auto& address) {
        address.key = addresses.available_primary_key();
        address.first_name = "Daniel";
        address.last_name = "Larimer";
        address.street = "1 EOS Way";
        address.city = "Blacksburg";
        address.state = "VA";
      });
    }
}
EOSIO_ABI( addressbook, (myaction) )
```