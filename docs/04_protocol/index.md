# EOSIO Protocol

## System

The EOSIO blockchain platform is unique in that the features and characteristics of the blockchain built on it are flexible, that is, they can be changed, or modified completely to suit each business case requirement. Core blockchain features such as consensus, fee schedules, account creation and modification, token economics, block producer registration, voting, multi-sig, etc., are implemented inside smart contracts which are deployed on the blockchain built on the EOSIO platform. These smart contracts are referred to as `system contracts` and the layer as the `EOSIO system` layer, or simply `system` layer.

Block.one implements and maintains these `system contracts`, as samples only, encapsulating the base functionality for an EOSIO based blockchain and they are listed below:

1. [eosio.bios](https://github.com/EOSIO/eosio.contracts/tree/master/docs/02_system_contracts/01_eosio_bios.md)
2. [eosio.system](https://github.com/EOSIO/eosio.contracts/tree/master/docs/02_system_contracts/02_eosio_system.md)
3. [eosio.msig](https://github.com/EOSIO/eosio.contracts/tree/master/docs/02_system_contracts/03_eosio_msig.md)
4. [eosio.token](https://github.com/EOSIO/eosio.contracts/tree/master/docs/02_system_contracts/04_eosio_token.md)
5. [eosio.wrap](https://github.com/EOSIO/eosio.contracts/tree/master/docs/02_system_contracts/05_eosio_wrap.md)

## Core

`EOSIO Core` provides the basic building blocks for the `system` layer and because they are implemented as smart contracts they do not provide the same level of flexibility. Nevertheless, the `core` implementation is also open source and it can be modified as well to suite custom business requirements. 