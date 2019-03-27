---
title: "exec"
excerpt: "Execute a transaction while bypassing authorisation checks"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `executer` _TEXT_ - Account executing the transaction and paying for the deferred transaction RAM (required)
- `transaction` _TEXT_ - The JSON string or filename defining the transaction to execute (required)
[block:api-header]
{
  "title": "Options"
}
[/block]
- `-h,--help` - Print this help message and exit
-  `-x,--expiration` - Set the time in seconds before a transaction expires, defaults to 30s
-  `-f,--force-unique` - Force the transaction to be unique. this will consume extra bandwidth and remove any protections against accidentally issuing the same transaction multiple times
-  `-s,--skip-sign` - Specify if unlocked wallet keys should be used to sign transaction
-  `-j,--json` - Print result as json
-  `-d,--dont-broadcast` - Don't broadcast transaction to the network (just print to stdout)
-  `--return-packed` - Used in conjunction with --dont-broadcast to get the packed transaction
-  `-r,--ref-block` _TEXT_ - Set the reference block num or block id used for TAPOS (Transaction as Proof-of-Stake)
-  `-p,--permission` _TEXT_ - An account and permission level to authorise, as in 'account@permission'
-  `--max-cpu-usage-ms` _UINT_ - Set an upper limit on the milliseconds of cpu usage budget, for the execution of the transaction (defaults to 0 which means no limit)
-  `--max-net-usage` _UINT_ - Set an upper limit on the net usage budget, in bytes, for the transaction (defaults to 0 which means no limit)
-  `--delay-sec` _UINT_ - Set the delay_sec seconds, defaults to 0s

[block:api-header]
{
  "title": "Usage"
}
[/block]
Use of the sudo command is intended as a multi signed action, Loading and running the the eosio.sudo contract is explained in detail here in the [sudo readme file](https://github.com/EOSIO/eos/tree/master/contracts/eosio.sudo)
[block:code]
{
  "codes": [
    {
      "code": "",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Output"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "",
      "language": "shell"
    }
  ]
}
[/block]