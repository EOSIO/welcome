---
title: "3.3 Deploy the contract to the test network"
excerpt: ""
---
This tutorial assumes you already coded and built the addressbook contract by following [this tutorial](https://developers.eos.io/eosio-home/docs/data-persistence). If you did not build your contract previously, please go through the steps of that tutorial and make sure you understand how to code a contract and how to build it.

If you've got this far, it is assumed the addressbook contract is built, and its sources and compiled binary files are located in this folder:
    CONTRACTS_DIR/addressbook/

To deploy the addressbook contract to the previously created account eostutorial1 open your wallet and run the below corresponding command.  Do not forget to replace the eostutorial1 account name with your account name:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active\n\ncleos --url=https://kylin.eoscanada.com set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active",
      "language": "shell",
      "name": "cleos set contract command"
    }
  ]
}
[/block]
If you get a similar error with the one below please ensure the keys for your account are in the wallet and the wallet is opened.
[block:code]
{
  "codes": [
    {
      "code": "Failed to get existing code hash, continue without duplicate check...\nReading WASM from /Users/ovi/eos/b1/test_contracts/abcounter/abcounter.wasm...\nPublishing contract...\nError 3090003: Provided keys, permissions, and delays do not satisfy declared authorizations\nEnsure that you have the related private keys inside your wallet and your wallet is unlocked.\nError Details:\ntransaction declares authority '{\"actor\":\"eostutorial1\",\"permission\":\"active\"}', but does not have signatures for it.",
      "language": "text"
    }
  ]
}
[/block]
If your wallet is opened and the keys for your account are stored in the wallet, you will receive an error similar to the one below:
[block:code]
{
  "codes": [
    {
      "code": "Publishing contract...\nError 3080001: Account using more than allotted RAM usage\nError Details:\naccount eostutorial1 has insufficient ram; needs 207892 bytes has 5471 bytes\n",
      "language": "text"
    }
  ]
}
[/block]
As you can see, we're already experiencing differences between a local single-node network and the test network.  The error is telling you that the account you are deploying the smart contract to doesn't have enough resources, specifically RAM. It is also telling you how much RAM you need to deploy the addressbook contract.

In order to solve this, you need to allocate more resources to the eostutorial1 account.  Specifically, you need to allocate exactly as many bytes as the error message is saying, 207892 bytes of RAM.

To do so lets first get more tokens in the second "eostutorial2" account, and then transfer the necessary amount of tokens from eostutorial2 to eostutorial1 . The eostutorial2 account doesn't currently have enough tokens, so you will have to get more.  Luckily, the test networks allow us to get more tokens via a faucet accessible on their web pages.

For the Jungle test network go to http://monitor.jungletestnet.io/#faucet and enter the account name "eostutorial2", go through the process that verifies you are not a robot and then press the "Send coins" button.

For the Cryptokilin test network go to http://faucet.cryptokylin.io/get_token?eostutorial2 (note the second account name in the url parameter) and you should see a "Succeeded" message which tells you that an amount of tokens has been transferred to the second "eostutorial2" account .

You can verify the account balance now with one of the commands below, pick the one that corresponds to the test network you chose to work with:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get account eostutorial2\ncleos --url=https://kylin.eoscanada.com get account eostutorial2",
      "language": "shell",
      "name": "cleos get account command"
    }
  ]
}
[/block]
Now notice the balance on your second account:
[block:code]
{
  "codes": [
    {
      "code": "EOS balances: \n  liquid:          100.0000 EOS\n  staked:            0.0000 EOS\n  unstaking:         0.0000 EOS\n  total:           100.0000 EOS\n",
      "language": "text"
    }
  ]
}
[/block]
In order to know the amount of tokens necessary to transfer from “eostutorial2” to “eostutorial1” for the RAM costs, you have to make a calculation using the current price of RAM.  Part of being a smart contract developer is knowing these calculations and using them to keep a smart contract up and running on the blockchain.  The more users are using your smart contract’s exposed actions, the more resources will be needed to handle these actions.  This is why it’s good to get familiar with these resource allocation calculations as early as possible.

Most of the EOSIO-based networks offer a way to find the price of RAM, which fluctuates depending on the amount of RAM available and the amount bought by the blockchain users. 

For the Jungle test network, go to https://jungle.bloks.io/ and in the "RAM Calculator" section notice the price of RAM expressed in the system currency token specific for the EOSIO-based network, in this case EOS. In the "KB" field enter the amount of KiB stated in the early error message, in our case 207892 bytes, subtracted by the amount already available (5471 bytes), and transformed in KiB is approximately 197.67 KiB, the calculation to get this number is the following: ((207892 - 5471) / 1024), and then press the conversion button. You will be shown the amount of tokens needed in order to buy the amount of RAM necessary to be deploy the contract, in our case 3.8499 EOS.  Of course, your case may differ because at the time when you make this operation the price of RAM will have fluctuated.

For Cryptokilin network, go to https://kylin.eosx.io/tools/ram/buy and you will be able to see the "Current RAM price". Use that price to calculate the amount of tokens you need to spend in order to buy the RAM necessary to deploy the contract based on this formula: 
RAM_bytes_needed / 1024 * EOS_per_KB_of_RAM = amount of tokens needed.

One more observation.  Because of RAM price fluctuations, and because when you buy RAM you also pay a fee (you pay a 0.5% fee both when you buy, as well as when you sell RAM) you will need to add to the amount of tokens calculated above an extra 10% to cover the possible fluctuations as well as the fees. Therefore you'll transfer 1.9514 EOS tokens.  Now that you know the amount of tokens needed let's transfer it from account eostutorial2 to eostutorial1.
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 transfer eostutorial2  eostutorial1 \"1.9514 EOS\" \"initial transfer to enable contract deployment\"\n    \ncleos --url=https://kylin.eoscanada.com transfer eostutorial2  eostutorial1 \"1.9514 EOS\" \"initial transfer to enable contract deployment\"",
      "language": "shell",
      "name": "cleos transfer command"
    }
  ]
}
[/block]
you should see a message similar to the one below:
[block:code]
{
  "codes": [
    {
      "code": "executed transaction: 3d4cee488410b0a75d8e8570e1e22a41058c7ab5e44969c18c56265899a521a7  176 bytes  271 us\n#   eosio.token <= eosio.token::transfer        {\"from\":\"eostutorial2\",\"to\":\"eostutorial1\",\"quantity\":\"1.9514 EOS\",\"memo\":\"initial transfer to enabl...\n#  eostutorial2 <= eosio.token::transfer        {\"from\":\"eostutorial2\",\"to\":\"eostutorial1\",\"quantity\":\"1.9514 EOS\",\"memo\":\"initial transfer to enabl...\n#  eostutorial1 <= eosio.token::transfer        {\"from\":\"eostutorial2\",\"to\":\"eostutorial1\",\"quantity\":\"1.9514 EOS\",\"memo\":\"initial transfer to enabl...\nwarning: transaction executed locally, but may not be confirmed by the network yet         ]",
      "language": "text"
    }
  ]
}
[/block]
The warning at the end is normal, it tells you that the transaction was received by the node you sent it to but it was not finalized on the blockchain yet.

Let's check the balance of the eostutorial1 account:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get account eostutorial1\ncleos --url=https://kylin.eoscanada.com get account eostutorial1\n",
      "language": "shell",
      "name": "cleos get account command"
    }
  ]
}
[/block]
Now you can buy the RAM necessary for the account to execute the transaction which deploys the smart contract.  Choose the corresponding test network command from below:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 system buyram eostutorial1 eostutorial1 \"1.9514 EOS\" -p eostutorial1@active\n\ncleos --url=https://kylin.eoscanada.com system buyram eostutorial1 eostutorial1 \"1.9514 EOS\" -p eostutorial1@active\n",
      "language": "shell",
      "name": "cleos guyram command"
    }
  ]
}
[/block]
You should see a result like the one below:
[block:code]
{
  "codes": [
    {
      "code": "executed transaction: e33e1ba90e4183065b55a9eeeda544eaa0c75c3b1ccf52b947d0e9142cec60a3  128 bytes  625 us\n#         eosio <= eosio::buyram                {\"payer\":\"eostutorial1\",\"receiver\":\"eostutorial1\",\"quant\":\"1.9514 EOS\"}\n#   eosio.token <= eosio.token::transfer        {\"from\":\"eostutorial1\",\"to\":\"eosio.ram\",\"quantity\":\"1.85383 EOS\",\"memo\":\"buy ram\"}\n#  eostutorial1 <= eosio.token::transfer        {\"from\":\"eostutorial1\",\"to\":\"eosio.ram\",\"quantity\":\"1.85383 EOS\",\"memo\":\"buy ram\"}\n#     eosio.ram <= eosio.token::transfer        {\"from\":\"eostutorial1\",\"to\":\"eosio.ram\",\"quantity\":\"1.85383 EOS\",\"memo\":\"buy ram\"}\n#   eosio.token <= eosio.token::transfer        {\"from\":\"eostutorial1\",\"to\":\"eosio.ramfee\",\"quantity\":\"0.09757 EOS\",\"memo\":\"ram fee\"}\n#  eostutorial1 <= eosio.token::transfer        {\"from\":\"eostutorial1\",\"to\":\"eosio.ramfee\",\"quantity\":\"0.09757 EOS\",\"memo\":\"ram fee\"}\n#  eosio.ramfee <= eosio.token::transfer        {\"from\":\"eostutorial1\",\"to\":\"eosio.ramfee\",\"quantity\":\"0.09757 EOS\",\"memo\":\"ram fee\"}\n#   eosio.token <= eosio.token::transfer        {\"from\":\"eosio.ramfee\",\"to\":\"eosio.rex\",\"quantity\":\"0.09757 EOS\",\"memo\":\"transfer from eosio.ramfee t...\n#  eosio.ramfee <= eosio.token::transfer        {\"from\":\"eosio.ramfee\",\"to\":\"eosio.rex\",\"quantity\":\"0.09757 EOS\",\"memo\":\"transfer from eosio.ramfee t...\n#     eosio.rex <= eosio.token::transfer        {\"from\":\"eosio.ramfee\",\"to\":\"eosio.rex\",\"quantity\":\"0.09757 EOS\",\"memo\":\"transfer from eosio.ramfee t...\nwarning: transaction executed locally, but may not be confirmed by the network yet         ] \n",
      "language": "text"
    }
  ]
}
[/block]
Now that you have the RAM secured you can successfully execute the transaction which deploys the addressbook contract code to the eostutorial1 account.
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active\n    \ncleos --url=https://kylin.eoscanada.com set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active",
      "language": "shell",
      "name": "cleos set contract command"
    }
  ]
}
[/block]
And the output of the command should be similar to the one below:
[block:code]
{
  "codes": [
    {
      "code": "Publishing contract...\nexecuted transaction: a223ade4e73f0165b1df645549225642b6d72dfa1d39494704a04dc7bbc9eeee  4920 bytes  654 us\n#         eosio <= eosio::setcode               {\"account\":\"eostutorial1\",\"vmtype\":0,\"vmversion\":0,\"code\":\"0061736d010000000192011860037f7e7f0060000...\n#         eosio <= eosio::setabi                {\"account\":\"eostutorial1\",\"abi\":\"0e656f73696f3a3a6162692f312e31000205636f756e7400020475736572046e616...\nwarning: transaction executed locally, but may not be confirmed by the network yet         ] \n",
      "language": "text"
    }
  ]
}
[/block]
If you will get an error message like the one we got previously, telling you the account doesn't have a sufficient amount of memory, you'll have to repeat the process.  Transfer more tokens from eostutorial2 to eostutorial1, buy more RAM, and re-execute the cleos set contract command until the error is no longer received.

If you successfully executed the previous command you have now deployed the contract to the public test network you chose to work with.  You are now ready to interact with it by pushing actions defined by the contract to the blockchain produced by the public test network. We will cover this in the next chapter along with an in-depth explanation of the resources that govern an EOSIO-based blockchain, specifically RAM, CPU, and NET.