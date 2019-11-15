---
title: "Transaction"
excerpt: "Defines API for sending transactions."
---
### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public void `[`send_deferred`](#send_deferred)`(const uint128_t & sender_id,`[`account_name`](#account_name)` payer,const char * serialized_transaction,size_t size,uint32_t replace_existing)`            | Sends a deferred transaction.
`public int `[`cancel_deferred`](#cancel_deferred)`(const uint128_t & sender_id)`            | Cancels a deferred transaction.
`public size_t `[`read_transaction`](#read_transaction)`(char * buffer,size_t size)`            | Access a copy of the currently executing transaction.
`public size_t `[`transaction_size`](#transaction_size)`()`            | Gets the size of the currently executing transaction.
`public int `[`tapos_block_num`](#tapos_block_num)`()`            | Gets the block number used for TAPOS on the currently executing transaction.
`public int `[`tapos_block_prefix`](#tapos_block_prefix)`()`            | Gets the block prefix used for TAPOS on the currently executing transaction.
`public `[`time`](#time)` `[`expiration`](#expiration)`()`            | Gets the expiration of the currently executing transaction.
`public int `[`get_action`](#get_action)`(uint32_t type,uint32_t index,char * buff,size_t size)`            | Retrieves the indicated action from the active transaction.
`public int `[`get_context_free_data`](#get_context_free_data)`(uint32_t index,char * buff,size_t size)`            | Retrieve the signed_transaction.context_free_data[index].