---
title: "EOSIO_ABI"
excerpt: "Convenient macro to create contract apply handler."
---
Convenient macro to create contract apply handler To be able to use this macro, the contract needs to be derived from [eosio::contract](#eosio::contract)

#### Parameters
* `TYPE` - The class name of the contract 

* `MEMBERS` - The sequence of available actions supported by this contract

Example: 
```cpp
EOSIO_ABI( eosio::bios, (setpriv)(setalimits)(setglimits)(setprods)(reqauth) )
```