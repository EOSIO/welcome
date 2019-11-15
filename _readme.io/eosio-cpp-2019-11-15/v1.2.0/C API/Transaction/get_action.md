---
title: "get_action"
excerpt: "Retrieves the indicated action from the active transaction."
---
Retrieves the indicated action from the active transaction.

#### Parameters
* `type` - 0 for context free action, 1 for action 

* `index` - the index of the requested action 

* `buff` - output packed buff of the action 

* `size` - amount of buff read, pass 0 to have size returned 

#### Returns
the size of the action, -1 on failure