---
title: "eosio_assert_message"
excerpt: "Aborts processing of this action and unwinds all pending changes."
---
Aborts processing of this action and unwinds all pending changes if the test condition is true 

#### Parameters
* `test` - 0 to abort, 1 to ignore 

* `msg` - a pointer to the start of string explaining the reason for failure 

* `msg_len` - length of the string