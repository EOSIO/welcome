---
title: "operator/="
excerpt: "Division assignment operator, with a number."
---
```cpp
public inline asset & operator/=(int64_t a)
```

Division assignment operator. Divide the amount of this asset with a number and then assign the value to itself.

#### Parameters
* `a` - The divisor for the asset's amount

#### Returns
asset - Reference to this asset

#### Post Condition
The amount of this asset is divided by a