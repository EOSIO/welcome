---
content_title: Smart Contract Guides
link_text: Smart Contract Guides
---

This section introduces you to the EOSIO smart contracts development workflow. You build your first basic Hello World smart contract to lay the groundwork to implement additional smart contracts such as token contracts, address book, payable actions, and more. You will gain advanced understanding on how data persistence works in the context of a smart contract and also how inline actions are implemented in a smart contract. 

### Before you Begin
Before you begin with the smart contracts development workflow, make sure the following prerequisites	are met:


1. You have set up your local development environment according to the instructions given in the [Set Up Development Environment](../30_getting-started-guide/20_local-development-environment) section of the _Getting Started Guide_.
2. Nodeos is running and producing blocks. See the [Start keosd and nodeos](../30_getting-started-guide/20_local-development-environment/40_start-nodeos-keosd.md) section of the _Getting Started Guide_ for detailed instructions. 

### Smart Contracts Development Workflow

Work your way through the following topics to build and deploy smart contracts. Start with Hello World and progressively build the other smart contracts. 

* [Hello World](10_hello-world.md): How to build, deploy and use a simple ["Hello World"](10_hello-world.md) smart contract
* [Deploy, Issue and Transfer Tokens](20_deploy-issue-and-transfer-tokens.md): How to use the eosio.token smart contract
* [Understanding ABI Files](30_understanding-ABI-files.md): How ABI files work and what they are 
* [Data Peristence](40_data-persistence.md): How to store data on the blockchain, with a single index
* [Secondary Indices](50_secondary-indices.md): How to store data on the blockchain, with muliple indices
* [Adding inline Actions](60_adding-inline-actions.md): How to call actions in your smart contract
* [Inline Actions to external contracts](70_inline-action-to-external-contract.md): How to call actions in other smart contracts
* [Linking custom permissions](80_linking-custom-permission.md): How to set up custom permissions on a smart contract
* [Payable Actions](90_payable-actions.md): How to be paid for calling smart contract actions
