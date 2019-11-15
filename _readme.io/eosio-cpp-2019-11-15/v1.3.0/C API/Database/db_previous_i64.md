---
title: "db_previous_i64"
excerpt: "Get the previous record before the given iterator from a primary 64-bit integer index table."
---
Get the previous record before the given iterator from a primary 64-bit integer index table

#### Parameters
* `iterator` - The iterator to the record 
* `primary` - It will be replaced with the primary key of the previous record 

#### Returns
iterator to the previous record 

#### Precondition
`iterator` is pointing to the existing data inside the table 

#### Post Condition
`primary` will be replaced with the primary key of the data preceeding the data pointed by the iterator

Example:

```cpp
uint64_t prim = 123;
int itr_prev = db_previous_i64(itr, &prim);
```