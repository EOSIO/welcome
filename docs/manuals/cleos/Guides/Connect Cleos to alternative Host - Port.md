---
title: "Connect Cleos to alternative Host & Port"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
`cleos` can be connected to different nodes by using the `-H, --host` and `-p, --port` optional arguments.
[block:callout]
{
  "type": "warning",
  "body": "This tutorial assumes that `eosiocpp`, `cleos`, `nodeos`, and `keosd` have all been added to your **$PATH**. Learn how to [Alias your EOSIO components](doc:aliasing-eosio-components)",
  "title": "Attention"
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "If no optional arguments are used (i.e. -H and -p), `cleos` automatically tries to connect to a locally running eos node (i.e. `nodeos`).",
  "title": "Default Behavior"
}
[/block]

[block:api-header]
{
  "title": "Commands"
}
[/block]
Connecting to Nodeos
[block:code]
{
  "codes": [
    {
      "code": "cleos -url localhost:8888 ${subcommand}",
      "language": "shell"
    }
  ]
}
[/block]
Connecting to Keosd
[block:code]
{
  "codes": [
    {
      "code": "cleos --wallet-url test1.eos.io:8888 ${subcommand}",
      "language": "shell"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Attention",
  "body": "`-H` and `-p` need to be used on each execution of `cleos` in order for commands to interact with the desired node."
}
[/block]