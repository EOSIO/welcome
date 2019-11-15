---
title: "operator<<"
excerpt: "Overload c++ iostream."
---
Overload c++ iostream 
#### Parameters
* `out` - Output strem 

* `v` - The value to be printed 

#### Returns
iostream& - Reference to the input output stream

Example:

```cpp
const char *s = "Hello World!";
uint64_t unsigned_64_bit_int = 1e+18;
uint128_t unsigned_128_bit_int (87654323456);
uint64_t string_as_unsigned_64_bit = N(abcde);
std::out << s << " " << unsigned_64_bit_int << " "  << unsigned_128_bit_int << " " << string_as_unsigned_64_bit;
// Output: Hello World! 1000000000000000000 87654323456 abcde
```