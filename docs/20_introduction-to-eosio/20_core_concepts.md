
## Accounts, Wallets and Permissions

**Accounts**

An account is a human-readable name that is stored on the blockchain. It can be owned through authorization by an individual or group of individuals depending on permissions configuration. An account is required to transfer or push any valid transaction to the blockchain.

**Wallets**

Wallets are clients that store keys that may or may not be associated with the permissions of one or more accounts. Ideally, a wallet has a locked (encrypted) and unlocked (decrypted) state that is protected by a high entropy password. The EOSIO/eos repository comes bundled with a CLI client called `cleos` that interfaces with a lite-client called `keosd` and together, they demonstrate this pattern.

**Authorization and Permissions**

Permissions are arbitrary names used to define the requirements for a transaction sent on behalf of that permission. Permissions can be assigned for authority over specific contract actions by *linking authorization* or linkauth.

For more information about these concepts, see the [_Accounts and Permissions_](../60_protocol-guides/40_accounts_and_permissions.md) documentation.


### Smart Contracts
A smart contract is a piece of code that can execute on a blockchain and keep the state of contract execution as a part of the immutable history of that blockchain instance. Therefore, developers can rely on that blockchain as a trusted computation environment in which inputs, execution, and the results of a smart contract are independent and free of external influence.

`youtube: https://www.youtube.com/watch?v=_I0dUL4kpTg`



### Delegated Proof of Stake (DPOS)

The EOSIO platform implements a proven decentralized consensus algorithm capable of meeting the performance requirements of applications on the blockchain called the _Delegated Proof of Stake_ (DPOS). Under this algorithm, if you hold tokens on a EOSIO-based blockchain, you can select block producers through a continuous approval voting system. Anyone can choose to participate in the block production and will be given an opportunity to produce blocks, provided they can persuade token holders to vote for them.

For more information about DPOS BFT, see [EOSIO Consensus](../60_protocol-guides/10_consensus_protocol.md#3-eosio-consensus-dpos--abft).

<!-- The link will be updated once the initial site is live -->

## System Resources

[[info | Note]]
| This section only applies to DPoS implementation of the EOSIO consensus mechanism. If you choose not to use DPoS, System Resources are not required.

### RAM

RAM, in a EOSIO-based blockchain, is one of the important system resources consumed by blockchain accounts and smart contracts. RAM acts as a permanent storage and is used to store account names, permissions, token balance and other data for speedy on-chain data access. RAM needs to be purchased and is not based on staking as it is a limited persistent resource.

More details about RAM as a system resource can be found [here](https://developers.eos.io/manuals/eosio.contracts/latest/index/#ram).


### CPU

CPU, in a EOSIO-based blockchain, represents the processing time of an action and is measured in microseconds (μs). CPU is referred to as `cpu bandwidth` in the cleos `get account` command output and indicates the amount of processing time an account has at its disposal when pushing actions to a contract. CPU is a transient system resource and falls under the staking mechanism of EOSIO.

More details about CPU as a system resource can be found [here](https://developers.eos.io/manuals/eosio.contracts/latest/index/#cpu).


### Network (NET)
Besides CPU and RAM, NET is also a very important resource in EOSIO-based blockchains. NET is the network bandwidth, measured in bytes, of transactions and is referred to as `net bandwidth` on the cleos `get account` command. NET is a also a transient system resource and falls under the staking mechanism of EOSIO.

More details about NET as a system resource can be found [here](https://developers.eos.io/manuals/eosio.contracts/latest/index/#net).
