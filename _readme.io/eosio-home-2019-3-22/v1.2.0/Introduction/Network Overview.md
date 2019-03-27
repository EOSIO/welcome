---
title: "Network Overview"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The EOS.IO network is comprised of a decentralized consensus algorithm (DPoS), a network resource management system, a governance process and a set of incentives for those using the network.


[block:api-header]
{
  "title": "Delegated Proof-Of-Stake"
}
[/block]
[Delegated Proof of Stake (DPOS)](https://steemit.com/dpos/@dantheman/dpos-consensus-algorithm-this-missing-white-paper) empowers tokens holders to select block producers through a continuous approval voting system. Anyone may choose to participate in block production and will be given an opportunity to produce blocks, provided they can persuade token holders to vote for them.

A holder of tokens on the EOS.IO blockchain, who may not have an immediate need to consume all or part of the available bandwidth the tokens provide, can delegate or rent such unconsumed bandwidth to others.
[block:api-header]
{
  "title": "Proposals"
}
[/block]
In addition to electing block producers, token holders can elect a number of Worker Proposals designed to benefit the community. The winning proposals will receive tokens of up to a configured percent of the token inflation minus those tokens that have been paid to block producers.
[block:api-header]
{
  "title": "Incentive"
}
[/block]
The EOS.IO blockchain will award new tokens to a block producer every time a block is produced. A cap on producer awards can be set such that the total annual increase in token supply does not exceed 5%.
[block:api-header]
{
  "title": "Staking"
}
[/block]
## Resources

On the EOS.IO blockchain, there are three broad classes of resources that are consumed by applications:

  *     Bandwidth and Log Storage (Disk);
  *     Computation and Computational Backlog (CPU); and
  *     State Storage (RAM).

## Consumption 

The EOS.IO software allows each account to consume a percentage of the available capacity proportional to the amount of tokens held in a 3-day staking contract. For example, if an account on the EOS.IO blockchain holds 1% of the total tokens distributable pursuant to that blockchain, then that account has the potential to utilize 1% of the state storage capacity.

While network and computation can be delegated, storage of application state will require an application developer to hold tokens, or stake them, until that state is deleted. If state is never deleted, then the tokens are effectively removed from circulation.


[block:api-header]
{
  "title": "Governance"
}
[/block]
The EOS.IO blockchain governance process recognizes that power originates with the token holders who then delegate that power to the block producers. The governance process efficiently directs the existing influence of block producers to line up to the interests of the token holders.

## Abilities

Block producers are given limited and checked authority to freeze accounts, update defective applications, and propose hard forking changes to the underlying protocol. Before any change can be made to the blockchain the block producers must approve it. If the block producers refuse to make changes desired by the token holders then they can be voted out.

##Constitution

The EOS.IO blockchain will establish a peer-to-peer terms of service agreement or a binding contract among those users who sign it, referred to as a "constitution". The content of this constitution defines obligations among the users which cannot be entirely enforced by code and facilitates dispute resolution by establishing jurisdiction and choice of law along with other mutually accepted rules. Every transaction broadcast on the network must incorporate the hash of the constitution as part of the signature and thereby explicitly binds the signer to the contract.

## Arbitration

The EOS.IO blockchain constitution will state that all users agree to settle disputes by arbitration.