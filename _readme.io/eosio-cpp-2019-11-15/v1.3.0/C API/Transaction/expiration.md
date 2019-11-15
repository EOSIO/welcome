---
title: "expiration"
excerpt: "Gets the expiration of the currently executing transaction."
---
Gets the expiration of the currently executing transaction.

#### Returns
expiration of the currently executing transaction Example: 
```cpp
time tm = expiration();
eosio_print(tm);
```