---
title: "Getting the Code"
excerpt: ""
---
To download all of the code, clone the `eos` repository and its submodules.
[block:code]
{
  "codes": [
    {
      "code": "git clone https://github.com/EOSIO/eos --recursive\n",
      "language": "shell"
    }
  ]
}
[/block]
If a repository is cloned without the `--recursive` flag, the submodules can be cloned at a later time: 
[block:code]
{
  "codes": [
    {
      "code": "git submodule update --init --recursive\n",
      "language": "shell"
    }
  ]
}
[/block]