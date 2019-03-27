---
title: "1.5 Install the CDT"
excerpt: ""
---
The EOSIO Contract Development Toolkit, CDT for short, is a collection of tools related to contract compilation. Subsequent tutorials use the CDT primarily for compiling contracts and generating ABIs.

Starting from 1.3.x, CDT supports Mac OS X brew, Linux Debian and RPM packages. The easiest option to install would be using one of these package systems. Pick one installation method only.
[block:callout]
{
  "type": "warning",
  "body": "If you have versions of eosio.cdt prior to 1.3.0 installed on your system, please uninstall before proceeding"
}
[/block]

[block:api-header]
{
  "title": "Homebrew (Mac OS X)"
}
[/block]
## Install
[block:code]
{
  "codes": [
    {
      "code": "brew tap eosio/eosio.cdt\nbrew install eosio.cdt",
      "language": "shell"
    }
  ]
}
[/block]
## Uninstall
[block:code]
{
  "codes": [
    {
      "code": "brew remove eosio.cdt",
      "language": "shell"
    }
  ]
}
[/block]
# Ubuntu (Debian) 

## Install
[block:code]
{
  "codes": [
    {
      "code": "wget https://github.com/EOSIO/eosio.cdt/releases/download/v1.4.1/eosio.cdt-1.4.1.x86_64.deb\nsudo apt install ./eosio.cdt-1.4.1.x86_64.deb",
      "language": "shell"
    }
  ]
}
[/block]
## Uninstall
[block:code]
{
  "codes": [
    {
      "code": "sudo apt remove eosio.cdt",
      "language": "shell"
    }
  ]
}
[/block]
# CentOS/Redhat (RPM) 
## Install
[block:code]
{
  "codes": [
    {
      "code": "wget https://github.com/EOSIO/eosio.cdt/releases/download/v1.4.1/eosio.cdt-centos-1.4.1.x86_64-0.x86_64.rpm\nsudo yum install ./eosio.cdt-centos-1.4.1.x86_64-0.x86_64.rpm",
      "language": "shell"
    }
  ]
}
[/block]
## Uninstall
[block:code]
{
  "codes": [
    {
      "code": "$ sudo yum remove eosio.cdt",
      "language": "shell"
    }
  ]
}
[/block]
# Install from Source

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
## Download
Clone version 1.4.1 of the `eosio.cdt` repository. 
[block:code]
{
  "codes": [
    {
      "code": "git clone --recursive https://github.com/eosio/eosio.cdt --branch v1.4.1 --single-branch\ncd eosio.cdt",
      "language": "text"
    }
  ]
}
[/block]
It may take up to 30 minutes to clone the repository

## Build
[block:code]
{
  "codes": [
    {
      "code": "./build.sh",
      "language": "shell"
    }
  ]
}
[/block]
### Install
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

Installing `eosio.cdt` will make the compiled binary global so it can be accessible anywhere. For this tutorial, **it is strongly suggested that you do not skip the install step for eosio.cdt**, failing to install will make it more difficult to follow this and other tutorials, and make usage in general more difficult.
[block:api-header]
{
  "title": "Troubleshooting"
}
[/block]
## Getting Errors during build.
- Search your errors for the string "/usr/local/include/eosiolib/"
- If found, `rm -fr /usr/local/include/eosiolib/` or navigate to `/usr/local/include/` and delete `eosiolib` using your operating system's file browser.