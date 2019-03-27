---
title: "4.2 eosio.bios"
excerpt: ""
---
The `eosio.bios` is the first sample of system smart contract provided by `block.one` through the EOSIO platform. It is a minimalist system contract because it only supplies the actions that are absolutely critical to bootstrap a chain and nothing more. This allows for a chain agnostic approach to bootstrapping a chain.

The actions implemented and publicly exposed by `eosio.bios` system contract are: setpriv, setalimits, setglimits, setprods, setparams, reqauth, setabi.
[block:parameters]
{
  "data": {
    "h-0": "Action name",
    "h-1": "Action description",
    "0-0": "setpriv",
    "1-0": "setalimits",
    "2-0": "setglimits",
    "3-0": "setprods",
    "4-0": "setparams",
    "5-0": "reqauth",
    "6-0": "setabi",
    "0-1": "Set privilege status for an account.",
    "1-1": "Set the resource limits of an account",
    "2-1": "Not implemented yet.",
    "3-1": "Set a new list of active producers, that is, a new producers' schedule.",
    "4-1": "Set the blockchain parameters.",
    "5-1": "Check if an account has authorization to access the current action.",
    "6-1": "Set the abi for a contract identified by an account name."
  },
  "cols": 2,
  "rows": 7
}
[/block]
The previous actions are enough to serve the functionality of a basic blockchain, however, a keen eye would notice that the actions listed above do not allow for creation of an account, nor updating permissions, and other important features. As we said, this sample system contract is minimalist in its implementation, therefore it relies also on some native EOSIO actions. These native actions are not implemented in the `eosio.bios` system contract, they are implemented at the EOSIO chain core level. In the `eosio.bios` contract they are simply declared and have no implementation, so they can show in the contracts ABI definition, and therefore users can push these actions to the account that holds the `eosio.bios` contract. When one of these actions are pushed to the chain, to the `eosio.bios` contract account holder, via a `cleos` command for example, the corresponding native action is executed by the blockchain first, [see the code here](https://github.com/EOSIO/eos/blob/3fddb727b8f3615917707281dfd3dd3cc5d3d66d/libraries/chain/apply_context.cpp#L58), and then the `eosio.bios` contract `apply` method is invoked, [see the code here](https://github.com/EOSIO/eos/blob/3fddb727b8f3615917707281dfd3dd3cc5d3d66d/libraries/chain/apply_context.cpp#L69), but having no implementation and not being part of the `EOSIO_DISPATCH`, at the contract level, this action will be a NOP, it will do nothing when called from core EOSIO code.
We will see in the next tutorial how we can actually implement any of these actions, and hook them into the `EOSIO_DISPATCH` to customize them to meet specific needs.

Below are listed the actions which are declared in the `eosio.bios` contract, mapped one-to-one with the native EOSIO actions, but having no implementation at the contract level:
[block:parameters]
{
  "data": {
    "h-0": "Action name",
    "h-1": "Description",
    "0-0": "newaccount",
    "0-1": "Called after a new account is created. This code enforces resource-limit rules for new accounts as well as new account naming conventions.",
    "1-0": "updateauth",
    "1-1": "Updates the permission for an account.",
    "2-0": "deleteauth",
    "2-1": "Delete permission for an account.",
    "5-0": "canceldelay",
    "4-0": "unlinkauth",
    "4-1": "Assigns a specific action from a contract to a permission you have created.",
    "5-1": "Allows for cancellation of a deferred transaction.",
    "3-0": "linkauth",
    "3-1": "Assigns a specific action from a contract to a permission you have created.",
    "6-0": "onerror",
    "7-0": "setcode",
    "7-1": "Allows for update of the contract code of an account.",
    "6-1": "Called every time an error occurs while a transaction was processed."
  },
  "cols": 2,
  "rows": 8
}
[/block]