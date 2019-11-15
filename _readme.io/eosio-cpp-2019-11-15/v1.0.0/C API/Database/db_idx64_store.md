---
title: "db_idx64_store"
excerpt: "Store a record's secondary index in a secondary 64-bit integer index table."
---
#### Parameters
* `scope` - The scope where the secondary index will be stored 
* `table` - The table name where the secondary index will be stored 
* `payer` - The account that is paying for this storage 
* `id` - The primary key of the record which secondary index to be stored 
* `secondary` - The pointer to the key of the secondary index to store 

#### Returns
iterator to the newly created secondary index 

#### Post Condition
new secondary index is created