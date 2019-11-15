---
title: "set_active_producers"
excerpt: "Set new active producers Set new active producers. Producers will only be activated once the block which starts the next round is irrreversible."
---
#### Parameters
* `producer_data` - pointer to producer schedule packed as bytes 

* `producer_data_size` - size of the packed producer schedule 

#### Precondition
`producer_data` is a valid pointer to a range of memory at least `producer_data_size` bytes long that contains serialized produced schedule data