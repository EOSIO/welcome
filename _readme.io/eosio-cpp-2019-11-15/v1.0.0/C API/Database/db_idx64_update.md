---
title: "db_idx64_update"
excerpt: "Update a record's secondary index inside a secondary 64-bit integer index table."
---
Update a record's secondary index inside a secondary 64-bit integer index table

#### Parameters
* `iterator` - The iterator to the secondary index 
* `payer` - The account that is paying for this storage 
* `secondary` - The pointer to the **new** key of the secondary index 

#### Precondition
`iterator` is pointing to existing secondary index 

#### Post Condition
the seconday index pointed by the iterator is updated by the new value