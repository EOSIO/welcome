---
title: "state_history_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The state_history_plugin caches blockchain data into files and is useful for obtaining historical data. The state_history listens on a socket for applications connecting to the state history plugin and send the blockchain data to the application.  

An example of an application which retrieves data from the state_history_plugin is [fill-postgresql](https://github.com/EOSIO/fill-postgresql)
[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "\n  --state-history-dir arg       (default=\"state-history\")\n                                The location of the state-history directory\n                                (absolute path or relative to application data\n                                dir)\n  --trace-history               Enable trace history\n  --chain-state-history         Enable chain state history\n  --state-history-endpoint arg  (default=0.0.0.0:8080)\n                                The endpoint upon which to listen for incoming\n                                connections\n  --delete-state-history        Clear state history files\n\nRequires the chain_plugin command\n\n  --disable-replay-opts         Disable optimizations that specifically target\n                                replay\n",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Usage"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::state_history_plugin\n\n# nodeos startup program\n--plugin eosio::state_history_plugin\n",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Dependencies"
}
[/block]
- [chain_plugin](doc:chain_plugin) 

## Load Dependency Examples
[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::chain_plugin\n\n\n# nodeos startup params\n--plugin eosio::chain_plugin --disable-replay-opts",
      "language": "shell"
    }
  ]
}
[/block]