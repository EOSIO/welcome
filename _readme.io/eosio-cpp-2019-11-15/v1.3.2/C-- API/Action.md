---
title: "Action"
excerpt: "Defines type-safe C++ wrapers for querying action and sending action."
---
There are some methods from the [Action C API](#Action C API) that can be used directly from C++

Additional documentation for group

### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`define `[`SEND_INLINE_ACTION`](#SEND_INLINE_ACTION)            | Send inline action.
`define `[`ACTION`](#ACTION)            | Extend a new defined action with the action meta.
`public template<>` `T `[`unpack_action_data`](#unpack_action_data)`()`            | Interpret the action body as type T.
`public template<>`  `void `[`require_recipient`](#require_recipient)`(`[`account_name`](#account_name)` name,accounts... remaining_accounts)`            | Notify an account for this action.
`public void `[`require_auth`](#require_auth)`(const permission_level & level)`            | Require the specified authorization for this action.
`struct `[`eosio::permission_level`](docs2/actioncppapi.md#structeosio_1_1permission__level) | Packed representation of a permission level (Authorization)
`struct `[`eosio::action`](docs2/actioncppapi.md#structeosio_1_1action) | Packed representation of an action.
`struct `[`eosio::action_meta`](docs2/actioncppapi.md#structeosio_1_1action__meta) | Base class to derive a new defined action from.