---
title: "net"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
Interact with local p2p network connections.
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
      "code": "$ ./cleos net",
      "language": "shell"
    }
  ]
}
[/block]
Subcommands
[block:api-header]
{
  "title": "Subcommands"
}
[/block]
  `cleos net connect` start a new connection to a peer
  `cleos net disconnect` close an existing connection
 `cleos net status` status of existing connection
  `cleos net peers` status of all existing peers
[block:code]
{
  "codes": [
    {
      "code": "ERROR: RequiredError: Subcommand required\nInteract with local p2p network connections\nUsage: ./cleos net SUBCOMMAND\n\nSubcommands:\n",
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
      "code": "$ ./cleos net connect",
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
      "code": "ERROR: RequiredError: host\nstart a new connection to a peer\nUsage: ./cleos net connect host\n\nPositionals:\n  host TEXT                   The hostname:port to connect to.",
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
      "code": "$ ./cleos net disconnect",
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
      "code": "ERROR: RequiredError: host\nclose an existing connection\nUsage: ./cleos net disconnect host\n\nPositionals:\n  host TEXT                   The hostname:port to disconnect from.",
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
      "code": "$ ./cleos net status",
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
      "code": "ERROR: RequiredError: host\nstatus of existing connection\nUsage: ./cleos net status host\n\nPositionals:\n  host TEXT                   The hostname:port to query status of connection",
      "language": "shell"
    }
  ]
}
[/block]