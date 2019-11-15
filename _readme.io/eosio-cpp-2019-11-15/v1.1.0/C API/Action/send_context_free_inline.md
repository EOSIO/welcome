---
title: "send_context_free_inline"
excerpt: "Send an inline context free action in the context of this action's parent transaction"
---
Send an inline context free action in the context of this action's parent transaction

#### Parameters
* `serialized_action` - serialized action 

* `size` - size of serialized action in bytes 

#### Precondition
`serialized_action` is a valid pointer to an array at least `size` bytes long