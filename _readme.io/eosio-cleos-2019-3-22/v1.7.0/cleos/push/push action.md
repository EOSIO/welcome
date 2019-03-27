---
title: "push action"
excerpt: "Push a transaction with a single action"
---
[block:api-header]
{
  "title": "Positionals"
}
[/block]
- `contract` _Type: Text_ - The account providing the contract to execute
- `action` _Type: Text_ - The action to execute on the contract
- `data` _Type: Text_ - The arguments to the contract

**Output**
[block:api-header]
{
  "title": "Options"
}
[/block]
- ` -h,--help` - Print this help message and exit
- `-x,--expiration` - set the time in seconds before a transaction expires, defaults to 30s
- `-f,--force-unique` - force the transaction to be unique. this will consume extra bandwidth and remove any protections against accidently issuing the same transaction multiple times
- ` -s,--skip-sign` - Specify if unlocked wallet keys should be used to sign transaction
- `-d,--dont-broadcast` - don't broadcast transaction to the network (just print to stdout)
- `-p,--permission` _Type: Text_ - An account and permission level to authorize, as in 'account@permission'
[block:api-header]
{
  "title": "Example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos push action eosio.token transfer '{\"from\":\"bob\",\"to\":\"alice\",\"quantity\":\"20.0000 SYS\",\"memo\":\"some SYS for you alice!\"}' -p bob@active",
      "language": "shell"
    }
  ]
}
[/block]