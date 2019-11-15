---
title: "db_find_i64"
excerpt: "Find a record inside a primary 64-bit integer index table."
---
Find a record inside a primary 64-bit integer index table

#### Parameters
* `scope` - The scope where the record is stored 
* `table` - The table name where the record is stored 
* `id` - The primary key of the record to look up 

#### Returns
iterator to the found record

#### Example

```cpp
int itr = db_find_i64(receiver, receiver, table1, N(charlie));
```