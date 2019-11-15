---
title: "Console"
excerpt: "Defnes C API to log/print text messages."
---
Defnes C API to log/print text messages.

### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public void `[`prints`](#prints)`(const char * cstr)`            | Prints string.
`public void `[`prints_l`](#prints_l)`(const char * cstr,uint32_t len)`            | Prints string.
`public void `[`printi`](#printi)`(int64_t value)`            | Prints value as a 64 bit signed integer.
`public void `[`printui`](#printui)`(uint64_t value)`            | Prints value as a 64 bit unsigned integer.
`public void `[`printi128`](#printi128)`(const int128_t * value)`            | Prints value as a 128 bit signed integer.
`public void `[`printui128`](#printui128)`(const uint128_t * value)`            | Prints value as a 128 bit unsigned integer.
`public void `[`printsf`](#printsf)`(float value)`            | Prints value as single-precision floating point number (i.e. float)
`public void `[`printdf`](#printdf)`(double value)`            | Prints value as double-precision floating point number (i.e. double)
`public void `[`printqf`](#printqf)`(const long double * value)`            | Prints value as quadruple-precision floating point number (i.e. long double)
`public void `[`printn`](#printn)`(uint64_t name)`            | Prints a 64 bit names as base32 encoded string.
`public void `[`printhex`](#printhex)`(const void * data,uint32_t datalen)`            |