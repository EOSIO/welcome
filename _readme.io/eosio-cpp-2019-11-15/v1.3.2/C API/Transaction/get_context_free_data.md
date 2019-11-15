---
title: "get_context_free_data"
excerpt: "Retrieve the signed_transaction.context_free_data[index]."
---
Retrieve the `signed_transaction.context_free_data[index]`

#### Parameters
* `index` - the index of the context_free_data entry to retrieve 

* `buff` - output buff of the context_free_data entry 

* `size` - amount of context_free_data[index] to retrieve into buff, 0 to report required size 

#### Returns
size copied, or context_free_data[index].size() if 0 passed for size, or -1 if index not valid