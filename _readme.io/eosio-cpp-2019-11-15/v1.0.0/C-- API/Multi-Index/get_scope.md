---
title: "get_scope"
excerpt: "Returns the `scope` member property."
---
Returns the `scope` member property. 

#### Returns
Scope id of the Scope within the Code of the Current Receiver under which the desired Primary Table instance can be found.

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
      eosio_assert(addresses.get_scope() == N(dan), "Scopes don't match");
    }
}
EOSIO_ABI( addressbook, (myaction) )
```