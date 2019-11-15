---
title: "Asset"
excerpt: "Defines CPP API for managing assets."
---
## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public int64_t` [`amount`](#amount) | The amount of the asset.
`public` [`symbol_type`](#symbol_type) [`symbol`](#symbol) | The symbol name of the asset.
`public inline  explicit` [`asset`](#asset)`(int64_t a,`[`symbol_type`](#symbol_type)` s)` | Construct a new asset object.
`public inline bool` [`is_amount_within_range`](#is_amount_within_range) `() const` | Check if the amount doesn't exceed the max amount.
`public inline bool` [`is_valid`](#is_valid) `() const` | Check if the asset is valid.
`public inline void `[`set_amount`](#set_amount)`(int64_t a)` | Set the amount of the asset.
`public inline `[`asset`](#asset)` `[`operator-`](#operator-)`() const` | Unary minus operator.
`public inline `[`asset`](#asset)` & `[`operator-=`](#operator-=)`(const `[`asset`](#asset)` & a)` | Subtraction assignment operator.
`public inline `[`asset`](#asset)` & `[`operator+=`](#operator+=)`(const `[`asset`](#asset)` & a)` | Addition Assignment operator.
`public inline `[`asset`](#asset)` & `[`operator*=`](#operator*=)`(int64_t a)` | Multiplication assignment operator, with a number.
`public inline `[`asset`](#asset)` & `[`operator/=`](#operator/=)`(int64_t a)` | Division assignment operator, with a number.
`public inline void `[`print`](#print)`() const` | Print the asset

### `public `[`amount`](#amount)`

The amount of the asset

### `public `[`symbol_type`](#symbol_type)` `[`symbol`](#symbol) 

The symbol name of the asset