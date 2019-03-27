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
If a repository is cloned without the `--recursive` flag, the submodules can be retrieved after the fact by running this command from within the repo:
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
Throughout the EOSIO documentation and tutorials, reference will be made to the top level of your local EOSIO source repository.  The location where you just cloned the `eos` repository is that location.  The notation ${EOSIO_SOURCE} represents the same thing.  For example, if you ran the `git clone` operation in a folder called `~/myprojects`, then `${EOSIO_SOURCE}=~/myprojects/eos`.  ***Note that ${EOSIO_SOURCE} is used in the documentation for notational purposes only.  No environment variable is implied or required.*** More commonly, for simplicity, this and other documents might simply refer to `eos`.  This is equivalent to `${EOSIO_SOURCE}`.