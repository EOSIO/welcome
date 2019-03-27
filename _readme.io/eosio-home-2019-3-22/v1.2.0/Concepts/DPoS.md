---
title: "DPoS"
excerpt: ""
---
[block:api-header]
{
  "title": "History"
}
[/block]
DPoS stands for "Delegated Proof of Stake" and is a consensus algorithm initially developed by Daniel Larimer in 2013 for Bitshares. It's sometimes referred to as "Democracy as Proof of Stake" 
[block:api-header]
{
  "title": "Description"
}
[/block]
In short, DPoS is a consensus mechanism that enables the network to elect block producers responsible for validating transactions for inclusion on the blockchain. 

There are many implementations of DPoS each with their own parameters on how DPoS behaves. On EOSIO by default there are 21 active block producers, and 79 standby producers. The 21 active block producers are equal to one another, and are paid for every block added to the blockchain from the inflation pool. The next 79 block producers are paid a smaller amount proportionate to their vote weight.