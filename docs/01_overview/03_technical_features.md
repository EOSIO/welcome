---
content_title: Technical Features
---

## High Throughput, Faster Confirmations and Lower Latency

EOSIO is designed with `high transactions throughput` in mind and each new version is achieving important improvements on this aspect. Because it uses the consensus mechanism of `Delegated Proof of Stake` (a.k.a. `DPOS`), higher transactions throughput is achieved when compared to other consensus mechanisms because `DPOS` does not need to wait for all nodes to complete a transaction to achieve finality. This also has as direct result `faster confirmations` and `lower latency` which opens possibilities for developers building on EOSIO based blockchain to compete with non-blockchain, centralized, alternatives.

EOSIO based blockchains benefit as well of a dedicated virtual machine, `EOS VM` which is designed from the ground up for the high demands of blockchain applications which require far more from a WebAssembly engine than those designed for web browsers or standards development. 


## Free Stake-Limited Transactions

The EOSIO blockchains are regulating the access to the infrastructure resources by a staking mechanism. The user interacting with the blockchain, either directly via cleos command line interface, or via RPC api, or via an application, can access infrastructure resources, e.g. RAM, CPU, and NET, by staking system tokens. After tokens are staked for RAM, CPU and NET, the user will have access to these resources proportional to the total amount of tokens staked by all other users for the same resource at the same time, thus she can transact at `no cost in the limits given by the staked tokens`, and because of that transactions are called `free stake-limited`. The tokens staked guarantee the proportional amount of resources no matter how much the system token price varies on the free market. Also applications built on EOSIO can adopt a freemium model in which applications’ users do not need to pay for the cost of resources needed to transact via the applications, the applications can do it on behalf of the users instead by staking enough system tokens to guarantee the resources needed.


## Comprehensive Permission Schema

The EOSIO platform has a comprehensive permission system for creating custom permission schemata for various use cases. For example, you can create custom permission and use it to protect one particular feature of a smart contract. You can also split the authorities necessary to invoke a smart contract function across multiple accounts with different authority weights. This comprehensive permission system allows you to build a permissioned application on top of a flexible infrastructure. 


## Upgradability

Applications deployed on EOSIO based blockchains are upgradeable. This means developers can deploy code fix, add features, and/or change application logic, as long as sufficient authority is provided. As a developer, you can iterate your application without the risk of being locked-in to a mistake or bug permanently. It is also possible, however, to deploy smart contracts that cannot be modified on EOSIO based blockchains. These decisions are at the discretion of developers rather than restricted by the protocol.


## Less energy consumption

With `DPOS` as the consensus mechanism, EOSIO consumes much less energy to validate transactions and secure a blockchain compared to other consensus algorithms.


## Programmable Economics and Governance

The resource allocation and governance mechanism of any EOSIO based blockchain are programmable via smart contracts. Developers only need to modify the system smart contracts to change resource allocation and governance rules of an EOSIO blockchain. On-chain governance becomes much simpler when using system smart contracts, as the base layer code does not have to be modified for changes to take place on the blockchain.
