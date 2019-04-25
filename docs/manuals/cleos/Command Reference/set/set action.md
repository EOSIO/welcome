---
title: "set action"
excerpt: "`./cleos set action`"
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Sets or updates an action's state on the blockchain.
[block:api-header]
{
  "title": "Info"
}
[/block]
**Command**
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos set action",
      "language": "shell"
    }
  ]
}
[/block]
**Output**
[block:code]
{
  "codes": [
    {
      "code": "ERROR: RequiredError: Subcommand required\nset or update blockchain action state\nUsage: ./cleos set action [OPTIONS] SUBCOMMAND\n\nOptions:\n  -h,--help                   Print this help message and exit\n\nSubcommands:\n  permission                  set parmaters dealing with account permissions",
      "language": "shell"
    }
  ]
}
[/block]
**Command**
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos set action permission",
      "language": "shell"
    }
  ]
}
[/block]
**Output**
[block:api-header]
{
  "title": "Positionals"
}
[/block]
`code` _Type: Text_ - The account that owns the code for the action
`type` _Type: Text_ the type of the action
`requirement` _Type: Text, Default: Null_ - The permission name require for executing the given action
[block:api-header]
{
  "title": "Options"
}
[/block]
`-h,--help` Print this help message and exit
`-a,--abi' _Type:Text_ - The ABI for the contract
`-x,--expiration _Type:Text_ - set the time in seconds before a transaction expires, defaults to 30s
`-f,--force-unique` - force the transaction to be unique. this will consume extra bandwidth and remove any protections against accidently issuing the same transaction multiple times
`-s,--skip-sign` Specify if unlocked wallet keys should be used to sign transaction
`-d,--dont-broadcast` - Don't broadcast transaction to the network (just print to stdout)
`-p,--permission`  _Type:Text_ - An account and permission level to authorize, as in 'account@permission' (defaults to 'account@active')
[block:code]
{
  "codes": [
    {
      "code": "ERROR: RequiredError: account\nset parmaters dealing with account permissions\nUsage: ./cleos set action permission [OPTIONS] account code type requirement\n\nPositionals:\n  account TEXT                The account to set/delete a permission authority for\n  code TEXT                   The account that owns the code for the action\n  type TEXT                   the type of the action\n  requirement TEXT            [delete] NULL, [set/update] The permission name require for executing the given action\n\nOptions:\n  -h,--help                   Print this help message and exit\n  -x,--expiration             set the time in seconds before a transaction expires, defaults to 30s\n  -f,--force-unique           force the transaction to be unique. this will consume extra bandwidth and remove any protections against accidently issuing the same transaction multiple times\n  -s,--skip-sign              Specify if unlocked wallet keys should be used to sign transaction\n  -d,--dont-broadcast         don't broadcast transaction to the network (just print to stdout)\n  -p,--permission TEXT ...    An account and permission level to authorize, as in 'account@permission' (defaults to 'account@active')",
      "language": "shell"
    }
  ]
}
[/block]