---
title: "Adding eosio.code to active authority with cleos' helper"
excerpt: ""
---
[block:api-header]
{
  "title": "Brief Explanation of eosio.code"
}
[/block]
When developing contracts you may require your contract to have the ability to broadcast inline actions. For your contract to have this ability, you will need to use your contract's `active` authority. However, for security purposes, contracts cannot sign with their active authority unless the contract's account has been configured to do so. `eosio.code` is a pseudo-authority that grants a contract active authority. Previously, a complex and potentially risky cleos command was required to add `yourcontract@eosio.code` to the active authority, this has been greatly simplified with the `eosio.code` helper. 
[block:api-header]
{
  "title": "Adding eosio.code to a contract's active authority"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos set account permission YOURCONTRACT active --add-code",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Removing eosio.code from a contract's active authority"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "cleos set account permission YOURCONTRACT active --remove-code",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "What --add-code and --remove-code are doing behind the scenes"
}
[/block]
When using --add-code and --remove-code, cleos obtains the current permissions of the account, and either appends to removes `YOURCONTRACT@eosio.code` from the active permission. It's suggested to use the `--add-code` helper, and not the following command because it's very easy to make a mistake that can potentially result in being locked out of an account. 
[block:code]
{
  "codes": [
    {
      "code": "cleos set account permission YOUR_CONTRACT active '{\"threshold\": 1,\"keys\": [{\"key\": \"CURRENT_PUBLIC_KEY(S)_IN_ACTIVE_PERM\",\"weight\": 1}], \"accounts\": [{\"permission\":{\"actor\":\"YOUR_CONTRACT\",\"permission\":\"eosio.code\"},\"weight\":1}]}' -p YOUR_CONTRACT@owner",
      "language": "shell"
    }
  ]
}
[/block]