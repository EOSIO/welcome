---
content_title: Platform and Toolchain
---

The EOSIO platform is made up of the following components and building blocks:

1. `nodeos` (node + EOSIO = nodeos):  the core EOSIO node daemon that can be configured with plugins to run a node. Example uses are block production, dedicated API endpoints, and local development.
2. `cleos` (CLI + EOSIO = cleos): the command line interface to interact with the blockchain and to manage wallets.
3. `keosd` (key + EOSIO = keosd): the component that securely stores EOSIO keys in wallets.
4. `EOSIO.CDT`: toolchain for WebAssembly (Wasm)  and a set of tools to facilitate smart contract writing for the EOSIO platform. 
5. Client SDKs: SDKs to build native mobile applications on the EOSIO platform. 

The basic relationship between these components and the toolchain is illustrated in the following diagram:
[EOSIO components](https://files.readme.io/582e059-411_DevRelations_NodeosGraphic_Option3.png)

## Nodeos

Nodeos is the core EOSIO node daemon. Nodeos handles the blockchain data persistence layer, peer-to-peer networking, and contract code scheduling. For development environments, nodeos enables you to set up a single node blockchain network. Nodeos offers a wide range of features through plugins which can be enabled or disabled at start time via the command line parameters or configuration files. 

You can read detailed documentation about `nodeos` [here](https://github.com/EOSIO/eos/tree/docs/starter/docs/nodeos/index.md).


## Cleos

`cleos` is a command line tool that interfaces with the REST APIs exposed by `nodeos`. You can also use `cleos` to deploy and test EOSIO smart contracts.

You can read detailed documentation about `cleos` [here](https://github.com/EOSIO/eos/tree/docs/starter/docs/cleos/index.md).


## Keosd

`keosd` is a key manager daemon for storing private keys and signing digital messages. `keosd` provides a secure key storage medium for keys to be encrypted in the associated wallet file. The `keosd` daemon also defines a secure enclave for signing transaction created by `cleos` or a third party library.


---
**NOTE**: `keosd` can be accessed using the wallet API, but it is important to note that the intended usage is for local light client applications. It is not for cross network access by web applications trying to access users’ wallets.

---

You can read detailed documentation about `keosd` [here](https://github.com/EOSIO/eos/tree/docs/starter/docs/keos/index).

## EOSIO.CDT
EOSIO.CDT is a toolchain for WebAssembly (Wasm) and a set of tools to facilitate contract writing for the EOSIO platform. In addition to being a general-purpose WebAssembly toolchain, EOSIO-specific optimizations are available to support building EOSIO smart contracts. This new toolchain is built around Clang 7, which means that EOSIO.CDT has most of the current optimizations and analyses from LLVM. 

## EOSJS
A Javascript API SDK for integration with EOSIO-based blockchains using the EOSIO RPC API.