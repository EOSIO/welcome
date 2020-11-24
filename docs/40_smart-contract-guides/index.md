---
content_title: EOSIO Smart Contract Guides
link_text: EOSIO Smart Contract Guides
---

This section will introduce you to the EOSIO library and show you the concepts you will use to build smart contracts. We have tutorials to show you:

* [Hello World](10_hello-world.md) - A simple smart contract
* [Deploy, Issue and Transfer Tokens](20_deploy-issue-and-transfer-tokens.md) - How to use the eosio.token smart contract
* [Understanding ABI Files](30_understanding-ABI-files.md) - The interface between webassembly and the outside world
* [Data Peristence](40_data-persistence.md) - Store data on the blockchain
* [Secondary Indices](50_secondary-indices.md) - Create secondary indices for data stored on the blockchain
* [Adding inline Actions](60_adding-inline-actions.md) - Call actions from your smart contract
* [Inline Actions to external contracts](70_inline-action-to-external-contract.md) - Call actions in other smart contracts
* [Linking custom permissions](80_linking-custom-permission.md) - How to set up permissions on smart contracts
* [Payable Actions](90_payable-actions.md) - Custom resource management




## Set up a cookie to assist in getting started with smart contracts

### Setup a development directory, stick to it.
You're going to need to pick a directory to work from, it's suggested to create a `contracts` directory somewhere on your local drive.
```shell
mkdir contracts
cd contracts
```

### Enter your local directory below.
Get the path of that directory and save it for later, as you're going to need it, you can use the following command to get your absolute path.
```
pwd
```

Enter the absolute path to your contract directory below, and it will be inserted throughout the documentation to make your life a bit easier. _This functionality requires cookies_

![cli](../images/cli_2.2.2.gif)

<div class="eosio-helper-box">
    <form id="CONTRACTS_DIR">
        <label>Absolute Path to Contract Directory</label>
        <input class="helper-cookie" name="CONTRACTS_DIR" type="text" />
        <input type="submit" />
        <span></span>
    </form>
</div>
