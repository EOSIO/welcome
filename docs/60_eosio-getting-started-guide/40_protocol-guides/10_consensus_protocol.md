---
content_title: Consensus Protocol
---

# 1. Overview

An EOSIO blockchain is a highly efficient, deterministic, distributed state machine that can operate in a decentralized fashion. The blockchain keeps track of transactions within a sequence of interchanged blocks. Each block cryptographically commits to the  previous blocks along the same chain. It is therefore intractable to modify a transaction recorded on a given block without breaking the cryptographic checks of successive blocks. This simple fact makes blockchain transactions immutable and secure.

## 1.1. Block Producers

In the EOSIO ecosystem, block production and block validation are performed by special nodes called "block producers". Producers are elected by EOSIO stakeholders (see [4. Producer Voting/Scheduling](#4-producer-votingscheduling)). Each producer runs an instance of an EOSIO node through the `nodeos` service. For this reason, producers that are on the active schedule to produce blocks are also called "active" or "producing" nodes.

## 1.2. The Need for Consensus

Block validation presents a challenge among any group of distributed nodes. A consensus model must be in place to validate such blocks in a fault tolerant way within the decentralized system. Consensus is the way for such distributed nodes and users to agree upon the current state of the blockchain (see [3. EOSIO Consensus (DPoS + aBFT)](#3-eosio-consensus-dpos--abft)).

# 2. Consensus Models

There are various ways to reach consensus among a group of distributed parties in a decentralized system. Most consensus models reach agreement through some proof. Two of the most popular ones are Proof of Work (PoW) and Proof of Stake (PoS), although other types of proof-based schemes exist, such as Proof of Activity (a hybrid between PoW and PoS), Proof of Burn, Proof of Capacity, Proof of Elapsed Time, etc. Other consensus schemes also exist, such as Paxos and Raft. This document focuses mainly on the EOSIO consensus model.

## 2.1. Proof of Work (PoW)

Two of the most common consensus models used in blockchains are Proof of Work and Proof of Stake. In Proof of Work, miner nodes compete to find a nonce added to the header of a block which causes the block to have some desired property (typically a certain number of zeros in the most significant bits of the cryptographic hash of the block header). By making it computationally expensive to find such nonces that make the blocks valid, it becomes difficult for attackers to create an alternative fork of the blockchain that would be accepted by the rest of the network as the best chain. The main disadvantage of Proof of Work is that the security of the network depends on spending a lot of resources on computing power to find the nonces.

## 2.2. Proof of Stake (PoS)

In Proof-of-Stake, nodes that own the largest stake or percentage of some asset have equivalent decision power. In other words, voting power is proportional to the stake held. One interesting variant is Delegated Proof-of-Stake (DPoS) in which a large number of participants or stakeholders elect a smaller number of delegates, which in turn make decisions for them.

# 3. EOSIO Consensus (DPoS + aBFT)

EOSIO-based blockchains use delegated proof of stake (DPoS) to elect the active producers who will be authorized to sign valid blocks in the network. However, this is only one half of the EOSIO consensus process. The other half is involved in the actual process of confirming each block until it becomes final (irreversible), which is performed in an asynchronous byzantine fault tolerant (aBFT) way. Therefore, there are two layers involved in the EOSIO consensus model:

* Layer 1 - The Native Consensus Model (aBFT).
* Layer 2 - Delegated Proof of Stake (DPoS).

The actual native consensus model used in EOSIO has no concept of delegations/voting, stake, or even tokens. These are used by the DPoS layer to generate the first schedule of block producers and, if applicable, update the set at most every schedule round after each producer has cycled through. These two layers are functionally separate in the EOSIO software.

## 3.1. Layer 1: Native Consensus (aBFT)

This layer ultimately decides which blocks, received and synced among the elected producers, eventually become final, and hence permanently recorded in the blockchain. It gets a schedule of producers proposed by the second layer (see [3.2. Layer 2: Delegated PoS](#32-layer-2-delegated-pos-dpos)) and uses that schedule to determine which blocks are correctly signed by the appropriate producer. For byzantine fault tolerance, the layer uses a two-stage block confirmation process by which a two-thirds supermajority of producers from the current scheduled set confirm each block twice. The first confirmation stage proposes a last irreversible block (LIB). The second stage confirms the proposed LIB as final. At this point, the block becomes irreversible. This layer is also used to signal producer schedule changes, if any, at the beginning of every schedule round.

### 3.1.1. EOSIO Algorithmic Finality
The EOSIO consensus model achieves algorithmic finality (differing from the merely probabilistic finality that at best can be achieved in Proof of Work models) through the signatures from the chosen set of special participants (active producers) that are arranged in a schedule to determine which party is authorized to sign the block at a particular time slot. Changes to this schedule can be initiated by privileged smart contracts running on the EOSIO blockchain, but any initiated changes to the schedule do not take effect until after the block that initiated the schedule change has been finalized by two stages of confirmations. Each stage of confirmations is performed by a supermajority of producers from the current scheduled set of active producers.

## 3.2. Layer 2: Delegated PoS (DPoS)

The Delegated PoS layer introduces the concepts of tokens, staking, voting/proxying, vote decay, vote tallying, producer ranking, and inflation pay. This layer is also in charge of generating new producer schedules from the rankings generated from producer voting. This occurs in schedule rounds of approximately two minutes (126 seconds) which is the period it takes for a block producer to be assigned a timeslot to produce and sign blocks. The timeslot lasts a total of 6 seconds per producer, which is the producer round, where a maximum of 12 blocks can be produced and signed. The DPoS layer is enabled by WASM smart contracts.

### 3.2.1. Stakeholders and Delegates

The actual selection of the active producers (the producer schedule) is open for voting every schedule round and it involves all EOSIO stakeholders who exercise their right to participate. In practice, the rankings of the active producers do not change often, though. The stakeholders are regular EOSIO account holders who vote for their block producers of preference to act on their behalf as DPoS delegates. A major departure from regular DPoS, however, is that once elected, all block producers have equal power regardless of the ranking of votes obtained. In other DPoS models, voting power is proportional to the number of votes obtained by each delegate.

## 3.3. The Consensus Process

The EOSIO consensus process consists of two parts:

* Producer voting/scheduling - performed by the the DPoS layer 2
* Block production/validation - performed by the native consensus layer 1

These two processes are independent and can be executed in parallel, except for the very first schedule round after the boot sequence when the blockchain’s first genesis block is created.

# 4. Producer Voting/Scheduling

The voting of the active producers to be included in the next schedule is implemented by the DPoS layer. Strictly speaking, a token holder must first stake some tokens to become a stakeholder and thus be able to vote with a given staking power.

## 4.1. Voting Process

Each EOSIO stakeholder can vote for up to 30 block producers in one voting action. The top 21 elected producers will then act as DPoS delegates to produce and sign blocks on behalf of the stakeholders. The remaining producers are placed in a standby list in the order of votes obtained. The voting process repeats every schedule round by adding up the number of votes obtained by each producer. Producers not voted on get to keep their old votes, albeit depreciated due to vote decay. Producers voted on also get to keep their old votes, except for the contribution of the last voting weight for each voter, which gets replaced by their new voting weight.

### 4.1.1. Voting Weight

The voting weight of each stakeholder is computed as a function of the number of tokens staked and the time elapsed since the EOSIO block timestamp epoch, defined as January 1, 2000. In the current implementation, the voting weight is directly proportional to the number of tokens staked and base-2 exponentially proportional to the time elapsed in years since the year 2000. The actual weight increases at a rate of $2^{1/52} = 1.013419$ per week. This means that the voting weight changes weekly and doubles each year for the same amount of tokens staked.

### 4.1.2. Vote Decay

Increasing the voting weight produces depreciation of the current votes held by each producer. Such vote decay is intentional and its reason is twofold:

* Encourage participation by allowing newer votes to have more weight than older votes.
* Give more voice to those users actively involved on important governance matters.

## 4.2. Producers schedule

After the producers are voted on and selected for the next schedule, they are simply sorted alphabetically by producer name. This determines the production order. Each producer receives the proposed set of producers for the next schedule round within the very first block to be validated from the current schedule round that is about to start. When the first block that contains the proposed schedule is deemed irreversible by a supermajority of producers plus one, the proposed schedule becomes active for the next schedule round.

### 4.2.1. Production Parameters

The EOSIO block production schedule is divided equally among the elected producers. The producers are scheduled to produce an expected number of blocks each schedule round, based on the following parameters (per schedule round):

Parameter | Description | Default | Layer
-|-|-|-
**P** (producers) | number of active producers | 21 | 2
**Bp** (blocks/producer) | number of contiguous blocks per producer | 12 | 1
**Tb** (s/block) | Production time per block (s: seconds) | 0.5 | 1

It is important to mention that Bp (number of contiguous blocks per producer), and Tb (production time per block) are layer 1 consensus constants. In contrast, P (number of active producers) is a layer 2 constant configured by the DPoS layer, which is enabled by WASM contracts.

The following variables can be defined from the above parameters (per schedule round):

Variable | Description | Equation
-|-|-
**B** (blocks) | Total number of blocks | Bp (blocks/producer) x P (producers)
**Tp** (s/producer) | Production time per producer | Tb (s/block) x Bp (blocks/producer)
**T** (s) | Total production time | Tp (s/producer) x P (producers)

Therefore, the value of P, being defined at layer 2, can change dynamically in an EOSIO blockchain. In practice, however, N is strategically set to 21 producers, which means that 15 producers are required for a two-thirds supermajority of producers plus one to reach consensus.

### 4.2.2. Production Default Values

With the current defaults: P=21 elected producers, Bp=12 blocks created per producer, and a block produced every T=0.5 seconds, current production times are as follows (per schedule round):

Variable | Value
-|-
**Tp**: Production time per producer | Tp =  0.5 (s/block) x 12 (blocks/producer) ⇒ Tp = 6 (s/producer)
**T**: Total production time | T = 6 (s/producer) x 21 (producers) ⇒ T = 126 (s)

When a block is not produced by a given producer during its assigned time slot, a gap results in the blockchain.

# 5. Block Lifecycle

Blocks are created by the active producer on schedule during its assigned timeslot, then relayed to other producer nodes for syncing and validation. This process continues from producer to producer until a new schedule of producers is approved at a later schedule round. When a valid block meets the consensus requirements (see [3. EOSIO Consensus](#3-eosio-consensus-dpos--abft)), the block becomes final and is considered irreversible. Therefore, blocks undergo three major phases during their lifespan: production, validation, and finality. Each phase goes through various stages as well.

## 5.1. Block Structure

As an inter-chained sequence of blocks, the fundamental unit within the blockchain is the block. A block contains records of pre-validated transactions and additional cryptographic overhead such as hashes and signatures necessary for block confirmation, re-execution of transactions during validation, blockchain replays, protection against replay attacks, etc. (see `block` schema below).

### block schema

Name | Type | Description
-|-|-
`timestamp` | `block_timestamp_type` | expected time slot this block is produced (ends in .000 or .500 seconds)
`producer` | `name` | account name for producer of this block
`confirmed` | `uint16_t` | number of prior blocks confirmed by the producer of this block in current producer schedule
`previous` | `block_id_type` | block ID for previous block
`transaction_mroot` | `checksum256_type` | merkle tree root hash of transaction receipts included in block
`action_mroot` | `checksum256_type` | merkle tree root hash of action receipts included in block
`schedule_version` | `uint32_t` | number of times producer schedule has changed since genesis
`new_producers` | `producer_schedule_type` | holds producer names and keys for new proposed producer schedule; null if no change
`header_extensions` | `extensions_type` | extends block fields to support additional features (included in block ID calculation)
`producer_signature` | `signature_type` | digital signature by producer that created and signed block
`transactions` | array of `transaction_receipt` | list of valid transaction receipts included in block
`block_extensions` | `extension_type` | extends block fields to support additional features (NOT included in block ID calculation)
`id` | `block_id_type` | UUID of this block ID (a function of block header and block number); can be used to query block for validation/retrieval purposes
`block_num` | `uint32_t` | block number (sequential counter value since genesis block 0); can be used to query block for validation/retrieval purposes
`ref_block_prefix` | `uint32_t` | lower 32 bits of block ID; used to prevent replay attacks

Some of the block fields are known in advance when the block is created, so they are added during block initialization. Others are computed and added during block finalization, such as the merkle root hashes for transactions and actions, the block number and block ID, the signature of the producer that created and signed the block, etc. (see [Network Peer Protocol: 3.1. Block ID](30_network_peer_protocol.md#31-block-id))

## 5.2. Block Production

During each schedule round of block production, the producer on schedule must create Bp=12 contiguous blocks containing as many validated transactions as possible. Each block is currently produced within a span of Tb=500 ms (0.5 s). To guarantee sufficient time to produce each block and transmit to other nodes for validation, the block production time is further divided into two configurable parameters:

* **maximum processing interval**: time window to push transactions into the block (currently set at 200 ms).
* **minimum propagation time**: time window to propagate blocks to other nodes (currently set at 300 ms).

All loose transactions that have not expired yet, or dropped as a result of a previous failed validation, are kept in a local queue for both block inclusion and syncing with other nodes. During block production, the scheduled transactions are applied and validated by the producer on schedule, and if valid, pushed to the pending block within the processing interval. If the transaction falls outside this window, it is unapplied and rescheduled for inclusion in the next block. If there are no more block slots available for the current producer, the transaction is picked up eventually by another producing node (via the peer-to-peer protocol) and pushed to another block. The maximum processing interval is slightly less for the last block (from the producer round of Bp blocks) to compensate for network latencies during handoff to the next producer. By the end of the processing interval, no more transactions are allowed in the pending block, and the block goes through a finalization step before it gets broadcasted to other block producers for validation.

Blocks go through various stages during production: apply, finalize, sign, and commit.

### 5.2.1. Apply Block

Apply block essentially pushes the transactions received and validated by the producing node into a block. Internally, this step involves the creation and initialization of the block header and the signed block instance. The signed block instance simply extends the block header with a signature field. This field eventually holds the signature of the producer that signs the block. Furthermore, recent changes in EOSIO allow multiple signatures to be included, which are stored in a header extensions field.

### 5.2.2. Finalize Block

Produced blocks need to be finalized before they can be signed, committed, relayed, and validated. During finalization, any field in the block header that is necessary for cryptographic validation is computed and stored in the block. This includes generating both merkle tree root hashes for the list of action receipts and the list of transaction receipts pushed to the block.

### 5.2.3. Sign Block

After the transactions have been pushed into the block and the block is finalized, the block is ready to be signed by the producer. This involves computing a signature digest from the serialized contents of the block header, which includes the transaction receipts included in the block. After the block is signed with the producer’s private key, the signature digest is added to the signed block instance. This completes the block signing.

### 5.2.4. Commit Block

After the block is signed, it is committed to the local chain. This pushes the block to the reversible block database (see [Network Peer Protocol: 2.2.3. Fork Database](30_network_peer_protocol.md#223-fork-database)). This makes the block available for syncing with other nodes for validation (see the [Network Peer Protocol](30_network_peer_protocol.md) for more information about block syncing).

## 5.3. Block Validation

Block validation is a fundamental operation necessary to reach consensus within an EOSIO blockchain. During block validation, producers receive incoming blocks from other peers and confirm the transactions included within each block. Block validation is about reaching enough quorum among active producers to agree upon:

* The integrity of the block and the transactions it contains.
* The deterministic, chronological order of transactions within each block.

The first step towards validating a block begins when a block is received by a node. At this point, some safety checks are performed on the block. If the block does not link to an already known block or it matches the block ID of any block already received and processed by the node, the block is discarded. If the block is new, it is pushed to the chain controller for processing.

### 5.3.1. Push Block

When the block is received by the chain controller, the software must determine where to add the block within the local chain. The fork database, or Fork DB for short, is used for this purpose. The fork database holds all the branches with reversible blocks that have been received but are not yet finalized. To that end, the following steps are performed:

1. Add block to the fork database.
2. If block is added to the main branch that contains the current head block, apply block (see [5.2.1. Apply Block](#521-apply-block)); or
3. If block must be added to a different branch, then:
    1. if that branch now becomes the preferred branch compared to the current main branch:  rewind all blocks up to the nearest common ancestor (and rollback the database state in the process), re-apply all blocks in the different branch, add the new block and apply it. That branch now becomes the new main branch.
    2. otherwise: add the new block to that branch in the fork database but do nothing else.

In order for the block to be added to fork database, some block validation must occur. Block header validation must always be done before adding a block to the fork database. And if the block must be applied, some validation of the transactions within the block must occur. The degree to which transactions are validated depends on the validation mode that nodeos is configured with. Two block validation modes are supported: full validation (the default mode), and light validation.

### 5.3.2. Full Validation

In full validation mode, every transaction that is applied is fully validated. This includes verifying the signatures on the transaction and checking authorizations.

### 5.3.3. Light Validation

In light validation mode, blocks signed by trusted producers (which can be configured locally per node) can skip some of the transaction validation done during full validation. For example, signature verification is skipped and all claimed authorizations on actions are assumed to be valid. 

## 5.4. Block Finality

Block finality is the final outcome of EOSIO consensus. It is achieved after a supermajority of active producers have validated the block according to the consensus rules (see [3.1. Layer 1: Native Consensus (aBFT)](#31-layer-1-native-consensus-abft)). Blocks that reach finality are permanently recorded in the blockchain and cannot be undone. In this regard, the last irreversible block (LIB) in the chain refers to the most recent block that has become final. Therefore, from that point backwards the transactions that have been recorded on the blockchain cannot be reversed, tampered, or erased.

### 5.4.1. Goal of Finality

The main point of finality is to give users confidence that transactions that were applied prior and up to the LIB block cannot be modified, rolled back, or dropped. The LIB block can also be useful for active nodes to determine quickly and efficiently which branch to build off from, regardless of which is the longest one. This is because a given branch might be longer without containing the most recent LIB, in which case a shorter branch with the most recent LIB must be selected.
