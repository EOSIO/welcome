---
title: "db_upperbound_i64"
excerpt: "Find the upperbound record given a key inside a primary 64-bit integer index table."
---
Find the upperbound record given a key inside a primary 64-bit integer index table Upperbound record is the first nearest record which primary key is < the given key

#### Parameters
* `code` - The name of the owner of the table 
* `scope` - The scope where the table resides 
* `table` - The table name 
* `id` - The primary key used as a pivot to determine the upperbound record 

#### Returns
iterator to the upperbound record