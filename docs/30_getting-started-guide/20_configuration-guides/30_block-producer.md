---
content_title: Distributed Multi-Node Blockchains
link_text: Block Producers
---

Block producers will generally operate in a distributed and/or decentralised environment. A [block producer](../../glossary/index#block-producer) may run many instances of [Nodeos](../../glossary/index#nodeos) and generally these may be in one of two modes:

 * [Producing Node](https://developers.eos.io/manuals/eos/latest/nodeos/usage/node-setups/producing-node)
 * [Non-Producing Node](https://developers.eos.io/manuals/eos/latest/nodeos/usage/node-setups/non-producing-node)

`Producing Nodes` are configured for block production. They connect to the peer-to-peer network and actively produce new blocks. Loose transactions are also validated and relayed. On mainnet, `Producing Nodes` only produce blocks if their assigned block producer is part of an active schedule.

`Non-Producing Nodes` connect to the peer-to-peer network but do not actively produce new blocks; they are useful for acting as proxy nodes, relaying API calls, validating transactions, broadcasting information to other nodes, etc. `Non-Producing Nodes` are also useful for monitoring the blockchain state.

For more information about being a block producer we are working on a Block Producer Getting Started Guide.
