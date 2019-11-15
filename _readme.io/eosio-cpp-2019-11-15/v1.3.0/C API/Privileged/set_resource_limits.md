---
title: "set_resource_limits"
excerpt: "Set the resource limit of an account Set the resource limit of an account."
---
#### Parameters
* `account` - name of the account whose resource limit to be set 

* `ram_bytes` - ram limit 

* `net_weight` - net limit 

* `cpu_weight` - cput limit

## set_proposed_producers 

Propose the new active producer schedule 
#### Parameters
* `producer_data` - packed data of produce_keys in the appropriate producer schedule order 

* `producer_data_size` - size of the data buffer

#### Returns
-1 if proposing a new producer schedule was unsuccessful, otherwise returns the version of the new proposed schedule