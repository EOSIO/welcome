---
title: "bidnameinfo"
excerpt: "Returns data about a particular name and it's bidding status"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
* `name` _TEXT_  - The name to lookup
[block:api-header]
{
  "title": "Options"
}
[/block]
* `-h,--help` - Print this help message and exit
* `-x,--expiration` - Set the time in seconds before a transaction expires, defaults to 30s
* `-f,--force-unique` - Force the transaction to be unique. this will consume extra bandwidth and remove any protections against accidently issuing the same transaction multiple times
* `-s,--skip-sign` - Specify if unlocked wallet keys should be used to sign transaction
* `-j,--json` - Print result as json
* `-d,--dont-broadcast` - Don't broadcast transaction to the network (just print to stdout)
* `-r,--ref-block` _TEXT_ - Set the reference block num or block id used for TAPOS (Transaction as Proof-of-Stake)
* `-p,--permission` _TEXT_ - An account and permission level to authorize, as in 'account@permission'
* `--max-cpu-usage-ms` _UINT_ - Set an upper limit on the milliseconds of cpu usage budget, for the execution of the transaction (defaults to 0 which means no limit)
* `--max-net-usage` _UINT_ - Set an upper limit on the net usage budget, in bytes, for the transaction (defaults to 0 which means no limit)
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos system bidnameinfo bob",
      "language": "shell"
    }
  ]
}
[/block]