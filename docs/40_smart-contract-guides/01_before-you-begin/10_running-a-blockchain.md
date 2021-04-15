---
content_title: "Running a blockchain"
link_text: "Running a blockchain"
---


Smart contracts are [deployed](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-deploy-a-smart-contract) to a blockchain and smart contract transactions are executed on a blockchain. Testing a smart contract requires a blockchain. You can run a local blockchain for testing smart contracts or use the [official Block.one testnet](https://testnet.eos.io/). See the [testnet quick start guide](../../70_quick-start-guides/testnet-quick-start-guide/index.md) for more information on how to use the official Block.one testnet. This tutorial shows how to run a blockchain on your local machine. This is commonly known as a `local single node testnet`.


This tutorial introduces the [EOSIO Blockchain.](../../20_introduction-to-eosio/index.md), the core components used in this tutorial are:
* [Nodeos](../../glossary/index/#nodeos) - The core daemon which runs in a network of daemons to create a blockchain 
* [Cleos](../../glossary/index/#cleos) - The command line tool to send commands and requests to nodeos
* [Keosd](../../glossary/index/#keosd) - A local secure store for private keys

This tutorial shows how to:
* Create a single node blockchain running on your local machine
* Import the private key to the default *eosio* system account

Once the tutorial is completed you should be able to run a local single node testnet.

## Before you begin
This tutorial requires the following:

* The EOSIO platform software, Click on this link for instructions on [installing EOSIO binaries](https://developers.eos.io/manuals/eos/latest/install/install-prebuilt-binaries)

## Run a Local Single-Node Blockchain
Run a local nodeos instance which produces blocks, creating a local single-node testnet, using these [instructions](https://developers.eos.io/manuals/eos/latest/nodeos/usage/development-environment/local-single-node-testnet).

You can use this local single-node testnet to follow the smart contract guides and for testing your own smart contracts. You can create more advanced local single node testnet with consensus protocols and multi node blockchain configurations [here](https://developers.eos.io/manuals/eos/v2.1/nodeos/usage/development-environment/index) and then look at the [Bios Boot Sequence Tutorial](../../80_tutorials/10_bios-boot-sequence.md) to see how real blockchains are bootstrapped.
 
### The *eosio* default system account
To use a blockchain requires blockchain accounts, when you launch a new EOSIO blockchain it creates a default system account called *eosio*. The *eosio* account is a special account that is used to bootstrap a blockchain. To use the *eosio* account on a local single node blockchain you must add the private key of the *eosio* account to a [wallet.](../../glossary/index/#wallet) You can then authorize transactions for the *eosio* account. Here we use [keosd](../../glossary/index#keosd). If you have not already created a wallet then follow this guide to [create a development wallet](../../30_getting-started-guide/20_local-development-environment/30_development-wallet.md). 


[[warning]]
| The private key is widely known and so any blockchain where the *eosio* account has not been [resigned](../../80_tutorials/10_bios-boot-sequence.md#3-resign-eosio-account-and-system-accounts) is not secure.

[[info]]
| The *eosio* private key is **5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3**

#### Add the *eosio* account private key to a local wallet

Use [Cleos](../../glossary/index/#cleos) to import the default *eosio* account private keys into a local wallet.

```shell
cleos wallet import --name local 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
```

## What's next?

* Create Accounts: [Learn about creating accounts and how accounts are used with smart contracts](20_accounts-and-permissions.md)