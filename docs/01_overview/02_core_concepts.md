## Blockchain

While there are many ways in which a blockchain can be defined, there are a few characteristics of the blockchain which can be found in almost all definitions such as `decentralized`, `immutable`, and `traceable/transparent`. A blockchain is a `decentralized` infrastructure software without a centralized entity controlling the blockchain. The transactions recorded on the blockchain form the `immutable` history of the blockchain. Any transaction or change on the blockchain history is `traceable` and can be audited publicly on the blockchain history, thus, making all the blockchain history `transparent` to anyone.

[What is blockchain?](https://youtu.be/MqSE5WLusko)


## Accounts, Keys & Permissions

TO DO: Content from: https://developers.eos.io/eosio-nodeos/docs/accounts-and-permissions


### Smart Contracts
A smart contract is a piece of code that can execute on a blockchain and keep the state of contract execution as a part of the immutable history of that blockchain instance. Therefore, developers can rely on that blockchain as a trusted computation environment in which inputs, execution, and the results of a smart contract are independent and free of outside influence. This addition opens up all kinds of new possibilities for developers.

[What is a smart contract?](https://youtu.be/_I0dUL4kpTg)


### Delegated Proof of Stake (DPOS)

The EOSIO platform implements the only known decentralized consensus algorithm proven capable of meeting the performance requirements of applications on the blockchain, `Delegated Proof of Stake (DPOS)`. Under this algorithm, those who hold tokens on a EOSIO-based blockchain may select block producers through a continuous approval voting system. Anyone can choose to participate in block production and will be given an opportunity to produce blocks, provided they can persuade token holders to vote for them.

More details about DPOS BFT— Pipelined Byzantine Fault Tolerance can be found [here](https://eos.io/news/dpos-bft-pipelined-byzantine-fault-tolerance/).


### RAM

RAM, in an EOSIO-based blockchain, is one of the important resources consumed by blockchain accounts and smart contracts. RAM in the EOSIO blockchain acts as a permanent storage and is used to store EOSIO account keys, token balance, and other data for speedy on-chain data access. RAM needs to be purchased and is not based on staking as it is a limited persistent resource.

More details about RAM as a resource can be found [here](https://github.com/EOSIO/eosio.contracts/blob/docs/split_index_md/docs/01_core_concepts/02_ram.md).


### CPU

CPU, in an EOSIO-based blockchain, represents the processing time of an action and is measured in microseconds (μs). CPU is referred to as `cpu bandwidth` in the cleos `get account` command output and indicates the amount of processing time an account has at its disposal when pushing actions to a contract.

More details about CPU as a resource can be found [here](https://github.com/EOSIO/eosio.contracts/blob/docs/split_index_md/docs/01_core_concepts/02_cpu.md).


### Network (NET)
Besides CPU and RAM, NET is also a very important resource in EOSIO-based blockchains. NET is the network bandwidth, measured in bytes, of transactions and is referred to as `net bandwidth` on the cleos `get account` command. This resource, like CPU, must be staked so that a contract's transactions can be executed.

More details about NET as a resource can be found [here](https://github.com/EOSIO/eosio.contracts/blob/docs/split_index_md/docs/01_core_concepts/04_net.md).
