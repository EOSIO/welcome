---
title: "Action"
excerpt: ""
---
Defines API for querying action and sending action.

A EOS.IO action has the following abstract structure:

```cpp
struct action {
  scope_name scope; // the contract defining the primary code to execute for code/type
  action_name name; // the action to be taken
  permission_level[] authorization; // the accounts and permission levels provided
  bytes data; // opaque data processed by code
};
```
This API enables your contract to inspect the fields on the current action and act accordingly.

Example: 

```cpp
// Assume this action is used for the following examples:
// {
//  "code": "eos",
//  "type": "transfer",
//  "authorization": [{ "account": "inita", "permission": "active" }],
//  "data": {
//    "from": "inita",
//    "to": "initb",
//    "amount": 1000
//  }
// }

char buffer[128];
uint32_t total = read_action(buffer, 5); // buffer contains the content of the action up to 5 bytes
print(total); // Output: 5

uint32_t msgsize = action_size();
print(msgsize); // Output: size of the above action's data field

require_recipient(N(initc)); // initc account will be notified for this action

require_auth(N(inita)); // Do nothing since inita exists in the auth list
require_auth(N(initb)); // Throws an exception

print(current_time()); // Output: timestamp (in microseconds since 1970) of current block
```

### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public uint32_t ` [`read_action_data`](#read_action_data) `(void * msg,uint32_t len)`            | Copy current action data to the specified location.
`public uint32_t `[`action_data_size`](#action_data_size)`()`            | Get the length of current action's data field.
`public void `[`require_recipient`](#require_recipient)`(`[`account_name`](#account_name)` name)`            | Add the specified account to set of accounts to be notified.
`public void `[`require_auth`](#require_auth)`(`[`account_name`](#account_name)` name)`            | Verify specified account exists in the set of provided auths.
`public bool `[`has_auth`](#has_auth)`(`[`account_name`](#account_name)` name)`            | Verifies that name has auth.
`public void `[`require_auth2`](#require_auth2)`(`[`account_name`](#account_name)` name,`[`permission_name`](#permission_name)` permission)`            | Verify specified account exists in the set of provided auths.
`public bool `[`is_account`](#is_account)`(`[`account_name`](#account_name)` name)`            | 
`public void `[`send_inline`](#send_inline)`(char * serialized_action,size_t size)`            | Send an inline action in the context of this action's parent transaction
`public void `[`send_context_free_inline`](#send_context_free_inline)`(char * serialized_action,size_t size)`            | Send an inline context free action in the context of this action's parent transaction
`public void `[`require_write_lock`](#require_write_lock)`(`[`account_name`](#account_name)` name)`            | Verifies that name exists in the set of write locks held.
`public void `[`require_read_lock`](#require_read_lock)`(`[`account_name`](#account_name)` name)`            | Verifies that name exists in the set of read locks held.
`public uint64_t `[`publication_time`](#publication_time)`()`            | Get the publication time.
`public `[`account_name`](#account_name)` `[`current_receiver`](#current_receiver)`()`            | Get the current receiver of the action.