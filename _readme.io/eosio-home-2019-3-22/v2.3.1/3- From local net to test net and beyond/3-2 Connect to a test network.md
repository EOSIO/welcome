---
title: "3.2 Connect to a test network"
excerpt: ""
---
[block:api-header]
{
  "type": "basic",
  "title": "3.2.1 Chose an existing public test network"
}
[/block]
As mentioned earlier we will be using one of the following public EOSIO-based test networks:
[Jungle TestNet](https://jungletestnet.io/) or [CryptoKylin TestNet](https://www.cryptokylin.io/).

Please pick one and then use only that one for all the steps of the tutorial, that is, the tutorial will present you with instructions for both but you'll have to always make sure you follow those of the test network you picked in this step.
[block:api-header]
{
  "title": "3.2.2 Create accounts to the test network"
}
[/block]
For this tutorial you will need two accounts on the test network you chose. So let's create them.

**For Jungle Test Network:** you will first have to generate public and private keys, one pair for active and one pair for owner permissions, and copy them in a safe place because you will use them shortly. You can generate two sets of private and public keys by running the below command twice at your shell prompt:
[block:code]
{
  "codes": [
    {
      "code": "cleos create key --to-console",
      "language": "shell",
      "name": "Generate keys command using cleos command line tool"
    }
  ]
}
[/block]
Let's say you generated them and you saved them for later use.

        Owner:
            Private key	5Kk2Btm2Ai7jrAJ5ZCpXfWkcqyth8BF1udP9aN6f8ZGbKVTw8Ve	
            Public key	EOS8JS4mfjxAQfhcrwsExkXTJsrCqDzU1FW3wRZPa6Rpi9ykmcj19	
        Active:
            Private key	5JD1pYda6UxnrfYAJrKfmqtzeu54TBBZULG42xPvYz7whYpvmcX
            Public key	EOS7PKPfDXVvfm2F5RaXY31evn17UPJXkSeCh47Qpehe3sXRirZXu

Go to https://monitor.jungletestnet.io/#account and enter the account name (be sure you follow the EOSIO rules of account name creation: "a-z,1-5 are allowed only. Length 12") and the public keys previously generated.

Let's say you entered eostutorial1 for the account name and the two public keys you created above you should see a response similar to this:
[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 79302f0634fe01216670c2f40bc629a2b8307dcb97c13784ecf2f74cffc24fa7 336 bytes 2750 us warn 2019-01-30T13:57:29.049 thread-0 main.cpp:482 print_result ] warning: transaction executed locally, but may not be confirmed by the network yet \n            # eosio <= eosio::newaccount {\"creator\":\"junglefaucet\",\"name\":\"eostutorial1\",\"owner\":{\"threshold\":1,\"keys\":[{\"key\":\"EOS8JS4mfjxAQ... # eosio <= eosio::buyrambytes {\"payer\":\"junglefaucet\",\"receiver\":\"eostutorial1\",\"bytes\":4096} # eosio.token <= eosio.token::transfer {\"from\":\"junglefaucet\",\"to\":\"eosio.ram\",\"quantity\":\"0.0771 EOS\",\"memo\":\"buy ram\"} # junglefaucet <= eosio.token::transfer {\"from\":\"junglefaucet\",\"to\":\"eosio.ram\",\"quantity\":\"0.0771 EOS\",\"memo\":\"buy ram\"} # eosio.ram <= eosio.token::transfer {\"from\":\"junglefaucet\",\"to\":\"eosio.ram\",\"quantity\":\"0.0771 EOS\",\"memo\":\"buy ram\"} # eosio.token <= eosio.token::transfer {\"from\":\"junglefaucet\",\"to\":\"eosio.ramfee\",\"quantity\":\"0.0004 EOS\",\"memo\":\"ram fee\"} # junglefaucet <= eosio.token::transfer {\"from\":\"junglefaucet\",\"to\":\"eosio.ramfee\",\"quantity\":\"0.0004 EOS\",\"memo\":\"ram fee\"} # eosio.ramfee <= eosio.token::transfer {\"from\":\"junglefaucet\",\"to\":\"eosio.ramfee\",\"quantity\":\"0.0004 EOS\",\"memo\":\"ram fee\"} # eosio.token <= eosio.token::transfer {\"from\":\"eosio.ramfee\",\"to\":\"eosio.rex\",\"quantity\":\"0.0004 EOS\",\"memo\":\"transfer from eosio.ramfee t... # eosio.ramfee <= eosio.token::transfer {\"from\":\"eosio.ramfee\",\"to\":\"eosio.rex\",\"quantity\":\"0.0004 EOS\",\"memo\":\"transfer from eosio.ramfee t... # eosio.rex <= eosio.token::transfer {\"from\":\"eosio.ramfee\",\"to\":\"eosio.rex\",\"quantity\":\"0.0004 EOS\",\"memo\":\"transfer from eosio.ramfee t... # eosio <= eosio::delegatebw {\"from\":\"junglefaucet\",\"receiver\":\"eostutorial1\",\"stake_net_quantity\":\"1.0000 EOS\",\"stake_cpu_quanti... # eosio.token <= eosio.token::transfer {\"from\":\"junglefaucet\",\"to\":\"eosio.stake\",\"quantity\":\"2.0000 EOS\",\"memo\":\"stake bandwidth\"} # junglefaucet <= eosio.token::transfer {\"from\":\"junglefaucet\",\"to\":\"eosio.stake\",\"quantity\":\"2.0000 EOS\",\"memo\":\"stake bandwidth\"} # eosio.stake <= eosio.token::transfer {\"from\":\"junglefaucet\",\"to\":\"eosio.stake\",\"quantity\":\"2.0000 EOS\",\"memo\":\"stake bandwidth\"}",
      "language": "text",
      "name": "Account creation output"
    }
  ]
}
[/block]
**For Cryptokilin Test Network:** to create an account (let's say eostutorial1) go to this link http://faucet.cryptokylin.io/create_account?eostutorial1

You will have to pick your own name because eostutorial1 is obviously taken, be sure you follow the EOSIO rules of account name creation: "a-z,1-5 are allowed only. Length 12"

You should see a response message similar to the one below, please make sure you save your private and public key in a safe place, you will need them later.
[block:code]
{
  "codes": [
    {
      "code": "{\"msg\": \"succeeded\", \"keys\": {\"active_key\": {\"public\": \"EOS8eRnhmEdTfyswJkwP8osMUTJkGzYcj9XkgWqgVRufWgej9JCgx\", \"private\": \"5JRpZH14BaJM5ggkoC8PYzdwotNJun7D1zAnF9FAQZJo6mvQH9M\"}, \"owner_key\": {\"public\": \"EOS6iTCLBRjrhQSxNrcPWz3314E2Gdwr1HtfkTVMHkCpFGqkpVRbw\", \"private\": \"5Hu6JTLyVwj2cMxgLEkVKTSHR3NFfRnHRdP9gnybZCD6YnuwZcR\"}}, \"account\": \"eostutorial3\"}\n{\"msg\": \"succeeded\", \"keys\": {\"active_key\": {\"public\": \"EOS7knYdhb5ZzNLBMtHb3CDp8MpQ9AgJ3rzNvANrkdN9MbPaXeqQA\", \"private\": \"5Hze2Mj1ZXfep29Yp5TPN2bd5b39ZYgyhkbNs9pZvyjJNF84owd\"}, \"owner_key\": {\"public\": \"EOS7Jb3Cz3hgZaZbhTtamL1bJRVFCiBk8egRgTry8TmAGbBzJMGqr\", \"private\": \"5JFj5REk2Y4T4GZgQF3YWBHZbhRq2kyJTBfdKuJKRECsY5j9pwK\"}}, \"account\": \"eostutorial4\"}",
      "language": "text"
    }
  ]
}
[/block]
Now go ahead and repeat the process and create a second account, let's call it eostutorial2. For simplicity you can re-use the same public and private keys used on eostutorial1, but in practice it is recommended to have separate keys on each account.
[block:api-header]
{
  "title": "3.2.3 Connect to the test network"
}
[/block]
In order to interact with the test network you will use the cleos command line tool. An interaction 
with the test network can be any of the following: deploy contracts, create accounts, transfer 
tokens between accounts, send actions to contracts, query the state of an account, or the 
state of the blockchain, etc.

The cleos command line tool is interacting with the test network by connecting to one of the nodes of the networks. You'll have to find and chose one of the nodes which is part of the network.

**For Jungle test network **go to http://monitor.jungletestnet.io/#apiendpoints
Wait until the page loads and then pick one of the listed urls in the "API Endpoints List" by copying it somewhere so it will be easily accessible for you to use later. Let's say you picked https://jungle2.cryptolions.io:443

**For CryptoKylin test network** go to https://github.com/cryptokylin/CryptoKylin-Testnet#http-api-list
and pick one url from the "API Nodes" section, strip the ending string "/v1/chain/get_info", and copy it somewhere so it will be easily accessible for you to use later. Let's say you picked https://kylin.eoscanada.com

You will be using this url to tell the cleos tool which node you want to connect to in order to interact with the blockchain. You can chose more than one url to save for later use, and use them interchangeably, however for the purpose of this tutorial you'll be working with one only.

Now you can execute any cleos command against the node you are connected to and thus interact with the blockchain produced by this EOSIO-based test network.

To get the state of the blockchain, execute one of the following commands, depending on which test network you have chosen. Please note the "--url=" parameter which receives the url of the node you saved above:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get info\ncleos --url=https://kylin.eoscanada.com get info",
      "language": "text"
    }
  ]
}
[/block]
If the command above is not responding with a message similar with the one below and instead it 
is yielding an error message or a failure message, go back to the list of endpoints urls and pick 
another one, and repeat the process until the "cleos ... get info" command above returns no error.
[block:code]
{
  "codes": [
    {
      "code": "{\n            \"server_version\": \"3fddb727\",\n            \"chain_id\": \"e70aaab8997e1dfce58fbfac80cbbb8fecec7b99cf982a9444273cbc64c41473\",\n            \"head_block_num\": 11634230,\n            \"last_irreversible_block_num\": 11633917,\n            \"last_irreversible_block_id\": \"00b184fd4064274df26ec1e5dd42f9900714deb3a08774980e49884d39b42c5e\",\n            \"head_block_id\": \"00b186362927738c061601745c7ce4ff6aedfc9de748549eb5ef7f2b0e0a025c\",\n            \"head_block_time\": \"2019-01-31T21:52:24.500\",\n            \"head_block_producer\": \"eosphereiobp\",\n            \"virtual_block_cpu_limit\": 200000000,\n            \"virtual_block_net_limit\": 1048576000,\n            \"block_cpu_limit\": 199920,\n            \"block_net_limit\": 1048576,\n            \"server_version_string\": \"v1.6.0\"\n}",
      "language": "text",
      "name": "cleos get info command output"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "3.2.4 Add the account's keys to the wallet"
}
[/block]
If you do not have a wallet please follow [the steps in this tutorial](https://developers.eos.io/eosio-home/docs/wallets#section-step-1-create-a-wallet) to create a wallet and open it.

Then add the keys for the two accounts you created earlier to the opened wallet by following [the steps in this tutorial](https://developers.eos.io/eosio-home/docs/wallets#section-step-6-import-the-development-key).

Wonderful, you now have a default wallet unlocked, loaded with the necessary keys, and are ready to proceed.