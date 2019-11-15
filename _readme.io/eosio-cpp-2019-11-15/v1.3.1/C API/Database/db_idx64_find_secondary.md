---
title: "db_idx64_find_secondary"
excerpt: "Get the secondary index of a record from a secondary 64-bit integer index table given the secondary index key."
---
#### Parameters
* `code` - The owner of the secondary index table 
* `scope` - The scope where the secondary index resides 
* `table` - The table where the secondary index resides 
* `secondary` - The pointer to the secondary index key 
* `primary` - It will be replaced with the primary key of the record which the secondary index contains 

#### Precondition
A correponding primary 64-bit integer index table with the given code, scope table must exist 

#### Post Condition
The secondary param will contains the appropriate secondary index key 

#### Post Condition
The primary param will contains the record that corresponds to the appropriate secondary index 

#### Returns
iterator to the secondary index which contains the given secondary index key