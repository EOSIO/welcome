---
title: "db_idx256_find_primary"
excerpt: "Get the secondary index of a record from a secondary 256-bit integer index table given the record's primary key."
---
Get the secondary index of a record from a secondary 256-bit integer index table given the record's primary key

#### Parameters
* `code` - The owner of the secondary index table 
* `scope` - The scope where the secondary index resides 
* `table` - The table where the secondary index resides 
* `data` - The buffer which will be replaced with the secondary index key 
* `data_len` - The buffer size 
* `primary` - The record's primary key 

#### Precondition
A correponding primary 256-bit integer index table with the given code, scope table must exist 

#### Post Condition
The data param will contains the appropriate secondary index key 

#### Post Condition
The primary param will contains the record that corresponds to the appropriate secondary index 

#### Returns
iterator to the secondary index which contains the given record's primary key