---
title: "Getting Started with Smart Contracts"
excerpt: ""
---
[block:callout]
{
  "type": "warning",
  "body": "Please [install EOSIO](https://developers.eos.io/eosio-nodeos/docs/docker-quickstart) if you have not already,"
}
[/block]

[block:api-header]
{
  "title": "Step 1: Install Contract Development Toolkit (CDT)"
}
[/block]
[EOSIO Contract Development Toolkit](https://github.com/EOSIO/eosio.cdt) - Follow Installation instructions and proceed. The `eosio-cpp` utility that compiles contracts and generates ABI files is included in this toolkit. 

First clone
```
git clone --recursive https://github.com/eosio/eosio.cdt --branch v1.2.1 --single-branch
cd eosio.cdt
```

Now run build.sh and provide the core symbol  for the EOSIO blockchain that intend to deploy to. build.sh will install any dependencies that are needed.

```
./build.sh <CORE_SYMBOL>
```

Finally, install the build 
[block:callout]
{
  "type": "info",
  "body": "This install will install the core to /usr/local/eosio.cdt and symlinks to the top level tools (compiler, ld, etc.) to /usr/local/bin"
}
[/block]
```
$ sudo ./install.sh
```
[block:api-header]
{
  "title": "Step 2: Start Your Node"
}
[/block]
If you're using docker and you're container isn't running, run the following.

```
docker start eosio
```

You can start your own single-node blockchain with this single command if you're running nodeos locally.

```
$ nodeos -e -p eosio --plugin eosio::chain_api_plugin \
        --plugin eosio::history_api_plugin
```

This command sets many flags and loads some optional plugins which we will need for the rest of this tutorial. Assuming everything worked properly, you should see a block generation message every 0.5 seconds.  

On Docker, 

```
docker logs --tail 25 eosio
```

```
...
3165501ms thread-0   producer_plugin.cpp:944       produce_block        ] Produced block 00000a4c898956e0... #2636 @ 2018-05-25T16:52:45.500 signed by eosio [trxs: 0, lib: 2635, confirmed: 0]
3166004ms thread-0   producer_plugin.cpp:944       produce_block        ] Produced block 00000a4d2d4a5893... #2637 @ 2018-05-25T16:52:46.000 signed by eosio [trxs: 0, lib: 2636, confirmed: 0]
...
```

[block:api-header]
{
  "title": "Step 3: Create a Wallet"
}
[/block]
A wallet is a repository of private keys necessary to authorize actions on the blockchain.  These keys are stored on disk encrypted using a password generated for you.  This password should be stored in a secure password manager or written down. 
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet create --to-console\nCreating wallet: default\nSave password to use in the future to unlock this wallet.\nWithout password imported keys will not be retrievable.\n\"PW5JuBXoXJ8JHiCTXf....\"",
      "language": "shell"
    }
  ]
}
[/block]
Your wallet will automatically lock after a period of time, here's how you unlock it
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet unlock\npassword:",
      "language": "text"
    }
  ]
}
[/block]
For security purposes it is generally best to leave your wallet locked when you are not using it.  To lock your wallet without shutting down `nodeos` you can do:
[block:code]
{
  "codes": [
    {
      "code": "cleos wallet lock\nLocked: default",
      "language": "shell"
    }
  ]
}
[/block]
You will need your wallet unlocked for the rest of this tutorial.

## Load the Tutorial Key

The private blockchain launched in the steps above is created with a default initial key which must be loaded into the wallet (provided below) 
[block:code]
{
  "codes": [
    {
      "code": "$ cleos wallet import --private-key 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3\nimported private key for: EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 4: Load BIOS Contract"
}
[/block]
Now that we have a wallet with the key for the `eosio` account loaded, we can set a default system contract.  For the purposes of development, the default `eosio.bios` contract can be used.  This contract enables you to have direct control over the resource allocation of other accounts and to access other privileged API calls. In a public blockchain, this contract will manage the staking and unstaking of tokens to reserve bandwidth for CPU and network activity, and memory for contracts. 

The `eosio.bios` contract can be found in the `contracts/eosio.bios` folder of your EOSIO source code.  The command sequence below assumes it is being executed from the root of the EOSIO source, but you can execute it from anywhere by specifying the full path to `${EOSIO_SOURCE}/build/contracts/eosio.bios`.

If you're using docker, the command is:
```
$ cleos set contract eosio contracts/eosio.bios -p eosio@active
Reading WAST...
Assembling WASM...
Publishing contract...
executed transaction: 414cf0dc7740d22474992779b2416b0eabdbc91522c16521307dd682051af083  4068 bytes  10000 cycles
#         eosio <= eosio::setcode               {"account":"eosio","vmtype":0,"vmversion":0,"code":"0061736d0100000001ab011960037f7e7f0060057f7e7e7e...
#         eosio <= eosio::setabi                {"account":"eosio","abi":{"types":[],"structs":[{"name":"set_account_limits","base":"","fields":[{"n...
```

If you built from source, the command is:
```
$ cleos set contract eosio build/contracts/eosio.bios -p eosio@active
Reading WAST...
Assembling WASM...
Publishing contract...
executed transaction: 414cf0dc7740d22474992779b2416b0eabdbc91522c16521307dd682051af083  4068 bytes  10000 cycles
#         eosio <= eosio::setcode               {"account":"eosio","vmtype":0,"vmversion":0,"code":"0061736d0100000001ab011960037f7e7f0060057f7e7e7e...
#         eosio <= eosio::setabi                {"account":"eosio","abi":{"types":[],"structs":[{"name":"set_account_limits","base":"","fields":[{"n...
```

The result of this command sequence is that `cleos` generated a transaction with two actions, `eosio::setcode` and `eosio::setabi`.  

The code defines how the contract runs and the abi describes how to convert between binary and json representations of the arguments.  While an abi is technically optional, all of the EOSIO tooling depends upon it for ease of use.  

Any time you execute a transaction you will see output like:
```
executed transaction: 414cf0dc7740d22474992779b2416b0eabdbc91522c16521307dd682051af083  4068 bytes  10000 cycles
#         eosio <= eosio::setcode               {"account":"eosio","vmtype":0,"vmversion":0,"code":"0061736d0100000001ab011960037f7e7f0060057f7e7e7e...
#         eosio <= eosio::setabi                {"account":"eosio","abi":{"types":[],"structs":[{"name":"set_account_limits","base":"","fields":[{"n...
```

This can be read as: The action `setcode` as defined by `eosio` was executed by `eosio` contract with `{args...}`.

```
#         ${executor} <= ${contract}:${action} ${args...}
> console output from this execution, if any
```

As we will see in a bit, actions can be processed by more than one contract.

The last argument to this call was `-p eosio@active`.  This tells `cleos` to sign this action with the active authority of the `eosio` account, i.e., to sign the action using the private key for the `eosio` account that we imported earlier. 
[block:api-header]
{
  "title": "Step 5: Create Accounts"
}
[/block]
Now that we have setup the basic system contract, we can start to create our own accounts.  We will create two accounts, `user` and `tester`, and we will need to associate a key with each account.  In this example, the same key will be used for both accounts.

To do this we first generate a key for the accounts. 

```
$ cleos create key --to-console
Private key: 5Jmsawgsp1tQ3GD6JyGCwy1dcvqKZgX6ugMVMdjirx85iv5VyPR
Public key: EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4
```

Then we import this key into our wallet:
```
$ cleos wallet import --private-key 5Jmsawgsp1tQ3GD6JyGCwy1dcvqKZgX6ugMVMdjirx85iv5VyPR
imported private key for: EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4
```
**NOTE:** Be sure to use the actual key value generated by the `cleos` command and not the one shown in the example above!

Keys are not automatically added to a wallet, so skipping this step could result in losing control of your account.

### Create Two User Accounts

Next we will create two accounts, `user` and `tester`, using the key we created and imported above.

```
$ cleos create account eosio user EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4 EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4
executed transaction: 8aedb926cc1ca31642ada8daf4350833c95cbe98b869230f44da76d70f6d6242  364 bytes  1000 cycles
#         eosio <= eosio::newaccount            {"creator":"eosio","name":"user","owner":{"threshold":1,"keys":[{"key":"EOS7ijWCBmoXBi3CgtK7DJxentZZ...

$ cleos create account eosio tester EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4 EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4
executed transaction: 414cf0dc7740d22474992779b2416b0eabdbc91522c16521307dd682051af083 366 bytes  1000 cycles
#         eosio <= eosio::newaccount            {"creator":"eosio","name":"tester","owner":{"threshold":1,"keys":[{"key":"EOS7ijWCBmoXBi3CgtK7DJxentZZ...
```
**NOTE:** The `create account` subcommand requires two keys, one for the OwnerKey (which in a production environment should be kept highly secure) and one for the ActiveKey.  In this tutorial example, the same key is used for both.

Because we are using the `eosio::history_api_plugin` we can query all accounts that are controlled by our key:

```
$ cleos get accounts EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4
{
  "account_names": [
    "tester",
    "user"
  ]
}
```
[block:api-header]
{
  "title": ""
}
[/block]