---
title: "Connect to Non-Default Host/Port"
excerpt: ""
---
[block:callout]
{
  "type": "info",
  "body": "This document might be out of date as it has been moved. Please see [current document here](https://developers.eos.io/eosio-cleos/docs/connecting-to-non-default-hostport)"
}
[/block]

[block:api-header]
{
  "title": "Description"
}
[/block]
`cleos` can be connected to different nodes by using the `--url` or `--wallet-url` optional arguments.
[block:callout]
{
  "type": "warning",
  "body": "This tutorial assumes that `eosiocpp`, `cleos`, `nodeos`, and `keosd` have all been added to your **$PATH**. Learn how to [Alias your EOSIO components](https://developers.eos.io/eosio-cpp/docs/aliasing-eosio-components)",
  "title": "Attention"
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "If no optional arguments are used (i.e. --url and --wallet-url), `cleos` automatically tries to connect to a locally running eos node (i.e. `nodeos`).",
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
      "code": "cleos --url http://127.0.0.1:8888 ${subcommand}",
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
      "code": "cleos --wallet-url http://test1.eos.io:8888 ${subcommand}",
      "language": "shell"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Attention",
  "body": "`--wallet-url` and or `--url` need to be used on each execution of `cleos` in order for commands to interact with the desired node."
}
[/block]
`keosd` is started automatically by `cleos`.  It is possible, when doing development and testing, that `keosd` is started manually (not by `cleos`) and you end up with multiple `keosd` processes running.  When multiple instances of `keosd` are running on the same server, you might find that your `cleos` command is not finding the right set of keys.  To check whether multiple instances of `keosd` are running, and what ports they are running on, you can try something like the following to isolate the `keosd` processes and ports in use:
```
$ pgrep keosd | xargs printf " -p %d" | xargs lsof -Pani
COMMAND   PID         USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
keosd   49590 tutorial        6u  IPv4 0x72cd8ccf8c2c2d03      0t0  TCP 127.0.0.1:8900 (LISTEN)
keosd   62812 tutorial        7u  IPv4 0x72cd8ccf90428783      0t0  TCP 127.0.0.1:8899 (LISTEN)
```