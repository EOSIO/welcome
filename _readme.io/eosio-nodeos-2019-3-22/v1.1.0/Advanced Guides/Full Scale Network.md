---
title: "Full Scale Network"
excerpt: ""
---
A full-scale EOSIO network consists of many servers (potentially thousands worldwide) performing a variety of functions.

The EOSIO network is depicted here in terms of layered concentric circles, where the innermost layer is the **EOSIO Core Network**, encapsulated within the **EOSIO Access Network**, which in turn is accessed by a global community of **EOSIO Consumers**.  The following diagram provides a conceptual view of these relationships.

_It is important to note that the boundaries between network layers are not hard, but rather are conceptual and used here solely for discussion purposes._ The "location" of a node in a particular network can, in fact, be quite fluid. Nodes can move between layers, e.g., depending on the votes of the community. Nodes can reside in multiple layers. There is no single owner enforcing the boundaries. The participants can come from distinctly different and independent organizations within the community. Anyone can position or lobby for position in any of the layers. The community will ultimately decide who plays what roles.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/81a9b0f-EOSIO-network-layered-diagram.png",
        "EOSIO-network-layered-diagram.png",
        1862,
        1866,
        "#dddddd"
      ]
    }
  ]
}
[/block]
## EOSIO Core Network

At the core of the EOSIO network are the block producers and accompanying server infrastructure.  A full-scale EOSIO network consists of 21 producing nodes that have been voted in by the EOSIO network community. These nodes are connected together in a full-mesh network, where each producer can readily communicate with all its peers.

The producing nodes are expected to be comprised of a networked server infrastructure that provides a robust, high performance, highly available set of producers, secured from nefarious access, and protected from arbitrary access that might negatively impact producer performance. The key design goal for this layer of the network is to keep the producing nodes focused on producing blocks and synchronizing among themselves. A producer might actually be implemented using a collection of geographically distributed highly available, high performance servers, each equipped with very high processing power and very large volumes of memory, significant disk (e.g., for log storage), connected by high capacity redundant links, protected by firewalls. Equally capable backup servers are ready to take over should an active server have problems.

These backups, along with other infrastructure, can offload unnecessary tasks from the primaries.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/56002a1-EOSIO-core-network-layered-diagram.png",
        "EOSIO-core-network-layered-diagram.png",
        3729,
        1866,
        "#eae9e9"
      ]
    }
  ]
}
[/block]
## EOSIO Access Network

The goal of the EOSIO access network is, effectively, to enable the core network to scale. It does this by providing filtering and buffering between the large number of EOSIO consumers and the small number of producers in the EOSIO core.  The access network also provides a place for aspiring block producers to establish their credibility and value, and position themselves to be voted in as producers.

Similar to the nodes in the core, the nodes in this layer are controlled and protected by serious providers willing and able to invest in the requisite significant infrastructure. These server nodes need to have significant processing, memory, and network capacities. The access network needs to be protected from attacks by bad actors, e.g., DDoS attacks.  Unlike the nodes in the core--where processing is intensive and communication is heaviest among peers within the core--nodes in the access network must reduce traffic from a very large numbers of clients in the EOSIO consumer network to only that which is essential to be managed in the core.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bef8a3d-EOSIO-access-network-layered-diagram.png",
        "EOSIO-access-network-layered-diagram.png",
        3966,
        2154,
        "#e9e6e6"
      ]
    }
  ]
}
[/block]
The nodes in the access network can be designated as **API** nodes or **Seed** nodes. This designation is based on the primary role that a node takes.  Aside from the set of plugins a node loads, there is no intrinsic property formalizing the node designation--technically speaking, a node can perform any of the given roles. Other significant infrastructure in the access network will be proxy services and load balancing, and DDoS protection.

### API Nodes

API nodes handle requests from `cleos` to perform transactions and query state.  API nodes communicate with `cleos` via http, and with other `nodeos` nodes using the EOSIO networking protocols. They effectively offload significant work from other nodes. A number of these nodes might operate collectively behind a proxy/load balancer.

API nodes perform an important role of "pre-processing" transactions using speculative state as they know it. In so doing, they can decrease the likelihood that faulty transactions make their way to producing nodes. Handling exceptions can significantly slow down a node's processing throughput. After processing action requests, the API node can filter out the bad transactions and relay the good transactions to one or more producer or other `nodeos` nodes.

Each producer node should have at least one associated API node.

### Seed Nodes

Seed nodes communicate with other `nodeos` nodes in order to maintain synchronization with the producer nodes. Seed nodes might be producer candidates that are maintaining synchronization with producers and servicing other nodes, and in so doing establishing their capability as producers in hopes of getting voted in by the community. They might provide access to another blockchain (inter-blockchain communication). They might also provide a layer of insulation between producers and other nodes (e.g., other seed nodes, API nodes) that are on the network. An important type of client of seed nodes is the **validating node**. Validating nodes operate in the Access or Consumer Networks, and track the validity of the blockchain.

Seed nodes typically only communicate blocks (not transactions) using the EOSIO network protocols, and are not configured to run the http protocols (i.e., cannot be accessed via `cleos`). Each producer node should have at least one associated seed node.

## EOSIO Consumer Network

The EOSIO Consumer Network is a very general thing. Basically, any general user who uses the blockchain, whether directly via `cleos` or indirectly using some application that interfaces with the blockchain, is part of the EOSIO Consumer Network.

Also included in the consumer network are Validating nodes that follow block production.

## Minimal Contracts

There are several contracts involved in bootstrapping and operating an EOSIO Network:

- **eosio.bios** -- Out of the box, `nodeos` starts up under the control of the `eosio.bios` contract. This contract is used to set basic operating behavior, set account and global operating limits, set privileges, set producers, and establish authorization levels. By default, `nodeos` starts under the authority of the `eosio` account. The system is bootstrapped using the `eosio` account and remains under its control until such time that the `eosio` account relinquishes control to or shares control with another account or accounts using the `eosio.bios` contract.
- **eosio.token** -- This simple but powerful contract provides the fundamental currency management capability of EOSIO.
With this, the community creates its currencies, issues currency to its account holders, and transfers currency among its members.
- **eosio.msig** -- This contract enables multiple signatures at various required levels of authorization to be supported. This works in conjunction with the EOSIO flexible permission level capabilities.
- **eosio.system** -- This contract enables users to stake tokens, and then configure and vote on producers and worker
proposals. The economics of the blockchain are effectively established and managed using this contract.