 ---
content_title: System Setup
link_text: System setup
---

EOSIO based blockchains execute smart contracts which are written in `C++` and then compiled to `bytecode` using the `EOSIO Contract Development Toolkit` or `CDT.` The resulting `WebAssembly` or `WASM` files are then executed by a virtual stack machine (see [eos vm](https://github.com/EOSIO/eos-vm)). WASM is an emerging web standard with widespread support from Google, Microsoft, Apple, and industry leading companies. In this section we discuss the options for setting up a local development environment.

## Installing EOSIO
To get started as quickly as possible we recommend using pre-built binaries. Building from source is a more advanced option but will set you back an hour or more and you may encounter build errors. See the [Installation Guides](10_installation-guides.md) for information on how to install the required EOSIO components.

## EOSIO Plugins
Plugins extend the core functionality of [Nodeos](../../glossary/index#nodeos) and [Keosd.](../../glossary/index#keosd). See the [Plugin Guides](15_plugin-guides.md) for more information.

## Configuring the EOSIO platform
The EOSIO platform is flexible. You can easily run a local blockchain, or you may want to connect to a blockchain network, see the [Configurations Guides](20_configuration-guides.md) for more information.  

