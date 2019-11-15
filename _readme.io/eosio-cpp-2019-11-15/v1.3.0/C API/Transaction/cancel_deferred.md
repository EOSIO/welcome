---
title: "cancel_deferred"
excerpt: "Cancels a deferred transaction."
---
#### Parameters
* `sender_id` - The id of the sender

#### Precondition
The deferred transaction ID exists. 

#### Precondition
The deferred transaction ID has not yet been published. 

#### Post Condition
Deferred transaction canceled.

#### Returns
1 if transaction was canceled, 0 if transaction was not found

Example:

```cpp
id = 0xffffffffffffffff
cancel_deferred( id );
```