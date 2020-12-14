---
content_title: FAQ
link_text: FAQ
---

This FAQ contains frequent questions and requests from the EOSIO community. If you don't see what you need here, search for the topic on the Developers Portal, visit the [EOSIO Stack Exchange](https://eosio.stackexchange.com/) forum, or join our [community Telegram](https://t.me/EOSproject) chat.

## Blockchain

### What are the backpressure signals indicating a blockchain is being fully utilized?

EOSIO-based blockchains are resilient to all types of situations created by real world scenarios. In case a blockchain is fully utilized, the only backpressure signal is that the transactions start to drop.

When you send a transaction to the blockchain, you can set a maximum transaction timeout value of 60 minutes. As soon as the blockchain receives the transaction, under normal uncongested operation, the transaction is processed right away. However, if the transaction is not processed right away, most likely because of congested operation, it is placed in the unapplied transactions queue (also known as incoming transactions queue). If the expiration period for a queued transaction waiting is met, the transaction is dropped from the queue, with no chance to be applied again. In this case, you need to resubmit the transaction to the blockchain. The default maximum size of the incoming transaction queue is 1020 MiB and it can be configured with the `incoming-transaction-queue-size-mb` parameter of the producer plugin. Exceeding this value subjectively drops the transaction with system resources exhaustion.

### Can you wipe/refresh a blockchain environment?

Yes, you can wipe a blockchain by the following actions:

1. Stop the `nodeos` service (ctrl+C)
2. Remove the content of data folder
3. Restart the `nodeos` service 

See the [nodeos manual](https://developers.eos.io/manuals/eos/latest/nodeos/index) for detailed information on how to use `nodeos`.  

Nodeos stores runtime data (e.g., shared memory and log content) in a data folder which can be optionally specified with the `-d` option when invoking nodeos. The default location of the data folder depends on your operating system.. The location of the data folder depends on your system:
* Mac OS -  ~/Library/Application\ Support/eosio/nodeos/data
* Linux  -  ~/.local/share/eosio/nodeos/data
* Configured - The `nodeos` --data-dir command line argument specifies the data folder location

### How to replicate a production blockchain environment in a local development environment?

The way to set up a local development environment that replicates a production environment is by setting up a local single-node blockchain configuration running on a single host. In the single node blockchain, you run a nodeos instance that acts as a block producing node.

To set up a local single-node blockchain configuration, follow the instructions in the below topic:

[Local Single-node Testnet](https://developers.eos.io/manuals/eos/v2.0/nodeos/usage/development-environment/local-single-node-testnet)

You can also use the [Block.one's official EOSIO Testnet.](https://testnet.eos.io/) To learn how to set up an account and use the EOSIO Testnet click here [EOSIO Testnet Quick Start Guide.](https://developers.eos.io/welcome/latest/quick-start-guides/testnet-quick-start-guide/index)

### What happens when there is a fork and how does this manifest itself in State History Plugin (SHiP)?

As a SHiP consumer, if you see the block numbers going backwards, it means a fork happened. Therefore, the forks are distinguishable and the consumers of the SHiP stream can handle them properly.

## Accounts and Keys

### What is the relationship between keys, eosio accounts, and smart contracts?

EOSIO accounts identify unique individuals or entities within an EOSIO blockchain. Keys in EOSIO are binary strings represented in Base58 used for signing and verification of transactions, blocks, and other messages. Keys are created within a digital wallet associated with an account. Since account ownership is defined solely by the account name, the keys associated with an account can be updated without compromising security. A novel permission scheme involving accounts, permissions, and authority tables determine what accounts can do and how the actions that make a transaction are authorized. To that end, each account is assigned a hierarchical permission structure and each permission is assigned a pair of keys (a public key and a private key) used for signing and verification. 

A smart contract is a low-level software library that contains the implementation of the actions that make a transaction. It also defines how the data that is accessed and processed by the actions are stored. A smart contract is implemented in a high-level language such as C++ and compiled into a WebAssembly (WASM) binary. Thereafter, smart contracts can be deployed and run within an account’s sandbox on the blockchain.

Further Reading
For more information on this topic, see the [Accounts and Permissions](https://developers.eos.io/welcome/latest/protocol/accounts_and_permissions) section.

### How can I change private keys for accounts?

Use the [cleos set account](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/set/set-account) command.

`cleos set account permission <accountname - account name> <permission - permission name> <authority - json structure> <parent - owner?> -p authorizing permission`

```sh
cleos set account permission accountname active '{"threshold": 1, "keys": [{"key": "NEW_ACTIVE_PUBLIC_KEY", "weight": 1}]}' owner
```

which can be simplified to

```sh
cleos set account permission <accountname> <permission> NEW_ACTIVE_PUBLIC_KEY owner -p accountname@owner
```

to update the key pairs associated with an account permission. This command replaces the existing authority structure associated with the permission. Keys are stored in the authority, which is referenced by the permission, which is referenced by the account. See [Account and Permissions](https://developers.eos.io/welcome/latest/protocol/accounts_and_permissions) for details.

If you are using a third party wallet with a UI, they may provide the ability to update your account public and private key pairs.

## Smart Contracts

### How to optimize smart contracts built to maximise throughput/performance?

For guidelines on how to build a performant smart contract, see the following resources:

* [For resource planning](https://developers.eos.io/manuals/eosio.cdt/latest/best-practices/resource-planning)
* [For data design and migration](https://developers.eos.io/manuals/eosio.cdt/latest/best-practices/data-design-and-migration)
* [For securing your smart contract](https://developers.eos.io/manuals/eosio.cdt/latest/best-practices/securing_your_contract)

### What are the onboarded system smart contracts and their versions? What other smart contracts are included with the deployment?

EOSIO offers a few smart contracts which should be used as reference smart contracts, namely:

* eosio.bios
* eosio.boot
* eosio.system
* eosio.token
* eosio.wrap
* eosio.msig

You can customize them to your business needs and deploy any number of them when you launch your EOSIO-based blockchain. We recommend using the latest released versions of the smart contracts.

Further Reading
[EOSIO.contracts](https://developers.eos.io/manuals/eosio.contracts/latest/index)

### Can we assign control of the eosio.token contract to any account?
Yes, you can deploy the eosio.token smart contract to any account for which you have at least the active private key.

### Why is the onblock() action callable on certain EOSIO system contracts?

You should not call `onblock()` action yourself, but as a blockchain developer you can define its semantics by changing its implementation to fit your blockchain business requirements. The `onblock()` action is called by the system on every block. In this way, the `onblock()` acts as a heart beat for the system contract and allows it to always execute all necessary actions (i.e. producer pay) to ensure a healthy system behavior.

See [onblock](https://developers.eos.io/manuals/eosio.contracts/latest/action-reference/eosio.system/index/?query=onblock&page=1#onblock)

## Transactions

### What happens when we send too many transactions to the blockchain and overwhelm it?

During congestion mode, transactions sent to the blockchain will likely be placed in the unapplied transactions queue (also known as incoming transactions queue) from which they will be speculatively processed and if they are valid they will make it to the next produced block. However, if there are too many transactions in the queue there is a chance that they will expire before they will be processed by the blockchain and thus they will be dropped, in which case you will have to resubmit them.

### Are there any plans to include transaction failure tracing in state history (github feature request)?

Yes, this is already supported in the upcoming EOSIO release. The original `transaction_tracing` logger has been replaced with two new loggers: 1. `transaction_success_tracing` and 2. `transaction_failure_tracing` logger, which provides detailed logs for successful or failed transaction confirmations from relay nodes on the P2P network, respectively. The node operator can selectively choose which logger to enable based on whether successful or failed transaction logs are desired.

### Are there any metrics for dropped transactions?

No, there are no metrics currently on blockchain for dropped transactions. However, it can be done by enabling the logging level, which logs dropped transactions, and then monitor the dropped transactions log entries.

### Should we use the block number returned by RPC to confirm if a transaction is added to a block?

No. Under normal circumstances, the block number you receive is a speculative block number and you should not rely on it to decide if your transaction was added to the block or not.

To find out if a transaction was included into a block after you sent the transaction with a custom or default expiration time, check if the transaction ID was included in a block and then wait for the block to become irreversible.

### How do we best determine if a transaction is in the blockchain so that we do not create duplicates with retries?

To find out if a transaction was included into a block, after you sent the transaction with a custom or default expiration time, check if the transaction ID was included in a block and then wait for _*the block to become irreversible*_.

_*Important*_: If you resubmit the same transaction while the first one you sent did not expire, the blockchain will not execute it twice. It is guaranteed it will be executed only once if the blockchain will have a chance to apply the transaction. But if you resign the transaction and resend it, then the blockchain will see it as a different transaction and will attempt to apply it as it does for any new transaction.

### How to ensure transactions entering into the blockchain are being confirmed? How to determine if a transaction needs to be requeued?

There are a few ways to confirm if a transaction made to a block; you can find them enumerated below. After you are sure the transaction is part of a block, you have to wait for the block to become irreversible. A block is irreversible when its height is lower than the current Last Irreversible Block (LIB). If the transaction did not make it to a block after its expiration time is met, you should re-send it to the blockchain.

Here are a few ways to check if a transaction made it to a block:

* Poll [get_block](https://developers.eos.io/manuals/eos/latest/nodeos/plugins/chain_api_plugin/api-reference/index#operation/get_block) of the Chain API and search for the transaction ID in the list of transactions included in the block. If the transaction expiration time is reached and your transaction ID was not found in any block, then you have to resend the transaction. Otherwise, if you find the transaction ID in a block then you can wait for the block to become irreversible. Only then you are 100% sure the transaction will make it in the blockchain.
* Poll [get_block](https://developers.eos.io/manuals/eos/latest/nodeos/plugins/trace_api_plugin/api-reference/index) of the Trace API and search for the transaction ID in the list of transactions included in the block. If the transaction expiration time is reached and your transaction ID was not found in any block then you have to resend the transaction. Otherwise, if you find the transaction ID in a block then you can wait for the block to become irreversible. Only then you are 100% sure the transaction will make it in the blockchain.
* Use third party tools which allow you to do that. One example is dfuse which provides an [end-point](https://docs.dfuse.io/eosio/public-apis/reference/rest/post-chain-push_transaction/) allowing you to probe the transactions. 

### How to reliably determine finality of transaction?

Finality of a transaction can be determined when the transaction ID is part of an irreversible block.

For more information on the EOSIO consensus model, see [Consensus Protocol.](https://developers.eos.io/welcome/latest/protocol/consensus_protocol/)

### How to reliably determine when to do a transaction retry?

If the transaction did not make it into any block and its expiration time was met then you can retry.
