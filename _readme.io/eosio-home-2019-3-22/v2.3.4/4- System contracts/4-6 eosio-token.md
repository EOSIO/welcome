---
title: "4.6 eosio.token"
excerpt: ""
---
The `eosio.token` contract defines the structures and actions that allow users to create, issue, and manage tokens on an EOSIO based blockchain.

These are the public actions the `eosio.token` contract is implementing:
[block:parameters]
{
  "data": {
    "h-0": "Action name",
    "h-1": "Action description",
    "0-0": "create",
    "1-0": "issue",
    "2-0": "open",
    "3-0": "close",
    "4-0": "transfer",
    "5-0": "retire",
    "0-1": "Allows an account to create a token in a given supply amount.",
    "1-1": "This action issues to an account a specific quantity of tokens.",
    "2-1": "Allows a first account to create another account with zero balance for specified token at the expense of first account.",
    "3-1": "This action is the opposite for `open` action, it closes the specified account for specified token.",
    "4-1": "Allows an account to transfer to another account the specified token quantity. One account is debited and the other is credited with the specified token quantity.",
    "5-1": "This action is the opposite for `create` action.  If all validations succeed, it debits the specified amount of tokens from the total balance."
  },
  "cols": 2,
  "rows": 6
}
[/block]
This `eosio.token` sample contract demonstrates one way to implement a smart contract which allows for creation and management of tokens. This contract gives anyone the ability to create a token. It is possible for one to create a similar contract which suits different needs.  However, it is recommended that if one only needs a token with the above listed actions, that one uses the `eosio.token` contract instead of developing their own.

The `eosio.token` contract class also implements two useful public static methods: `get_supply` and `get_balance`. The first allows one to check the total supply of a specified token, created by an account and the second allows one to check the balance of a token, for a specified account (the token creator account has to be specified as well).

The `eosio.token` contract manages the set of tokens, accounts and their corresponding balances, by using two internal multi-index structures: the `accounts` and `stats`. The `accounts` multi-index table holds, for each row, instances of `account` object and the `account` object holds information about the balance of one token. If we remember how multi-index tables work, see [here](https://developers.eos.io/eosio-cpp/docs/using-multi-index-tables), then we understand also that the `accounts` table is scoped to an eosio account, and it keeps the rows indexed based on the token's symbol.  This means that when one queries the `accounts` multi-index table for an account name the result is all the tokens that account holds at the moment.

Similarly, the `stats` multi-index table, holds instances of `currency_stats` objects for each row, which contains information about current supply, maximum supply, and the creator account for a symbol token. The `stats` table is scoped to the token symbol.  Therefore, when one queries the `stats` table for a token symbol the result is one single entry/row corresponding to the queried symbol token if it was previously created, or nothing, otherwise.

[block:api-header]
{
  "title": "Useful commands"
}
[/block]
We assume the `eosio.token`contract code is deployed to `eostutorial1` account.

To create a new token 'TOK', in supply of 1 million tokens, open the wallet, make sure the `eostutorial1` active key is in the wallet, then run the following command:
[block:code]
{
  "codes": [
    {
      "code": "cleos push action eostutorial1 create ‘[“eostutorial1”,”1000000.0000 TOK”]’ -p eostutorial1@active",
      "language": "shell",
      "name": "Create a new token by eostutorial1"
    }
  ]
}
[/block]
To issue 1000 `TOK` tokens to `eostutorial2` account, open your wallet, make sure the `eostutorial1` account active keys is in it, and then run the following command:
[block:code]
{
  "codes": [
    {
      "code": "cleos push action eostutorial1 issue '{\"to\": \"eostutorial2\", \"quantity\": \"1000.0000 TOK\", \"memo\": \"your first 1000 TOK have arrived\"}' -p eostutorial1@active",
      "language": "shell",
      "name": "Issue tokens to eostutorial2 account"
    }
  ]
}
[/block]
To check the `eostutorial2` all tokens balance, run the following command which will list the `accounts` table rows, for account/owner `eostutorial1` and scope `eostutorial2`:
[block:code]
{
  "codes": [
    {
      "code": "cleos get table eostutorial1 eostutorial2 accounts",
      "language": "shell",
      "name": "Check all tokens balance for eostutorial2 account"
    }
  ]
}
[/block]
To check the status on `TOK` token, run the following command, which will list the `stat` table rows for account/owner `eostutorial1` and scope `TOK`:
[block:code]
{
  "codes": [
    {
      "code": "cleos get table eostutorial1 TOK stat",
      "language": "shell",
      "name": "Check TOPK token status:"
    }
  ]
}
[/block]
And this is how to push a transfer action, on the blockchain, which will transfer from `eostutorial1` account to `eostutorial2` account 1000 TOK:
[block:code]
{
  "codes": [
    {
      "code": "cleos push action eostutorial1 transfer '{\"from\": \"eostutorial1\", \"to\": \"eostutorial2\", \"quantity\": \"1000.0000 TOK\", \"memo\": \"test transfer\"}' -p eostutorial1@active",
      "language": "shell",
      "name": "Transfer from 1000 TOK from eostutorial1 to eostutorial2"
    }
  ]
}
[/block]