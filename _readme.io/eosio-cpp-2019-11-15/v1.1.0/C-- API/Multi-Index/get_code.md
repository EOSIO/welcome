---
title: "get_code"
excerpt: "Returns the `code` member property."
---
Returns the `code` member property. 
#### Returns
Account name of the Code that owns the Primary Table.

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
      address_index addresses(N(dan), N(dan)); // code, scope
      eosio_assert(addresses.get_code() == N(dan), "Codes don't match.");
    }
}
EOSIO_ABI( addressbook, (myaction) )
```