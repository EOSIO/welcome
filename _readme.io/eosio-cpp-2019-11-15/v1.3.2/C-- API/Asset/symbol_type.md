---
title: "symbol_type"
excerpt: ""
---
```
public inline explicit asset (int64_t a, symbol_type s)
````
Construct a new asset given the symbol name and the amount

#### Parameters
* `a` - The amount of the asset
* `s` - The name of the symbol, default to CORE_SYMBOL

### `public inline bool `[`is_amount_within_range`](#is_amount_within_range)`() const`

Check if the amount doesn't exceed the max amount

#### Returns
true - if the amount doesn't exceed the max amount

#### Returns
false - otherwise