---
title: "Read Modes"
excerpt: ""
---
EOSIO provides [a set of services and interfaces](https://developers.eos.io/eosio-cpp/docs/db-api) that enable contract developers to persist state across action, and consequently transaction, boundaries.
Contracts may use it for different purposes. For example, `eosio.token` contract keeps balances of all users in the database.

Each instance of `nodeos` keeps the database in memory, so contracts can read and write data and
`nodeos` provides access to this data over HTTP RPC API for reading the database.

However, at any given time there can be multiple correct ways to query that data: 
- `speculative` : this includes the side effects of unconfirmed transactions.
- `head` : this only includes the side effects of transactions which have been included in the produced and signed blocks that are part of the best chain `nodeos`
- `irreversible` : this only includes side effects of transactions which have been confirmed by the network as irreversible.

# Read Modes

## Speculative

Clients such as `cleos` and the RPC API, will see database state as of current head block plus changes made by all transactions known to this node but potentially not included in the chain, unconfirmed transactions for example. 

Speculative mode is low latency but fragile, there is no guarantee that the transactions reflected in the state will be included in the chain OR that they will reflected in the same order the state implies.  

This mode features the lowest latency, but is the least consistent. 

In speculative mode `nodeos` is able to execute transactions which have TaPOS pointing to any valid block in a fork considered to be the best fork by this node.

## Head

Clients such as `cleos` and the RPC API will see database state as of current head block of the chain.  Since current head block is not yet irreversible and short-lived forks are possible, state read in this mode may become inaccurate  if `nodeos` switches to a better fork.  

This mode represents a good trade between highly consistent views of the data and latency.

In this mode `nodeos` is able to execute transactions which have TaPOS pointing to any valid block in a fork considered to be the best fork by this node.

## Irreversible

Clients (`cleos` and RPC API users) will see database state as of latest irreversible block (LIB).  This state is guaranteed to be accurate as of the given LIB.  

This mode has the strongest guarantee of consistency but the highest latency.

In this mode `nodeos` can only execute and relay transactions with TaPOS pointing to blocks before the LIB or to LIB itself.