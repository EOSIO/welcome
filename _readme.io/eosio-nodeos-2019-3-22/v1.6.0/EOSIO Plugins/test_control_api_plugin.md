---
title: "test_control_api_plugin"
excerpt: "This plugin is designed for testing nodeos"
---
[block:api-header]
{
  "title": "Description"
}
[/block]
This allows you to send a control message to the [test_control_plugin](doc:test_control_plugin) telling the test_control_plugin to shut down a nodeos instance when reaching a particular block.

It is intended for testing.
[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl %s/v1/test_control/kill_node_on_producer -d '{ \\\"producer\\\":\\\"%s\\\", \\\"where_in_sequence\\\":%d, \\\"based_on_lib\\\":\\\"%s\\\" }' -X POST -H \\\"Content-Type: application/json\\\"\" % \\\n            ",
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
      "code": "# nodeos startup params\n--plugin eosio::test_control_api_plugin",
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
- [test_control_plugin](doc:test_control_plugin) 
- [chain_plugin](doc:chain_plugin) 
- [http_plugin](doc:http_plugin)
[block:api-header]
{
  "title": "Load Dependancy Examples"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "# config.ini\nplugin = eosio::chain_plugin\nplugin = eosio::http_plugin\n\n# nodeos startup params\n--plugin eosio::test_control_plugin \n\n\n# nodeos startup params\n--plugin eosio::test_control_plugin --plugin eosio::chain_plugin --plugin eosio::http_plugin",
      "language": "shell"
    }
  ]
}
[/block]