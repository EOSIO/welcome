# EOSIO Protocol

## Core

`EOSIO Core` provides the basic building blocks for the `system` layer and because they are not implemented as smart contracts they do not provide the same level of flexibility. Nevertheless, the `core` implementation is also open source and thus it can be modified as well to suit custom business requirements.

The core protocols are:

1. [Consensus Protocol](01_consensus_protocol.md)
2. [Transactions Protocol](02_transactions_protocol.md)
3. [Network or Peer to Peer Protocol](03_network_peer_protocol.md)
4. [Accounts and Permissions](04_accounts_and_permissions.md)

## System

The EOSIO blockchain platform is unique in that the features and characteristics of the blockchain built on it are flexible, that is, they can be changed, or be modified completely to suit each business case requirement. Core blockchain features such as consensus, fee schedules, account creation and modification, token economics, block producer registration, voting, multi-sig, etc., are implemented inside smart contracts which are deployed on the blockchain built on the EOSIO platform. These smart contracts are referred to as `system contracts` and the layer as the `EOSIO system` layer, or simply `system` layer.

Block.one implements and maintains these `system contracts`, as samples only, encapsulating the base functionality for an EOSIO based blockchain and they are listed below:

1. [eosio.bios](/manuals/eosio.contracts/latest/action-reference/eosio.bios)
2. [eosio.system](/manuals/eosio.contracts/latest/action-reference/eosio.system)
3. [eosio.msig](/manuals/eosio.contracts/latest/action-reference/eosio.msig)
4. [eosio.token](/manuals/eosio.contracts/latest/action-reference/eosio.token)
5. [eosio.wrap](/manuals/eosio.contracts/latest/action-reference/eosio.wrap)

Also part of the `system` layer are the following concepts:

1. [System accounts](https://github.com/EOSIO/eosio.contracts/tree/master/docs/01_core_concepts/01_system.md)
2. [RAM](https://github.com/EOSIO/eosio.contracts/tree/master/docs/01_core_concepts/02_ram.md)
3. [CPU](https://github.com/EOSIO/eosio.contracts/tree/master/docs/01_core_concepts/03_cpu.md)
4. [NET](https://github.com/EOSIO/eosio.contracts/tree/master/docs/01_core_concepts/04_net.md)
5. [Stake](https://github.com/EOSIO/eosio.contracts/tree/master/docs/01_core_concepts/05_stake.md)
6. [Vote](https://github.com/EOSIO/eosio.contracts/tree/master/docs/01_core_concepts/06_vote.md)
