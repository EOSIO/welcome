
[[info]]
|
This article assumes you have installed the EOSIO software and are familiar with using the EOSIO nodeos and cleos tools. It is recommended that you have completed [the Getting Started section](https://developers.eos.io/eosio-home/docs)
# Introduction

This tutorial is a guide for monitoring the status of transactions on the blockchain. 

As an example, we will show how an application can monitor EOS token transfers, how a transaction state changes, how this affects the blockchain, and when a transaction is deemed irreversible. The example will show the transfer of tokens using standard-conforming EOSIO token contracts. The eosio.token contract conforms to this standard. 


# Running Nodeos

It is recommended that a local instance of nodeos is used to monitor activity. This local instance will connect to the blockchain, and when run with the state history plugin, it will collect the history of actions on the blockchain.
[[info]]
|
The local instance in this tutorial will be run as a non-producing node see [Non-Producing Node](https://developers.eos.io/eosio-nodeos/docs/environment-non-producing-node) for more details.
Nodeos can be run in three modes:

   1. **Speculative**: In this mode, you can see transactions and state changes up to the current head block along with changes in the pending block. The state changes in the pending block are also included in the chain state file. 

   2. **Head**: In this mode, you can see transactions and state changes up to the current head block. This node will produce a pending block, though the pending block is not included in the chain state file.

   3. **Read-only**: In this mode, mode you can see transactions and state changes up to the current head block. This node will not produce a pending block.

[[info | Info]]
| * The **Speculative** mode is the default mode.
| * The chain state file is a memory mapped file containing the state of the blockchain for each block. A record of chain state is kept for each block going back to the last irreversible block. 
| * The pending block is the block currently being built by a producing node, transactions are added to the pending block as they are received and processed. The pending block becomes the head block once it is written to the blockchain. Pending blocks are discarded when in **Head** mode. Pending blocks are not produced when in **Read-only** mode. 

Nodes used for monitoring transactions should be run in:
 - **Speculative** mode to see transactions as they arrive (Confirmed and unconfirmed)
 - **Read-only** mode to see transactions once they are recorded in the blockchain (Confirmed only)

For more information see [Read Modes](https://developers.eos.io/eosio-nodeos/docs/read-modes)
[[warning]]
|
A transaction is only complete once it has a status of executed and the block containing the transaction is irreversible.
A transaction is confirmed once it has been written to a block on the blockchain.
A transaction is unconfirmed if it has been received by nodeos but has not yet been written to a block on the blockchain.
A transaction may also fail or expire.
 ## Transaction States

Transactions can have the following states:

- **executed**: The transaction has succeeded, no error handler executed
- **soft_fail**: The transaction has objectively failed (not executed) and the error handler executed 
 successfully (onerror)
- **hard_fail**: The transaction has objectively failed and error handler objectively failed, thus, no state change occurred (onerror also failed)
- **delayed**: The transaction is delayed/deferred/scheduled for future execution
- **expired**: The transaction is expired and the storage space refunded to the user

A transaction is not executed until the status is executed, and the transaction can be cancelled up until it is executed, failed or expired, i.e., while it is waiting to be executed.

Transactions can be delayed for **up to** 45 days, these are known as `deferred transactions`,  and the delay can **only** be set when the transaction is generated. A `deferred transaction` can be cancelled at any time before it is executed. For more information about deferred transactions, see [Communication Model](doc:communication-model) 
[[warning]]
|
A transaction may be executed, but only when the block containing the transaction is irreversible can you be sure that the operation is final and complete. A block is irreversible if the block number is less than the block number of the last irreversible block (LIB). The last irreversible block (LIB) is the most recent block which has been acknowledged by 2/3 of the block producers.
## Tracking your transaction

It is always possible that transactions similar to your transactions are processed while you are monitoring the public mainnet. Ensure that you use ALL identifying fields to look at the right transaction. 

Some of the fields you should use to identify a transaction are: transaction_id, account, name, data, to, receiver, memo, transaction_id. 

## Ensuring a Transaction is complete and final

When the block containing a transaction has a `"block_num"` <= `"last_irreversible_block"`, then the transaction is also irreversible.

Once the last irreversible block has moved past the expiration time of a transaction, you can safely mark a transaction as **failed**.

## Handling Errors

Sometimes, network issues will cause a transaction to fail and never be included in a block. Your internal database will need to know when this has happened so that it can inform the user and/or try again. If you do not get an immediate error when you submit your local transfer, then you must wait for the transaction to expire. Every transaction has an "expiration", after which the transaction can never be applied. Once the last irreversible block has moved past the expiration time, you can safely mark your attempted withdrawal as failed and not worry about it "floating around the ether" to be applied when you least expect.

## Monitoring Options

Now that we understand the various states that a transaction can be in, and how this relates to blockchain and the last irreversible block (LIB), we can look at the various options for monitoring transactions and their current state. 

In part II, [Monitoring with State History Plugin,](doc:monitoring-with-state-history) we will discuss monitoring state using the state history plugin.

In part III, [Monitoring with 3rd Party plugins,](doc:monitoring-with-3rd-party) we will discuss 3rd party plugins which may also be used for monitoring state. 