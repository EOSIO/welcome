---
title: "1.3 About the Stack"
excerpt: ""
---
Before you start using the tools you just installed, it's a good idea to understand each of the components and how they interact with one another. 

* `nodeos` (node + eos = nodeos)  - the core EOSIO **node** daemon that can be configured with plugins to run a node. Example uses are block production, dedicated API endpoints, and local development. 
* `cleos` (cli + eos = cleos) - command line interface to interact with the blockchain and to manage wallets.
* `keosd` (key + eos = keosd) - component that securely stores EOSIO keys in wallets. 
* `eosio-cpp` - Part of `eosio.cdt`, it compiles C++ code to `WASM` and can generate ABIs.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/582e059-411_DevRelations_NodeosGraphic_Option3.png",
        "411_DevRelations_NodeosGraphic_Option3.png",
        1866,
        984,
        "#3f4769"
      ],
      "caption": "EOSIO Architecture"
    }
  ]
}
[/block]