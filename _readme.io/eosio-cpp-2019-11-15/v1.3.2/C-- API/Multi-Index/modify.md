---
title: "modify"
excerpt: "Modifies an existing object in a table."
---
Modifies an existing object in a table.

#### Parameters
* `itr` - an iterator pointing to the object to be updated

* `payer` - account name of the payer for the Storage usage of the updated row

* `updater` - lambda function that updates the target object

#### Precondition
* itr points to an existing element
* payer is a valid account that is authorized to execute the action and be billed for storage usage.

#### Post Condition
* The modified object is serialized, then replaces the existing object in the table.
*  Secondary indices are updated; the primary key of the updated object is not changed.
* The payer is charged for the storage usage of the updated object.
* If payer is the same as the existing payer, payer only pays for the usage difference between existing and updated object (and is refunded if this difference is negative).
* If payer is different from the existing payer, the existing payer is refunded for the storage usage of the existing object.

Exceptions: If called with an invalid precondition, execution is aborted.

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
      addresses.modify( itr, account payer, [&]( auto& address ) {
        address.city = "San Luis Obispo";
        address.state = "CA";
      });
    }
}
EOSIO_ABI( addressbook, (myaction) )
```