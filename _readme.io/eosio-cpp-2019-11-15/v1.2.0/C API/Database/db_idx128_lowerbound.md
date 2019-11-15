---
title: "db_idx128_lowerbound"
excerpt: "Get the secondary index of a record from a secondary 128-bit integer index table given the secondary index key."
---
Get the lowerbound secondary index from a secondary 128-bit integer index table given the secondary index key Lowerbound secondary index is the first secondary index which key is <= the given secondary index key

#### Parameters
* `code` - The owner of the secondary index table 
* `scope` - The scope where the secondary index resides 
* `table` - The table where the secondary index resides 
* `secondary` - The pointer to the secondary index key which acts as lowerbound pivot point, later on it will be replaced with the lowerbound secondary index key 
* `primary` - It will be replaced with the primary key of the record which the lowerbound secondary index contains 

#### Precondition
A correponding primary 128-bit integer index table with the given code, scope table must exist 

#### Post Condition
The secondary param will contains the lowerbound secondary index key 

#### Post Condition
The primary param will contains the record that corresponds to the lowerbound secondary index 

#### Returns
iterator to the lowerbound secondary index