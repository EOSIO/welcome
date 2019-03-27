---
title: "1.2 Before You Begin"
excerpt: ""
---
[block:api-header]
{
  "title": "Step 1: Install binaries"
}
[/block]
This tutorial is going to use pre-build binaries. For you to get started as quickly as possible this is the best option. Building from source is an option, but will set you back an hour or more and you may encounter build errors.

The below commands will download binaries for respective operating systems.

## Mac OS X Brew Install:
[block:code]
{
  "codes": [
    {
      "code": "brew tap eosio/eosio\nbrew install eosio",
      "language": "shell"
    }
  ]
}
[/block]
## Ubuntu 18.04 Debian Package Install:
[block:code]
{
  "codes": [
    {
      "code": "wget https://github.com/eosio/eos/releases/download/v1.4.4/eosio_1.4.4-1-ubuntu-18.04_amd64.deb\nsudo apt install ./eosio_1.4.4-1-ubuntu-18.04_amd64.deb",
      "language": "shell"
    }
  ]
}
[/block]
## Ubuntu 16.04 Debian Package Install:
[block:code]
{
  "codes": [
    {
      "code": "wget https://github.com/eosio/eos/releases/download/v1.4.4/eosio_1.4.4-1-ubuntu-16.04_amd64.deb\nsudo apt install ./eosio_1.4.4-1-ubuntu-16.04_amd64.deb",
      "language": "shell"
    }
  ]
}
[/block]
## CentOS RPM Package Install:
[block:code]
{
  "codes": [
    {
      "code": "wget https://github.com/eosio/eos/releases/download/v1.4.4/eosio-1.4.4-1.el7.x86_64.rpm\nsudo yum install ./eosio-1.4.4-1.el7.x86_64.rpm",
      "language": "shell"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "Looking for this series with [Docker](https://developers.eos.io/eosio-home/v1.7.0/docs/introduction)?"
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "If you have previous versions of eosio installed on your system, please uninstall before proceeding. Detail instruction see [here](https://github.com/EOSIO/eos/blob/master/README.md)"
}
[/block]

[block:api-header]
{
  "title": "Step 2: Setup a development directory, stick to it."
}
[/block]
You're going to need to pick a directory to work from, it's suggested to create a `contracts` directory somewhere on your local drive. 
[block:code]
{
  "codes": [
    {
      "code": "mkdir contracts\ncd contracts",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 3: Enter your local directory below."
}
[/block]
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