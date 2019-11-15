---
title: "db_store_i64"
excerpt: "Store a record in a primary 64-bit integer index table"
---
#### Parameters
* `scope` - The scope where the record will be stored 

* `table` - The ID/name of the table within the current scope/code context 

* `payer` - The account that is paying for this storage 

* `id` - Id of the entry 

* `data` - Record to store 

* `len` - Size of data 

#### Precondition
len >= sizeof(data) 

#### Precondition
data is a valid pointer to a range of memory at least `len` bytes long 

#### Precondition
`*((uint64_t*)data)` stores the primary key 

#### Precondition
this method is being called from an apply context (not validate or precondition) 

#### Returns
iterator to the newly created object 

#### Post Condition
a new entry is created in the table