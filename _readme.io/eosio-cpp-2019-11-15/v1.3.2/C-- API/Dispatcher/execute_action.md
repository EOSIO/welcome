---
title: "execute_action"
excerpt: "Unpack the received action and execute the correponding action handler."
---
Unpack the received action and execute the correponding action handler

#### Parameters
* `T` - The contract class that has the correponding action handler, this contract should be derived from [eosio::contract](#eosio::contract)
* `Q` - The namespace of the action handler function 
* `Args` - The arguments that the action handler accepts, i.e. members of the action 

#### Parameters
* `obj` - The contract object that has the correponding action handler 
* `func` - The action handler 

#### Returns
true