---
title: "emplace"
excerpt: "Adds a new object (i.e., row) to the table."
---
#### Parameters
* `payer` - Account name of the payer for the Storage usage of the new object

* `constructor` - Lambda function that does an in-place initialization of the object to be created in the table

#### Precondition
A multi index table has been instantiated

#### Post Condition
* A new object is created in the Multi-Index table, with a unique primary key (as specified in the object). The object is serialized and written to the table. If the table does not exist, it is created.
* Secondary indices are updated to refer to the newly added object. If the secondary index tables do not exist, they are created.
* The payer is charged for the storage usage of the new object and, if the table (and secondary index tables) must be created, for the overhead of the table creation.

#### Returns
A primary key iterator to the newly created object

Exception - The account is not authorized to write to the table.

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
    }
}
EOSIO_ABI( addressbook, (myaction) )
```