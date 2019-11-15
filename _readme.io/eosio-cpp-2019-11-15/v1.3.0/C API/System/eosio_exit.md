---
title: "eosio_exit"
excerpt: "Aborts execution of wasm without failing the contract."
---
This method will abort execution of wasm without failing the contract. This is used to bypass all cleanup / destructors that would normally be called. 

#### Parameters
* `code` - the exit code Example:

```cpp
eosio_exit(0);
eosio_exit(1);
eosio_exit(2);
eosio_exit(3);
```