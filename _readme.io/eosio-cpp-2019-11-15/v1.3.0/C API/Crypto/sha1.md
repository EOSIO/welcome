---
title: "sha1"
excerpt: "Hashes `data` using `sha1` and stores result in memory pointed to by hash."
---
Hashes `data` using `sha1` and stores result in memory pointed to by hash. 

#### Parameters
* `data` - Data you want to hash 

* `length` - Data length 

* `hash` - Hash pointer

#### Example

```cpp
checksum calc_hash;
sha1( data, length, &calc_hash );
eos_assert( calc_hash == hash, "invalid hash" );
```