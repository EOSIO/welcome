---
title: "actions"
excerpt: "Retrieves all actions with specific account name referenced in their scope."
---
We can also query list of actions that have an account as a receiver. The only accounts queryable are those listed as the receiver in the `--filter-on receiver:action:actor` option.
[block:api-header]
{
  "title": "Positional Parameters"
}
[/block]
- `account_name` _TEXT_ - name of account to query on
[block:api-header]
{
  "title": "Examples"
}
[/block]
Get actions belonging to eosio
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos get actions eosio.token\n#  seq  when                              contract::action => receiver      trx id...   args\n================================================================================================================\n#  976   2018-06-01T19:54:05.000     eosio.token::transfer => eosio.token   1d1fe154... {\"from\":\"useraaaaaaae\",\"to\":\"useraaaaaaaa\",\"quantity\":\"0.000...\n#  977   2018-06-01T19:54:05.000     eosio.token::transfer => eosio.token   a0c9e5bc... {\"from\":\"useraaaaaaab\",\"to\":\"useraaaaaaaa\",\"quantity\":\"0.000...\n#  978   2018-06-01T19:54:05.000     eosio.token::transfer => eosio.token   3749d0d1... {\"from\":\"useraaaaaaab\",\"to\":\"useraaaaaaah\",\"quantity\":\"0.000...\n#  979   2018-06-01T19:54:05.000     eosio.token::transfer => eosio.token   dda205b0... {\"from\":\"useraaaaaaai\",\"to\":\"useraaaaaaaj\",\"quantity\":\"0.000...\n#  980   2018-06-01T19:54:05.000     eosio.token::transfer => eosio.token   14089e9b... {\"from\":\"useraaaaaaab\",\"to\":\"useraaaaaaae\",\"quantity\":\"0.000...\n#  981   2018-06-01T19:54:05.000     eosio.token::transfer => eosio.token   6882cefc... {\"from\":\"useraaaaaaaj\",\"to\":\"useraaaaaaab\",\"quantity\":\"0.000...\n...",
      "language": "shell"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "These transactions will not exist on your blockchain",
  "title": "Important Note"
}
[/block]