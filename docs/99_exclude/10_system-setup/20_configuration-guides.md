---
content_title: Configuration Guides
link_text: Configuration Guides
---

The configuration guides section will show you how to configure [Nodeos.](../../glossary/index#nodeos) How [Nodeos](../../glossary/index#nodeos) is configured will depend on what your desired usage is. [Nodeos](../../glossary/index#nodeos) configuration controls which [plugins](../../glossary/index#plugin) are used and how those [plugins](../../glossary/index#plugin) are configured. The [plugins](../../glossary/index#plugin) are used to specify [Nodeos](../../glossary/index#nodeos) behaviour for specific purposes. 

## Smart Contracts and blockchain configuration
The `EOSIO platform` provides a blockchain platform and a key feature of the `EOSIO platform` is it's flexibility. Smart Contracts are part of this flexibility. Many features are implemented using smart contracts, and as smart contracts can be edited and built so you can customise blockchain behaviour. Some examples are consensus, governance and resource models. For more information see [eosio.contracts](https://developers.eos.io/manuals/eosio.contracts/latest/index) and the [bios boot sequence tutorial.](../../80_tutorials/10_bios-boot-sequence.md)    

## Development and Testing
There are several ways to configure a [Nodeos](../../glossary/index#nodeos) environment for development and testing. Which option to use largely depends on what the project goals are. Some practical options are provided below.

### Local Single-Node Testnet
This runs a blockchain, with a single node, locally. The local single-node testnet is the simplest blockchain configuration. A local single-node testnet is generally used as a test envronment to get started developing smart contracts.    

* [Configure Nodeos as a Local Single-node Testnet](https://developers.eos.io/manuals/eos/latest/nodeos/usage/development-environment/local-single-node-testnet) 

### Local Multi-Node Testnet
A local single node testnet is a great place to start, but a blockchain running on a single node is not much of a blockchain. To run many nodes locally see the guides listed below. Often multi node testnets will be used for advanced development and testing giving a more realistic blockchain environment. Other uses for a a multi node testnet are benchmarking, optimization and experimentation, or to increase your knowledge. 

* [Configure Nodeos as a Local Two-Node Testnet](https://developers.eos.io/manuals/eos/latest/nodeos/usage/development-environment/local-multi-node-testnet)
* [Configure Nodeos as a Local 21-Node Testnet](https://github.com/EOSIO/eos/blob/master/tutorials/bios-boot-tutorial/README.md)

### EOSIO Testnet
The EOSIO Testnet is Block.one's offical testnet and uses the latest EOSIO software. 

* [EOSIO Testnet](https://testnet.eos.io/) Block.one's official EOSIO Testnet.
* [EOSIO Testnet Quick Start Guide.](https://developers.eos.io/welcome/latest/quick-start-guides/testnet-quick-start-guide/index) 

## Block Producers
Block producers operate in a distributed and/or decentralised environment. A [block producer](../../glossary/index#block-producer) may run many instances of [Nodeos](../../glossary/index#nodeos) and these may be in one of two modes:

 * [Producing Node](https://developers.eos.io/manuals/eos/latest/nodeos/usage/node-setups/producing-node)
 * [Non-Producing Node](https://developers.eos.io/manuals/eos/latest/nodeos/usage/node-setups/non-producing-node)

`Producing Nodes` are configured for block production. They connect to the peer-to-peer network and actively produce new blocks. Loose transactions are also validated and relayed. On mainnet, `Producing Nodes` only produce blocks if their assigned block producer is part of an active schedule.

`Non-Producing Nodes` connect to the peer-to-peer network but do not actively produce new blocks; they are useful for acting as proxy nodes, relaying API calls, validating transactions, broadcasting information to other nodes, etc. `Non-Producing Nodes` are also useful for monitoring the blockchain state.

For more information about being a block producer we are working on a Block Producer Getting Started Guide.
