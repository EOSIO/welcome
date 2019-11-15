---
title: "assert_ripemd160"
excerpt: "Tests if the ripemod160 hash generated from data matches the provided checksum."
---
Tests if the ripemod160 hash generated from data matches the provided checksum. 

#### Parameters
* `data` - Data you want to hash 

* `length` - Data length 

* `hash` - `checksum160*` hash to compare to

#### Precondition
**assert160 hash** of `data` equals provided `hash` parameter. 

#### Post Condition
Executes next statement. If was not `true`, hard return.

#### Example

```cpp
checksum hash;
char data;
uint32_t length;
assert_ripemod160( data, length, hash )
//If the ripemod160 hash generated from data does not equal provided hash, anything below will never fire.
eosio::print("ripemod160 hash generated from data equals provided hash");
```