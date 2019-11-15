---
title: "read_action_data"
excerpt: "Copy current action data to the specified location."
---
```
uint32_t read_action_data( void* msg, uint32_t len );
```

Copy up to len bytes of current action data to the specified location

#### Parameters
* `msg` - a pointer where up to len bytes of the current action data will be copied 
* `len` - len of the current action data to be copied, 0 to report required size 

#### Returns
the number of bytes copied to msg, or number of bytes that can be copied if len==0 passed 

#### Precondition
`msg` is a valid pointer to a range of memory at least `len` bytes long 

#### Post Condition
`msg` is filled with packed action data