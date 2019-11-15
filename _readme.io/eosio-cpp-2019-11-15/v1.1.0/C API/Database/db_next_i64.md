---
title: "db_next_i64"
excerpt: "Get the next record after the given iterator from a primary 64-bit integer index table."
---
Get the next record after the given iterator from a primary 64-bit integer index table

#### Parameters
* `iterator` - The iterator to the record 
* `primary` - It will be replaced with the primary key of the next record 

#### Returns
iterator to the next record 

#### Precondition
`iterator` is pointing to the existing data inside the table 

#### Post Condition
`primary` will be replaced with the primary key of the data proceeding the data pointed by the iterator

Example:

```cpp
int charlie_itr = db_find_i64(receiver, receiver, table1, N(charlie));
// nothing after charlie
uint64_t prim = 0
int end_itr = db_next_i64(charlie_itr, &prim);
```