---
content_title: Install the EOSIO.CDT
link_text: Install the EOSIO.CDT
---

The EOSIO Contract Development Toolkit, CDT for short, is a collection of tools related to contract compilation. Subsequent tutorials use the CDT primarily for compiling contracts and generating ABIs.

Starting from 1.3.x, CDT supports Mac OS X brew, Linux Debian and RPM packages. The easiest option to install would be using one of these package systems. Pick one installation method only.

[[warning]]
| If you have versions of eosio.cdt prior to 1.3.0 installed on your system, please uninstall before proceeding

# Mac OS X
## Install
```shell
brew tap eosio/eosio.cdt
brew install eosio.cdt
```
## Uninstall
```shell
brew remove eosio.cdt
```
# Ubuntu (Debian)

## Install
```shell
wget https://github.com/EOSIO/eosio.cdt/releases/download/v1.6.3/eosio.cdt_1.6.3-1-ubuntu-18.04_amd64.deb

sudo apt install ./eosio.cdt_1.6.3-1-ubuntu-18.04_amd64.deb
```
## Uninstall
```shell
sudo apt remove eosio.cdt
```
# CentOS/Redhat (RPM)
## Install
```shell
wget https://github.com/EOSIO/eosio.cdt/releases/download/v1.6.3/eosio.cdt-1.6.3-1.el7.x86_64.rpm

sudo yum install ./eosio.cdt-1.6.3-1.el7.x86_64.rpm
```
## Uninstall
```shell
$ sudo yum remove eosio.cdt
```
# Install from Source

The location where `eosio.cdt` is cloned is not that important because you will be installing `eosio.cdt` as a local binary in later steps. For now, you can clone `eosio.cdt` to your "contracts" directory previously created, or really anywhere else on your local system you see fit.
```text
cd CONTRACTS_DIR
```
## Download
Clone version 1.6.3 of the `eosio.cdt` repository.
```text
git clone --recursive https://github.com/eosio/eosio.cdt --branch v1.6.3 --single-branch
cd eosio.cdt
```
It may take up to 30 minutes to clone the repository

[[success | Virtual machine environment]]
| In case you are using a virtual machine. It should be configured with at least 2 CPUs (does not have to be two physical ones) and 8G of memory to avoid compilation errors

## Build
```shell
./build.sh
```
### Install
```shell
sudo ./install.sh
```
The above command needs to be ran with `sudo` because `eosio.cdt`'s various binaries will be installed locally. You will be asked for your computer's account password.

Installing `eosio.cdt` will make the compiled binary global so it can be accessable anywhere. For this tutorial, **it is strongly suggested that you do not skip the install step for eosio.cdt**, failing to install will make it more difficult to follow this and other tutorials, and make usage in general more difficult.

# Troubleshooting
## Getting Errors during build
- Search your errors for the string "/usr/local/include/eosiolib/"
- If found, `rm -fr /usr/local/include/eosiolib/` or navigate to `/usr/local/include/` and delete `eosiolib` using your operating system's file browser.

## What's Next?
[Create Development Wallet](30_development-wallet.md): Steps to create a new development wallet to store public-private key pair.
