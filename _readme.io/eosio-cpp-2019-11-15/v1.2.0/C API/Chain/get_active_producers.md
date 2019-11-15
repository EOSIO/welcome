---
title: "get_active_producers"
excerpt: "Gets the set of active producers."
---
Gets the set of active producers. 
#### Parameters
* `producers` - Pointer to a buffer of account names 

* `datalen` - Byte length of buffer

#### Returns
uint32_t - Number of bytes actually populated 

#### Precondition
`producers` is a pointer to a range of memory at least `datalen` bytes long 

#### Post Condition
the passed in `producers` pointer gets the array of active producers.

Example:

```cpp
account_name producers[21];
uint32_t bytes_populated = get_active_producers(producers, sizeof(account_name)*21);
```