---
title: "Exchange Deposit/Withdraw"
excerpt: ""
---
# Exchange Deposit and Withdrawal

This tutorial is targeted toward exchanges that wish to automate deposit and withdrawal of standard-conforming EOSIO token contracts. The EOSIO blockchain's native token conforms to the standard. In this tutorial, the methods for depositing to and withdrawing from the exchange are shown, but perhaps more importantly for the process of automation, the means by which activity can be monitored and reported are shown.

## Setup

### Prerequisites

It is assumed that you have a local `nodeos` server connected to an EOSIO blockchain; that an account has been created for `eosio.token`; and that the `eosio.token` contract has been deployed.  Completing the [Getting Started with Smart Contracts](introduction-to-smart-contracts) and [Eosio.token, Exchange, and Eosio.msig Contracts](token-tutorial) tutorials prior to this tutorial will have satisfied these prerequisites.

This tutorial uses the transfer action of the `eosio.token` contract for handling deposits and withdrawals. It does _**not**_ use the sample `exchange` contract provided with the EOSIO source distribution, and that was loaded in the [Eosio.token, Exchange, and Eosio.msig Contracts](token-tutorial).

### Ensure `eosio::history_api_plugin` is running

This tutorial uses the `cleos` command line tool to query the log history of accounts. This requires the `eosio::history_api_plugin` to be installed. If your `nodeos` was not started with this plugin, you will need to restart `nodeos` and add `--plugin eosio::history_api_plugin` to the command line.

### Activate log filtering

This tutorial depends on transaction logging from `nodeos`.  In earlier versions of `nodeos`, the history plugin defaulted to logging the history of all accounts. Now, by default, the history plugin will not log transactions at all without explicitly specifying filtering. To log transactions, use the `filter-on` option and specify what you wish logged. The format is `--filter-on <receiver>:<action>:[<actor>] (actor can be blank to get all). Add the following option to your `nodeos` command line to activate log filtering on the `tokenxchange` receiver, `transfer` action, for all accounts (do not forget the trailing ":"):

```
    --filter-on tokenxchange:transfer:
```
You will need to filter on each receiver that you wish to track.  In this case, add the following options to `nodeos`:
```
    --filter-on tokenxchange:transfer: --filter-on scott:transfer: --filter-on eosio.token:transfer:
```

### Replay the blockchain

If you have already synced the blockchain without the history plugin, then you might need to replay the blockchain to pickup any historical activity. Add the following option to your `nodeos` command line to replay the blockchain.

```
    --replay-blockchain
```

You only need to replay once. Subsequent runs of `nodeos` should not use the replay flag, as this could cause unnecessarily long startup times.

### Set up additional accounts

The exchange to be set up here will be called `tokenxchange`, to avoid confusion with the `exchange` account and contract.  Create an account named `tokenxchange` using what you've learned from previous tutorials.

This tutorial uses an account named `scott`. Using what you've learned from previous tutorials, create an account named `scott` and deposit 900.0000 SYS into it.

## Accepting Deposits

In this tutorial, we assume that an exchange will poll `nodeos` for incoming transactions and will want to know when a transfer is considered irreversible or final. 

With eosio-based chains, finality of a transaction occurs once 2/3 + 1 of block producers have either directly or indirectly confirmed the block. This could take from less than a second to a couple of minutes, but either way `nodeos` will keep you posted on the status.

### Initial Condition

Verify that account `scott` has the correct token balance.
```
$ cleos get currency balance eosio.token scott SYS
900.0000 SYS
```

We will now deposit some funds to `tokenxchange`.  In the memo for the transfer, we will use a unique internal identifer for scott, in this case the value "12345".

```
$ cleos transfer scott tokenxchange "1.0000 SYS" 12345
executed transaction: ce32ac1fbc96e74ea9318d5b18769be9d84f704c9c0f0eab23c6ce95e4b9ce49  136 bytes  505 us
#   eosio.token <= eosio.token::transfer        {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS","memo":"12345"}
#         scott <= eosio.token::transfer        {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS","memo":"12345"}
#  tokenxchange <= eosio.token::transfer        {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS","memo":"12345"}
```

This output indicates that the action `eosio.token::transfer` was delivered to three accounts/contracts: _"eosio.token"_, _"scott"_, and _"tokenxchange"_. The eosio token standard requires that both the sender and receiver account/contract be notified of all transfer actions so that those accounts can run custom logic.  At this time, neither _scott_ nor _tokenxchange_ has any contract set that will act on such notifications, but the transaction log will still show that they were notified.  

## Polling Account History 
The account history consists of all actions that were either authorized by the account or received by the account. Since the exchange received the `eosio.token::transfer` action, it is listed in the history. If you are using the console, confirmed and irreversible transactions are printed in "green" while unconfirmed transactions are printed in "yellow". Independent of color, you can tell whether a transaction is confirmed by the first character in the line in the transaction log: '#' for irreversible and '?' for potentially reversible.  
```
$ cleos get actions tokenxchange
#  seq  when                              contract::action => receiver      trx id...   args
================================================================================================================
#    0   2018-06-03T15:24:34.500     eosio.token::transfer => tokenxchange  ce32ac1f... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
```

Do a few more transfers:
```
$ cleos transfer scott tokenxchange "1.0000 SYS" 12345
executed transaction: 9d9f981674073065d81491dc53a6d436fc383ff26eb34189f414f63481463822  136 bytes  549 us
#   eosio.token <= eosio.token::transfer        {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS","memo":"12345"}
#         scott <= eosio.token::transfer        {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS","memo":"12345"}
#  tokenxchange <= eosio.token::transfer        {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS","memo":"12345"}

...
```

Now look at the transaction log:

```
$ cleos get actions tokenxchange
#  seq  when                              contract::action => receiver      trx id...   args
================================================================================================================
#    0   2018-06-03T15:24:34.500     eosio.token::transfer => tokenxchange  ce32ac1f... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
#    1   2018-06-03T15:28:12.000     eosio.token::transfer => tokenxchange  9d9f9816... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
?    2   2018-06-03T15:29:33.000     eosio.token::transfer => tokenxchange  05fd45b6... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
```

The last transfer is still pending, waiting on irreversibility. 

The "seq" column represents the index of actions for your specific account. It will always increment as new relevant actions are added.

The `cleos get actions` command allows you some control over which actions are fetched. You can view the help for this command with `-h` 

```
$ cleos get actions -h
ERROR: RequiredError: account_name
Retrieve all actions with specific account name referenced in authorization or receiver
Usage: cleos get actions [OPTIONS] account_name [pos] [offset]

Positionals:
  account_name TEXT           name of account to query on (required)
  pos INT                     sequence number of action for this account, -1 for last
  offset INT                  get actions [pos,pos+offset] for positive offset or [pos-offset,pos) for negative offset

Options:
  -j,--json                   print full json
  --full                      don't truncate action json
  --pretty                    pretty print full action json 
  --console                   print console output generated by action 
```

To get only the last action you would do the following:

```
$ cleos get actions tokenxchange -1 -1
#  seq  when                              contract::action => receiver      trx id...   args
================================================================================================================
#    2   2018-06-03T15:29:33.000     eosio.token::transfer => tokenxchange  05fd45b6... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
```

This command says to go to the last sequence number (indicated by pos = -1) and then fetch "1" item prior to it (offset = -1).  Using the example above, this will return a sequence in the range [3-1,3) or [2,3) which is only row 2.  In this case, "-1" position means "one past the last sequence" and operates like an end iterator from C++ containers.

### Fetching only "New" Actions

Since we presume your exchange is running a polling micro-service, it will want to fetch the "next unprocessed deposit". In this case the microservice will need to track the seq number of the "last processed seq".  For the sake of this example, we will assume that "seq 0" has been processed and that we want to fetch "seq 1" if any.

We pass pos=1 and offset=0 to get the range [1,1+0] or [1,1].
```
$ cleos get actions tokenxchange 1 0
#  seq  when                              contract::action => receiver      trx id...   args
================================================================================================================
#    2   2018-06-03T15:29:33.000     eosio.token::transfer => tokenxchange  05fd45b6... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
```

We can call this in a loop, processing each confirmed action (those starting with #) until we either run  out of items or we find an unconfirmed action (starting with ?).

```
$ cleos get actions tokenxchange 3 0
#  seq  when                              contract::action => receiver      trx id...   args
================================================================================================================
```

### Machine Readable Account History (JSON)

So far this tutorial has focused on using `cleos` to fetch and display the history. However, `cleos` is merely a light-weight wrapper around a JSON-RPC interface.  `cleos` can dump the raw JSON returned from the JSON-RPC request, or you can make your own JSON-RPC request.

Here is the JSON returned when querying sequence 2.
```
$ cleos get actions tokenxchange 2 0 -j
{
  "actions": [{
      "global_action_seq": 2132,
      "account_action_seq": 2,
      "block_num": 2099,
      "block_time": "2018-06-03T15:29:33.000",
      "action_trace": {
        "receipt": {
          "receiver": "tokenxchange",
          "act_digest": "3a49a62f23db41c4ed8a8fa52509a04056c8afdcb15de7544a430b2cadfbaf68",
          "global_sequence": 2132,
          "recv_sequence": 3,
          "auth_sequence": [[
              "scott",
              9
            ]
          ],
          "code_sequence": 1,
          "abi_sequence": 1
        },
        "act": {
          "account": "eosio.token",
          "name": "transfer",
          "authorization": [{
              "actor": "scott",
              "permission": "active"
            }
          ],
          "data": {
            "from": "scott",
            "to": "tokenxchange",
            "quantity": "1.0000 SYS",
            "memo": "12345"
          },
          "hex_data": "00000000809c29c2a0d8340df5a920cd10270000000000000453595300000000053132333435"
        },
        "elapsed": 2,
        "cpu_usage": 0,
        "console": "",
        "total_cpu_usage": 0,
        "trx_id": "05fd45b61df815a4cdeb768e732adb292500b2399517fc9c98b6e6b136d7a4d1",
        "inline_traces": []
      }
    }
  ],
  "last_irreversible_block": 2543
}
```

Given this JSON, an action is irreversible (final) if its `"block_num" < "last_irreversible_block"`.  

You can identify irreversible deposits by the following:

```
    actions[0].action_trace.act.account == "eosio.token" &&
    actions[0].action_trace.act.name == "transfer" &&
    actions[0].action_trace.act.data.quantity == "X.0000 SYS" &&
    actions[0].action_trace.to == "tokenxchange" && 
    actions[0].action_trace.memo == "KEY TO IDENTIFY INTERNAL ACCOUNT" && 
    actions[0].action_trace.receipt.receiver == "tokenxchange"  &&
    actions[0].block_num < last_irreversible_block
```

### WARNING

It is critical that you validate all of the conditions above, including the token symbol name. Users can create other contracts with "transfer" actions that "notify" your account. If you do not validate all of the above properties, then you may process "false deposits".  

```
    actions[0].action_trace.act.account == "eosio.token" &&
    actions[0].action_trace.receipt.receiver == "tokenxchange" 
```

### Validating Balance

Now that we have received three deposits, we should see that the exchange has a balance of 3.0000 SYS.

```
$ cleos get currency balance eosio.token tokenxchange SYS
3.0000 SYS
```

## Processing Withdrawals

When a user requests a withdrawal from your exchange, they will need to provide you with their eosio account name and the amount to be withdrawn.  You can then run the `cleos` command to perform the withdrawal. `cleos` will interact with the "unlocked" wallet running on `nodeos`, which should only enable localhost connections.

Let's assume _scott_ wants to withdraw `1.0000 SYS`:
```
$ cleos transfer tokenxchange scott  "1.0000 SYS"
executed transaction: 26a1d1f1601c35a1d97c294974ba26f3eea3b76f3c3df736c7bbab930df24c9f  128 bytes  514 us
#   eosio.token <= eosio.token::transfer        {"from":"tokenxchange","to":"scott","quantity":"1.0000 SYS","memo":""}
#  tokenxchange <= eosio.token::transfer        {"from":"tokenxchange","to":"scott","quantity":"1.0000 SYS","memo":""}
#         scott <= eosio.token::transfer        {"from":"tokenxchange","to":"scott","quantity":"1.0000 SYS","memo":""}

```

At this stage your local `nodeos` client accepted the transaction and likely broadcast it to the broader network. 

We can get the history and see that there are three new actions listed, all with transaction id `26a1d1f1...`, as reported by our `transfer` command. Because _tokenxchange_ authorized the transaction, it is informed of all accounts that processed and accepted the `transfer`.  In this case the `eosio.token` contract processed the transfer and updated balances, the sender (_tokenxchange_) processed it, as did the receiver (_scott_). All three contracts/accounts approved it and/or performed state transitions based upon the action.

```
$ cleos get actions tokenxchange -1 -9
#  seq  when                              contract::action => receiver      trx id...   args
================================================================================================================
#    0   2018-06-03T15:24:34.500     eosio.token::transfer => tokenxchange  ce32ac1f... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
#    1   2018-06-03T15:28:12.000     eosio.token::transfer => tokenxchange  9d9f9816... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
#    2   2018-06-03T15:29:33.000     eosio.token::transfer => tokenxchange  05fd45b6... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
#    3   2018-06-03T15:37:35.500     eosio.token::transfer => tokenxchange  3d89c983... {"from":"scott","to":"tokenxchange","quantity":"1.0000 SYS",...
#    4   2018-06-03T15:38:44.500     eosio.token::transfer => tokenxchange  f13ea506... {"from":"tokenxchange","to":"scott","quantity":"1.0000 SYS",...
#    5   2018-06-04T00:18:11.500     eosio.token::transfer => tokenxchange  95cbb1ce... {"from":"tokenxchange","to":"scott","quantity":"1.0000 SYS",...
#    6   2018-06-04T00:18:11.500     eosio.token::transfer => scott         95cbb1ce... {"from":"tokenxchange","to":"scott","quantity":"1.0000 SYS",...
#    7   2018-06-04T01:09:53.500     eosio.token::transfer => eosio.token   26a1d1f1... {"from":"tokenxchange","to":"scott","quantity":"1.0000 SYS",...
#    8   2018-06-04T01:09:53.500     eosio.token::transfer => tokenxchange  26a1d1f1... {"from":"tokenxchange","to":"scott","quantity":"1.0000 SYS",...
#    9   2018-06-04T01:09:53.500     eosio.token::transfer => scott         26a1d1f1... {"from":"tokenxchange","to":"scott","quantity":"1.0000 SYS",...
```

By processing the history, we can be informed when our transaction was confirmed. In practice, we expect you will maintain private database state to track the withdrawal process. It can be useful to embed an exchange-specific memo in the withdraw request in order to map to your private database state. Another approach is to simply use the transaction ID for your mapping. When your account history microservice comes across _seq 5_ and sees it is irreversible, it can then mark your withdrawal as complete.

## Handling Errors

Sometimes network issues will cause a transaction to fail and never be included in a block. Your internal database will need to know when this has happened so that it can inform the user and/or try again. If you do not get an immediate error when you submit your local transfer, then you must wait for the transaction to expire. Every transaction has an "expiration", after which the transaction can never be applied. Once the last irreversible block has moved past the expiration time, you can safely mark your attempted withdrawal as failed and not worry about it "floating around the ether" to be applied when you least expect.

By default, `cleos` sets an expiration window of 2 minutes.  This is long enough to allow all 21 producers an opportunity to include the transaction.

```
$ cleos transfer tokenxchange scott  "1.0000 SYS" -j -d
{
  "expiration": "2018-06-04T00:36:39",
  "ref_block_num": 8209,
  "ref_block_prefix": 2405809535,
  "max_net_usage_words": 0,
  "max_cpu_usage_ms": 0,
  "delay_sec": 0,
  "context_free_actions": [],
  ...

```

Your microservice can query the last irreversible block number and the head block time using `cleos`. 
```
$ cleos get info
{
  "server_version": "0961a560",
  "chain_id": "cf057bbfb72640471fd910bcb67639c22df9f92470936cddc1ade0e2f2e7dc4f",
  "head_block_num": 8356,
  "last_irreversible_block_num": 8355,
  "last_irreversible_block_id": "000020a3df1d1a2e963f8586347839bc9425d8b613c315fa7005e2336ec6b35a",
  "head_block_id": "000020a4f9fb2371f04cd2c3cd05dbf63eb7005564d75abe787bd990b50f9348",
  "head_block_time": "2018-06-04T00:37:22",
  "head_block_producer": "producer2"
  ...
}
```

## Exchange Security 

This tutorial shows the minimal viable deposit/withdraw handlers and assumes a single wallet which contains all keys necessary to authorize deposits and withdrawals. A security-focused exchange would take the following additional steps:

1. keep vast majority of funds in a time-delayed, multi-sig controlled account
2. use multi-sig on the hot wallet with several independent processes/servers double-checking all withdrawals 
3. deploy a custom contract that only allows withdrawals to KYC'd accounts and require multi-sig to white-list accounts
4. deploy a custom contract that only accepts deposits of known tokens from KYC'd accounts
5. deploy a custom contract that enforces a mandatory 24-hour waiting period for all withdrawals
6. utilize hardware wallets for all signing, even automated withdrawal

Customers want immediate withdrawals, but they also want the exchange to be protected. The blockchain-enforced 24-hour period lets the customer know the money is "on the way" while also informing potential-hackers that the exchange has 24 hours to respond to unauthorized access. Furthermore, if the exchange emails/text messages users upon start of withdrawal, users have 24 hours to contact the exchange and fix any unauthorized access to their individual account.

Information on how to utilize these more advanced techniques will be available in a future document.