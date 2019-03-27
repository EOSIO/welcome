---
title: "set account permission"
excerpt: "Creates or updates an account's permission"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `account` _TEXT_ - The account to set/delete a permission authority for
- `permission` _TEXT_ - The permission name to set/delete an authority for
- `authority` _TEXT_ - [delete] NULL, [create/update] public key, JSON string, or filename defining the authority
- `parent` _TEXT_ - [create] The permission name of this parents permission (Defaults to: "Active")
[block:api-header]
{
  "title": "Options"
}
[/block]
- `-h,--help` Print this help message and exit
- `-a,--abi` _TEXT_ - The ABI for the contract
- `-x,--expiration` _TEXT_ - set the time in seconds before a transaction expires, defaults to 30s
- `-f,--force-unique` - force the transaction to be unique. this will consume extra bandwidth and remove any protections against accidently issuing the same transaction multiple times
- `-s,--skip-sign` Specify if unlocked wallet keys should be used to sign transaction
- `-d,--dont-broadcast` - Don't broadcast transaction to the network (just print to stdout)
- `-r,--ref-block` _TEXT_         set the reference block num or block id used for TAPOS (Transaction as Proof-of-Stake)
- `-p,--permission`  _TEXT_ - An account and permission level to authorize, as in 'account@permission' (defaults to 'account@active')
- `--max-cpu-usage-ms` _UINT_ - set an upper limit on the milliseconds of cpu usage budget, for the execution of the transaction (defaults to 0 which means no limit)
- `--max-net-usage` _UINT_ - set an upper limit on the net usage budget, in bytes, for the transaction (defaults to 0 which means no limit)
[block:api-header]
{
  "title": "Usage"
}
[/block]
To modify permissions of an account, you must have the authority over the account and the permission of which you are modifying.

# Basic usage, set new key to a permission
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos set account permission testaccount active EOSPUBLICKEY owner -p testaccount@owner",
      "language": "shell"
    }
  ]
}
[/block]
# Basic usage, set an account (instead of a key) as authority for a permission. 
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos set account permission testaccount active diffaccount owner -p testaccount@owner",
      "language": "text"
    }
  ]
}
[/block]
## Advanced Usage, weight/thresholds
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos set account permission testaccount active '{\"threshold\" : 100, \"keys\" : [], \"accounts\" : [{\"permission\":{\"actor\":\"user1\",\"permission\":\"active\"},\"weight\":25}, {\"permission\":{\"actor\":\"user2\",\"permission\":\"active\"},\"weight\":75}]}' owner -p testaccount@owner",
      "language": "shell"
    }
  ]
}
[/block]
The JSON object used in this command is actually composed of two different types of objects

The authority JSON object ...
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"threshold\"       : 100,    /*An integer that defines cumulative signature weight required for authorization*/\n  \"keys\"            : [],     /*An array made up of individual permissions defined with an EOSIO-style PUBLIC KEY*/\n  \"accounts\"        : []      /*An array made up of individual permissions defined with an EOSIO-style ACCOUNT*/\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Returns"
}
[/block]
...contains 0 or more objects in the keys array
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"key\"           : \"EOS8X7Mp7apQWtL6T2sfSZzBcQNUqZB7tARFEm9gA9Tn9nbMdsvBB\",\n  \"weight\"        : 25      /*Set the weight of a signature from this permission*/\n}",
      "language": "json"
    }
  ]
}
[/block]
...contains 0 or more objects in the accounts array
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"permission\" : {\n    \"actor\"       : \"sandwich\",\n    \"permission\"  : \"active\"\n  },\n  \"weight\"      : 75      /*Set the weight of a signature from this permission*/\n}\n",
      "language": "json"
    }
  ]
}
[/block]