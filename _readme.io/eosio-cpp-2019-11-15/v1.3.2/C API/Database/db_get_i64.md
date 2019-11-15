---
title: "db_get_i64"
excerpt: "Get a record inside a primary 64-bit integer index table."
---
Get a record inside a primary 64-bit integer index table

#### Parameters
* `iterator` - The iterator to the record 
* `data` - The buffer which will be replaced with the retrieved record 
* `len` - Size of the buffer 

#### Returns
size of the retrieved record 

#### Precondition
`iterator` is pointing to the existing data inside the table 

#### Precondition
`data` is a valid pointer to a range of memory at least `len` bytes long 

#### Precondition
`len` needs to be larger than the size of the data that is going to be retrieved 

#### Post Condition
`data` will be filled with the retrieved data

Example:

```cpp
char value[50];
auto len = db_get_i64(itr, value, buffer_len);
value[len] = '\0';
std::string s(value);
```