---
content_title: "EOSIO Getting Started Guide"
link_text: "EOSIO Getting Started Guide"
---

Welcome to the `EOSIO platform`. This getting started guide will guide you to the information you need to install and use the `EOSIO platform`. The sections below should let you easily find the information you need to understand how the EOSIO platfrom works and how to install the components you need. Once you understand the `EOSIO platform` follow our getting started guides to learn how to build [smart contracts](../70_smart-contract-getting-started) or how to be a [block producer](../80_block-producer-getting-started).

# Installation Guides

There are two ways to install and use the EOSIO software:

* [Install EOSIO Prebuilt Binaries](https://developers.eos.io/manuals/eos/latest/install/install-prebuilt-binaries)
* [Build EOSIO from Source](https://developers.eos.io/manuals/eos/latest/install/build-from-source/index)

[[info]]
| If you are new to EOSIO, it is recommended that you install the [EOSIO Prebuilt Binaries](https://developers.eos.io/manuals/eos/latest/install/install-prebuilt-binaries), then proceed to the [Getting Started](https://developers.eos.io/eosio-home/docs/) section of the [EOSIO Developer Portal](https://developers.eos.io/). If you are an advanced developer, a block producer, or no binaries are available for your platform, you may need to [Build EOSIO from source](https://developers.eos.io/manuals/eos/latest/install/build-from-source/index) instead.

# Plugin Guides
Use plugins to extend, or specialise, the behaviour of nodeos and kleosd:

* [Nodeos Plugins](https://developers.eos.io/manuals/eos/latest/nodeos/plugins/index) 
* [Keosd PLugins](https://developers.eos.io/manuals/eos/latest/keosd/plugins/index)

# Configuration Guides
For information about configuring your EOSIO components click [here.](20_configuration-guides) These configuration guides will show you how to run a local blockchain, become a block producer, and set up an environment to build, test and deply smart contracts. 

# Development Environment
Smart contracts are written in C++. Any editor or IDE can be used to create a smart contract. The EOSIO.CDT provides eosio libraries and tools used to compile the smart contract before it can be deployed to the blockchain. Follow this link [Development Environment](25_development-environment) to see how to set up your development environment.  

# Quick Start Guides
Building distributed applications on EOSIO follows familiar development patterns and programming languages used for developing non-blockchain applications. In the quick start guides we show you the primitives you need to build your own blockchain applications. Follow this link [Quick Start Guides](30_quick-start-guides) to start your journey on the EOSIO platform.
 
# Protocol Guides
In this section we describe the base components and protocols used in the EOSIO platform. `EOSIO Core` provides the basic building blocks for the `system` layer and because they are not implemented as smart contracts they do not provide the same level of flexibility. Nevertheless, the `core` implementation is also open source and thus it can be modified as well to suit custom business requirements. Follw this link [Protocol Guides](40_protocol-guides) to read more about `EOSIO Core.`

# Manuals (Component Guides)
Click on the following links to find detailed documentation for each component.

## Core Components
The main components of the EOSIO platform.
* [nodeos](https://developers.eos.io/manuals/eos/latest/nodeos/index) : The core service daemon that runs on every EOSIO node.
* [cleos](https://developers.eos.io/manuals/eos/latest/cleos/index) : A command line interface to interact with the blockchain and manage wallets.
* [keosd](https://developers.eos.io/manuals/eos/latest/keosd/index) : A key manager service daemon for storing private keys and signing digital messages.
* [eosio.cdt](https://developers.eos.io/manuals/eosio.cdt/latest/index) : Contract Development Toolkit is a suite of tools used to build EOSIO contracts.
* [eosio.contracts](https://developers.eos.io/manuals/eosio.contracts/latest/index) : Smart contracts that provide some of the basic functions of the EOSIO blockchain.
* [eos-vm](https://github.com/EOSIO/eos-vm) : EOS VM - A Low-Latency, High Performance and Extensible WebAssembly Engine.
        
## Tools
Tools to help you use the EOSIO platform.
* [eosio-explorer](https://github.com/EOSIO/eosio-explorer) : An application providing Web GUI to communicate with EOSIO blockchain in a local development environment.
* [eosio-toppings](https://github.com/EOSIO/eosio-toppings) : A monorepo composed of the various packages which work together to create a web-based development tool to help users create applications on the EOSIO blockchain.
* [eosio-web-ide](https://github.com/EOSIO/eosio-web-ide) : EOSIO Quickstart Web IDE lets developers start experiment building applications on EOSIO platform in a matter of minutes.
* [demux-js](https://github.com/EOSIO/demux-js) : Demux is a backend infrastructure pattern for sourcing blockchain events to deterministically update queryable datastores and trigger side effects.
* [history-tools](https://developers.eos.io/welcome/latest/tools/history-tools/index) : Set of tools built to facilitate highly performant searches, written in C++, that can efficiently and scalably sift through terabytes of data from the full history of EOSIO blockchains.
        
## Javascript SDK
Connect to the EOSIO platform in javascript.
* [eosjs](https://developers.eos.io/manuals/eosjs/latest/index) : A Javascript library which provides an API for integrating with EOSIO-based blockchains using the EOSIO Nodeos RPC API.
* [eosjs-keygen](https://github.com/EOSIO/eosjs-keygen) : A Javascript library for managing keys in local storage.
        
## Swift SDK
Connect to the EOSIO platform in swift.
* [eosio-swift](https://github.com/EOSIO/eosio-swift) : An API for integrating with EOSIO-based blockchains using the EOSIO RPC API.
* [eosio-swift-abieos-serialization-provider](https://github.com/EOSIO/eosio-swift-abieos-serialization-provider) : A pluggable serialization provider for EOSIO SDK for Swift.
* [eosio-swift-ecc](https://github.com/EOSIO/eosio-swift-ecc) : A library for working with public and private keys, cryptographic signatures, encryption/decryption, etc. as part of the EOSIO SDK for Swift family of libraries.
* [eosio-swift-reference-ios-authenticator-signature-provider](https://github.com/EOSIO/eosio-swift-reference-ios-authenticator-signature-provider) : A pluggable signature provider for EOSIO SDK for Swift.
* [eosio-swift-softkey-signature-provider](https://github.com/EOSIO/eosio-swift-softkey-signature-provider) : An example pluggable signature provider for EOSIO SDK for Swift. It allows for signing transactions using in-memory K1 keys.
* [eosio-swift-vault-signature-provider](https://github.com/EOSIO/eosio-swift-vault-signature-provider) : A pluggable signature provider for EOSIO SDK for Swift.
* [eosio-swift-vault](https://github.com/EOSIO/eosio-swift-vault) : An utility library for working with public/private keys and signing with Apple's Keychain and Secure Enclave.

## Java SDK
Connect to the EOSIO platform in java.
* [eosio-java-android-abieos-serialization-provider](https://github.com/EOSIO/eosio-java-android-abieos-serialization-provider) : A pluggable serialization provider for EOSIO SDK for Java.
* [eosio-java-android-rpc-provider](https://github.com/EOSIO/eosio-java-android-rpc-provider) : An Android RPC provider implementation for use within EOSIO SDK for Java as a plugin.
* [eosio-java-softkey-signature-provider](https://github.com/EOSIO/eosio-java-softkey-signature-provider) : An example pluggable signature provider for EOSIO SDK for Java.
* [eosio-android-keystore-signature-provider](https://github.com/EOSIO/eosio-android-keystore-signature-provider): An example pluggable signature provider for EOSIO SDK for Java written in Kotlin.      

## EOSIO Labs
Libraries to connect and authenticate blockchain transactions.
* [eosjs-ios-browser-signature-provider-interface](https://github.com/EOSIO/eosjs-ios-browser-signature-provider-interface) : A Signature Provider Interface for communicating with an authenticator from iOS Safari using the EOSIO Authentication Transport Protocol Specification.
* [eosjs-ledger-signature-provider](https://github.com/EOSIO/eosjs-ledger-signature-provider) : A SignatureProvider for communicating with eosjs from a Ledger device.
* [eosjs-signature-provider-interface](https://github.com/EOSIO/eosjs-signature-provider-interface) : An abstract class that implements the EOSJS Signature Provider interface, and provides helper methods for interacting with an authenticator using the EOSIO Authentication Transport Protocol Specification.
* [eosjs-window-message-signature-provider-interface](https://github.com/EOSIO/eosjs-window-message-signature-provider-interface) : A Signature Provider Interface for communicating with an authenticator over the Window Messaging API using the EOSIO Authentication Transport Protocol Specification.
* [ual-authenticator-walkthrough](https://github.com/EOSIO/ual-authenticator-walkthrough) : A tutorial walks through the steps required to create a UAL for Ledger Authenticator.
* [ual-reactjs-renderer](https://github.com/EOSIO/ual-reactjs-renderer) : A library provides a React renderer around the Universal Authenticator Library.       

## Examples
Sample applications.
* [eosio-java-android-example-app](https://github.com/EOSIO/eosio-java-android-example-app) : Application demonstrating integration with EOSIO-based blockchains using EOSIO SDK for Java
* [eosio-swift-ios-example-app](https://github.com/EOSIO/eosio-swift-ios-example-app) : Application demonstrating integration with EOSIO-based blockchains using EOSIO SDK for Swift
* [tropical-example-web-app](https://github.com/EOSIO/tropical-example-web-app) : An example for developers showing an application built on EOSIO combining UAL, Manifest Spec, and Ricardian Contracts

# Testnet
The EOSIO Testnet is a web application that you can access using your login credentials. You don't have to download binaries to install the system as no external installation or configuration is required. The EOSIO Testnet is Block.one's offical testnet and uses the latest EOSIO software.

* [EOSIO Testnet](https://testnet.eos.io/) Block.one's official EOSIO Testnet.

# EOSIO Blockchain Networks
There are many public blockchains using the EOSIO platform, follow this link [EOSIO Blockchains](65_eosio-blockchain-networks) to see a list of blockchains, and click [here](../50_provide-feedback) to let us know about your EOSIO based blockchain.

# Hello World
Let's start with a simple smart contract producing the traditional "hello world." The [Hello World](../70_smart-contract-getting-started/10_hello-world.md) tutorial will guide you step by step in building a simple smart contract and deploying this smart contract to an EOSIO blockchain. 

# Next Steps
Want to [get involved in the EOSIO platform?](80_next-steps) 


