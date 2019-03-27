---
title: "Docker Quickstart"
excerpt: ""
---
# Install Docker

To start, we need to have Docker installed on your computer. 

Docker is a container management service. Docker intends to simplify application deployment by enabling developers to create fully-configured system environments within portable containers. The system environment consists of the target application(s) running in an operating system configuration that provides all of the runtime support that the application requires. The developer creates the desired system configuration within a container, and then packages the container for distribution. The goal is that an application user can get a copy of the container and deploy it in his own Docker environment and be off and running without needing to do a lot of system and application configuration.

To install Docker please follow this guide:

https://docs.docker.com/install/

# EOSIO Dev Docker image

EOSIO Dev Docker image is a compiled version of the EOSIO software designed for local development.

Pull the image from the repository:

```bash
docker pull eosio/eos-dev
```

And start the EOSIO node:

```bash
sudo docker run --rm --name eosio -d -p 8888:8888 -p 9876:9876 -v /tmp/work:/work -v /tmp/eosio/data:/mnt/dev/data -v /tmp/eosio/config:/mnt/dev/config eosio/eos-dev  /bin/bash -c "nodeos -e -p eosio --plugin eosio::wallet_api_plugin --plugin eosio::wallet_plugin --plugin eosio::producer_plugin --plugin eosio::history_plugin --plugin eosio::chain_api_plugin --plugin eosio::history_api_plugin --plugin eosio::http_plugin -d /mnt/dev/data --config-dir /mnt/dev/config --http-server-address=0.0.0.0:8888 --access-control-allow-origin=* --http-validate-host=false --contracts-console"
```

Check it is working:

```bash
sudo docker logs --tail 10 eosio
```

Your output should be similar to this:

```bash
1929001ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366974ce4e2a... #13929 @ 2018-05-23T16:32:09.000 signed by eosio [trxs: 0, lib: 13928, confirmed: 0]
1929502ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366aea085023... #13930 @ 2018-05-23T16:32:09.500 signed by eosio [trxs: 0, lib: 13929, confirmed: 0]
1930002ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366b7f074fdd... #13931 @ 2018-05-23T16:32:10.000 signed by eosio [trxs: 0, lib: 13930, confirmed: 0]
1930501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366cd8222adb... #13932 @ 2018-05-23T16:32:10.500 signed by eosio [trxs: 0, lib: 13931, confirmed: 0]
1931002ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366d5c1ec38d... #13933 @ 2018-05-23T16:32:11.000 signed by eosio [trxs: 0, lib: 13932, confirmed: 0]
1931501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366e45c1f235... #13934 @ 2018-05-23T16:32:11.500 signed by eosio [trxs: 0, lib: 13933, confirmed: 0]
1932001ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366f98adb324... #13935 @ 2018-05-23T16:32:12.000 signed by eosio [trxs: 0, lib: 13934, confirmed: 0]
1932501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 00003670a0f01daa... #13936 @ 2018-05-23T16:32:12.500 signed by eosio [trxs: 0, lib: 13935, confirmed: 0]
1933001ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 00003671e8b36e1e... #13937 @ 2018-05-23T16:32:13.000 signed by eosio [trxs: 0, lib: 13936, confirmed: 0]
1933501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000367257fe1623... #13938 @ 2018-05-23T16:32:13.500 signed by eosio [trxs: 0, lib: 13937, confirmed: 0]
```

Congrats! You have a very simple single node blockchain running in your Docker container!

Also go to this address in the browser to check that RPC interface is working: `http://localhost:8888/v1/chain/get_info`

You should see a message similar to following:

```json
{
    "server_version": "0961a560",
    "chain_id": "cf057bbfb72640471fd910bcb67639c22df9f92470936cddc1ade0e2f2e7dc4f",
    "head_block_num": 13780,
    "last_irreversible_block_num": 13779,
    "last_irreversible_block_id": "000035d36e1ca29ba378081c574ab3b5ab4214ba29754dd42b512690a9f03e80",
    "head_block_id": "000035d4165c9225d7a04822d142fbcb15f997a6f2571dc7bae8437dea782205",
    "head_block_time": "2018-05-23T16:30:54",
    "head_block_producer": "eosio",
    "virtual_block_cpu_limit": 100000000,
    "virtual_block_net_limit": 1048576000,
    "block_cpu_limit": 99900,
    "block_net_limit": 1048576
}

```

# Cleos

`cleos` is a command line interface to interact with the blockchain and to manage wallets.

For convenience we will create a bash alias for cleos running inside our container. In terminal, run:

```bash
alias cleos='docker exec -it eosio /opt/eosio/bin/cleos -u http://0.0.0.0:8888'
```

Later to stop:
```bash
docker stop eosio
```

Now try to run `cleos --help` in your Terminal. You should see a following output:

```
Command Line Interface to EOSIO Client
Usage: /opt/eosio/bin/cleos [OPTIONS] SUBCOMMAND

Options:
  -h,--help                   Print this help message and exit
  -u,--url TEXT=http://localhost:8888/
                              the http/https URL where nodeos is running
  --wallet-url TEXT=http://localhost:8900/
                              the http/https URL where keosd is running
  -r,--header                 pass specific HTTP header; repeat this option to pass multiple headers
  -n,--no-verify              don't verify peer certificate when using HTTPS
  -v,--verbose                output verbose actions on error

Subcommands:
  version                     Retrieve version information
  create                      Create various items, on and off the blockchain
  get                         Retrieve various items and information from the blockchain
  set                         Set or update blockchain state
  transfer                    Transfer EOS from account to account
  net                         Interact with local p2p network connections
  wallet                      Interact with local wallet
  sign                        Sign a transaction
  push                        Push arbitrary transactions to the blockchain
  multisig                    Multisig contract commands
  system                      Send eosio.system contract action to the blockchain.
```

Awesome! We are up and running.