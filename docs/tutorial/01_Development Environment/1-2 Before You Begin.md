---
title: "1.2 Before You Begin"
excerpt: ""
---
[[info]]
|
Looking for the version of this series that uses [Docker](https://developers.eos.io/eosio-home/v1.7.0/docs/introduction)?

## Step 1: Install binaries
This tutorial is going to use pre-built binaries. For you to get started as quickly as possible this is the best option. Building from source is an option, but will set you back an hour or more and you may encounter build errors.

The below commands will download binaries for respective operating systems.

## Mac OS X Brew Install:

```shell
brew tap eosio/eosio
brew install eosio
```
## Ubuntu 18.04 Debian Package Install:

```shell
wget https://github.com/EOSIO/eos/releases/download/v1.7.0/eosio_1.7.0-1-ubuntu-18.04_amd64.deb
sudo apt install ./eosio_1.7.0-1-ubuntu-18.04_amd64.deb
```
## Ubuntu 16.04 Debian Package Install:

```shell
wget https://github.com/EOSIO/eos/releases/download/v1.7.0/eosio_1.7.0-1-ubuntu-16.04_amd64.deb
sudo apt install ./eosio_1.7.0-1-ubuntu-16.04_amd64.deb
```
## CentOS RPM Package Install:

```shell
wget https://github.com/EOSIO/eos/releases/download/v1.7.0/eosio-1.7.0-1.el7.x86_64.rpm
sudo yum install ./eosio-1.7.0-1.el7.x86_64.rpm
```
## Fedora RPM Package Install

```text
wget https://github.com/EOSIO/eos/releases/download/v1.7.0/eosio-1.7.0-1.fc27.x86_64.rpm
sudo yum install ./eosio-1.7.0-1.fc27.x86_64.rpm
```

[[warning]]
|
If you have previous versions of eosio installed on your system, please uninstall before proceeding. Detail instruction see [here](https://github.com/EOSIO/eos/blob/master/README.md)

## Step 2: Setup a development directory, stick to it.
You're going to need to pick a directory to work from, it's suggested to create a `contracts` directory somewhere on your local drive. 

```shell
mkdir contracts
cd contracts
```

## Step 3: Enter your local directory below.
Get the path of that directory and save it for later, as you're going to need it, you can use the following command to get your absolute path.
```
pwd
```

Enter the absolute path to your contract directory below, and it will be inserted throughout the documentation to make your life a bit easier. _This functionality requires cookies_
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3cdb3df-cli-2.2.2.gif",
        "cli-2.2.2.gif",
        622,
        94,
        "#020202"
      ]
    }
  ]
}
[/block]

[block:html]
{
  "html": "<div class=\"eosio-helper-box\">\n  <form> \n    <label>Absolute Path to Contract</label>\n    <input class=\"helper-cookie\" name=\"CONTRACTS_DIR\" type=\"text\" />\n    <input type=\"submit\" />\n    <span></span>\n  </form>\n</div>"
}
[/block]