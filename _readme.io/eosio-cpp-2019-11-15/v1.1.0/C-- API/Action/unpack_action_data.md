---
title: "unpack_action_data"
excerpt: "Interpret the action body as type T."
---
This method unpacks the current action at type T.

#### Returns
Unpacked action data casted as T.

Example:

```cpp
struct dummy_action {
  char a; //1
  unsigned long long b; //8
  int  c; //4

  EOSLIB_SERIALIZE( dummy_action, (a)(b)(c) )
};
dummy_action msg = unpack_action_data<dummy_action>();
```

#