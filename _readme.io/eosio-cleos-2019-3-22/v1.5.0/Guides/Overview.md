---
title: "Overview"
excerpt: ""
---
`cleos` is a command line tool that interfaces with the REST API exposed by `nodeos`. In order to use `cleos` you will need to have the end point (IP address and port number) to a `nodeos` instance and also configure `nodeos` to load the 'eosio::chain_api_plugin'.  `cleos` contains documentation for all of its commands. For a list of all commands known to `cleos`, simply run it with no arguments:

[block:code]
{
  "codes": [
    {
      "code": "Command Line Interface to EOSIO Client\nUsage: ./programs/cleos/cleos [OPTIONS] SUBCOMMAND\n\nOptions:\n  -h,--help                   Print this help message and exit\n  -u,--url TEXT=http://localhost:8888/\n                              the http/https URL where nodeos is running\n  --wallet-url TEXT=http://localhost:8900/\n                              the http/https URL where keosd is running\n  -r,--header                 pass specific HTTP header; repeat this option to pass multiple headers\n  -n,--no-verify              don't verify peer certificate when using HTTPS\n  -v,--verbose                output verbose actions on error\n\nSubcommands:\n  version                     Retrieve version information\n  create                      Create various items, on and off the blockchain\n  get                         Retrieve various items and information from the blockchain\n  set                         Set or update blockchain state\n  transfer                    Transfer EOS from account to account\n  net                         Interact with local p2p network connections\n  wallet                      Interact with local wallet\n  sign                        Sign a transaction\n  push                        Push arbitrary transactions to the blockchain\n  multisig                    Multisig contract commands\n  system                      Send eosio.system contract action to the blockchain.",
      "language": "text"
    }
  ]
}
[/block]
To get help with any particular subcommand, run it with no arguments as well:
[block:code]
{
  "codes": [
    {
      "code": "Create various items, on and off the blockchain\nUsage: ./cleos create SUBCOMMAND\n\nSubcommands:\n  key                         Create a new keypair and print the public and private keys\n  account                     Create an account, buy ram, stake for bandwidth for the account\n\n\nCreate an account, buy ram, stake for bandwidth for the account\nUsage: ./programs/cleos/cleos create account [OPTIONS] creator name OwnerKey [ActiveKey]\n\nPositionals:\n  creator TEXT                The name of the account creating the new account (required)\n  name TEXT                   The name of the new account (required)\n  OwnerKey TEXT               The owner public key for the new account (required)\n  ActiveKey TEXT              The active public key for the new account\n\nOptions:\n  -h,--help                   Print this help message and exit\n  -x,--expiration             set the time in seconds before a transaction expires, defaults to 30s\n  -f,--force-unique           force the transaction to be unique. this will consume extra bandwidth and remove any protections against accidently issuing the same transaction multiple times\n  -s,--skip-sign              Specify if unlocked wallet keys should be used to sign transaction\n  -j,--json                   print result as json\n  -d,--dont-broadcast         don't broadcast transaction to the network (just print to stdout)\n  -r,--ref-block TEXT         set the reference block num or block id used for TAPOS (Transaction as Proof-of-Stake)\n  -p,--permission TEXT ...    An account and permission level to authorize, as in 'account@permission'\n  --max-cpu-usage-ms UINT     set an upper limit on the milliseconds of cpu usage budget, for the execution of the transaction (defaults to 0 which means no limit)\n  --max-net-usage UINT        set an upper limit on the net usage budget, in bytes, for the transaction (defaults to 0 which means no limit)",
      "language": "text"
    }
  ]
}
[/block]