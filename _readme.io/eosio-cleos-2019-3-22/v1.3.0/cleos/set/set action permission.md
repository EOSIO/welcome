---
title: "set action permission"
excerpt: "Set's authorization for a contract's specific action"
---
See [set account permission](ref:cleos-set-account) 
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `account` _TEXT_ - The account to set/delete a permission authority for (required)
- `code` _TEXT_ - The account that owns the code for the action
- `type` _TEXT_  the type of the action
- `requirement` _TEXT_  - The permission name require for executing the given action
[block:api-header]
{
  "title": "Options"
}
[/block]
- `-h,--help` - Print this help message and exit
- `-a,--abi' _TEXT_ - The ABI for the contract
- `-x,--expiration _TEXT_ - set the time in seconds before a transaction expires, defaults to 30s
- `-f,--force-unique` - force the transaction to be unique. this will consume extra bandwidth and remove any protections against accidently issuing the same transaction multiple times
- `-s,--skip-sign` - Specify if unlocked wallet keys should be used to sign transaction
- `-d,--dont-broadcast` - Don't broadcast transaction to the network (just print to stdout)
- `-p,--permission`  _TEXT_ - An account and permission level to authorize, as in 'account@permission' (defaults to 'account@active')
- `--max-cpu-usage-ms` _UINT_ - Set an upper limit on the milliseconds of cpu usage budget, for the execution of the transaction (defaults to 0 which means no limit)
- `--max-net-usage` _UINT_ - Set an upper limit on the net usage budget, in bytes, for the transaction (defaults to 0 which means no limit)
[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "#cleos set action permission @ACCOUNT @CONTRACT ACTION_NAME PERMISSION_NAME\n\n#Link a `voteproducer` action to the 'vote' permissions\ncleos set action permission sandwichfarm eosio.system voteproducer voting -p sandwichfarm@voting\n\n#Now can execute the transaction with the previously set permissions. \ncleos system voteproducer approve sandwichfarm someproducer -p sandwichfarm@voting",
      "language": "shell"
    }
  ]
}
[/block]