---
title: "db_remove_i64"
excerpt: "Remove a record inside a primary 64-bit integer index table."
---
Remove a record inside a primary 64-bit integer index table

#### Parameters
* `iterator` - The iterator pointing to the record to remove 

#### Precondition
`iterator` is pointing to the existing data inside the table 

#### Post Condition
the data is removed

Example: 
```cpp
int itr = db_find_i64(receiver, receiver, table1, N(alice));
eosio_assert(itr >= 0, "primary_i64_general - db_find_i64");
db_remove_i64(itr);
itr = db_find_i64(receiver, receiver, table1, N(alice)); 
```