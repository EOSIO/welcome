---
title: "EOSIO_ABI"
excerpt: "Dispatcher macro for apply handlers"
---
The EOSIO_ABI is a convenience macro that accepts a "class" and public methods from that class that dispatches actions. Data passed to the action is unpacked and applied positionally to the method in the class.

#### Parameters
* `TYPE` - The contract class that has the correponding action handler, this contract should be derived from [eosio::contract](#eosio::contract)
* `MEMBERS` - The namespace of the action handler function

#### Returns
n/a

#### Example
```c++
EOSIO_ABI( myclass, (myaction1)(myaction2)(myaction3) )
```