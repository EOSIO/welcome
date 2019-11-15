---
title: "Memory"
excerpt: "Defines common memory functions."
---
### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public void * `[`malloc`](#malloc)`(size_t size)`            | Allocate additional memory.
`public void * `[`calloc`](#calloc)`(size_t count,size_t size)`            | Allocate a block of memory for an array of **count** elements, each of them **size** bytes long, and initializes all bits with 0.
`public void * `[`realloc`](#realloc)`(void * ptr,size_t size)`            | Reallocate the given area of memory.
`public void `[`free`](#free)`(void * ptr)`            | Deallocates the given area of memory.