---
title: "2.2 Deploy, Issue and Transfer Tokens"
excerpt: ""
---
[block:api-header]
{
  "title": "Step 1: Obtain Contract Source"
}
[/block]
Navigate to your contracts directory.
[block:code]
{
  "codes": [
    {
      "code": "cd CONTRACTS_DIR",
      "language": "shell"
    }
  ]
}
[/block]
Pull version 1.3.1 of the `eosio.contracts` repository
[block:code]
{
  "codes": [
    {
      "code": "git clone https://github.com/EOSIO/eosio.contracts --branch v1.3.1 --single-branch",
      "language": "shell"
    }
  ]
}
[/block]
This repository contains several contracts, but it's the `eosio.token` contract that is important now. Navigate to the directory now.
[block:code]
{
  "codes": [
    {
      "code": "cd eosio.contracts/eosio.token",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 2: Create Account for Contract"
}
[/block]
Before we can deploy the token contract we must create an account to deploy it to, we'll use the **eosio development key** for this account.
[block:callout]
{
  "type": "info",
  "body": "You may have to unlock your wallet first!"
}
[/block]
```
cleos create account eosio eosio.token EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
```
[block:api-header]
{
  "title": "Step 3: Compile the Contract"
}
[/block]
The ABI is included by this repo, so no need to regenerate the ABI. 
[block:code]
{
  "codes": [
    {
      "code": "eosio-cpp -I include -o eosio.token.wasm src/eosio.token.cpp ",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 4: Deploy the Token Contract"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos set contract eosio.token CONTRACTS_DIR/eosio.contracts/eosio.token --abi abi/eosio.token.abi -p eosio.token@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "Reading WAST...\nAssembling WASM...\nPublishing contract...\nexecuted transaction: 528bdbce1181dc5fd72a24e4181e6587dace8ab43b2d7ac9b22b2017992a07ad  8708 bytes  10000 cycles\n#         eosio <= eosio::setcode               {\"account\":\"eosio.token\",\"vmtype\":0,\"vmversion\":0,\"code\":\"0061736d0100000001ce011d60067f7e7f7f7f7f00...\n#         eosio <= eosio::setabi                {\"account\":\"eosio.token\",\"abi\":{\"types\":[],\"structs\":[{\"name\":\"transfer\",\"base\":\"\",\"fields\":[{\"name\"...",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 5: Create the Token"
}
[/block]
To create a new token call the `create(...)` action with the proper arguments. This action accepts 1 argument, it's a `symbol_name` type composed of two pieces of data, a maximum supply float and a `symbol_name` in capitalized alpha characters only, for example "1.0000 SYM". The issuer will be the one with authority to call issue and or perform other actions such as freezing, recalling, and whitelisting of owners.

Below is the concise way to call this method, using positional arguments:
[block:code]
{
  "codes": [
    {
      "code": "cleos push action eosio.token create '[ \"eosio\", \"1000000000.0000 SYS\"]' -p eosio.token@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 0e49a421f6e75f4c5e09dd738a02d3f51bd18a0cf31894f68d335cd70d9c0e12  120 bytes  1000 cycles\n#   eosio.token <= eosio.token::create          {\"issuer\":\"eosio\",\"maximum_supply\":\"1000000000.0000 SYS\"}",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
An alternate approach uses named arguments:
[block:code]
{
  "codes": [
    {
      "code": "cleos push action eosio.token create '{\"issuer\":\"eosio\", \"maximum_supply\":\"1000000000.0000 SYS\"}' -p eosio.token@active",
      "language": "text"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 0e49a421f6e75f4c5e09dd738a02d3f51bd18a0cf31894f68d335cd70d9c0e12  120 bytes  1000 cycles\n#   eosio.token <= eosio.token::create          {\"issuer\":\"eosio\",\"maximum_supply\":\"1000000000.0000 SYS\"}",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
This command created a new token `SYS` with a precision of 4 decimals and a maximum supply of 1000000000.0000 SYS.  To create this token requires the permission of the `eosio.token` contract. For this reason, `-p eosio.token@active` was passed to authorize the request.
[block:api-header]
{
  "title": "Step 6: Issue Tokens"
}
[/block]
The issuer can issue new tokens to the "alice" account created earlier. 
[block:code]
{
  "codes": [
    {
      "code": "cleos push action eosio.token issue '[ \"alice\", \"100.0000 SYS\", \"memo\" ]' -p eosio@active",
      "language": "text"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 822a607a9196112831ecc2dc14ffb1722634f1749f3ac18b73ffacd41160b019  268 bytes  1000 cycles\n#   eosio.token <= eosio.token::issue           {\"to\":\"user\",\"quantity\":\"100.0000 SYS\",\"memo\":\"memo\"}\n>> issue\n#   eosio.token <= eosio.token::transfer        {\"from\":\"eosio\",\"to\":\"user\",\"quantity\":\"100.0000 SYS\",\"memo\":\"memo\"}\n>> transfer\n#         eosio <= eosio.token::transfer        {\"from\":\"eosio\",\"to\":\"user\",\"quantity\":\"100.0000 SYS\",\"memo\":\"memo\"}\n#          user <= eosio.token::transfer        {\"from\":\"eosio\",\"to\":\"user\",\"quantity\":\"100.0000 SYS\",\"memo\":\"memo\"}",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
This time the output contains several different actions:  one issue and three transfers.  While the only action signed was `issue`, the `issue` action performed an "inline transfer" and the "inline transfer" notified the sender and receiver accounts.  The output indicates all of the action handlers that were called, the order they were called in, and whether or not any output was generated by the action.

Technically, the `eosio.token` contract could have skipped the `inline transfer` and opted to just modify the balances directly.  However, in this case the `eosio.token` contract is following our token convention that requires that all account balances be derivable by the sum of the transfer actions that reference them.  It also requires that the sender and receiver of funds be notified so they can automate handling deposits and withdrawals. 

To inspect the transaction, try using the `-d -j` options, they indicate "don't broadcast" and "return transaction as json," which you may find useful during development. 
[block:code]
{
  "codes": [
    {
      "code": "cleos push action eosio.token issue '[\"alice\", \"100.0000 SYS\", \"memo\"]' -p eosio@active -d -j",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 7: Transfer Tokens"
}
[/block]
Now that account `alice` has been issued tokens, transfer some of them to account `bob`.  It was previously indicated that `alice` authorized this action using the argument `-p alice@active`.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action eosio.token transfer '[ \"alice\", \"bob\", \"25.0000 SYS\", \"m\" ]' -p alice@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 06d0a99652c11637230d08a207520bf38066b8817ef7cafaab2f0344aafd7018  268 bytes  1000 cycles\n#   eosio.token <= eosio.token::transfer        {\"from\":\"alice\",\"to\":\"bob\",\"quantity\":\"25.0000 SYS\",\"memo\":\"Here you go bob!\"}\n>> transfer\n#          user <= eosio.token::transfer        {\"from\":\"alice\",\"to\":\"bob\",\"quantity\":\"25.0000 SYS\",\"memo\":\"Here you go bob!\"}\n#        tester <= eosio.token::transfer        {\"from\":\"alice\",\"to\":\"bob\",\"quantity\":\"25.0000 SYS\",\"memo\":\"Here you go bob!\"}",
      "language": "shell",
      "name": "Result"
    }
  ]
}
[/block]
Now check if "bob" got the tokens using [cleos get currency balance](https://developers.eos.io/eosio-cleos/reference#currency-balance)
[block:code]
{
  "codes": [
    {
      "code": "cleos get currency balance eosio.token bob SYS\n25.00 SYS",
      "language": "shell"
    }
  ]
}
[/block]
Check "alice's" balance, notice that tokens were deducted from the account 
[block:code]
{
  "codes": [
    {
      "code": "cleos get currency balance eosio.token alice SYS\n75.00 SYS",
      "language": "shell"
    }
  ]
}
[/block]
Excellent! Everything adds up.