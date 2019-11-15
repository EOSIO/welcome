---
title: "db_idx64_next"
excerpt: "Get the next secondary index inside a secondary 64-bit integer index table."
---
#### Parameters
* `iterator` - The iterator to the secondary index 
* `primary` - It will be replaced with the primary key of the record which is stored in the **next** secondary index 

#### Returns
iterator to the next secondary index 

#### Precondition
`iterator` is pointing to the existing secondary index inside the table 

#### Post Condition
`primary` will be replaced with the primary key of the secondary index proceeding the secondary index pointed by the iterator