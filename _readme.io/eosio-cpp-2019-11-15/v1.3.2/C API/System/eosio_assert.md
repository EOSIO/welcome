---
title: "eosio_assert"
excerpt: "Aborts processing of this action and unwinds all pending changes."
---
Aborts processing of this action and unwinds all pending changes if the test condition is true 

#### Parameters
* `test` - 0 to abort, 1 to ignore

Example:

```cpp
eosio_assert(1 == 2, "One is equal to two."); # fail, unwinds pending changes
eosio_assert(1 != 1, "One is not equal to one."); # fail, unwinds pending changes
eosio_assert(1 == 1, "One is not equal to one."); # success, continues
```