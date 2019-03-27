---
title: "BIOS Boot Sequence"
excerpt: ""
---
> _The steps here can be readily expanded for the networked case. Some assumptions are made here regarding how the parties involved will coordinate with each other. However, there are many ways that the community can choose to coordinate. The technical aspects of the process are objective; assumptions of how the coordination might occur are speculative. Several approaches have already been suggested by the community. You are encouraged to review the various approaches and get involved in the discussions as appropriate._

# Step 1: Configure the initial set of `nodeos` nodes
In this tutorial, we will start a number of `nodeos` nodes, point them to each other, and eventually vote on a set of producers.  All of the `nodeos` nodes will run on the same server.  In the following sections, we take various steps to prepare our candidate set of producers.  We will use the naming convention `accountnumXY`, with XY chosen from the digits 1-5, e.g.,
```
accountnum11
accountnum12
..
accountnum15
accountnum21
...
accountnum55
```
> _As stated above, the [bios-boot-tutorial.py script](https://github.com/EOSIO/eos/blob/master/tutorials/bios-boot-tutorial/bios-boot-tutorial.py) implements these steps, however, it uses different (and many more) data values.  See the file `accounts.json` for the producer names and the user account names that the script uses._

## Step 1a: Create config and data directories for each `nodeos`
Since all of the `nodeos` nodes will run on the same server, we need separate config and data directories for each. The following example creates directories for each `nodeos` under the directory `~/eosio_test`. Use whatever method works best for you to create a number of accounts, keeping in mind the naming restrictions that account names must be exactly 12 characters, from the set of a-z and 1-5.
```
$ mkdir ~/eosio_test
$ for (( i = 1; i <= 5; i++ )); do for (( j = 1 ; j <=5 ; j++ )); do mkdir ~/eosio_test/accountnum$i$j; done; done
```
You will use these directories with the `--config-dir` and `--data-dir` parameters on the `nodeos` command line.

## Step 1b: Prepare IP addresses for peer-to-peer communication
When we set up our producers, we will want to configure them to point to each other in order to perform peer-to-peer communication. If you set up a full mesh configuration, each node will point to all other nodes. A full mesh network will quickly grow unwieldy. The description below tells how to point nodes to other nodes in order to create the peer-to-peer communication. Use this for the nodes you select to be peers, but it is recommended NOT to use this for all nodes, as your configuration will grow explosively.

Determine the set of IP addresses and port numbers for peer-to-peer communication among each `nodeos` node (you will use this later when you actually start your producer nodes). Each `nodeos` can be configured by setting the `p2p-peer-address` configuration property, either on the command line when starting `nodeos` (one argument per peer), or by setting the property in the `config.ini` file for `nodeos` (one line per peer).

For example, assuming we are using port numbers 9011-9055 for the producers (i.e., `accountnum11` - `accountnum55`, respectively), include the following arguments on the `nodeos` command line for `accountnum12`:
```
--p2p-peer-address localhost:9011 --p2p-peer-address localhost:9013 --p2p-peer-address localhost:9014 ...
```
_**OR**_
In the `config.ini` file for `accountnum12`, add lines for each peer:
``` 
p2p-peer-address = localhost:9011
p2p-peer-address = localhost:9013
p2p-peer-address = localhost:9014
...
```
If using the configuration file approach, you will have many copies of the `config.ini` file, one in each `~/eosio_test/accountnumXY` directory. Whether using the command line or config file approach, be careful to NOT include the producer's own address in the list of peers.


# Step 2: Start the "genesis" node
The "genesis" node is the first `nodeos` that we start, that will originate the blockchain. All other nodes will derive from the genesis node. Do the following on the genesis node.

## Step 2a: Create a wallet
Create a wallet. By default, `keosd` is automatically started to manage the wallet.
```
$ cleos wallet create
```
Be sure to save the wallet password to enable unlocking the wallet in the future.

The same wallet will be used for all key management for all accounts in this tutorial, regardless of which `nodeos` is being accessed. In a distributed deployment, wallet management should be a local-only activity.


## Step 2b: Configure the `genesis.json` file.
The `genesis.json` file defines the initial chain state. All nodes must start from the same initial state. Two properties in particular are highlighted here. The `initial_timestamp` represents the start time of the blockchain. The `initial_key` is used by the genesis node to start producing. It needs to be the same among all nodes. The `initial_key` property in `genesis.json` must match the public key of the genesis `nodeos`. The `nodeos` key pair can be specified using the `--private-key` argument on the `nodeos` command line, or by setting the `private-key` property in the `config.ini` file.

The `genesis.json` file used by the script can be found in the `tutorial/bios-boot-tutorial` directory. All `nodeos` instances will be started using this file. The script specifies the `nodeos` key pair on the command line. The script allows you to specify the key pair for the genesis node (`--private-key` and `--public-key` options). If specifying the genesis node's key, be sure to make any necessary changes to your `genesis.json` file. The script will start the genesis node with that key pair, and will create the `eosio.*` accounts using this key pair.

## Step 2c: Create the key for the `eosio` account
`nodeos` comes pre-configured with a key pair, but we don't want to use that key. Create a key pair to be used for the `eosio` account when starting the genesis node. _The tutorial script comes pre-configured with its own custom key pair. (see above)_
``` 
$ cleos create key
Private key: 5JGxnezvp3N4V1NxBo8LPBvCrdR85bZqZUFvBZ8ACrbRC3ZWNYv
Public key: EOS8VJybqtm41PMmXL1QUUDSfCrs9umYN4U1ZNa34JhPZ9mU5r2Cm
```
### Step 2d: Start the genesis `nodeos` node
Start the genesis node using the generated key pair.
```
$ nodeos -e -p eosio --private-key '[ "EOS8VJybqtm41PMmXL1QUUDSfCrs9umYN4U1ZNa34JhPZ9mU5r2Cm","5JGxnezvp3N4V1NxBo8LPBvCrdR85bZqZUFvBZ8ACrbRC3ZWNYv" ]' --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::history_api_plugin
```

# Step 3: Create important system accounts
There are several system accounts that are needed.  These are:

```
  eosio.bpay
  eosio.msig
  eosio.names
  eosio.ram
  eosio.ramfee
  eosio.saving
  eosio.stake
  eosio.token
  eosio.vpay
```

Repeat the following steps to create an account for each of the system accounts.  In this tutorial, we will use the same key pair for both the account owner and active keys, so we only need to provide the key value once on the command line. For most general accounts, it is good practice to use separate keys for owner and active. The script uses the same key for all of the `eosio.*` accounts. You can use different keys for each.

``` 
$ cleos create key  # for eosio.bpay
Private key: 5KAVVPzPZnbAx8dHz6UWVPFDVFtU1P5ncUzwHGQFuTxnEbdHJL4
Public key: EOS84BLRbGbFahNJEpnnJHYCoW9QPbQEk2iHsHGGS6qcVUq9HhutG

$ cleos wallet import --private-key 5KAVVPzPZnbAx8dHz6UWVPFDVFtU1P5ncUzwHGQFuTxnEbdHJL4
imported private key for: EOS84BLRbGbFahNJEpnnJHYCoW9QPbQEk2iHsHGGS6qcVUq9HhutG

$ cleos create account eosio eosio.bpay EOS84BLRbGbFahNJEpnnJHYCoW9QPbQEk2iHsHGGS6qcVUq9HhutG
executed transaction: ca68bb3e931898cdd3c72d6efe373ce26e6845fc486b42bc5d185643ea7a90b1  200 bytes  280 us
#         eosio <= eosio::newaccount            {"creator":"eosio","name":"eosio.bpay","owner":{"threshold":1,"keys":[{"key":"EOS84BLRbGbFahNJEpnnJH...
```

# Step 4: Install the `eosio.token`contract
Set the `eosio.token` contract. This contract enables you to create, issue, transfer, and get information about tokens. Note that the example assumes you built `eos` in the `~/Documents/eos` folder.

```
$ cleos set contract eosio.token ~/Documents/eos/build/contracts/eosio.token
Reading WAST/WASM from /Users/tutorial/Documents/eos/build/contracts/eosio.token/eosio.token.wasm...
Using already assembled WASM...
Publishing contract...
executed transaction: 17fa4e06ed0b2f52cadae2cd61dee8fb3d89d3e46d5b133333816a04d23ba991  8024 bytes  974 us
#         eosio <= eosio::setcode               {"account":"eosio.token","vmtype":0,"vmversion":0,"code":"0061736d01000000017f1560037f7e7f0060057f7e...
#         eosio <= eosio::setabi                {"account":"eosio.token","abi":{"types":[],"structs":[{"name":"transfer","base":"","fields":[{"name"...
```

# Step 5: Set the `eosio.msig` contract
Set the `eosio.msig` contract. The msig contract enables and simplifies defining and managing permission levels and performing multi-signature actions. Note that this assumes that you built EOSIO in the `~/Documents/eos` folder.

```
$ cleos set contract eosio.msig ~/Documents/eos/build/contracts/eosio.msig
Reading WAST/WASM from /Users/tutorial/Documents/eos/build/contracts/eosio.msig/eosio.msig.wasm...
Using already assembled WASM...
Publishing contract...
executed transaction: 007507ad01de884377009d7dcf409bc41634e38da2feb6a117ceced8554a75bc  8840 bytes  925 us
#         eosio <= eosio::setcode               {"account":"eosio.msig","vmtype":0,"vmversion":0,"code":"0061736d010000000198011760017f0060047f7e7e7...
#         eosio <= eosio::setabi                {"account":"eosio.msig","abi":{"types":[{"new_type_name":"account_name","type":"name"}],"structs":[{...
```

# Step 6: Create and allocate the `SYS`  currency
Create the `SYS` currency with a maximum value of 10 billion tokens. Then issue one billion tokens. Replace `SYS` with your specific currency designation.

```
$ cleos push action eosio.token create '[ "eosio", "10000000000.0000 SYS" ]' -p eosio.token@active
executed transaction: 0440461e0d8816b4a8fd9d47c1a6a53536d3c7af54abf53eace884f008429697  120 bytes  326 us
#   eosio.token <= eosio.token::create          {"issuer":"eosio","maximum_supply":"10000000000.0000 SYS"}

$ cleos push action eosio.token issue '[ "eosio", "1000000000.0000 SYS", "memo" ]' -p eosio@active
executed transaction: a53961a566c1faa95531efb422cd952611b17d728edac833c9a55582425f98ed  128 bytes  432 us
#   eosio.token <= eosio.token::issue           {"to":"eosio","quantity":"1000000000.0000 SYS","memo":"memo"}
```

In the first step above, the `create` action from the `eosio.token` contract, authorized by the `eosio.token` account, creates 10B `SYS` tokens in the `eosio` account. This effectively creates the maximum supply of tokens, but does not put any tokens into circulation. Tokens not in circulation can be considered to be held in reserve.

In the second step, the `eosio.token` contract's `issue` action takes 1B `SYS` tokens out of reserve and puts them into circulation. At the time of issue, the tokens are held within the `eosio` account. Since the `eosio` account owns the reserve of uncirculated tokens, its authority is required to do the action.

_As a point of interest, from an economic point of view, moving token from reserve into circulation, such as by issuing tokens, is an inflationary action. Issuing tokens is just one way that inflation can occur._

# Step 7: Set the `eosio.system`  contract
Set the `eosio.system` contract. This contract provides the actions for pretty much all token-based operational behavior. Prior to installing the system contract, actions are done independent of accounting. Once the system contract is enabled, actions now have an economic element to them. Resources (cpu, network, memory) must be paid for. Likewise, new accounts must be paid for. The system contract enables tokens to be staked and unstaked, resources to be purchased, potential producers to be registered and subsequently voted on, producer rewards to be claimed, privileges and limits to be set, and more.

```
$ cleos set contract eosio ~/Documents/eos/build/contracts/eosio.system
Reading WAST/WASM from /Users/tutorial/Documents/eos/build/contracts/eosio.system/eosio.system.wasm...
Using already assembled WASM...
Publishing contract...
executed transaction: 2150ed87e4564cd3fe98ccdea841dc9ff67351f9315b6384084e8572a35887cc  39968 bytes  4395 us
#         eosio <= eosio::setcode               {"account":"eosio","vmtype":0,"vmversion":0,"code":"0061736d0100000001be023060027f7e0060067f7e7e7f7f...
#         eosio <= eosio::setabi                {"account":"eosio","abi":{"types":[],"structs":[{"name":"buyrambytes","base":"","fields":[{"name":"p...
```

# Step 8: Transition from single producer to multiple producers

In the next set of steps, we will transition from a single block producer (the genesis node) to multiple producers. Up to this point, only the built-in `eosio` account has been privileged and can sign blocks. The target is to manage the blockchain by a collection of elected producers operating under a rule of 2/3 + 1 producers agreeing before a block is final

Producers are chosen by election. The list of producers can change. Rather than give privileged authority directly to any producer, the governing rules are associated with a special built-in account named `eosio.prods`. This account represents the group of elected producers. The `eosio.prods` account (effectively the producer group) operates using permissions defined by the `eosio.msig` contract.

As soon as possible after installing the `eosio.system` contract, we want to make `eosio.msig` a privileged account so that it can authorize on behalf of the `eosio` account. As soon as possible, `eosio` will resign its authority and `eosio.prods` will take over.

### Make `eosio.msig` a privileged account

We make `eosio.msig` privileged using the following. 

```
$ cleos push action eosio setpriv '["eosio.msig", 1]' -p eosio@active
```

# Step 9: Stake tokens and expand the network
If you've followed the tutorial steps above to this point, you now have a single host, single-node configuration with the following contracts installed:

- eosio.token
- eosio.msig
- eosio.system

Accounts `eosio` and `eosio.msig` are privileged accounts.  The other `eosio.*` accounts have been created but are not privileged.

We are now ready to begin staking accounts and expanding the network of producers.

# Step 10: Create staked accounts

Staking is the process of allocating tokens acquired by an entity in the "real world" (e.g., an individual purchasing something at a Crowdsale or some other means) to an account within the EOSIO system.  Staking and unstaking are an on-going process throughout the life of a blockchain. The initial staking done during the bios boot process is special. During the bios boot sequence, accounts are staked with their tokens. However, until producers are elected, tokens are effectively in a frozen state. Thus the goal of the initial staking done during the bios boot sequence is to get tokens allocated to their accounts and ready for use, and get the voting process going so that producers can get elected and the blockchain running "live".

The following recommendation is given for the initial staking process:

1.  0.1 token (literally, not 10% of the account's tokens) is staked for RAM.  By default, `cleos` stakes 8 KB of RAM on account creation, paid by the account creator. In the initial staking, the `eosio` account is the account creator doing the staking. Tokens staked during the initial token staking process cannot be unstaked and made liquid until after the minimum voting requirements have been met.
2.  0.45 token is staked for CPU, and 0.45 token is staked for network.
3.  The next available tokens up to 9 total are held as liquid tokens.
4.  Remaining tokens are staked 50/50 CPU and network.

```
Example 1.  accountnum11 has 100 SYS. It will be staked as 0.1000 SYS on RAM; 45.4500 SYS on CPU; 45.4500 SYS on network; and 9.0000 SYS held for liquid use.

Example 2.  accountnum33 has 5 SYS. It will be staked as 0.1000 SYS on RAM; 0.4500 SYS on CPU; 0.4500 SYS on network; and 4.0000 SYS held for liquid use.
```

To make the tutorial more realistic, we distribute the 1B tokens to accounts using a Pareto distribution. The Pareto distribution models an 80-20 rule, e.g., in this case, 80% of the tokens are held by 20% of the population. The examples here do not show how to generate the distribution, focusing instead on the commands to do the staking. The script `bios-boot-tutorial.py` that accompanies this tutorial uses the Python NumPy (numpy) library to generate a Pareto distribution.

## Step 10a: Create a staked account
Use the following steps to stake tokens for each account. These steps must be done individually for each account.

> _The key pair is created here for this tutorial. In a "live" scenario, the key value(s) and token share for an account should already be established through some well-defined out-of-band process._

```
	$ cleos create key  # for accountnum11
	Private key: 5K7EYY3j1YY14TSFVfqgtbWbrw3FA8BUUnSyFGgwHi8Uy61wU1o
	Public key: EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt
	   
	$ cleos wallet import --private-key 5K7EYY3j1YY14TSFVfqgtbWbrw3FA8BUUnSyFGgwHi8Uy61wU1o
	imported private key for: EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt
```

Create a staked account with initial resources and public key.

```
$ cleos system newaccount eosio --transfer accountnum11 EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt --stake-net "100000.0000 SYS" --stake-cpu "100000.0000 SYS" --buy-ram-kbytes 8192
775292ms thread-0   main.cpp:419                  create_action        ] result: {"binargs":"0000000000ea30551082d4334f4d113200200000"} arg: {"code":"eosio","action":"buyrambytes","args":{"payer":"eosio","receiver":"accountnum11","bytes":8192}} 
775295ms thread-0   main.cpp:419                  create_action        ] result: {"binargs":"0000000000ea30551082d4334f4d113200ca9a3b00000000045359530000000000ca9a3b00000000045359530000000001"} arg: {"code":"eosio","action":"delegatebw","args":{"from":"eosio","receiver":"accountnum11","stake_net_quantity":"100000.0000 SYS","stake_cpu_quantity":"100000.0000 SYS","transfer":true}} 
executed transaction: fb47254c316e736a26873cce1290cdafff07718f04335ea4faa4cb2e58c9982a  336 bytes  1799 us
#         eosio <= eosio::newaccount            {"creator":"eosio","name":"accountnum11","owner":{"threshold":1,"keys":[{"key":"EOS8mUftJXepGzdQ2TaC...
#         eosio <= eosio::buyrambytes           {"payer":"eosio","receiver":"accountnum11","bytes":8192}
#         eosio <= eosio::delegatebw            {"from":"eosio","receiver":"accountnum11","stake_net_quantity":"100000.0000 SYS","stake_cpu_quantity...
```

# Step 11: Select the producers
Some set of the accounts created will be registered as producers. Choose some set of the staked accounts to be producers.

## Step 11a: Register as a producer
Use the following command to register as a producer. This makes the node a candidate to be a producer, but the node will not actually be a producer unless it is elected.

```
$ cleos system regproducer accountnum11 EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt https://accountnum11.com/EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt
1487984ms thread-0   main.cpp:419                  create_action        ] result: {"binargs":"1082d4334f4d11320003fedd01e019c7e91cb07c724c614bbf644a36eff83a861b36723f29ec81dc9bdb4e68747470733a2f2f6163636f756e746e756d31312e636f6d2f454f53386d5566744a586570477a64513254614364754e7553504166584a48663232756578347534316162314556763945416857740000"} arg: {"code":"eosio","action":"regproducer","args":{"producer":"accountnum11","producer_key":"EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt","url":"https://accountnum11.com/EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt","location":0}} 
executed transaction: 4ebe9258bdf1d9ac8ad3821f6fcdc730823810a345c18509ac41f7ef9b278e0c  216 bytes  896 us
#         eosio <= eosio::regproducer           {"producer":"accountnum11","producer_key":"EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt","u...
```

## Step 11b: List the producers
To facilitate the voting process, list the available producers.

```
$ cleos system listproducers
Producer      Producer key                                           Url                                                         Scaled votes
accountnum11  EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt  https://accountnum11.com/EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22 0.0000
accountnum22  EOS5kgeCLuQo8MMLnkZfqcBA3GRFgQsPyDddHWmXceRLjRX8LJRaH  https://accountnum22.com/EOS5kgeCLuQo8MMLnkZfqcBA3GRFgQsPyD 0.0000
accountnum33  EOS63CnoyfeEQDjXXxwywN5PPKW7RYHC9tbtmvb8vFBGZooktz7kG  https://accountnum33.com/EOS63CnoyfeEQDjXXxwywN5PPKW7RYHC9t 0.0000
accountnum44  EOS6kBaCHrvz7VdUfFBLrLdhNjXYaKBmRkpDXU9PhbEUiHbspr7rz  https://accountnum44.com/EOS6kBaCHrvz7VdUfFBLrLdhNjXYaKBmRk 0.0000
```

## Step 11c: Start the producers
Use the following command to start the producers.  Recall that in this tutorial, all of the producers are running on a single server, so command line arguments are used to ensure each producer is using its own directory.

In a separate window for each producer, run the following `nodeos` command, adjusting the command line arguments for each producer.
```
$ nodeos --genesis-json ~/eosio_test/accountnum11/genesis.json --blocks-dir ~/eosio_test/accountnum11/blocks --config-dir ~/eosio_test/accountnum11/ --data-dir ~/eosio_test/accountnum11/ --http-server-address 127.0.0.1:8011 --p2p-listen-endpoint 127.0.0.1:9011 --enable-stale-production --producer-name accountnum11 --private-key '[ "EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt","5K7EYY3j1YY14TSFVfqgtbWbrw3FA8BUUnSyFGgwHi8Uy61wU1o" ]' --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::history_api_plugin --p2p-peer-address localhost:9022  --p2p-peer-address localhost:9033  --p2p-peer-address localhost:9044 
```
Note that until all producers are up, connection error messages such as the following will be generated.
```
1826099ms thread-0   net_plugin.cpp:2927           plugin_startup       ] starting listener, max clients is 25
1826099ms thread-0   net_plugin.cpp:676            connection           ] created connection to localhost:9022
1826099ms thread-0   net_plugin.cpp:1948           connect              ] host: localhost port: 9022 
1826099ms thread-0   net_plugin.cpp:676            connection           ] created connection to localhost:9033
1826099ms thread-0   net_plugin.cpp:1948           connect              ] host: localhost port: 9033 
1826099ms thread-0   net_plugin.cpp:676            connection           ] created connection to localhost:9044
1826099ms thread-0   net_plugin.cpp:1948           connect              ] host: localhost port: 9044 
1826100ms thread-0   net_plugin.cpp:1989           operator()           ] connection failed to localhost:9022: Connection refused
1826100ms thread-0   net_plugin.cpp:1989           operator()           ] connection failed to localhost:9033: Connection refused
1826100ms thread-0   net_plugin.cpp:1989           operator()           ] connection failed to localhost:9044: Connection refused
```


For convenience, the following command lines can be copied to run `nodeos` in separate shell windows for accounts `accountnum22`, `accountnum33`, and `accountnum44`. If you run these, you can see how multiple nodes respond when running in a peer-to-peer configuration. This assumes that accounts have been staked using the relevant key pairs (the key pairs can be seen in each of the command lines below).

```
$ nodeos --genesis-json ~/eosio_test/accountnum22/genesis.json --block-log-dir ~/eosio_test/accountnum22/blocks --config-dir ~/eosio_test/accountnum22/ --data-dir ~/eosio_test/accountnum22/ --http-server-address 127.0.0.1:8022 --p2p-listen-endpoint 127.0.0.1:9022 --enable-stale-production --producer-name accountnum22 --private-key '[ "EOS5kgeCLuQo8MMLnkZfqcBA3GRFgQsPyDddHWmXceRLjRX8LJRaH","5Jh4rseyguLx5Y7KE2oLL81PRmDcyyzbyyyJd3GvdHijKqENbRk" ]' --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --p2p-peer-address localhost:9011  --p2p-peer-address localhost:9033  --p2p-peer-address localhost:9044
$ nodeos --genesis-json ~/eosio_test/accountnum33/genesis.json --block-log-dir ~/eosio_test/accountnum33/blocks --config-dir ~/eosio_test/accountnum33/ --data-dir ~/eosio_test/accountnum33/ --http-server-address 127.0.0.1:8033 --p2p-listen-endpoint 127.0.0.1:9033 --enable-stale-production --producer-name accountnum33 --private-key '[ "EOS63CnoyfeEQDjXXxwywN5PPKW7RYHC9tbtmvb8vFBGZooktz7kG","5JWp5K24x5dbAFBNP7hwzSRS7XjD7wjHL4nrAwSLdRuJnERjgqB" ]' --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --p2p-peer-address localhost:9011  --p2p-peer-address localhost:9022  --p2p-peer-address localhost:9044
$ nodeos --genesis-json ~/eosio_test/accountnum44/genesis.json --block-log-dir ~/eosio_test/accountnum44/blocks --config-dir ~/eosio_test/accountnum44/ --data-dir ~/eosio_test/accountnum44/ --http-server-address 127.0.0.1:8044 --p2p-listen-endpoint 127.0.0.1:9044 --enable-stale-production --producer-name accountnum44 --private-key '[ "EOS6kBaCHrvz7VdUfFBLrLdhNjXYaKBmRkpDXU9PhbEUiHbspr7rz","5KeGoDkbhEdkZTpYqQg2rPZvtxqfWAtGgixuCLUt1Dmoq4NmXCj" ]' --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --p2p-peer-address localhost:9011  --p2p-peer-address localhost:9022  --p2p-peer-address localhost:9033
```

## Step 11c: The genesis node `genesis.json` file
 This also expects that the `genesis.json` file, e.g, see below, has been copied to the respective account directories.
```json
{
  "initial_timestamp": "2018-03-02T12:00:00.000",
  "initial_key": "EOS8Znrtgwt8TfpmbVpTKvA2oB8Nqey625CLN8bCN3TEbgx86Dsvr",
  "initial_configuration": {
    "max_block_net_usage": 1048576,
    "target_block_net_usage_pct": 1000,
    "max_transaction_net_usage": 524288,
    "base_per_transaction_net_usage": 12,
    "net_usage_leeway": 500,
    "context_free_discount_net_usage_num": 20,
    "context_free_discount_net_usage_den": 100,
    "max_block_cpu_usage": 100000,
    "target_block_cpu_usage_pct": 500,
    "max_transaction_cpu_usage": 50000,
    "min_transaction_cpu_usage": 100,
    "max_transaction_lifetime": 3600,
    "deferred_trx_expiration_window": 600,
    "max_transaction_delay": 3888000,
    "max_inline_action_size": 4096,
    "max_inline_action_depth": 4,
    "max_authority_depth": 6,
    "max_generated_transaction_count": 16
  },
  "initial_chain_id": "0000000000000000000000000000000000000000000000000000000000000000"
}
```

_**Note:  Output from each node is captured in the file `stderr` within that node's working directory, e.g., `./nodes/accountnum44/stderr`. By default, the nodes started by the script continue to run. Care must be taken to avoid the disk filling from 30+ nodes running simultaneously, each separately writing its output to  a file in the file system.**_



# Step 12: Resign `eosio` 

Once producers have been elected and the minimum number requirements have been met, the `eosio` account can resign, leaving the `eosio.msig` account as the only privileged account.

Resigning basically involves setting the keys of the `eosio.*` accounts to null. Use the following command to clear the `eosio.*` accounts' owner and active keys:

```
$ cleos push action eosio updateauth '{"account": "eosio", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": "active"}}]}}' -p eosio@owner
$ cleos push action eosio updateauth '{"account": "eosio", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": "active"}}]}}' -p eosio@active
```