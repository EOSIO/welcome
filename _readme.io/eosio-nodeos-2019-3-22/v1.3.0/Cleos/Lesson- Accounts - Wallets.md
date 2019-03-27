---
title: "Lesson: Accounts & Wallets"
excerpt: ""
---
[block:callout]
{
  "type": "info",
  "body": "This lesson is geared towards use on a private single node testnet (Such as with a Docker container [Docker Quickstart](doc:docker-quickstart)), but will work on a public network with minor modifications.",
  "title": "Important Note"
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "This is a lesson intended to teach **developers** about wallets, keys and accounts at a **low level** for a better understanding of EOSIO."
}
[/block]

[block:api-header]
{
  "title": "Introduction"
}
[/block]
## Lesson Audience

This lesson is for developers who want to learn about wallet and account management, how to use `cleos` to manage wallets and accounts, and how the wallet and account management EOSIO components interact with each other.  Additional information about cleos can be found in the [Cleos Command Reference](doc:command-reference) 

## What You'll Learn 

You'll learn how to create and manage wallets, their keys and then use this wallet to interact with the blockchain through `cleos`.  You will then learn how to create accounts using `cleos`.  The tutorial will introduce you to some of the interaction between `cleos`, `keosd`, and `nodeos` to sign content published to the blockchain.

## Prerequisites

- Built and running copy of [cleos](doc:cleos-overview)  and [keosd](doc:keosd-overview)  on your system. 
- Built and _ready to run_ copy of [nodeos](doc:overview-1) on your system.
- Basic understanding of command line interfaces. 

You can use the [Docker Quickstart](doc:docker-quickstart) for a quick setup which including a set of working environment mentioned above
[block:api-header]
{
  "title": "EOSIO Accounts and Wallets Conceptual Overview"
}
[/block]
The diagram below provides a simple conceptual view of accounts and wallets in EOSIO.  While there are other supported deployment configurations, this view matches the one that we will use for this tutorial.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/646c321-Accounts-and-Wallets-Overview.png",
        "Accounts-and-Wallets-Overview.png",
        1654,
        904,
        "#f9f9f9"
      ]
    }
  ]
}
[/block]
The wallet can be thought of as an encrypted repository of public-private key pairs.  These are needed to sign operations performed on the blockchain.  Wallets and their content are managed by `keosd`.  Wallets are accessed using `cleos`.

An account can be thought of as an on-chain identifier that has access permissions associated with it (i.e., a security principal).  `nodeos` manages the publishing of accounts and account-related actions on the blockchain.  The account management capabilities of `nodeos` are also accessed using `cleos`.

There is no inherent relationship between accounts and wallets.  Accounts do not know about wallets, and vice versa.  Correspondingly, there is no inherent relationship between `nodeos` and `keosd`.  Their basic functions are fundamentally different.  (_Having said that, there are deployment configurations that blur the distinction.  However, that topic is beyond the scope of this tutorial._)

Where overlap occurs is when signatures are required, e.g., to sign transactions.  The wallet facilitates obtaining signatures in a secure manner by storing keys locally in an encrypted store that can be locked.  `cleos` effectively serves as an intermediary between `keosd` key retrieval operations and `nodeos` account (and other) blockchain actions that require signatures generated using those keys.
[block:api-header]
{
  "title": "Creating and Managing Wallets"
}
[/block]
Open your terminal and change to the directory where EOSIO was built.  This will make it easier for us to interact with `cleos`, which is a command line interface for interacting with `nodeos` and `keosd`.
[block:callout]
{
  "type": "info",
  "title": "Note",
  "body": "In case you are using a Docker container setup , you can 'shell' into container by the following:\n\ndocker  exec -it eosio bash (Assumed the docker image called eosio)"
}
[/block]
Please note that `cleos` needs a running instance of `keosd` to interact with, and it will launch an instance of `keosd` the first time that you run it with a subcommand.
[block:callout]
{
  "type": "info",
  "body": "In case you are using the setup from [Docker Quickstart](doc:docker-quickstart), the executables will be included in the PATH. So you would not need to do the following step",
  "title": ""
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cd /path_to_eos/build/programs/cleos",
      "language": "shell"
    }
  ]
}
[/block]
The first thing you'll need to do is create a wallet; use the `wallet create` command of `cleos`. 
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet create --to-console\nCreating wallet: default\nSave password to use in the future to unlock this wallet.\nWithout password imported keys will not be retrievable.\n\"A MASTER PASSWORD\"",
      "language": "shell"
    }
  ]
}
[/block]
A wallet called _default_ is now inside `keosd` and has returned the **master password** for this wallet. Be sure to save this password somewhere safe. This password is used to unlock (decrypt) your wallet file. 

The file for this wallet is named `default.wallet`.  By default, `keosd` stores wallets in the `~/eosio-wallet` folder.    The location of the wallet data folder can be specified on the command line using the `--wallet-dir` argument.

## Managing Multiple Wallets and Wallet Names

`cleos` is capable of managing multiple wallets. Each individual wallet is protected by different wallet master passwords. The example below creates another wallet and demonstrates how to name it by using the `-n` argument.

[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet create -n periwinkle --to-console\nCreating wallet: periwinkle\nSave password to use in the future to unlock this wallet.\nWithout password imported keys will not be retrievable.\n\"A MASTER PASSWORD\"",
      "language": "shell"
    }
  ]
}
[/block]
Now confirm that the wallet was created with your chosen name.
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet list\nWallets:\n[\n  \"default *\",\n  \"periwinkle *\"\n]",
      "language": "shell"
    }
  ]
}
[/block]
It's important to notice the asterisk (*) after each listed wallet, which means that the respective wallet is unlocked. When using `create wallet` the resulting wallet is unlocked by default for your convenience.

Lock that second wallet using `wallet lock`
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet lock -n periwinkle\nLocked: 'periwinkle'",
      "language": "shell"
    }
  ]
}
[/block]
Upon running `wallet list` again, you will see that the asterisk is gone, meaning that the wallet is now locked.
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet list\nWallets:\n[\n  \"default *\",\n  \"periwinkle\"\n]",
      "language": "text"
    }
  ]
}
[/block]
Unlocking a named wallet entails calling `wallet unlock` with an `-n` parameter followed by the name of the wallet and the '--password' parameter  (yes, you can paste the password). Go ahead and grab the master key for the second wallet you created, execute the command below and paste in the master password.
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet unlock -n periwinkle --password YOUR_MASTER_KEY",
      "language": "shell"
    }
  ]
}
[/block]
cleos will let you know that the wallet was unlocked


[block:code]
{
  "codes": [
    {
      "code": "Unlocked: 'periwinkle'",
      "language": "shell"
    }
  ]
}
[/block]
Now check your progress:
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet list\nWallets:\n[\n  \"default *\",\n  \"periwinkle *\"\n]",
      "language": "shell"
    }
  ]
}
[/block]
The _periwinkle_ wallet is followed by an asterisk, so it is now unlocked. 

_**Note:** Interacting with the 'default' wallet using the wallet command does not require the `-n` parameter_

Now stop `keosd`, and then go back to where you were calling `cleos` and run the following command (remember that `cleos` will check that `keosd` is running and will launch an instance of it if it is not).  To stop 'keosd' you can execute the shell commands described below.
[block:code]
{
  "codes": [
    {
      "code": "# Now find the process id for keosd\nps -aef | grep keosd\n\n# and use that process id to kill the running keosd\nkill PID_RETURNED_FROM_LAST_COMMAND",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet list\nWallets:\n[]",
      "language": "shell"
    }
  ]
}
[/block]
Wallets first need to be opened before they can be operated on, including listing them.  The wallets were locked when you shut down `keosd`.  When `keosd` was restarted, the wallet wasn't open.  Run the following commands to open, then list the default wallet.
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet open\n$ cleos wallet list\nWallets:\n[\n  \"default\"\n]",
      "language": "shell"
    }
  ]
}
[/block]
You'll notice in the last response that the default wallet is locked by default.  Unlock it now; you'll need it in the subsequent steps. 
[block:callout]
{
  "type": "info",
  "body": "If you want to open a named wallet, you would run `$ cleos wallet open -n periwinkle"
}
[/block]
Run the `wallet unlock` command using your _default_ wallet's master password. 
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet unlock --password DEFAULT_MASTER_KEY\nUnlocked: 'default'",
      "language": "shell"
    }
  ]
}
[/block]
Check that the wallet is unlocked:
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet list\nWallets:\n[\n  \"default *\"\n]",
      "language": "shell"
    }
  ]
}
[/block]
The wallet is accompanied by an asterisk, so it's unlocked. 

You've learned how to create multiple wallets, and interact with them in `cleos`.  However, an empty wallet doesn't do you much good.  We will now learn to import keys into the wallet. 

## Generating and Importing EOSIO Keys

There are several ways to generate an EOSIO key pair, but this tutorial will focus on the `create key` command in `cleos`.

Generate two public/private key pairs.  Note the general format of the keys.
[block:code]
{
  "codes": [
    {
      "code": "$ cleos create key --to-console\nPrivate key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nPublic key: EOSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n$ cleos create key --to-console\nPrivate key: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nPublic key: EOSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
      "language": "shell"
    }
  ]
}
[/block]
With adding the `--file filename` flag instead of `--to-console`, you can have your keys written to a local file.

You now have two EOSIO keypairs. At this point, these are just arbitrary keypairs and by themselves have no authority.

If you followed all of the previous steps, your _default_ wallet should be open and unlocked.

In this next step, we will import the private keys into the default wallet.  To do this, execute `wallet import` twice, once for each *private key* that was generated earlier.
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet import --private-key PRIVATE_KEY_1",
      "language": "shell"
    }
  ]
}
[/block]
And then again with the second private key
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet import --private-key PRIVATE_KEY_2",
      "language": "shell"
    }
  ]
}
[/block]
If successful, each time `wallet import` command responds with the public key corresponding to your private key, your console should look something like:
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet --private-key import 5Hvgh37WMCWAc4GuyRBiFrk4SArCnSQVMhNtEQVoszhBh6RgdWr\nimported private key for: EOS84jJqXj5XBz3RqLreXZCMxXRKspUadXg3AVy8eb5J2axj8cywc",
      "language": "shell"
    }
  ]
}
[/block]
We can check which keys are loaded by calling `wallet keys` (public keys only) or `wallet private_keys` (private keys and public keys)
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet keys\n[\n\t\"EOS6....\",\n\t\"EOS3....\"\n]\n$ cleos wallet private_keys --password YOUR WALLET PASSWORD\npassword:\n[[\n    \"EOS6....\",\n    \"5KQwr...\"\n  ],\n  [\n    \"EOS3....\",\n    \"5Ks0e...\"\n  ]\n]",
      "language": "shell"
    }
  ]
}
[/block]
the wallet file itself is encrypted, so the wallet will protect these keys when it's locked.  Accessing the keys in a locked wallet requires the master password that was provided to you during wallet creation. 

## Backing up your wallet

Now that your wallet contains keys, it's good to get into the habit of backing up the wallet, e.g., to a flash drive or other media, to protect against the loss of the wallet file.  Without the password, the wallet file is encrypted with high entropy, and the keys inside are incredibly difficult (improbable by all reasonable measures) to access.

You can find your wallet files in the `data-dir`. If you did not specify a `--data-dir` parameter when launching eos, your wallet files are stored in the `~/eosio-wallet` folder.
[block:code]
{
  "codes": [
    {
      "code": "$ cd ~/eosio-wallet && ls\nblockchain   blocks   config.ini   default.wallet   periwinkle.wallet",
      "language": "text"
    }
  ]
}
[/block]
If you've been following the steps of this tutorial, you will see the two files, `default.wallet` and `periwinkle.wallet`.  Save these files in a safe location.
[block:api-header]
{
  "title": "Creating an Account"
}
[/block]
Performing actions on the blockchain requires the use of accounts.  We use `cleos` to request `nodeos` to create accounts and publish them on the blockchain.  At this point in our tutorial, we need to start `nodeos`.  The following command will start a single node testnet.  See [Creating and Launching a Single Node Testnet](doc:local-single-node-testnet) for more on setting up a local environment.

 For this part of the tutorial, we need keosd and nodeos to run simultaneously.  Presently, the default port for `keosd` and `nodeos` is the same (port 8888).  To simplify running nodeos for this part of the tutorial, we will change the port for `keosd` to 8899.  There are two ways that we can do this:

1.  Edit the `keosd` config file (`~/eosio-wallet/config.ini`) and change the http-server-address property to:
   
       `http-server-address = 127.0.0.1:8899 `
  
2.  Start keosd using the command line argument --http-server-address=localhost:8899

Restart keosd using the comand line argument:
[block:code]
{
  "codes": [
    {
      "code": "$ pkill keosd\n$ keosd --http-server-address=localhost:8899",
      "language": "text"
    }
  ]
}
[/block]

     
    
 Unlock your default wallet (it was locked when keosd was restarted).  Since keosd was started listening on port 8899, you will need to use the --wallet-url command line argument to cleos.
  
      cleos --wallet-url=http://localhost:8899 wallet unlock
 
When prompted for the password, enter the wallet password generated in the previous section when the wallet was created.

To start `nodeos`, open a new terminal window, go to the folder that contains your `nodeos` executable, and run the following:
[block:code]
{
  "codes": [
    {
      "code": "$ cd eos/build/programs/nodeos\n$ nodeos -e -p eosio --plugin eosio::chain_api_plugin --plugin eosio::history_api_plugin",
      "language": "shell"
    }
  ]
}
[/block]
In this tutorial, `eosio` is the authorizing account.  The actions performed on the blockchain must be signed using the keys associated with the `eosio` account.  The `eosio` account is a special account used to bootstrap EOSIO nodes.  The keys for this account can be found in the `nodeos` config file, located at `~/.local/share/eosio/nodeos/config/config.ini` on Linux platforms, and `~/Libraries/Application Support/eosio/nodeos/config/config.ini` on MacOS.

Or you can just use the command below
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet import --private-key 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3",
      "language": "shell"
    }
  ]
}
[/block]
Now we can create the account.  Here is the structure of the `cleos create account` command.
[block:code]
{
  "codes": [
    {
      "code": "$ cleos create account eosio NEW_ACCOUNT OWNER_KEY ACTIVE_KEY\n",
      "language": "shell"
    }
  ]
}
[/block]
- `authorizing_account` is the name of the account that will fund the account creation, and subsequently the new account.
- `new_account` is the name of the account you would like to create
- `owner_key` is a public key to be assigned to the **owner** authority of the account.  (See [Accounts and Permissions](https://developers.eos.io/eosio-nodeos/docs/accounts-and-permissions))
- `active_key` is a public key to be assigned to the **active** authority of your account, and the second one will be permissioned for the active authority of your account. 

We need a name for our new account.  Account names must conform to the following guidelines:

- Must be less than 13 characters
- Can only contain the following symbols:   .12345abcdefghijklmnopqrstuvwxyz 

We will use the name "myaccount" for the new account.

We will use the public keys that you generated above and imported into your wallet (recall that the public keys begin with `EOS`). The keys are arbitrary until you have assigned them to an authority.  However, once assigned, it is important to remember the assignments.  Your owner key equates to full control of your account, whereas your active key equates to full access over funds in your account. 

Use `cleos create account` to create your account:
[block:code]
{
  "codes": [
    {
      "code": "$ cleos --wallet-url=http://localhost:8899 create account eosio myaccount PUBLIC_KEY_1 PUBLIC_KEY_2\n",
      "language": "shell"
    }
  ]
}
[/block]
If successful, you will see output similar to the following.
[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 7f1c6b87cd6573365a7bb3c6aa12f8162c3373d57d148f63f2a2d3373ad2fd54  352 bytes  102400 cycles\n#         eosio <= eosio::newaccount            {\"creator\":\"eosio\",\"name\":\"myaccount\",\"owner\":{\"threshold\":1,\"keys\":[{\"key\":\"EOS5kkAs8HZ88m2N7iZWy4J...",
      "language": "shell"
    }
  ]
}
[/block]