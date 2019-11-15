---
title: "Console"
excerpt: "Defines C++ wrapper to log/print text messages."
---
This API uses C++ variadic templates and type detection to make it easy to print any native type. You can even overload the `[print()](#print())` method for your own custom types.

**Example:**
```cpp
print( "hello world, this is a number: ", 5 );
```

Overriding Print for your TypesThere are two ways to overload print:* implement void print( const T& )

* implement T::print()const

### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public template<>`  <br/>`inline void `[`print_f`](#print_f)`(const char * s,Arg val,Args... rest)`            | Prints formatted string.
`public template<>`  <br/>`void `[`print`](#print)`(Arg && a,Args &&... args)`            | Print out value / list of values.
`public template<>`  <br/>`inline iostream & `[`operator<<`](#operator<<)`(iostream & out,const T & v)`            | Overload c++ iostream.
`class `[`eosio::iostream`](docs2/consolecppapi.md#classeosio_1_1iostream) | Simulate C++ style streams