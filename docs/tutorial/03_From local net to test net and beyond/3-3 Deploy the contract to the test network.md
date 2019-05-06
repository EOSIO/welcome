---
title: "3.3 Deploy the contract to the test network"
excerpt: ""
---
This tutorial assumes you already coded and built the addressbook contract by following [this tutorial](https://developers.eos.io/eosio-home/docs/data-persistence). If you did not built your contract previously please go through the steps of that tutorial and make sure you understand how to code a contract and how to build it.

If you got thus far, it is assumed the addressbook contract is built and its sources and compiled binary files are located in this folder:
    CONTRACTS_DIR/addressbook/

To deploy the addressbook contract to previously created account eostutorial1 open your wallet first and then run the below corresponding command, also do not forget to replace the eostutorial1 account name with your account name:
cleos set contract command
```shell
cleos --url=https://jungle2.cryptolions.io:443 set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active

cleos --url=https://kylin.eoscanada.com set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active
```
If you get a similar error with the one below please check to be sure the keys for your account are in the wallet and the wallet is opened.

```text
Failed to get existing code hash, continue without duplicate check...
Reading WASM from /Users/ovi/eos/b1/test_contracts/abcounter/abcounter.wasm...
Publishing contract...
Error 3090003: Provided keys, permissions, and delays do not satisfy declared authorizations
Ensure that you have the related private keys inside your wallet and your wallet is unlocked.
Error Details:
transaction declares authority '{"actor":"eostutorial1","permission":"active"}', but does not have signatures for it.
```
If your wallet is opened and the keys for your account are stored in the wallet, you will receive an error similar to the one below:

```text
Publishing contract...
Error 3080001: Account using more than allotted RAM usage
Error Details:
account eostutorial1 has insufficient ram; needs 207892 bytes has 5471 bytes

```
As you can see you're already hitting a different scenario on the test network, the error is telling you that the account you are deploying the smart contract to doesn't have enough resources, specifically RAM. It is also telling you how much RAM you need to deploy the addressbook contract.

In order to solve this matter you need to allocated more resources to the account eostutorial1, specifically exactly as much as the error message is saying, in the printed error here 207892 bytes of RAM.

To do so let's first get more tokens in the second account eostutorial2 and then transfer from eostutorial2 to eostutorial1 the exact amount needed. The account eostutorial2 doesn't have yet enough tokens, you will have to get more and the test networks allows us to get more tokens via a faucet accessible via a web page.

For Jungle test network go to http://monitor.jungletestnet.io/#faucet enter the account name eostutorial2, go through the process that verifies you are not a robot and then press "Send coins" button.

For Cryptokilin test network go to http://faucet.cryptokylin.io/get_token?eostutorial2 (note the second account name in the url parameter) and you should see a "Succeeded" message which tell you that an amount of tokens has been transferred to second account.

You can verify the account balance now with one of the commands below, pick the one that corresponds to the test network you chose to work with:
cleos get account command
```shell
cleos --url=https://jungle2.cryptolions.io:443 get account eostutorial2
cleos --url=https://kylin.eoscanada.com get account eostutorial2
```
Notice now the balance on your second account:

```text
EOS balances: 
  liquid:          100.0000 EOS
  staked:            0.0000 EOS
  unstaking:         0.0000 EOS
  total:           100.0000 EOS

```
In order to transfer the amount of tokens to cover for the amount of RAM needed you have to make a calculation, you need to know the price of RAM in order to know how much tokens to transfer from eostutorial2 account to the eostutorial1 account. This kind of calculations and approximations will be needed later as well, and are part of the process of keeping a smart contract up and running on the blockchain, the more actions the smart contract needs to support, the more users will be using your contract making use of the exposed actions, the more resources will be needed. That's why it is good to get familiar with these resources allocation and get a good understanding of them as early as possible.

To check the price of RAM, most of the EOSIO-based networks offers a way to find out the price of RAM which fluctuates, sometimes more and sometimes less, depending on the amount available and the amount bought by the blockchain users. 

For Jungle test network, go to https://jungle.bloks.io/ and in the "RAM Calculator" section notice the price of RAM expressed in the system currency token specific for the EOSIO-based network, in this case EOS. In the field "KB" enter the amount of KiB the error message was saying earlier, in our case 207892 bytes subtracts the amount already available 5471 bytes, transformed in KiB is approximately 197.67 KiB, the calculus to get this number is the following: ((207892 - 5471) / 1024), and then press the conversion button. You will be shown the amount of tokens needed have in order to buy the amount of RAM needed to be deploy the contract, in our case 3.8499 EOS, of course in your case might differ because at the time when you'll make this operation the price of RAM is probably different.

For Cryptokilin network, go to https://kylin.eosx.io/tools/ram/buy and you will be able to see the "Current RAM price". Use that price to calculate the amount of tokens you need to spend in order to buy the amounto of RAM you need based to deploy the contract based on this formula: 
RAM_bytes_needed / 1024 * EOS_per_KB_of_RAM = amount of tokens needed.

Now that you know amount of tokens needed let's transfer it from account eostutorial2 to eostutorial1. One more observation, because of the RAM price fluctuations, and because when you buy RAM you also pay a fee (you pay 0.5% fee when you buy RAM and you pay 0.5% fee when you sell RAM as well) you will add to the amount of tokens needed an extra 10% to cover the possible fluctuations as well as the fees. Therefore you'll transfer 1.9514 EOS tokens. 
cleos transfer command
```shell
cleos --url=https://jungle2.cryptolions.io:443 transfer eostutorial2  eostutorial1 "1.9514 EOS" "initial transfer to enable contract deployment"
    
cleos --url=https://kylin.eoscanada.com transfer eostutorial2  eostutorial1 "1.9514 EOS" "initial transfer to enable contract deployment"
```
you should see a message similar to the one below:

```text
executed transaction: 3d4cee488410b0a75d8e8570e1e22a41058c7ab5e44969c18c56265899a521a7  176 bytes  271 us
#   eosio.token <= eosio.token::transfer        {"from":"eostutorial2","to":"eostutorial1","quantity":"1.9514 EOS","memo":"initial transfer to enabl...
#  eostutorial2 <= eosio.token::transfer        {"from":"eostutorial2","to":"eostutorial1","quantity":"1.9514 EOS","memo":"initial transfer to enabl...
#  eostutorial1 <= eosio.token::transfer        {"from":"eostutorial2","to":"eostutorial1","quantity":"1.9514 EOS","memo":"initial transfer to enabl...
warning: transaction executed locally, but may not be confirmed by the network yet         ]
```
The warning at the end it is normal, it tells you that the transaction was received by the node you sent it to but it was not finalized yet.

Let's check the balance of the eostutorial1 account:
cleos get account command
```shell
cleos --url=https://jungle2.cryptolions.io:443 get account eostutorial1
cleos --url=https://kylin.eoscanada.com get account eostutorial1

```
Now you can go ahead and buy the RAM necessary for the account to be able to execute the transaction which deploys the smart contract, chose the corresponding test network command from below:
cleos guyram command
```shell
cleos --url=https://jungle2.cryptolions.io:443 system buyram eostutorial1 eostutorial1 "1.9514 EOS" -p eostutorial1@active

cleos --url=https://kylin.eoscanada.com system buyram eostutorial1 eostutorial1 "1.9514 EOS" -p eostutorial1@active

```
You should see a result like the one below:

```text
executed transaction: e33e1ba90e4183065b55a9eeeda544eaa0c75c3b1ccf52b947d0e9142cec60a3  128 bytes  625 us
#         eosio <= eosio::buyram                {"payer":"eostutorial1","receiver":"eostutorial1","quant":"1.9514 EOS"}
#   eosio.token <= eosio.token::transfer        {"from":"eostutorial1","to":"eosio.ram","quantity":"1.85383 EOS","memo":"buy ram"}
#  eostutorial1 <= eosio.token::transfer        {"from":"eostutorial1","to":"eosio.ram","quantity":"1.85383 EOS","memo":"buy ram"}
#     eosio.ram <= eosio.token::transfer        {"from":"eostutorial1","to":"eosio.ram","quantity":"1.85383 EOS","memo":"buy ram"}
#   eosio.token <= eosio.token::transfer        {"from":"eostutorial1","to":"eosio.ramfee","quantity":"0.09757 EOS","memo":"ram fee"}
#  eostutorial1 <= eosio.token::transfer        {"from":"eostutorial1","to":"eosio.ramfee","quantity":"0.09757 EOS","memo":"ram fee"}
#  eosio.ramfee <= eosio.token::transfer        {"from":"eostutorial1","to":"eosio.ramfee","quantity":"0.09757 EOS","memo":"ram fee"}
#   eosio.token <= eosio.token::transfer        {"from":"eosio.ramfee","to":"eosio.rex","quantity":"0.09757 EOS","memo":"transfer from eosio.ramfee t...
#  eosio.ramfee <= eosio.token::transfer        {"from":"eosio.ramfee","to":"eosio.rex","quantity":"0.09757 EOS","memo":"transfer from eosio.ramfee t...
#     eosio.rex <= eosio.token::transfer        {"from":"eosio.ramfee","to":"eosio.rex","quantity":"0.09757 EOS","memo":"transfer from eosio.ramfee t...
warning: transaction executed locally, but may not be confirmed by the network yet         ] 

```
Now that you have the RAM secured you can execute successfully the transaction which deploys the addressbook contract code to the eostutorial1 account.
cleos set contract command
```shell
cleos --url=https://jungle2.cryptolions.io:443 set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active
    
cleos --url=https://kylin.eoscanada.com set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active
```
And the output of the command should be similar to the one below:

```text
Publishing contract...
executed transaction: a223ade4e73f0165b1df645549225642b6d72dfa1d39494704a04dc7bbc9eeee  4920 bytes  654 us
#         eosio <= eosio::setcode               {"account":"eostutorial1","vmtype":0,"vmversion":0,"code":"0061736d010000000192011860037f7e7f0060000...
#         eosio <= eosio::setabi                {"account":"eostutorial1","abi":"0e656f73696f3a3a6162692f312e31000205636f756e7400020475736572046e616...
warning: transaction executed locally, but may not be confirmed by the network yet         ] 

```
In the eventuality you will get an error message like the one we got previously, telling you the account doesn't have sufficient amount of memory, you'll have to repeat the process, transfer more tokens from eostutorial2 to eostutorial1, buy more RAM, and re-execute the cleos set contract command.

If you successfully executed the previous command you have now deployed the contract to the public test network you chose to work with, and you are ready to interact with it by pushing actions defined by the contract to the blockchain produced by the public test network. We will cover this in the next chapter along with understanding in more depth more aspects that govern an EOSIO-based blockchain: resources, specifically RAM, CPU and NET.