---
content_title: "Getting Started Guide"
link_text: "Getting Started Guide"
---

The EOSIO getting started guide contains guided instructions on how to set up your development environment by installing the EOSIO software components and other related dependencies. This is the fastest way to onboard the EOSIO development ecosystem and get acquainted with the smart contracts development workflow in a local environment.

## Local Development Environment
As a developer, begin with setting up your [Local Development Environment](20_local-development-environment) and progress to smart contract development and deployment. This pathway involves satisying system requirements and installing OS-specific EOSIO binaries.


## Pre-configured Web Environment
To quickly get familiar with the EOSIO development ecosystem, we recommend you follow the local development environment setup pathway. However, if you have any system constraints and would like to try the EOSIO environment without the need of binary installation, you can try the following pathways:

1. [EOSIO Quickstart Web IDE](30_pre-configured-development-environment): Use the Gitpod pre-configured EOSIO development environment
2. [The EOSIO Testnet](../70_quick-start-guides): Use the EOSIO Testnet as a testing environment to deploy smart contracts and build blockchain applications on EOSIO.

## EOSIO Guides
In addition to the getting started pathways, we have the following guides to help you understand EOSIO and use the components at an advanced level. 

### Protocols
In this section we describe the base components and protocols used in the EOSIO platform. `EOSIO Core` provides the basic building blocks for the `system` layer and because they are not implemented as smart contracts they do not provide the same level of flexibility. Nevertheless, the `core` implementation is also open source and thus it can be modified as well to suit custom business requirements. Follow this link [Protocol Guides](../60_protocol-guides) to read more about `EOSIO Core.`

### Advanced System Setup 

* [Installation Guides]():
* [Plugin Guides](): Use plugins to extend, or specialise, the behaviour of nodeos and kleosd
* [Configuration Guides](10_system-setup/20_configuration-guides.md): Learn how to run a local blockchain, become a block producer, and set up an environment to build, test and deploy smart contracts.



### Core Components
The main components of the EOSIO platform.
* [nodeos](https://developers.eos.io/manuals/eos/latest/nodeos/index) : The core service daemon that runs on every EOSIO node.
* [cleos](https://developers.eos.io/manuals/eos/latest/cleos/index) : A command line interface to interact with the blockchain and manage wallets.
* [keosd](https://developers.eos.io/manuals/eos/latest/keosd/index) : A key manager service daemon for storing private keys and signing digital messages.
* [eosio.cdt](https://developers.eos.io/manuals/eosio.cdt/latest/index) : Contract Development Toolkit is a suite of tools used to build EOSIO contracts.
* [eosio.contracts](https://developers.eos.io/manuals/eosio.contracts/latest/index) : Smart contracts that provide some of the basic functions of the EOSIO blockchain.
* [eos-vm](https://github.com/EOSIO/eos-vm) : EOS VM - A Low-Latency, High Performance and Extensible WebAssembly Engine.



