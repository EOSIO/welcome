---
title: "1.4 Build the CDT"
excerpt: "Build the Contract Development Toolkit"
---
The EOSIO Contract Development Toolkit, CDT for short, is a collection of tools related to contract compilation. Subsequent tutorials use the CDT primarily for compiling contracts and generating ABIs.

The location where `eosio.cdt` is cloned is not that important because you will be installing `eosio.cdt` as a local binary in later steps. For now, you can clone `eosio.cdt` to your "contracts" directory previously created, or really anywhere else on your local system you see fit. 
[block:code]
{
  "codes": [
    {
      "code": "cd CONTRACTS_DIR",
      "language": "text"
    }
  ]
}
[/block]
Clone version 1.2.1 of the `eosio.cdt` repository. 
[block:code]
{
  "codes": [
    {
      "code": "git clone --recursive https://github.com/eosio/eosio.cdt --branch v1.2.1 --single-branch\ncd eosio.cdt",
      "language": "text"
    }
  ]
}
[/block]
It may take up to 30 minutes to clone the repository
[block:callout]
{
  "type": "warning",
  "title": "Important",
  "body": "This documentation uses 1.2.1 of the contract development toolkit."
}
[/block]

[block:api-header]
{
  "title": "Step 1: Build"
}
[/block]
When building the `eosio.cdt`, you need to define the symbol. 

**All tutorials on this site are network agnostic,** the symbol `SYS` is used as the local development environment's **core symbol**. The core symbol is the symbol of the primary token used for the network you are developing on.
[block:code]
{
  "codes": [
    {
      "code": "./build.sh SYS",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 2: Install"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "sudo ./install.sh",
      "language": "shell"
    }
  ]
}
[/block]
The above command needs to be ran with `sudo` because `eosio.cdt`'s various binaries will be installed locally. You will be asked for your computer's account password. 

Installing `eosio.cdt` will make the compiled binary global so it can be accessable anywhere. For this tutorial, **it is strongly suggested that you do not skip the install step for eosio.cdt**, failing to install will make it more difficult to follow this and other tutorials, and make usage in general more difficult.
[block:api-header]
{
  "title": "Troubleshooting"
}
[/block]
## Getting Errors during build.
- Search your errors for the string "/usr/local/include/eosiolib/"
- If found, `rm -fr /usr/local/include/eosiolib/` or navigate to `/usr/local/include/` and delete `eosiolib` using your operating system's file browser.