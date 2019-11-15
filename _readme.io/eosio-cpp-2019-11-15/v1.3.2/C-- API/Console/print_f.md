---
title: "print_f"
excerpt: "Prints formatted string."
---
Prints formatted string, behaves similar to C printf.

#### Parameters
* `Arg` - Type of the value used to replace the format specifier 

* `Args` - Type of the value used to replace the format specifier 

#### Parameters
* `s` - Null terminated string with to be printed (it can contains format specifier) 

* `val` - The value used to replace the format specifier 

* `rest` - The values used to replace the format specifier

Example: 
```cpp
print_f("Number of apples: %", 10);
```