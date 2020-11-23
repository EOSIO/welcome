---
content_title: Configuration Guides
link_text: Configuration Guides
---

The configuration guides section will show you how to configure [Nodeos.](../../glossary/index#nodeos) How [Nodeos](../../glossary/index#nodeos) is configured will depend on what your desired usage is. [Nodeos](../../glossary/index#nodeos) configuration controls which [plugins](../../glossary/index#plugin) are used and how those [plugins](../../glossary/index#plugin) are configured. The [plugins](../../glossary/index#plugin) are used to specify [Nodeos](../../glossary/index#nodeos) behaviour for specific purposes. 

# Smart Contracts and blockchain configuration

The `EOSIO platform` provides a blockchain platform and a key feature of the `EOSIO platform` is it's flexibility. Smart Contracts are part of this flexibility. Many features are implemented using smart contracts, and as smart contracts can be edited and built so you can customise blockchain behaviour. Some examples are consensus, governance and resource models. For more information see [eosio.contracts](https://developers.eos.io/manuals/eosio.contracts/latest/index) and the [bios boot sequence tutorial.](../../90_tutorials/10_bios-boot-sequence.md)    

# Development and Testing

There are several ways to configure a [Nodeos](../../glossary/index#nodeos) environment for development and testing. Which option to use largely depends on what the project goals are. Some practical options are provided below.

## Local Single-Node Testnet

This is the go-to option for smart contract developers, aspiring Block Producers or Non-Producing Node operators. It has the most simple configuration with the least number of requirements.

* [Configure Nodeos as a Local Single-node Testnet](https://developers.eos.io/manuals/eos/latest/nodeos/usage/development-environment/local-single-node-testnet) 

## Local Multi-Node Testnet

While this option can technically be used for smart contract development, it may be overkill. This is most beneficial for those who are working on aspects of core development, such as benchmarking, optimization and experimentation. It's also a good option for hands-on learning and concept proofing.

* [Configure Nodeos as a Local Two-Node Testnet](https://developers.eos.io/manuals/eos/latest/nodeos/usage/development-environment/local-multi-node-testnet)
* [Configure Nodeos as a Local 21-Node Testnet]../../80_eosio-tutorials/10_bios-boot-sequence)

# Block Producers

For block producers `Nodeos` generally runs in two modes:

 * [Producing Node](https://developers.eos.io/manuals/eos/latest/nodeos/usage/node-setups/producing-node)
 * [Non-Producing Node](https://developers.eos.io/manuals/eos/latest/nodeos/usage/node-setups/non-producing-node)

`Producing Nodes` are configured for block production. They connect to the peer-to-peer network and actively produce new blocks. Loose transactions are also validated and relayed. On mainnet, `Producing Nodes` only produce blocks if their assigned block producer is part of an active schedule.

`Non-Producing Nodes` connect to the peer-to-peer network but do not actively produce new blocks; they are useful for acting as proxy nodes, relaying API calls, validating transactions, broadcasting information to other nodes, etc. `Non-Producing Nodes` are also useful for monitoring the blockchain state.
