---
content_title: "EOSIO Getting Started Guide"
link_text: "EOSIO Getting Started Guide"
---

# Welcome
Welcome to the EOSIO platform. This getting started guide will quickly show you how to use the EOSIO platform.

The EOSIO platform is made up of the following components and toolchain:

1. `nodeos`:  the core EOSIO node daemon that can be configured with plugins to run a node. Example uses are block production, dedicated API endpoints, and local development.
2. `cleos`: the command line interface to interact with the blockchain and to manage wallets.
3. `keosd`: the component that securely stores EOSIO keys in wallets.
4. `EOSIO.CDT`: toolchain for WebAssembly (Wasm)  and a set of tools to facilitate smart contract writing for the EOSIO platform.

In the getting started guide we introduce you to concepts, tools and SDK's you will use to build robust blockchain solutions. 

# Blockchain Terminology in an EOSIO World
You can find EOSIO definitions in our [Glossary](https://developers.eos.io/welcome/latest/glossary/index)

# Configuration Guides

## Plugin Guides
Use plugins to extend, or specialise, the behaviour of nodeos and kleosd:

* [Nodeos Plugins](https://developers.eos.io/manuals/eos/latest/nodeos/plugins/index) 
* [Keosd PLugins](https://developers.eos.io/manuals/eos/latest/keosd/plugins/index)

## Development Environment
Smart contracts are written in C++. Any editor or IDE can be used to create a smart contract. The EOSIO.CDT provides eosio libraries and tools used to compile the smart contract before it can be deployed to the blockchain.   

### Example Editors and IDEs

- [Sublime Text](https://www.sublimetext.com/)
- [Atom Editor](https://atom.io/)
- [CLion](https://www.jetbrains.com/clion/)
- [Eclipse](http://www.eclipse.org/downloads/packages/release/oxygen/1a/eclipse-ide-cc-developers)
- [Visual Studio Code](https://code.visualstudio.com/)

Alternatively, you can use IDEs specifically developed for EOSIO:

- [EOS Studio](https://www.eosstudio.io/)

[[info]]
| The resources listed above are developed, offered, and maintained by third-parties and not by block.one. Providing information, material, or commentaries about such third-party resources does not mean we endorse or recommend any of these resources. We are not responsible, and disclaim any responsibility or liability, for your use of or reliance on any of these resources. Third-party resources may be updated, changed or terminated at any time, so the information below may be out of date or inaccurate. USAGE AND RELIANCE IS ENTIRELY AT YOUR OWN RISK


# Quick Start Guides
Building distributed applications on EOSIO follows familiar development patterns and programming languages used for developing non-blockchain applications. In the following guides we show you the primitives you need to build your own smart contracts:


* Build and Deploy smart contracts:
	* [Understand resources see HK engineer samples](https://developers.eos.io/welcome/badlink)
	* [How to build and Deploy see HK engineer samples](https://developers.eos.io/welcome/badlink)
	* [Understanding ABI files](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/understanding-ABI-files)

* Hello World: 
	* [Your first smart contract deployed to a blocklchain](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/hello-world)

* Write to the blockchain:
	* Work with state in your smart contract 
		* [Data Persistence](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/data-persistence)
		* [Secondary Indices](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/secondary-indices)
	* Store data in the blocks.log 
		* [Store files to blocks.log - see HK engineer samples](https://developers.eos.io/welcome/badlink)

* Read from the blockchain:
	* [State History  - TBD](https://developers.eos.io/welcome/badlink)
	* [EOSIO History Tools  - TBD](https://developers.eos.io/welcome/badlink)
	* [Dfuse  - TBD](https://developers.eos.io/welcome/badlink)

* Calling Actions:
	* [Adding inline Actions](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/adding-inline-actions)
	* [Inline Actions to External Contracts](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/inline-action-to-external-contract)

* Payable Actions:
	* [Payable Actions](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/payable_actions)

# Protocol Guides
In this section we describe the base components and protocols used in the EOSIO platform.

## Core
`EOSIO Core` provides the basic building blocks for the `system` layer. The `core` implementation is open source.

The core protocols are:

1. [Consensus Protocol](01_consensus_protocol.md)
2. [Transactions Protocol](02_transactions_protocol.md)
3. [Network or Peer to Peer Protocol](03_network_peer_protocol.md)
4. [Accounts and Permissions](04_accounts_and_permissions.md)

## System
Core blockchain features such as consensus, fee schedules, account creation and modification, token economics, block producer registration, voting, multi-sig, etc are implemented with smart contracts which are deployed on an EOSIO blockchain. These smart contracts are known as `system contracts` or the `system` layer. 

1. [eosio.bios](https://developers.eos.io/manuals/eosio.contracts/latest/action-reference/eosio.bios)
2. [eosio.system](https://developers.eos.io/manuals/eosio.contracts/latest/action-reference/eosio.system)
3. [eosio.msig](https://developers.eos.io/manuals/eosio.contracts/latest/action-reference/eosio.msig)
4. [eosio.token](https://developers.eos.io/manuals/eosio.contracts/latest/action-reference/eosio.token)
5. [eosio.wrap](https://developers.eos.io/manuals/eosio.contracts/latest/action-reference/eosio.wrap)

The `system` layer also includes:

1. [System accounts](https://developers.eos.io/manuals/eosio.contracts/latest/index/#system-contracts-system-accounts-priviledged-accounts)
2. [RAM](https://developers.eos.io/manuals/eosio.contracts/latest/index/#ram)
3. [CPU](https://developers.eos.io/manuals/eosio.contracts/latest/index/#cpu)
4. [NET](https://developers.eos.io/manuals/eosio.contracts/latest/index/#net)
5. [Stake](https://developers.eos.io/manuals/eosio.contracts/latest/index/#stake)
6. [Vote](https://developers.eos.io/manuals/eosio.contracts/latest/index/#vote)


# Manuals (Component Guides)
Click on the following links to find detailed documentation for each component.

## Core Components
The main componets of the EOSIO platform.
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
        
# Hello World
Let's start with a simple smart contract producing the traditional "hello world." The [Hello World](./03_smart-contract-development/01_hello-world.md) tutorial will guide you step by step in building a simple smart contract and deploying the smart contract to an EOSIO blockchain. 

# Testnet
The EOSIO Testnet is a web application that you can access using your login credentials. You don't have to download binaries to install the system as no external installation or configuration is required. The EOSIO Testnet is Block.one's offical testnet and uses the latest EOSIO software.

* [EOSIO Testnet](https://testnet.eos.io/) Block.one's official EOSIO Testnet.

## What's next?

- [Payable Actions](../28_smart-contract-development/10_payable_actions.md): Learn how to create payable actions.
- [Deploy, Issue and Transfer Tokens](../28_smart-contract-development/20_deploy-issue-and-transfer-tokens.md): Learn how to create, issue and trasnfer tokens using eosio.token.
- [Understand ABI files](../28_smart-contract-development/30_understanding-ABI-files.md): Learn about ABI files.
- [Data Persistence](../28_smart-contract-development/40_data-persistence.md): Learn how to save state on the blockchain.
- [Secondary Indices](../28_smart-contract-development/50_secondary-indices.md): Learn how to use secondary indices on multi index.
- [Add Inline Actions ](../28_smart-contract-development/60_adding-inline-actions.md): Learn how to call inline actions.
- [Call Actions on External Contracts](../28_smart-contract-development/70_inline-action-to-external-contract.md): Learn how to call actions in other smart contracts.
- [Linking Custom Permissions](../28_smart-contract-development/80_linking-custom-permission.md): Learn how to link custom permissions.


