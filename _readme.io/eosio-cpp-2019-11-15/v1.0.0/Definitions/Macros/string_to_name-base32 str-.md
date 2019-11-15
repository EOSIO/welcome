---
title: "string_to_name(base32 str)"
excerpt: "Converts a base32 string to a uint64_t."
---
Converts a base32 string to a uint64_t. This is a constexpr so that this method can be used in template arguments as well.

#### Parameters
* `str` - String representation of the name

#### Returns
constexpr uint64_t - 64-bit unsigned integer representation of the name