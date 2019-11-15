---
title: "db_idx256_end"
excerpt: "Get the last secondary index from a secondary 256-bit integer index table."
---
Get the last secondary index from a secondary 256-bit integer index table

#### Parameters
* `code` - The owner of the secondary index table 

* `scope` - The scope where the secondary index resides 
* `table` - The table where the secondary index resides 

#### Returns
iterator to the last secondary index

## db_idx_double_store 

Store a record's secondary index in a secondary double index table.

Store a record's secondary index in a secondary double index table

#### Parameters
* `scope` - The scope where the secondary index will be stored 

* `table` - The table name where the secondary index will be stored 

* `payer` - The account that is paying for this storage 

* `id` - The primary key of the record which secondary index to be stored 

* `secondary` - The pointer to the key of the secondary index to store 

#### Returns
iterator to the newly created secondary index