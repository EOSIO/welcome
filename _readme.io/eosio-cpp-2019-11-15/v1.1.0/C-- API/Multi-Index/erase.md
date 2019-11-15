---
title: "erase"
excerpt: "Remove an existing object from a table using its primary key."
---
Remove an existing object from a table using its primary key.

#### Parameters
* `itr` - An iterator pointing to the object to be removed

#### Precondition
itr points to an existing element

#### Post Condition
* The object is removed from the table and all associated storage is reclaimed.
* Secondary indices associated with the table are updated.
* The existing payer for storage usage of the object is refunded for the table and secondary indices usage of the removed object, and if the table and indices are removed, for the associated overhead.

#### Returns
For the signature with `[const_iterator](#const_iterator)`, returns a pointer to the object following the removed object.

#### Exceptions 
The object to be removed is not in the table. The action is not authorized to modify the table. The given iterator is invalid.

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
      addresses.emplace(_self, [&](auto& address) {
        address.account_name = N(dan);
        address.first_name = "Daniel";
        address.last_name = "Larimer";
        address.street = "1 EOS Way";
        address.city = "Blacksburg";
        address.state = "VA";
      });
      auto itr = addresses.find(N(dan));
      eosio_assert(itr != addresses.end(), "Address for account not found");
      addresses.erase( itr );
      eosio_assert(itr != addresses.end(), "Address not erased properly");
    }
}
EOSIO_ABI( addressbook, (myaction) )
```