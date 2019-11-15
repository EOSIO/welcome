---
title: "assert_sha1"
excerpt: "Tests if the sha1 hash generated from data matches the provided checksum."
---
Tests if the sha1 hash generated from data matches the provided checksum. This method is optimized to a NO-OP when in fast evaluation mode. 

#### Parameters
* `data` - Data you want to hash 

* `length` - Data length 

* `hash` - `checksum160*` hash to compare to

#### Precondition
**sha1 hash** of `data` equals provided `hash` parameter. 

#### Post Condition
Executes next statement. If was not `true`, hard return.

#### Example

```cpp
checksum hash;
char data;
uint32_t length;
assert_sha1( data, length, hash )
//If the sha1 hash generated from data does not equal provided hash, anything below will never fire.
eosio::print("sha1 hash generated from data equals provided hash");
```