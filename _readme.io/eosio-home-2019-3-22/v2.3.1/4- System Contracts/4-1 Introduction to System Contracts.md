---
title: "4.1 Introduction to System Contracts"
excerpt: ""
---
[block:api-header]
{
  "title": "4.1.1 About System Contracts"
}
[/block]
EOSIO is unique in that the parameters of the network aren't protocol level, instead all the network parameters such as consensus, fee schedules and account modification exist inside privileged contracts on the EOSIO network. 

These privileged contracts are the subject of this tutorial, they are `eosio.system`, `eosio.bios`, `eosio.msig`, and `eosio.wrap`. As part of this tutorial is also `eosio.token` although not a privileged contract it is part of the system contracts.
[block:api-header]
{
  "title": "4.1.2. What is Privileged?"
}
[/block]
When you first boot EOSIO, it has no rules, no consensus mechanisms and is essentially a blank slate. The implementation details of EOSIO are up to any individual network. Block.one maintains a repository of default system contracts, but nobody is bound to using these particular contracts on an EOSIO network. 
[block:api-header]
{
  "title": "4.1.3. The BIOS Boot Process"
}
[/block]
In short, the "BIOS Boot Process" is the act of setting up a chain through the master "eosio" account. This account has full privileges over the network, and can do just about anything it wants to. Once the chain is configured, the BIOS Boot node would remove privilege for this user and then make it's keys publicly available, so anyone could replicate it's boot process for verification to ensure that nothing malicious was done during the boot process
[block:api-header]
{
  "title": "4.1.4. Social Mechanics of Booting an EOSIO Network"
}
[/block]
The social mechanics of the BIOS Boot Process is really determined by the network's BIOS Boot node operator. But in general, it looks something like this

1. A group of aligned interests randomly selects a participant as the Boot node. These individuals are referred to as "Appointed Block Producers" or ABP for short. How these ABPs are chosen is largely up to any individual community, but often, it's the ones who step up to the plate and volunteer. It's beneficial when the boot process prevents ABPs from receiving any kind of rewards from the chain.  They are volunteers. They use verifiable and deterministic randomization as to maintain trust during this process.
2. The Selected boot node performs the boot as previously agreed to by this previously defined group of individuals. 
3. Once the Boot node operator has done their own internal testing, they withdraw privilege for the `eosio` account, freeze the chain, publish the "boot keys" and make their identity known. At this point, the other participants of the boot process validate that the boot node operator did not diverge from the agreed-upon plan. They verify the system contracts, validate genesis balances if any and validate that no malicious actions were committed to the chain. In the event that a discrepancy is found, they burn their node and start over. Usually excluding the malicious boot node operator from the second attempt. They then repeat the process, until there is consensus on the chain state, the chain is unfrozen, and starts producing blocks. 
4. While the chain is now producing blocks, it's in a restricted state. Depending on the system contract's logic, there may be a threshold set that determines when a chain has reached community support. For the popular "EOS" chain, the mechanics were 15% supply approval by genesis accounts. This approval was reached by genesis accounts voting for block producers. Once the total supply met the threshold as configured in the system contract, the chain was "active" and all functionalities are unlocked. Of course, the specifics of a system contract really depend on how the system contract is configured.