---
title: "Privileged"
excerpt: ""
---
# privilegedcapi <a name=""></a>

Defines C Privileged API.

### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public void `[`set_resource_limits`](#set_resource_limits)`(`[`account_name`](#account_name)` account,int64_t ram_bytes,int64_t net_weight,int64_t cpu_weight)`            | Set the resource limit of an account Set the resource limit of an account.
`public int64_t `[`set_proposed_producers`](#set_proposed_producers)`(char * producer_data,uint32_t producer_data_size)`            | Propose the new active producer schedule 
`public void `[`set_active_producers`](#set_active_producers)`(char * producer_data,uint32_t producer_data_size)`            | Set new active producers Set new active producers. Producers will only be activated once the block which starts the next round is irrreversible.
`public bool `[`is_privileged`](#is_privileged)`(`[`account_name`](#account_name)` account)`            | Check if an account is privileged
`public void `[`set_privileged`](#set_privileged)`(`[`account_name`](#account_name)` account,bool is_priv)`            | Set the privileged status of an account Set the privileged status of an account.
`public void `[`set_blockchain_parameters_packed`](#set_blockchain_parameters_packed)`(char * data,uint32_t datalen)`            | Set the blockchain parameters
`public uint32_t `[`get_blockchain_parameters_packed`](#get_blockchain_parameters_packed)`(char * data,uint32_t datalen)`            | Retrieve the blolckchain parameters parameters.
`public void `[`activate_feature`](#activate_feature)`(int64_t f)`            | Activate new feature Activate new feature.