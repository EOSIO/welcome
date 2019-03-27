---
title: "Non-Producing Node"
excerpt: ""
---
A full node running nodeos that is only watching and verifying for itself each block, and maintaining its own local full copy of the blockchain. A non-producing node that is in the "standby pool" can, through the process of being voted in, become a [Producing Node](doc:block-producing-node). A producing node, if voted out, will become a non-producing node. For large EOSIO changes, non-producing nodes are outside the realm of the "standby pool".