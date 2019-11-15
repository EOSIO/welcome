---
title: "System"
excerpt: "Defines API for interacting with system level intrinsics."
---
### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public void `[`eosio_assert`](#eosio_assert)`(uint32_t test,const char * msg)`            | Aborts processing of this action and unwinds all pending changes.
`public void `[`eosio_assert_message`](#eosio_assert_message)`(uint32_t test,const char * msg,uint32_t msg_len)`            | Aborts processing of this action and unwinds all pending changes.
`public void `[`eosio_assert_code`](#eosio_assert_code)`(uint32_t test,uint64_t code)`            | Aborts processing of this action and unwinds all pending changes.
`public void `[`eosio_exit`](#eosio_exit)`(int32_t code)`            | Aborts execution of wasm without failing the contract.
`public uint64_t `[`current_time`](#current_time)`()`            | Get time of the last accepted block.
`public uint32_t `[`now`](#now)`()`            | Get time (rounded down to the nearest second) of the current block (i.e. the block including this action)