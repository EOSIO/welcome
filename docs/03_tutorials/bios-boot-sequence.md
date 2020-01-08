---
content_title: BIOS Boot Sequence
link_text: BIOS Boot Sequence
---

> _The steps here can be readily expanded for the networked case. Some assumptions are made here regarding how the parties involved will coordinate with each other. However, there are many ways that the community can choose to coordinate. The technical aspects of the process are objective; assumptions of how the coordination might occur are speculative. Several approaches have already been suggested by the community. You are encouraged to review the various approaches and get involved in the discussions as appropriate._

## 1. Create, configure and start the genesis node
This tutorial is going to walk you through the preparation steps needed to set up your `eos` environment and through the steps needed to start your own genenis eos node and then the steps needed to set up additional eos nodes, and connect them to the genesis node and between themselves; at the end you'll have a full eos blockchain running locally.

The [bios-boot-tutorial.py](https://github.com/EOSIO/eos/blob/master/tutorials/bios-boot-tutorial/bios-boot-tutorial.py) python script implements the same steps, thus automating them, however, it uses different (and many more) data values. See the file `accounts.json` for the producer names and the user account names that the script uses.

If your goal is to see a full EOS blockchain at work on your local machine you can run the script directly following the [README.md](https://github.com/EOSIO/eos/blob/master/tutorials/bios-boot-tutorial/README.md) instructions.

If your goal is to go beyond and understand what the script is doing, you can follow this tutorial which will get you through the same steps explaining also along the way each step needed to go through.

### **1.1. Install pre-compiled eosio and eosio.cdt binaries**

Go to [Install EOSIO pre-compiled binaries](https://developers.eos.io/eosio-home/docs/setting-up-your-environment) tutorial and install the `nodeos` binaries but do not start the `nodeos` yet.

Go to [Install EOSIO.CDT binaries](https://github.com/EOSIO/eosio.cdt#binary-releases) tutorial and install the `EOSIO.CDT` binaries; you can stop following that tutorial at the step "Building your first smart contract".

### **1.2. Set up wallet**

Go to [Create development wallet](https://developers.eos.io/eosio-home/docs/wallets) tutorial, configure your default wallet, create a public and private development keys (we will refer to them as `EOS_PUB_DEV_KEY` and `EOS_PRIV_DEV_KEY`) and import them into the wallet you created previously.

### **1.3. Create '~/biosboot/genesis' directory**

Inside this directory we'll start the genesis node, by executing `nodeos` with specific parameters, which will create the blockchain database, log file and config file inside this directory.
```shell
cd ~
mkdir biosboot
cd biosboot
mkdir genesis
cd genesis
```
### **1.4. Create genesis.json file, in `~/biosboot/` directory**

Create the empty `genesis.json` file in the `~/biosboot/` directory and open it in a text editor (in this case we use nano):
```shell
cd ~/biosboot
touch genesis.json
nano genesis.json
```
Copy below json content to clipboard
```json
{
  "initial_timestamp": "2018-12-05T08:55:11.000",
  "initial_key": "EOS_PUB_DEV_KEY",
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
    "max_authority_depth": 6
  },
  "initial_chain_id": "0000000000000000000000000000000000000000000000000000000000000000"
}

```
Paste the content of your clipboard into the edited genesis json file.
The `EOS_PUB_DEV_KEY` is the public key you created in the previous 1.2 step. 

Last, save and exit the text editor using below key strokes:
```shell
[CTRL]+X
y
[ENTER]

```
### **1.5. Start the genesis node by running genesis_start.sh**

First let's create the `genesis_start.sh` shell script file in the `~/biosnode/genesis/` directory.
Execute these below commands:
```shell
cd ~/biosboot/genesis
touch genesis_start.sh
nano genesis_start.sh

```
Copy to clipboard below shell script content:
```shell
#!/bin/bash
DATADIR="./blockchain"

if [ ! -d $DATADIR ]; then
  mkdir -p $DATADIR;
fi

nodeos \
--genesis-json $DATADIR"/../../genesis.json" \
--signature-provider EOS_PUB_DEV_KEY=KEY:EOS_PRIV_DEV_KEY \
--plugin eosio::producer_plugin \
--plugin eosio::producer_api_plugin \
--plugin eosio::chain_plugin \
--plugin eosio::chain_api_plugin \
--plugin eosio::http_plugin \
--plugin eosio::history_api_plugin \
--plugin eosio::history_plugin \
--data-dir $DATADIR"/data" \
--blocks-dir $DATADIR"/blocks" \
--config-dir $DATADIR"/config" \
--producer-name eosio \
--http-server-address 127.0.0.1:8888 \
--p2p-listen-endpoint 127.0.0.1:9010 \
--access-control-allow-origin=* \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors \
--enable-stale-production \
--p2p-peer-address localhost:9011 \
--p2p-peer-address localhost:9012 \
--p2p-peer-address localhost:9013 \
>> $DATADIR"/nodeos.log" 2>&1 & \
echo $! > $DATADIR"/eosd.pid"

```
Paste the content of your clipboard in the editor of your choice.
Make sure you replace the `EOS_PUB_DEV_KEY` and `EOS_PRIV_DEV_KEY` with the keys you generated in step 1.2 previously.
Save and exit (using same keystroke as previous step: `CTRL+X, y, ENTER`).

Now we have to assign execution privileges to `genesis_start.sh` shell script file in order for us to be able to run it. And after that execute the `genesis_start.sh` script which will start the genesis `nodeos` which
- has the name eosio
- produces blocks
- listens for http request on 127.0.0.1:8888
- listens for peer connections requests on 127.0.0.1:9010
- initiates periodic peer connections to localhost:9011, localhost:9012 and localhost:9013; these nodes are not running yet so it is ok if you see these connection attempts failing
- has parameter `--contracts-console` which is printing contracts output to console, in our case this info is good for troubleshooting problems
```shell
cd ~/biosboot/genesis/
chmod 755 genesis_start.sh
./genesis_start.sh

```
To stop `nodeos` execute `stop.sh` shell script from the same `~/biosboot/genesis/` directory.
The script `stop.sh` is present below, and you can create it following the same steps you did for creating and assigning execution privileges for `genesis_start.sh`
```shell
#!/bin/bash
DATADIR="./blockchain/"

if [ -f $DATADIR"/eosd.pid" ]; then
pid=`cat $DATADIR"/eosd.pid"`
echo $pid
kill $pid
rm -r $DATADIR"/eosd.pid"
echo -ne "Stoping Node"
while true; do
[ ! -d "/proc/$pid/fd" ] && break
echo -ne "."
sleep 1
done
echo -ne "\rNode Stopped. \n"
fi

```
After stopping the `nodeos` process, you will not be able to restart it using the same `.genesis_start.sh` script because once a node has been running and producing blocks, thus blockchain database has been initialized and it is not empty, `nodeos` can not start anymore with `--genesis-json` parameter; therefore it is recommended to create another script `start.sh` the same way as you created the other script with the below content, give execution privileges to it and use it from here onward to re-start the node after you stopped it.
```shell
#!/bin/bash
DATADIR="./blockchain"

if [ ! -d $DATADIR ]; then
  mkdir -p $DATADIR;
fi

nodeos \
--signature-provider EOS_PUB_DEV_KEY=KEY:EOS_PRIV_DEV_KEY \
--plugin eosio::producer_plugin \
--plugin eosio::producer_api_plugin \
--plugin eosio::chain_plugin \
--plugin eosio::chain_api_plugin \
--plugin eosio::http_plugin \
--plugin eosio::history_api_plugin \
--plugin eosio::history_plugin \
--data-dir $DATADIR"/data" \
--blocks-dir $DATADIR"/blocks" \
--config-dir $DATADIR"/config" \
--producer-name eosio \
--http-server-address 127.0.0.1:8888 \
--p2p-listen-endpoint 127.0.0.1:9010 \
--access-control-allow-origin=* \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors \
--enable-stale-production \
--p2p-peer-address localhost:9011 \
--p2p-peer-address localhost:9012 \
--p2p-peer-address localhost:9013 \
>> $DATADIR"/nodeos.log" 2>&1 & \
echo $! > $DATADIR"/eosd.pid"

```
Sometimes, restarting a `nodeos` requires the parameter `--hard-replay` which is replaying all the transactions from the genesis. You will know when this is needed when you'll start `nodeos` and you'll notice an error in the log file mentioning exactly this `"perhaps we need to replay"`. Also you should read about these other parameters you can use to start `nodeos`: `--truncate-at-block, --delete-all-blocks, --replay-blockchain, --hard-replay-blockchain`

We present here the `hard_replay.sh` shell script which is using the `--hard-replay-blockchain` parameter:
```shell
#!/bin/bash
DATADIR="./blockchain"

if [ ! -d $DATADIR ]; then
  mkdir -p $DATADIR;
fi

nodeos \
--signature-provider EOS_PUB_DEV_KEY=KEY:EOS_PRIV_DEV_KEY \
--plugin eosio::producer_plugin \
--plugin eosio::producer_api_plugin \
--plugin eosio::chain_plugin \
--plugin eosio::chain_api_plugin \
--plugin eosio::http_plugin \
--plugin eosio::history_api_plugin \
--plugin eosio::history_plugin \
--data-dir $DATADIR"/data" \
--blocks-dir $DATADIR"/blocks" \
--config-dir $DATADIR"/config" \
--producer-name eosio \
--http-server-address 127.0.0.1:8888 \
--p2p-listen-endpoint 127.0.0.1:9010 \
--access-control-allow-origin=* \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors \
--enable-stale-production \
--p2p-peer-address localhost:9011 \
--p2p-peer-address localhost:9012 \
--p2p-peer-address localhost:9013 \
--hard-replay-blockchain \
>> $DATADIR"/nodeos.log" 2>&1 & \
echo $! > $DATADIR"/eosd.pid"

```
Last copy below content and create a shell script name clean.sh and give execution permission to it.
```shell
#!/bin/bash
rm -fr blockchain
ls -al

```
If you want to wipe out the current configuration, blockchain data and config and log, first run the `stop.sh` script and after that run the `clean.sh` script which you'll have to create from below content:
```shell
cd ~/biosboot/genesis/
./stop.sh
./clean.sh
./genesis_start.sh
```
### **1.6. Inspect the `nodeos.log` file**

You can inspect the `nodeos.log` file with below command, and use `CTRL+C to` exit the listing mode.
```shell
cd ~/biosboot/genesis/
tail -f ./blockchain/nodeos.log
```
### **1.7. Create important system accounts**
There are several system accounts that are needed, namely the following:

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
  eosio.rex
```

Repeat the following steps to create an account for each of the system accounts.  In this tutorial, we will use the same key pair for both the account owner and active keys, so we only need to provide the key value once on the command line. For most general accounts, it is good practice to use separate keys for owner and active. The script uses the same key for all of the `eosio.*` accounts. You can use different keys for each.
```text
cleos create key --to-console

```
```
Private key: 5KAVVPzPZnbAx8dHz6UWVPFDVFtU1P5ncUzwHGQFuTxnEbdHJL4
Public key: EOS84BLRbGbFahNJEpnnJHYCoW9QPbQEk2iHsHGGS6qcVUq9HhutG
```
```shell
cleos wallet import --private-key
```
```
5KAVVPzPZnbAx8dHz6UWVPFDVFtU1P5ncUzwHGQFuTxnEbdHJL4
imported private key for: EOS84BLRbGbFahNJEpnnJHYCoW9QPbQEk2iHsHGGS6qcVUq9HhutG
```
```shell
cleos create account eosio eosio.bpay EOS84BLRbGbFahNJEpnnJHYCoW9QPbQEk2iHsHGGS6qcVUq9HhutG
```
```
executed transaction: ca68bb3e931898cdd3c72d6efe373ce26e6845fc486b42bc5d185643ea7a90b1  200 bytes  280 us
#         eosio <= eosio::newaccount            {"creator":"eosio","name":"eosio.bpay","owner":{"threshold":1,"keys":[{"key":"EOS84BLRbGbFahNJEpnnJH...
```

### **1.8. Build `eosio.contracts`**

In order to build `eosio.contracts` execute the commands below, they will create a dedicated directory for `eosio.contracts`, clone the `eosio.contracts` sources, build them and finally it will print at the console the current directory which you should make note of it, we will reference to this directory as `EOSIO_CONTRACTS_DIRECTORY` from here onward when needed.
```shell
cd ~
git clone https://github.com/EOSIO/eosio.contracts.git
cd ./eosio.contracts/
./build.sh
cd ./build/contracts/
pwd
```

You will also need an older version of `eosio.contracts` specifically v1.8.0, so follow the instructions below to build it and remember the path where they are built:

1. Install eosio.cdt version 1.6.3 binaries by following the steps outlined in below tutorial
[Install eosio.cdt binaries](https://github.com/EOSIO/eosio.cdt/tree/release/1.6.x#binary-releases)

2. After the eosio.cdt 1.6.3 version is installed you can compile the older version of eosio.contracts:

```shell
cd ~
git clone https://github.com/EOSIO/eosio.contracts.git eosio.contracts-1.8.x
cd ./eosio.contracts-1.8.x/
git checkout release/1.8.x
./build.sh
cd ./build/contracts/
pwd
```

Make note of the printed local path, we will reference to this directory as `EOSIO_OLD_CONTRACTS_DIRECTORY` from here onward when needed.

### **1.9. Install the `eosio.token` contract**

Now we have to set the `eosio.token` contract. This contract enables you to create, issue, transfer, and get information about tokens.

```shell
cleos set contract eosio.token EOSIO_CONTRACTS_DIRECTORY/eosio.token/
```

You should see something like this on the command line after the above command is executed:
```
Reading WAST/WASM from /Users/tutorial/Documents/eos/contracts/eosio.token/eosio.token.wasm...
Using already assembled WASM...
Publishing contract...
executed transaction: 17fa4e06ed0b2f52cadae2cd61dee8fb3d89d3e46d5b133333816a04d23ba991  8024 bytes  974 us
#         eosio <= eosio::setcode               {"account":"eosio.token","vmtype":0,"vmversion":0,"code":"0061736d01000000017f1560037f7e7f0060057f7e...
#         eosio <= eosio::setabi                {"account":"eosio.token","abi":{"types":[],"structs":[{"name":"transfer","base":"","fields":[{"name"...
```

### **1.10. Set the `eosio.msig` contract**

Set the `eosio.msig` contract. The msig contract enables and simplifies defining and managing permission levels and performing multi-signature actions.
```shell
cleos set contract eosio.msig EOSIO_CONTRACTS_DIRECTORY/eosio.msig/
```

```
Reading WAST/WASM from /Users/tutorial/Documents/eos/build/contracts/eosio.msig/eosio.msig.wasm...
Using already assembled WASM...
Publishing contract...
executed transaction: 007507ad01de884377009d7dcf409bc41634e38da2feb6a117ceced8554a75bc  8840 bytes  925 us
#         eosio <= eosio::setcode               {"account":"eosio.msig","vmtype":0,"vmversion":0,"code":"0061736d010000000198011760017f0060047f7e7e7...
#         eosio <= eosio::setabi                {"account":"eosio.msig","abi":{"types":[{"new_type_name":"account_name","type":"name"}],"structs":[{...
```

### **1.11. Create and allocate the `SYS` currency**

Create the `SYS` currency with a maximum value of 10 billion tokens. Then issue one billion tokens. Replace `SYS` with your specific currency designation.
```shell
cleos push action eosio.token create '[ "eosio", "10000000000.0000 SYS" ]' -p eosio.token@active
```
```
executed transaction: 0440461e0d8816b4a8fd9d47c1a6a53536d3c7af54abf53eace884f008429697  120 bytes  326 us
#   eosio.token <= eosio.token::create          {"issuer":"eosio","maximum_supply":"10000000000.0000 SYS"}
```
```shell
cleos push action eosio.token issue '[ "eosio", "1000000000.0000 SYS", "memo" ]' -p eosio@active
```
```
executed transaction: a53961a566c1faa95531efb422cd952611b17d728edac833c9a55582425f98ed  128 bytes  432 us
#   eosio.token <= eosio.token::issue           {"to":"eosio","quantity":"1000000000.0000 SYS","memo":"memo"}
```

In the first step above, the `create` action from the `eosio.token` contract, authorized by the `eosio.token` account, creates 1B `SYS` tokens in the `eosio` account. This effectively creates the maximum supply of tokens, but does not put any tokens into circulation. Tokens not in circulation can be considered to be held in reserve.

In the second step, the `eosio.token` contract's `issue` action takes 1B `SYS` tokens out of reserve and puts them into circulation. At the time of issue, the tokens are held within the `eosio` account. Since the `eosio` account owns the reserve of uncirculated tokens, its authority is required to do the action.

_As a point of interest, from an economic point of view, moving token from reserve into circulation, such as by issuing tokens, is an inflationary action. Issuing tokens is just one way that inflation can occur._


### **1.12. Set the `eosio.system` contract**

All of the protocol upgrade features introduced in v1.8 and v2.0 first require a special protocol feature (codename `PREACTIVATE_FEATURE`) to be activated and for an updated version of the system contract that makes use of the functionality introduced by that feature to be deployed. 
So first activate the the special protocol feature `PREACTIVATE_FEATURE` by running the command below:

```shell
curl --request POST \
    --url http://127.0.0.1:8888/v1/producer/schedule_protocol_feature_activations \
    -d '{"protocol_features_to_activate": ["0ec7e080177b2c02b278d5088611686b49d739925a92d9bfcacd7fc6b74053bd"]}'
```

Set the `eosio.system` contract. This contract provides the actions for pretty much all token-based operational behavior. Prior to installing the system contract, actions are done independent of accounting. Once the system contract is enabled, actions now have an economic element to them. Resources (cpu, network, memory) must be paid for. Likewise, new accounts must be paid for. The system contract enables tokens to be staked and unstaked, resources to be purchased, potential producers to be registered and subsequently voted on, producer rewards to be claimed, privileges and limits to be set, and more. In the first phase we will install the older version of the `eosio.system` contract.

```shell
cleos set contract eosio EOSIO_OLD_CONTRACTS_DIRECTORY/eosio.system/
```

```
Reading WAST/WASM from /Users/tutorial/Documents/eos/build/contracts/eosio.system/eosio.system.wasm...
Using already assembled WASM...
Publishing contract...
executed transaction: 2150ed87e4564cd3fe98ccdea841dc9ff67351f9315b6384084e8572a35887cc  39968 bytes  4395 us
#         eosio <= eosio::setcode               {"account":"eosio","vmtype":0,"vmversion":0,"code":"0061736d0100000001be023060027f7e0060067f7e7e7f7f...
#         eosio <= eosio::setabi                {"account":"eosio","abi":{"types":[],"structs":[{"name":"buyrambytes","base":"","fields":[{"name":"p...
```

After you set the `eosio.system` contract run the below commands to enable the rest of the features which are highly recommended to be enabled for an EOSIO based blockchain; of course you can chose not to have them enabled if you really want to do it this way.

```shell
# GET_SENDER
cleos push action eosio activate '["f0af56d2c5a48d60a4a5b5c903edfb7db3a736a94ed589d0b797df33ff9d3e1d"]' -p eosio

# FORWARD_SETCODE
cleos push action eosio activate '["2652f5f96006294109b3dd0bbde63693f55324af452b799ee137a81a905eed25"]' -p eosio

# ONLY_BILL_FIRST_AUTHORIZER
cleos push action eosio activate '["8ba52fe7a3956c5cd3a656a3174b931d3bb2abb45578befc59f283ecd816a405"]' -p eosio

# RESTRICT_ACTION_TO_SELF
cleos push action eosio activate '["ad9e3d8f650687709fd68f4b90b41f7d825a365b02c23a636cef88ac2ac00c43"]' -p eosio

# DISALLOW_EMPTY_PRODUCER_SCHEDULE
cleos push action eosio activate '["68dcaa34c0517d19666e6b33add67351d8c5f69e999ca1e37931bc410a297428"]' -p eosio

 # FIX_LINKAUTH_RESTRICTION
cleos push action eosio activate '["e0fb64b1085cc5538970158d05a009c24e276fb94e1a0bf6a528b48fbc4ff526"]' -p eosio

 # REPLACE_DEFERRED
cleos push action eosio activate '["ef43112c6543b88db2283a2e077278c315ae2c84719a8b25f25cc88565fbea99"]' -p eosio

# NO_DUPLICATE_DEFERRED_ID
cleos push action eosio activate '["4a90c00d55454dc5b059055ca213579c6ea856967712a56017487886a4d4cc0f"]' -p eosio

# ONLY_LINK_TO_EXISTING_PERMISSION
cleos push action eosio activate '["1a99a59d87e06e09ec5b028a9cbb7749b4a5ad8819004365d02dc4379a8b7241"]' -p eosio

# RAM_RESTRICTIONS
cleos push action eosio activate '["4e7bf348da00a945489b2a681749eb56f5de00b900014e137ddae39f48f69d67"]' -p eosio

# WEBAUTHN_KEY
cleos push action eosio activate '["4fca8bd82bbd181e714e283f83e1b45d95ca5af40fb89ad3977b653c448f78c2"]' -p eosio

# WTMSIG_BLOCK_SIGNATURES
cleos push action eosio activate '["299dcb6af692324b899b39f16d5a530a33062804e41f09dc97e9f156b4476707"]' -p eosio
```

Now deploy the latest version of the `eosio.system` contract:

```shell
cleos set contract eosio EOSIO_CONTRACTS_DIRECTORY/eosio.system/
```

## 2. Transition from single genesis producer to multiple producers
In the next set of steps, we will transition from a single block producer (the genesis node) to multiple producers. Up to this point, only the built-in `eosio` account has been privileged and can sign blocks. The target is to manage the blockchain by a collection of elected producers operating under a rule of 2/3 + 1 producers agreeing before a block is final

Producers are chosen by-election. The list of producers can change. Rather than give privileged authority directly to any producer, the governing rules are associated with a special built-in account named `eosio.prods`. This account represents the group of elected producers. The `eosio.prods` account (effectively the producer group) operates using permissions defined by the `eosio.msig` contract.

As soon as possible after installing the `eosio.system` contract, we want to make `eosio.msig` a privileged account so that it can authorize on behalf of the `eosio` account. As soon as possible, `eosio` will resign its authority and `eosio.prods` will take over.

### **2.1. Make `eosio.msig` a privileged account**

We make `eosio.msig` privileged using the following.
```shell
cleos push action eosio setpriv '["eosio.msig", 1]' -p eosio@active
```
### **2.2. Initialize system account**

Below command initializes the `system` account with code zero (needed at initialization time) and `SYS` token with precision 4; precision can range from [0 .. 18].  
```shell
cleos push action eosio init '["0", "4,SYS"]' -p eosio@active
```
### **2.3. Stake tokens and expand the network**

If you've followed the tutorial steps above to this point, you now have a single host, single-node configuration with the following contracts installed:

- eosio.token
- eosio.msig
- eosio.system

Accounts `eosio` and `eosio.msig` are privileged accounts.  The other `eosio.*` accounts have been created but are not privileged.

We are now ready to begin staking accounts and expanding the network of producers.

### **2.4. Create staked accounts**

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

Use the following steps to stake tokens for each account. These steps must be done individually for each account.

> _The key pair is created here for this tutorial. In a "live" scenario, the key value(s) and token share for an account should already be established through some well-defined out-of-band process._
```shell
	$ cleos create key --to-console

```
```
	Private key: 5K7EYY3j1YY14TSFVfqgtbWbrw3FA8BUUnSyFGgwHi8Uy61wU1o
	Public key: EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt
```
```shell
cleos wallet import --private-key 5K7EYY3j1YY14TSFVfqgtbWbrw3FA8BUUnSyFGgwHi8Uy61wU1o

```
```
	imported private key for: EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt
```

Create a staked account with initial resources and public key.
```text
cleos system newaccount eosio --transfer accountnum11 EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt --stake-net "100000000.0000 SYS" --stake-cpu "100000000.0000 SYS" --buy-ram-kbytes 8192
```
```
775292ms thread-0   main.cpp:419                  create_action        ] result: {"binargs":"0000000000ea30551082d4334f4d113200200000"} arg: {"code":"eosio","action":"buyrambytes","args":{"payer":"eosio","receiver":"accountnum11","bytes":8192}}
775295ms thread-0   main.cpp:419                  create_action        ] result: {"binargs":"0000000000ea30551082d4334f4d113200ca9a3b00000000045359530000000000ca9a3b00000000045359530000000001"} arg: {"code":"eosio","action":"delegatebw","args":{"from":"eosio","receiver":"accountnum11","stake_net_quantity":"100000.0000 SYS","stake_cpu_quantity":"100000.0000 SYS","transfer":true}}
executed transaction: fb47254c316e736a26873cce1290cdafff07718f04335ea4faa4cb2e58c9982a  336 bytes  1799 us
#         eosio <= eosio::newaccount            {"creator":"eosio","name":"accountnum11","owner":{"threshold":1,"keys":[{"key":"EOS8mUftJXepGzdQ2TaC...
#         eosio <= eosio::buyrambytes           {"payer":"eosio","receiver":"accountnum11","bytes":8192}
#         eosio <= eosio::delegatebw            {"from":"eosio","receiver":"accountnum11","stake_net_quantity":"100000.0000 SYS","stake_cpu_quantity...
```

### **2.5. Register the new account as a producer**

Use the following command to register as a producer. This makes the node a candidate to be a producer, but the node will not actually be a producer unless it is elected, that is, voted for.
```shell
cleos system regproducer accountnum11 EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt https://accountnum11.com EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt
```
```
1487984ms thread-0   main.cpp:419                  create_action        ] result: {"binargs":"1082d4334f4d11320003fedd01e019c7e91cb07c724c614bbf644a36eff83a861b36723f29ec81dc9bdb4e68747470733a2f2f6163636f756e746e756d31312e636f6d2f454f53386d5566744a586570477a64513254614364754e7553504166584a48663232756578347534316162314556763945416857740000"} arg: {"code":"eosio","action":"regproducer","args":{"producer":"accountnum11","producer_key":"EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt","url":"https://accountnum11.com/EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt","location":0}}
executed transaction: 4ebe9258bdf1d9ac8ad3821f6fcdc730823810a345c18509ac41f7ef9b278e0c  216 bytes  896 us
#         eosio <= eosio::regproducer           {"producer":"accountnum11","producer_key":"EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt","u...
```

### **2.6. List the producers**

To facilitate the voting process, list the available producers. At this point you will see only one account registered as producer
```shell
cleos system listproducers
```
```
Producer      Producer key                                           Url                                                         Scaled votes
accountnum11  EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt  https://accountnum11.com/EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22 0.0000
```

### **2.7. Set up and start a new producer**

We will set up now a new producer using the previously created accountnum11 account. To set up the new producer execute these steps to create a dedicated folder for it
```text
cd ~/netbios/
mkdir accountnum11
cd accountnum11
copy ~/netbios/genesis/stop.sh
copy ~/netbios/genesis/clean.sh

```
Create the below three shell scripts files and assign execution permission to them: `genesis_start.sh, start.sh, hard_start.sh`
```shell
#!/bin/bash
DATADIR="./blockchain"
CURDIRNAME=${PWD##*/}

if [ ! -d $DATADIR ]; then
  mkdir -p $DATADIR;
fi

nodeos \
--genesis-json $DATADIR"/../../genesis.json" \
--signature-provider EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt=KEY:5K7EYY3j1YY14TSFVfqgtbWbrw3FA8BUUnSyFGgwHi8Uy61wU1o \
--plugin eosio::producer_plugin \
--plugin eosio::producer_api_plugin \
--plugin eosio::chain_plugin \
--plugin eosio::chain_api_plugin \
--plugin eosio::http_plugin \
--plugin eosio::history_api_plugin \
--plugin eosio::history_plugin \
--data-dir $DATADIR"/data" \
--blocks-dir $DATADIR"/blocks" \
--config-dir $DATADIR"/config" \
--producer-name $CURDIRNAME \
--http-server-address 127.0.0.1:8011 \
--p2p-listen-endpoint 127.0.0.1:9011 \
--access-control-allow-origin=* \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors \
--enable-stale-production \
--p2p-peer-address localhost:9010 \
--p2p-peer-address localhost:9012 \
--p2p-peer-address localhost:9013 \
>> $DATADIR"/nodeos.log" 2>&1 & \
echo $! > $DATADIR"/eosd.pid"
```

```shell
#!/bin/bash
DATADIR="./blockchain"
CURDIRNAME=${PWD##*/}

if [ ! -d $DATADIR ]; then
  mkdir -p $DATADIR;
fi

nodeos \
--signature-provider EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt=KEY:5K7EYY3j1YY14TSFVfqgtbWbrw3FA8BUUnSyFGgwHi8Uy61wU1o \
--plugin eosio::producer_plugin \
--plugin eosio::producer_api_plugin \
--plugin eosio::chain_plugin \
--plugin eosio::chain_api_plugin \
--plugin eosio::http_plugin \
--plugin eosio::history_api_plugin \
--plugin eosio::history_plugin \
--data-dir $DATADIR"/data" \
--blocks-dir $DATADIR"/blocks" \
--config-dir $DATADIR"/config" \
--producer-name $CURDIRNAME \
--http-server-address 127.0.0.1:8011 \
--p2p-listen-endpoint 127.0.0.1:9011 \
--access-control-allow-origin=* \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors \
--enable-stale-production \
--p2p-peer-address localhost:9010 \
--p2p-peer-address localhost:9012 \
--p2p-peer-address localhost:9013 \
>> $DATADIR"/nodeos.log" 2>&1 & \
echo $! > $DATADIR"/eosd.pid"

```

```shell
#!/bin/bash
DATADIR="./blockchain"
CURDIRNAME=${PWD##*/}

if [ ! -d $DATADIR ]; then
  mkdir -p $DATADIR;
fi

nodeos \
--signature-provider EOS8mUftJXepGzdQ2TaCduNuSPAfXJHf22uex4u41ab1EVv9EAhWt=KEY:5K7EYY3j1YY14TSFVfqgtbWbrw3FA8BUUnSyFGgwHi8Uy61wU1o \
--plugin eosio::producer_plugin \
--plugin eosio::producer_api_plugin \
--plugin eosio::chain_plugin \
--plugin eosio::chain_api_plugin \
--plugin eosio::http_plugin \
--plugin eosio::history_api_plugin \
--plugin eosio::history_plugin \
--data-dir $DATADIR"/data" \
--blocks-dir $DATADIR"/blocks" \
--config-dir $DATADIR"/config" \
--producer-name $CURDIRNAME \
--http-server-address 127.0.0.1:8011 \
--p2p-listen-endpoint 127.0.0.1:9011 \
--access-control-allow-origin=* \
--contracts-console \
--http-validate-host=false \
--verbose-http-errors \
--enable-stale-production \
--p2p-peer-address localhost:9010 \
--p2p-peer-address localhost:9012 \
--p2p-peer-address localhost:9013 \
--hard-replay-blockchain \
>> $DATADIR"/nodeos.log" 2>&1 & \
echo $! > $DATADIR"/eosd.pid"

```
So if you executed everything step without error your folder structure should look like this:
```shell
cd ~/biosboot/accountnum11/
ls -al
```
```
drwxr-xr-x   8 owner  group   256 Dec  7 14:17 .
drwxr-xr-x   3 owner  group   960 Dec  5 10:00 ..
-rwxr-xr-x   1 owner  group   40  Dec  5 13:08 clean.sh
-rwxr-xr-x   1 owner  group   947 Dec  5 14:31 genesis_start.sh
-rwxr-xr-x   1 owner  group   888 Dec  5 13:08 hard_start.sh
-rwxr-xr-x   1 owner  group   901 Dec  6 15:44 start.sh
-rwxr-xr-x   1 owner  group   281 Dec  5 13:08 stop.sh

```
You are now ready to start the second producer node by executing follow commands:
```shell
cd ~/biosboot/accountnum11/
./genesis_start.sh
tail -f blockchain/nodeos.log
```
After executing the above commands you should see in the command shell a live stream of nodeos.log file which is getting written to by the `nodeos` continuously. You can stop the live stream monitor buy pressing CTRL+C keys.

To stop the new node you have to executed the stop.sh script and after that to restart the node you'll have to execute the start.sh script not the genesis_start.sh (this one is used only once at the very beginning).

To wipe everything and start from scratch you can execute the following set of commands:
```shell
cd ~/biosboot/accountnum11/
./stop.sh
./clean.sh
./genesis_start.sh
tail -f blockchain/nodeos.log
```
### **2.8. repeat the process of creating as many producers as you want**

You can now repeat the process (started at point 2.4. till 2.8.) of creating as many producers as you want each with its own staked account, own dedicated directory named accountnumXY (with X and Y int values in interval [1..5]), and their own dedicated script files: `genesis_start.sh, start.sh, stop.sh, clean.sh` located in their corresponding folder.

Also please be aware how you mesh these nodes between each other, so pay particular attention to the following parameters in the genesis_start.sh, start.sh and hard_start.sh scripts:

```
--producer-name $CURDIRNAME \ # Producer name, set in the script to be the parent directory name
...
--http-server-address 127.0.0.1:8011 \ # http listening port for API incoming requests
--p2p-listen-endpoint 127.0.0.1:9011 \ # p2p listening port for incoming connection requests
...
...
--p2p-peer-address localhost:9010 \   # Meshing with peer `genesis` node
--p2p-peer-address localhost:9012 \   # Meshing with peer `accountnum12` node
--p2p-peer-address localhost:9013 \.  # Meshing with peer `accountnum13` node
```

### **2.9. vote for each of the block producers started**

At this point the nodes are started, they are meshed together in a network, and they receive blocks from genesis node but they do not produce.

[[info|15% Requirement]]
| In order for them to produce blocks, a total of 15% of the token supply must be staked and then voted for all available producers. We gave accountnum11 enough tokens earlier.
To elect block producers execute below command which allows one account to vote for as up to 30 block producer identified by their account name:

```shell
cleos system voteproducer prods accountnum11 accountnum11 accountnum12 accountnum13
```

## 3. Resign eosio account and system accounts
Once producers have been elected and the minimum number requirements have been met, that is minimum 15% of tokens have been staked to producers votes, the `eosio` account can resign, leaving the `eosio.msig` account as the only privileged account.

Resigning basically involves setting the keys of the `eosio.*` accounts to null. Use the following command to clear the `eosio.*` accounts' owner and active keys:

```shell
cleos push action eosio updateauth '{"account": "eosio", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": "active"}}]}}' -p eosio@owner
cleos push action eosio updateauth '{"account": "eosio", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio.prods", "permission": "active"}}]}}' -p eosio@active
```

Also the system accounts created in step `1.7. Create important system accounts` should be resigned as well running below commands:

```shell
cleos push action eosio updateauth '{"account": "eosio.bpay", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.bpay@owner
cleos push action eosio updateauth '{"account": "eosio.bpay", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.bpay@active

cleos push action eosio updateauth '{"account": "eosio.msig", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.msig@owner
cleos push action eosio updateauth '{"account": "eosio.msig", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.msig@active

cleos push action eosio updateauth '{"account": "eosio.names", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.names@owner
cleos push action eosio updateauth '{"account": "eosio.names", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.names@active

cleos push action eosio updateauth '{"account": "eosio.ram", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.ram@owner
cleos push action eosio updateauth '{"account": "eosio.ram", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.ram@active

cleos push action eosio updateauth '{"account": "eosio.ramfee", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.ramfee@owner
cleos push action eosio updateauth '{"account": "eosio.ramfee", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.ramfee@active

cleos push action eosio updateauth '{"account": "eosio.saving", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.saving@owner
cleos push action eosio updateauth '{"account": "eosio.saving", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.saving@active

cleos push action eosio updateauth '{"account": "eosio.stake", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.stake@owner
cleos push action eosio updateauth '{"account": "eosio.stake", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.stake@active

cleos push action eosio updateauth '{"account": "eosio.token", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.token@owner
cleos push action eosio updateauth '{"account": "eosio.token", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.token@active

cleos push action eosio updateauth '{"account": "eosio.vpay", "permission": "owner", "parent": "", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.vpay@owner
cleos push action eosio updateauth '{"account": "eosio.vpay", "permission": "active", "parent": "owner", "auth": {"threshold": 1, "keys": [], "waits": [], "accounts": [{"weight": 1, "permission": {"actor": "eosio", "permission": "active"}}]}}' -p eosio.vpay@active

```

## 4. Monitor, test, monitor
###**4.1. You can monitor each nodeos started (either the genesis node or any of the block producers nodes) by executing these commands**
```shell
cd ~/biosboot/genesis/
tail -f ./blockchain/nodeos.log

```

```text
cd ~/biosboot/accountnum11/
tail -f ./blockchain/nodeos.log

```
### **4.2. You can test various commands, create accounts, check balance on accounts, transfer tokens between accounts, etc.**

To create new accounts you can use the commands presented in [`Create test accounts`](https://developers.eos.io/eosio-home/docs/accounts-1) tutorial.

To issue, allocate and transfer tokens between accounts you can use the commands presented in [`Deploy, Issue and Transfer Tokens`](https://developers.eos.io/eosio-home/docs/token-contract) toturial
