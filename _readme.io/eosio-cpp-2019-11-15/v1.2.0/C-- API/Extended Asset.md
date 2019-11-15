---
title: "Extended Asset"
excerpt: "Extended asset which stores the information of the owner of the asset."
---
```
struct eosio::extended_asset
  : public eosio::asset
```

Extended asset which stores the information of the owner of the asset

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`account_name`](#account_name)` `[`contract`](#contract) | The owner of the asset.
`public inline `[`extended_symbol`](#extended_symbol)` `[`get_extended_symbol`](#get_extended_symbol)`() const` | Get the extended symbol of the asset.
`public  `[`extended_asset`](#extended_asset)`() = default` | Construct a new extended asset object.
`public inline  `[`extended_asset`](#extended_asset)`(int64_t v,`[`extended_symbol`](#extended_symbol)` s)` | Construct a new extended asset object.
`public inline  `[`extended_asset`](#extended_asset)`(`[`asset`](#asset)` a,`[`account_name`](#account_name)` c)` | Construct a new extended asset object.
`public inline void `[`print`](#print)`() const` | Print the extended asset
`public inline `[`extended_asset`](#extended_asset)` `[`operator-`](#operator-)`() const` | Unary minus operator.

## Members

### `public `[`account_name`](#account_name)` `[`contract`](#contract)

The owner of the asset

### `public inline `[`extended_symbol`](#extended_symbol)` `[`get_extended_symbol`](#get_extended_symbol)`() const`

Get the extended symbol of the asset

#### Returns
[extended_symbol](#extended_symbol) - The extended symbol of the asset

### `public  `[`extended_asset`](#extended_asset)`() = default`

Construct a new extended asset object.

Default constructor

### `public inline  `[`extended_asset`](#extended_asset)`(int64_t v,`[`extended_symbol`](#extended_symbol)` s)`

Construct a new extended asset given the amount and extended symbol

### `public inline  `[`extended_asset`](#extended_asset)`(`[`asset`](#asset)` a,`[`account_name`](#account_name)` c)`

Construct a new extended asset given the asset and owner name

### `public inline void `[`print`](#print)`() const`

Print the extended asset

### `public inline `[`extended_asset`](#extended_asset)` `[`operator-`](#operator-)`() const`

Unary minus operator

#### Returns
[extended_asset](#extended_asset) - New extended asset with its amount is the negative amount of this extended asset