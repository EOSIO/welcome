---
title: "transfer"
excerpt: "Transfer a token"
---
[block:api-header]
{
  "title": "Positional Parameters"
}
[/block]
- `sender` _TEXT_ - The account sending tokens
- `recipient` _TEXT_ - The account receiving tokens
- `amount` _TEXT_ - The amount of tokens to send and the token symbol
- `memo` _TEXT_ - The memo for the transfer

[block:api-header]
{
  "title": "Options"
}
[/block]
- `-c, --contract`_TEXT_  - The contract which controls the token. Defaults to eosio.token.

[block:api-header]
{
  "title": "Usage"
}
[/block]
Transfer 1 SYS from **inita** to **tester**
[block:code]
{
  "codes": [
    {
      "code": "$ ./cleos transfer useraaaaaaaa useraaaaaaac \"1.0000 SYS\" \"hello world\"\n$ ./cleos transfer useraaaaaaaa useraaaaaaac -c eosio.token \"1.0000 SYS\" \"hello world\"",
      "language": "shell"
    }
  ]
}
[/block]
The response will look something like this
[block:code]
{
  "codes": [
    {
      "code": "executed transaction: ac989464a987e9061d4eabdfad0e5707a23ba769798a01f3ce010c5b3775b554  128 bytes  490 us\n#   eosio.token <= eosio.token::transfer        {\"from\":\"useraaaaaaaa\",\"to\":\"useraaaaaaac\",\"quantity\":\"1.0000 SYS\",\"memo\":\"hello world\"}",
      "language": "shell"
    }
  ]
}
[/block]