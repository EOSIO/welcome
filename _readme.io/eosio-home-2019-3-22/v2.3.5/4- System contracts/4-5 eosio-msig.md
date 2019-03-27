---
title: "4.5 eosio.msig"
excerpt: ""
---
The `eosio.msig` allows for the creation of proposed transactions which require authorization from a list of accounts, approval of the proposed transactions by those accounts required to approve it, and finally, the execution of the approved transactions on the blockchain.

The flow to propose, review, approve and then executed a transaction is describe in details [here](https://github.com/EOSIO/eosio.contracts/tree/master/eosio.wrap#212-propose-the-transaction-to-create-the-eosiowrap-account), and goes like this:
- first you create a transaction json file, 
- then you submit this proposal to the `eosio.msig` contract, and you also insert the account permissions required to approve this proposal into the command that submits the proposal to the blockchain,
- the proposal then gets stored on the blockchain by the `eosio.msig` contract, and is accessible for review and approval to those accounts required to approve it.
- After each of the appointed accounts required to approve the proposed transactions reviews and approves it, you can execute the proposed transaction.  The `eosio.msig` contract will execute it automatically, but not before validating that the transaction has not expired, it is not cancelled, and it has been signed by all the permissions in the initial proposal's required permission list.

These are the actions implemented and publicly exposed by the `eosio.msig` contract:
[block:parameters]
{
  "data": {
    "h-0": "Action name",
    "h-1": "Action description",
    "0-0": "propose",
    "1-0": "approve",
    "2-0": "unapprove",
    "3-0": "cancel",
    "4-0": "exec",
    "5-0": "invalidate",
    "0-1": "Creates a proposal containing one transaction.",
    "1-1": "Approves an existing proposal.",
    "2-1": "Revokes an existing proposal.",
    "3-1": "Cancels an existing proposal.",
    "4-1": "Allows an account to execute a proposal.",
    "5-1": "Invalidate proposal."
  },
  "cols": 2,
  "rows": 6
}
[/block]