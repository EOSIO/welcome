---
title: "Primary Index (eosio::multi_index)"
excerpt: ""
---
This section documents the `eosio::multi_index` C++ API.  This interface is, effectively, an adaptation of the Boost Multi-Index container library.  It makes direct use of the `boost/multi_index/const_mem_fun` class template for key  extraction.  It also uses the Boost Hana library for metaprogramming.  Please refer to the Boost documentation at [www.boost.org](https://www.boost.org) for additional conceptual information and detail.

In the descriptions below, the following aliases will be used for common template declarations.

Alias | Description
----- | -----
_object_type_ | The type of an object in the Multi-Index table
_secondary_index_ | The type of the appropriate Secondary Index of the Multi-Index table

## Copy & Assignment
Copy constructors and assignment operators are not supported.