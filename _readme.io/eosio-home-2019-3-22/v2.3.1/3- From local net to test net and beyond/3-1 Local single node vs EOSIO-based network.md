---
title: "3.1 Local single node vs EOSIO-based network"
excerpt: ""
---
***In this tutorial you will make the transition from a local single node to an EOSIO-based test network that is bound to a system contract. At the end of this tutorial you will know what the differences between these two scenarios with respect to developing a smart contract, deploying it, and testing it.  This will get you very close to learning how to write, deploy, and test on the public EOS network as well as any EOSIO-based networks (either public, private, or test). Also you will learn about the resources a developer must manage while developing a smart contract.***
[block:api-header]
{
  "title": "3.1.1 Local single node vs EOSIO-based network"
}
[/block]
A local single node is when you launch one nodeos instance and it is the only node that is producing blocks and the only node you interact with. It is the same environment which this journey helped you set up so far, starting with the [Introductory Journey](https://developers.eos.io/eosio-home/docs/introduction), continuing with the [Hello World Contract](https://developers.eos.io/eosio-home/docs/your-first-contract), [Data Persistence in a Smart Contract](https://developers.eos.io/eosio-home/docs/data-persistence), and finishing with the [Contract Actions Dispatcher](https://developers.eos.io/eosio-home/docs/writing-a-custom-dispatcher), that is, you had only one node you were running and interacting with.

An EOSIO-based network is any network that is using the EOSIO platform or a fork of the EOSIO platform code to launch and run a blockchain. The network, and thus the blockchain produced, can be public or private.  As well as being public or private, a network can also be test or production. A test network is exactly that, a EOSIO-based network that is used as a testing environment, its purpose is for testing the alpha and beta version of new releases of the EOSIO code, or forks of the EOSIO code, and/or smart contracts serving blockchain applications. There can be multiple test networks for the same EOSIO-based network. For example at the time of writing this tutorial, approximately Feb 2019, there are two test networks for the public EOS network (which is an EOSIO-based network), and they are the [Jungle TestNet](https://jungletestnet.io/) and [CryptoKylin TestNet](https://www.cryptokylin.io/).

Throughout this tutorial we will be referencing both mentioned test networks and you will have the option to use either of the two.
[block:api-header]
{
  "title": "3.1.2 Principles governing a EOSIO-based network"
}
[/block]
The next step is to understand a few principles that govern an EOSIO-based network, be it test, private, public, or production.

In an EOSIO-based network the blockchain is kept alive by nodes which are interconnected into a mesh, communicating with one another via peer-to-peer protocols. Some of these nodes are elected by the token holders to be producer nodes. They produce blocks, validate them, and reach consensus on what transactions are allowed into each block, their order, and what blocks are finalized and stored forever in the blockchain's memory.

The single local node network that you’re familiar with up to this point is governed by the eosio privileged account.  Because you controlled the eosio account’s public and private keys, and because this account is privileged, you did not have any restrictions on blockchain resources (RAM, bandwidth, and CPU).  Later, this tutorial will explain in depth the resources you must be cognizant of when writing smart contracts on EOSIO-based platforms.  On any EOSIO-based network (either public or private), the eosio account is reassigned, and control of the blockchain is in the hands of the nodes which are elected as block producers.  One consequence of this is that your smart-contract, deployed to the account which you control via it’s public and private keys, is limited by the amount of resources your account staked for the contract to use.

Governance (the mechanism by which collective decisions are made) of the blockchain is achieved through the 21 active block producers which are appointed by token holders' votes. It's the 21 active block producers which continuously create the blockchain by creating blocks, and securing them by validating them, and reaching consensus. Consensus is reached when (2/3)+1 active block producers agree on validity of a block, therefore on all transactions contained in it and their order. This aspect was also not present on the single-node local test network that you used previously.

To run a smart contract on the blockchain the contract has to be deployed to the blockchain using one of the blockchain nodes.  This is the same way it was deployed in the previous tutorial on a single node.  However this time, the node you will deploy to will make sure to transfer it to its peer nodes, and those nodes to its peers and so on and so forth until the transaction that deploys the contract is validated by the minimum number of nodes, thus reaching finality. Once the deploying transaction reaches finality it is stored in the blockchain memory forever. After this, of course, you can alter the contract through future transactions, either modify its code, or deleting the contract altogether. One thing to note here is that the transactions that reached finality will stay in the blockchain history forever, not the contract code itself, as this can be changed by the owner of the contract at a later time.

There are several public, private, and test EOSIO-based networks. Below is a list of some of these networks, gathered at the time of the writing of this tutorial, in no particular order:

  * **Public EOSIO-based networks**: EOS, Tellos, BOSCORE, Meet.One, Enumivo, EOSForce, UOS.
  * **Private EOSIO-based networks**: Everipedia, WAX, Worbli, EvaCoop.
  * **Public test EOSIO-based networks**: [Jungle TestNet](https://jungletestnet.io/) and [CryptoKylin TestNet](https://www.cryptokylin.io/).

Please note that this list is by *no means* intended to be a comprehensive list.