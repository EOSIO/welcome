---
title: "db_update_i64"
excerpt: "Update a record inside a primary 64-bit integer index table."
---
Update a record inside a primary 64-bit integer index table

#### Parameters
* `iterator` - Iterator of the record to update 

* `payer` - The account that is paying for this storage 

* `data` - New updated record 

* `len` - Size of data 

#### Precondition
len >= sizeof(data) 

#### Precondition
`data` is a valid pointer to a range of memory at least `len` bytes long 

#### Precondition
`*((uint64_t*)data)` stores the primary key 

#### Precondition
this method is being called from an apply context (not validate or precondition) 

#### Precondition
`iterator` is pointing to the existing data inside the table 

#### Post Condition
the data pointed by the iterator is replaced with the new data