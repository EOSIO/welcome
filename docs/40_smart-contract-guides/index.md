---
content_title: Smart Contract Guides
link_text: Smart Contract Guides
---

This section will introduce you to the EOSIO library and show you the concepts you will use to build smart contracts. We have tutorials to show you:

* [Hello World](10_hello-world.md) - How to build, deploy and use a simple "Hello World" smart contract
* [Deploy, Issue and Transfer Tokens](20_deploy-issue-and-transfer-tokens.md) - How to use the eosio.token smart contract
* [Understanding ABI Files](30_understanding-ABI-files.md) - How ABI files work and what they are 
* [Data Peristence](40_data-persistence.md) - How to store data on the blockchain, with a single index
* [Secondary Indices](50_secondary-indices.md) - How to store data on the blockchain, with muliple indices
* [Adding inline Actions](60_adding-inline-actions.md) - How to call actions in your smart contract
* [Inline Actions to external contracts](70_inline-action-to-external-contract.md) - How to call actions in other smart contracts
* [Linking custom permissions](80_linking-custom-permission.md) - How to set up custom permissions on a smart contract
* [Payable Actions](90_payable-actions.md) - How to be paid for calling smart contract actions


## Before you begin
To get started as quickly as possible we recommend using pre-built binaries. Building from source is a more advanced option but will set you back an hour or more and you may encounter build errors. See the [Installation Guides](../30_getting-started-guide/10_system-setup/10_installation-guides.md) for details on how to install the required EOSIO components.


## Using cookies for the tutorials

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
