---
title: "ripemd160"
excerpt: "Hashes `data` using `ripemod160` and stores result in memory pointed to by hash."
---
#### Parameters
* `data` - Data you want to hash 

* `length` - Data length 

* `hash` - Hash pointer

#### Example

```cpp
checksum calc_hash;
ripemod160( data, length, &calc_hash );
eos_assert( calc_hash == hash, "invalid hash" );
```