---
title: "Secondary Index (eosio::multi_index::index)"
excerpt: ""
---
An EOSIO Multi-Index table can have up to 16 secondary indices.  An index can be retrieved from the `multi_index` object using the `get_index` method, and can then be iterated using a common C++ iterator pattern.

The `index` API described here operates in many ways the same as the `multi_index` described above, but it also differs in some significant ways.
- An `index` is intended to provide alternate means to access the Multi-Index Table.
- The content of a secondary index table is basically a key mapping to a primary key.  That mapping is transparent to the user.
- Some operations do not apply to secondary indices, most notably, one does not `emplace` content using a secondary index.
Objects can be modified and erased using a secondary index.
- Operations for retrieving primary content using a secondary table are virtually the same, differing primarily in the key values that are used (you cannot pass an object to a secondary index to find it in the table). The key values will be one of the supported secondary index types:
    - `idx64` - Primitive 64-bit unsigned integer key
    - `idx128` - Primitive 128-bit unsigned integer key
    - `idx256` - 256-bit fixed-size lexicographical key (does not support arithmetic operations)
    - `idx_double` - Double precision floating point key
    - `idx_long_double` - Long Double (quadruple) precision floating point key
- Secondary indices have `code` and `scope` member properties, the same as the corresponding properties on the Multi-Index table.

Alias | Description
----- | -----
_object_type_ | The typename of an object in the Multi-Index table
_secondary_index_ | An appropriately typed reference to a Secondary Index

## Copy and Assignment
Copy constructors and assignment operators are not supported.