---
title: "read_transaction"
excerpt: "Access a copy of the currently executing transaction."
---
Access a copy of the currently executing transaction.

#### Parameters
* `buffer` - a buffer to write the current transaction to 

* `size` - the size of the buffer, 0 to return required size 

#### Returns
the size of the transaction written to the buffer, or number of bytes that can be copied if size==0 passed