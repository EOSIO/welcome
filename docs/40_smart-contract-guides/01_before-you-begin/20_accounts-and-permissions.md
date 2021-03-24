---
content_title: "Accounts and Permissions"
link_text: "Accounts and Permissions"
---

To use an EOSIO blockchain you need an account. This tutorial introduces accounts, permissions and authorities. Accounts identify participants in the blockchain. You deploy a smart contract to an account and use account permissions to authorize smart contract transactions.

This tutorial introduces the following key concepts:
* [Accounts](../../../glossary/index#account) - Accounts control authentication on the blockchain. See the protocol guide on [accounts and permissions ](../../60_protocol-guides/40_accounts_and_permissions/#2-accounts) for details about how accounts work. Accounts contain permissions, and permissions have authority.  
* [Permission](../../../glossary/index/#permission) and [Authority](../../../glossary/index/#authority) - Permissions control authorization on the blockchain. See the protocol guide on [permissions](../../60_protocol-guides/60_protocol-guides/40_accounts_and_permissions/#3-permissions) for details on how permissions use authority to authorize transactions. 
* Key Pairs  - Paired [public key](../../../glossary/index/#public-key) and [private key](../../../glossary/index/#private-key) cryptographic keys.
* [Cleos](../../../glossary/index#cleos) - The command line tool to send commands and requests to nodeos.
* [Keosd](../../../glossary/index#keosd) - A local secure store for private keys.
* [Signing Transactions](../../60_protocol-guides/20_transactions_protocol/#22-signed-transaction-instance) - Authorizing smart contract action calls.

 This tutorial shows how to:
* Create accounts and key pairs. These accounts may be used in the smart contract guides.
* Generate Key pairs.
* Update account key pairs.

Once the tutorial is completed you should be able to create and use accounts, permissions and keys.

## Before you begin

This tutorial requires the following:
* Access to a running blockchain. Click on this link for instructions on [running a blockchain](10_running-a-blockchain.md)

## Accounts and Permissions

A blockchain account has a human readable name which is between 1 and 12 characters in length. Each account identifies a blockchain participant and the permissions of that participant. Permissions control what EOSIO accounts can do and how actions are authorized.

[[info]]
| Alice has an account called Alice. The Alice account by default has two permissions `owner` and `active`. Alice can also add and [customize permissions](../../60_protocol-guides/40_accounts_and_permissions/#341-custom-permissions). 
The account and permission is written as:
* Alice@owner
* Alice@active

Loading a smart contract requires an account; an account can own one smart contract instance and a smart contract instance must be loaded by an account.

## About Key Pairs

Accounts are stored on the blockchain with their public keys. Each account requires at least one key pair public key and private key. The blockchain uses asymmetric cryptography to verify that the account pushing a transaction has signed the transaction with the matching private key stored in a local wallet.
 
Account authorization is controlled by the public-private key pairs. The public key is stored on the blockchain and the private key is stored locally in a secure [wallet](../../../glossary/index/#wallet), for example [keosd](../../../glossary/index#keosd). 

Signing a transaction with a private key authorizes the blockchain to execute a transaction for the specified account. [Cleos](../../../glossary/index#cleos) commands will automatically look for the required private key in the `keosd` wallet. 

## About Permissions and Authorities

Account authorization is controlled by public-private key pairs. Signing a transaction with a [private key] provides the blockchain with the data used to validate the transaction. If an account permission has the authority and is signed correctly then a smart contract action can be executed. 

`Cleos` commands use the `-p` command switch to specify the account and permission to use for signing a transaction. `Cleos` will look in `keosd` for the private key which corresponds to the specified account and permission.

[[info]]
| Alice wants to use the account called Alice and the `active` permission to sign a `cleos` command. To use this permission add:
-p Alice@active

* If the local `keosd` contains a private key for the active permission of the account then the transaction will be successfully signed and submitted to the blockchain.
* If the private key matches the public key stored on the blockchain the blockchain will try to execute the transaction.
* If the account and permission has the authority to execute the transaction then the transaction should be executed. A record of this transaction and who authorised the transaction is permanently stored on blockchain.

[[warning]]
| Keep your keys safe! Use a wallet to securely store private keys. Keep your private keys private and do not share your private keys with anyone. A private key provides full access to a blockchain account.

## Create a wallet
The following procedure shows you how to create a wallet. 

1. Create a wallet - [How To Create A Wallet](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-create-a-wallet)

To use a wallet and the keys contained in a wallet, the wallet must be **open** and **unlocked**.

## Create Accounts

The following procedure shows you how to create an account after you have a local wallet. Ensure that the local wallet is open and unlocked.

1. Create key pair - [How To Create Key Pairs](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-create-key-pairs)
2. Create the account - [How To Create An Account](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-create-an-account)
3. Import the account private key to the wallet - [How To Import A Key](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-import-a-key)
 
You can now check the account on the blockchain - [How to get account information.](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-get-account-information) 

[[info]]
| You can update account permissions and keys with the [cleos set account](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/set/set-account) command

## What's Next?

Looked at how to write smart contracts in the [Smart Contract Guides.](../40_smart-contract-guides/index.md)