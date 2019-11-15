---
title: "get_blockchain_parameters_packed"
excerpt: "Retrieve the blockchain parameters"
---
#### Parameters
* `data` - output buffer of the blockchain parameters, only retrieved if sufficent size to hold packed data. 

* `datalen` - size of the data buffer, 0 to report required size. 

#### Returns
size of the blockchain parameters 

#### Precondition
`data` is a valid pointer to a range of memory at least `datalen` bytes long 

#### Post Condition
`data` is filled with packed blockchain parameters