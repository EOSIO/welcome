---
title: "Programs and Tools"
excerpt: ""
---
[block:api-header]
{
  "title": "Nodeos"
}
[/block]
The core EOSIO daemon that can be configured with plugins to run a node. Nodeos can be configured in a number of ways
- As a block producing node
- As a validating node
- As an HTTP RPC API service for the Chain 
- As an HTTP RPC API service for the Wallet 
- Or any combination of the above...

[block:api-header]
{
  "title": "Cleos"
}
[/block]
`cleos` is a command line tool that interfaces with the REST API exposed by `nodeos`. In order to use `cleos` you will need to have the end point (IP address and port number) to a `nodeos` instance and also configure `cleos` to load the 'eosio::chain_api_plugin'.  `cleos` contains documentation for all of its commands.
[block:api-header]
{
  "title": "Keosd"
}
[/block]
`keosd` is a light-client wallet responsible for managing wallets to protect keys and sign transactions prior to broadcasting to the network. 
[block:api-header]
{
  "title": "Eosiocpp"
}
[/block]
`eosiocpp` is a C++ to WASM and ABI compiler. It generates `.wasm` and `.abi` files that are uploaded to the blockchain.