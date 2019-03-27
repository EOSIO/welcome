---
title: "1.3 Start Your Node & Setup"
excerpt: ""
---
If you don't already have docker installed, you can download it here: https://www.docker.com/community-edition
[block:api-header]
{
  "title": "Step 1: Get the docker image"
}
[/block]
The below statement will download an Ubuntu image which contains the compiled software. 

```
$ docker pull eosio/eos:v1.4.2
```
[block:api-header]
{
  "title": "Step 2: Boot Node and Wallet"
}
[/block]

[block:html]
{
  "html": "<div class=\"no-contracts-dir\">\n  In the last step you created a `contracts` directory, obtained the absolute path. Replace both occurrences of \"CONTRACTS_DIR\" in the command below with the absolute path to your `contracts` directory.\n</div>"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "docker run --name eosio \\\n  --publish 7777:7777 \\\n  --publish 127.0.0.1:5555:5555 \\\n  --volume CONTRACTS_DIR:CONTRACTS_DIR \\\n  --detach \\\n  eosio/eos:v1.4.2 \\\n  /bin/bash -c \\\n  \"keosd --http-server-address=0.0.0.0:5555 & exec nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::history_plugin --plugin eosio::history_api_plugin --plugin eosio::http_plugin -d /mnt/dev/data --config-dir /mnt/dev/config --http-server-address=0.0.0.0:7777 --access-control-allow-origin=* --contracts-console --http-validate-host=false --filter-on='*'\"",
      "language": "shell"
    }
  ]
}
[/block]
These settings accomplish the following:
1. Forward port 7777 and 5555 to host machine
2. Alias a work volume on your local drive to the docker container. 
3. Run the Nodeos startup in bash. This command loads all the basic plugins, set the server address, enable CORS and add some contract debugging. 
4. Enable CORS with no restrictions (*)


[block:callout]
{
  "type": "warning",
  "body": "In the above configuration, CORS is enabled for `*` **for development purposes only**, you should **never** enable CORS for `*` on a node that is publicly accessible!"
}
[/block]

[block:api-header]
{
  "title": "Step 3: Check the installation"
}
[/block]
## Step 3.1: Check that Nodeos is Producing Blocks

Run the following command
[block:code]
{
  "codes": [
    {
      "code": "docker logs --tail 10 eosio",
      "language": "shell"
    }
  ]
}
[/block]
You should see some output in the console that looks like this:
[block:code]
{
  "codes": [
    {
      "code": "1929001ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366974ce4e2a... #13929 @ 2018-05-23T16:32:09.000 signed by eosio [trxs: 0, lib: 13928, confirmed: 0]\n1929502ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366aea085023... #13930 @ 2018-05-23T16:32:09.500 signed by eosio [trxs: 0, lib: 13929, confirmed: 0]\n1930002ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366b7f074fdd... #13931 @ 2018-05-23T16:32:10.000 signed by eosio [trxs: 0, lib: 13930, confirmed: 0]\n1930501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366cd8222adb... #13932 @ 2018-05-23T16:32:10.500 signed by eosio [trxs: 0, lib: 13931, confirmed: 0]\n1931002ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366d5c1ec38d... #13933 @ 2018-05-23T16:32:11.000 signed by eosio [trxs: 0, lib: 13932, confirmed: 0]\n1931501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366e45c1f235... #13934 @ 2018-05-23T16:32:11.500 signed by eosio [trxs: 0, lib: 13933, confirmed: 0]\n1932001ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000366f98adb324... #13935 @ 2018-05-23T16:32:12.000 signed by eosio [trxs: 0, lib: 13934, confirmed: 0]\n1932501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 00003670a0f01daa... #13936 @ 2018-05-23T16:32:12.500 signed by eosio [trxs: 0, lib: 13935, confirmed: 0]\n1933001ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 00003671e8b36e1e... #13937 @ 2018-05-23T16:32:13.000 signed by eosio [trxs: 0, lib: 13936, confirmed: 0]\n1933501ms thread-0   producer_plugin.cpp:585       block_production_loo ] Produced block 0000367257fe1623... #13938 @ 2018-05-23T16:32:13.500 signed by eosio [trxs: 0, lib: 13937, confirmed: 0]",
      "language": "text"
    }
  ]
}
[/block]

## Step 3.2: Check the Wallet

Open the shell
[block:code]
{
  "codes": [
    {
      "code": "docker exec -it eosio bash",
      "language": "shell"
    }
  ]
}
[/block]
Run the following command 

```
cleos --wallet-url http://127.0.0.1:5555 wallet list
```

You should see a response

```
Wallets:
[]
```

Now exit the shell

```
exit
```

Now that `keosd` is running correctly, type `exit` and then press enter to leave the `keosd` shell. From this point forward, you won't need to enter the containers with bash, and you'll be executing commands from your local system (Linux or Mac) 

## Step 3.3: Check Nodeos endpoints

This will check that the RPC API is working correctly, pick one. 

1. Check the `get_info` endpoint provided by the `chain_api_plugin` in your browser: [http://localhost:7777/v1/chain/get_info](http://localhost:7777/v1/chain/get_info)
2. Check the same thing, but in console on your **host machine**

```
curl http://localhost:7777/v1/chain/get_info
```


[block:api-header]
{
  "title": "Step 4: Aliasing Cleos"
}
[/block]
You don't want to enter into the Docker container's bash every time you need to interact with Nodeos or Keosd. A solution to this is to create an alias. 

Execute the following in your terminal for a temporary alias, or add it to your `.bash_rc` file if on Linux, or `.profile` file in on Mac OS if you wish for your alias to persist indefinitely.
[block:code]
{
  "codes": [
    {
      "code": "alias cleos='docker exec -it eosio /opt/eosio/bin/cleos --url http://127.0.0.1:7777 --wallet-url http://127.0.0.1:5555'",
      "language": "shell"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "If you add the alias to your `.bash_rc`, you will need restart your bash session"
}
[/block]

[block:api-header]
{
  "title": "Step 5: Take Note of Useful Docker Commands"
}
[/block]
## Start/Stop Container

```
docker start eosio
docker stop eosio
```

## Bash
```
docker exec -it eosio bash
```

## Remove the EOSIO Container
```
docker rm eosio
```