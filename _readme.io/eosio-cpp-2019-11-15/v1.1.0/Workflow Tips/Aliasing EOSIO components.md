---
title: "Aliasing EOSIO components"
excerpt: ""
---
[block:callout]
{
  "type": "success",
  "title": "Recommended Step",
  "body": "Aliasing your EOS components will simplify your development workflow, as you won't have to call the full or relative path. You will also be able to more easily follow EOSIO documentation."
}
[/block]

[block:api-header]
{
  "title": "Determining your paths"
}
[/block]
## Find your path to eos
[block:code]
{
  "codes": [
    {
      "code": "$ cd eos\n$ pwd\n/Users/sandwich/Develop/block.one/eos",
      "language": "shell"
    }
  ]
}
[/block]
Open your `~/.bash_profile` file in a text editor and replace `YOURPATH` in examples below with the path you just retrieved.
[block:api-header]
{
  "title": "Using alias"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "#NODEOS\nalias nodeos=YOURPATH/build/programs/nodeos\n#CLEOS\nalias cleos=YOURPATH/build/programs/cleos\n#KEOSD\nalias keosd=YOURPATH/build/programs/keosd\n#EOSIOCPP\nalias eosiocpp=YOURPATH/build/tools/eosiocpp",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Using PATH variables"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "#VIM\nvi ~/.bash_profile\n#NANO\nnano ~/.bash_profile\n#PICO\npico ~/.bash_profile\n#ATOM\natom ~/.bash_profile\n#Default text editor (mac)\nopen ~/.bash_profile",
      "language": "shell"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "#CLEOS\nexport PATH=YOURPATH/build/programs/cleos:$PATH\n#NODEOS\nexport PATH=YOURPATH/build/programs/nodeos:$PATH\n#KEOSD\nexport PATH=YOURPATH/build/programs/keosd:$PATH\n#EOSIOCPP\nexport PATH=YOURPATH/build/tools/eosiocpp:$PATH",
      "language": "shell"
    }
  ]
}
[/block]
Using the path I discovered with `pwd` in the example a few steps above, here's what my paths look like:
[block:code]
{
  "codes": [
    {
      "code": "#CLEOS\nexport PATH=YOURPATH/build/programs/cleos:$PATH\n#NODEOS\nexport PATH=YOURPATH/build/programs/nodeos:$PATH\n#KEOSD\nexport PATH=YOURPATH/build/programs/keosd:$PATH\n#EOSIOCPP\nexport PATH=YOURPATH/build/tools/eosiocpp:$PATH",
      "language": "shell"
    }
  ]
}
[/block]
I can now access cleos, nodeos, keosd, eosiocpp from anywhere on my system. 
[block:code]
{
  "codes": [
    {
      "code": "$ cleos\nERROR: RequiredError: Subcommand required\nCommand Line Interface to EOSIO Client\nUsage: cleos [OPTIONS] SUBCOMMAND\n\nOptions:\n  -h,--help                   Print this help message and exit\n  -H,--host TEXT=localhost    the host where nodeos is running\n  -p,--port UINT=8888         the port where nodeos is running\n  --wallet-host TEXT=localhost\n                              the host where keosd is running\n  --wallet-port UINT=8888     the port where keosd is running\n  -v,--verbose                output verbose actions on error\n\nSubcommands:\n  version                     Retrieve version information\n  create                      Create various items, on and off the blockchain\n  get                         Retrieve various items and information from the blockchain\n  set                         Set or update blockchain state\n  transfer                    Transfer EOS from account to account\n  net                         Interact with local p2p network connections\n  wallet                      Interact with local wallet\n  sign                        Sign a transaction\n  push                        Push arbitrary transactions to the blockchain\n  multisig                    Multisig contract commands",
      "language": "shell"
    }
  ]
}
[/block]
Above, I gave a messy example of aliasing your EOSIO programs and tools. This was so you could easily alias individual components. This one-liner is a bit more clean
[block:code]
{
  "codes": [
    {
      "code": "export PATH=YOURPATH/build/programs/cleos:YOURPATH/build/programs/nodeos:YOURPATH/build/programs/keosd:YOURPATH/build/tools/eosiocpp:$PATH",
      "language": "shell"
    }
  ]
}
[/block]