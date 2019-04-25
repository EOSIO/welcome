---
title: "4.1 Introduction to System Contracts"
excerpt: ""
---
[block:api-header]
{
  "title": "1. About System Contracts"
}
[/block]
The EOSIO blockchain platform is unique in that the features and characteristics of the blockchain built on it are flexible, that is, they can be changed, or modified completely to suit each business case requirement. Core blockchain features such as consensus, fee schedules, account creation and modification, token economics, block producer registration, voting, multi-sig, etc., are implemented inside smart contracts which are deployed on the blockchain built on the EOSIO platform.

Block.one implements and maintains EOSIO open source platform which contains as an example, the system contracts which encapsulates the base functionality for an EOSIO based blockchain and this tutorial will explain each of them: eosio.bios, eosio.system, eosio.msig, eosio.wrap (formerly known as sudo) and eosio.token.

Just as a heads up, the next step in our journey, after you master the system contracts presented in this tutorial, is to learn how you can modify these system contracts and roll your own custom EOSIO based blockchain.
[block:api-header]
{
  "title": "2. System contracts, system accounts,  priviledged accounts"
}
[/block]
At the genesis of an EOSIO based blockchain, there is only one account present: eosio, which is the main system account. There are other system accounts, which are created by eosio, and control specific actions of the system contracts mentioned earlier. Note that we are introducing the notion of system contract/s and system account/s. Also note that privileged accounts are accounts which can execute a transaction while skipping the standard authorization check. To ensure that this is not a security hole, the permission authority over these accounts is granted to eosio.prods.

As you learned earlier the relation between an account and a contract, we are adding here that not all system accounts contain a system contract, but each system account has important roles in the blockchain functionality, as follows:
[block:parameters]
{
  "data": {
    "h-0": "Account",
    "h-1": "Priviledged",
    "h-2": "Has contract",
    "0-0": "eosio",
    "0-1": "Yes",
    "0-2": "It contains the `eosio.system` contract",
    "1-0": "eosio.msig",
    "1-1": "Yes",
    "1-2": "It contains the `eosio.msig` contract",
    "4-0": "eosio.names",
    "4-1": "No",
    "4-2": "No",
    "6-0": "eosio.prods",
    "6-1": "No",
    "6-2": "No",
    "7-0": "eosio.ram",
    "7-1": "No",
    "7-2": "No",
    "2-0": "eosio.wrap",
    "2-1": "Yes",
    "2-2": "It contains the `eosio.wrap` contract.",
    "5-0": "eosio.bpay",
    "5-2": "No",
    "5-1": "No",
    "3-0": "eosio.token",
    "3-1": "No",
    "3-2": "It contains the `eosio.token` contract.",
    "8-0": "eosio.ramfee",
    "8-1": "No",
    "8-2": "No",
    "9-0": "eosio.saving",
    "9-1": "No",
    "9-2": "No",
    "10-0": "eosio.stake",
    "10-1": "No",
    "11-1": "No",
    "11-0": "eosio.vpay",
    "10-2": "No",
    "11-2": "No",
    "0-3": "The main system account on an EOSIO based blockchain.",
    "h-3": "Description",
    "1-3": "Allows the signing of a multi-sig transaction proposal for later execution if all required parties sign the proposal before the expiration time.",
    "2-3": "Simplifies block producer superuser actions by making them more readable and easier to audit.",
    "3-3": "Defines the structures and actions allowing users to create, issue, and manage tokens on EOSIO based blockchains.",
    "4-3": "The account which is holding funds from namespace auctions.",
    "5-3": "The account that pays the block producers for producing blocks. It assigns 0.25% of the inflation based on the amount of blocks a block producer created in the last 24 hours.",
    "6-3": "The account representing the union of all current active block producers permissions.",
    "7-3": "The account that keeps track of the SYS balances based on users actions of buying or selling RAM.",
    "8-3": "The account that keeps track of the fees collected from users RAM trading actions: 0.5% from the value of each trade goes into this account.",
    "9-3": "The account which holds the 4% of network inflation.",
    "10-3": "The account that keeps track of all SYS tokens which have been staked for NET or CPU bandwidth.",
    "11-3": "The account that pays the block producers accordingly with the votes won. It assigns 0.75% of inflation based on the amount of votes a block producer won in the last 24 hours.",
    "12-0": "eosio.rex",
    "12-1": "No",
    "12-2": "No",
    "12-3": "The account that keeps track of fees and balances resulted from REX related actions execution."
  },
  "cols": 4,
  "rows": 13
}
[/block]

[block:api-header]
{
  "title": "3. Useful commands"
}
[/block]
To view an account status, e.g. eosio, run the following command:
[block:code]
{
  "codes": [
    {
      "code": "cleos get account eosio",
      "language": "shell",
      "name": "Shows account status"
    }
  ]
}
[/block]
If you see an error message like the one below, it means the account is not created yet, in the error below the account `eosio.bios` is not created:
[block:code]
{
  "codes": [
    {
      "code": "error 2019-03-03T07:20:04.601 thread-0  main.cpp:3449                 main                 ] Failed with error: unspecified (0)\nunknown key (boost::tuples::tuple<bool, eosio::chain::name, boost::tuples::null_type, boost::tuples::null_type, boost::tuples::null_type, boost::tuples::null_type, boost::tuples::null_type, boost::tuples::null_type, boost::tuples::null_type, boost::tuples::null_type>): (0 eosio.bios)",
      "language": "text",
      "name": "Error saying eosio.bios account is not created"
    }
  ]
}
[/block]
To view an account's abi, and thus inspect the smart contract associated with it, i.e. its actions and types, run the following command:
[block:code]
{
  "codes": [
    {
      "code": "cleos get abi eosio",
      "language": "shell",
      "name": "Shows account's contract abi"
    }
  ]
}
[/block]
If it displays an error message similar to the one below it means the account doesn't have an abi, meaning the account doesn't have an associated contract:
[block:code]
{
  "codes": [
    {
      "code": "error 2019-03-03T07:22:10.495 thread-0  main.cpp:3449                 main                 ] Failed with error: unspecified (0)\nunknown key (eosio::chain::name): eosio.bios\n",
      "language": "text",
      "name": "Error saying eosio.bios account doesn't have an account deployet"
    }
  ]
}
[/block]