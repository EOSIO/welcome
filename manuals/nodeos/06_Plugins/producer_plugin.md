---
title: "producer_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The **producer_plugin** loads functionality required for a node to produce blocks.
[block:callout]
{
  "type": "info",
  "body": "Additional configuration is required to produce blocks. Please reference the following: \n- [Configuring Block Producing Node](doc:environment-producing-node)"
}
[/block]

[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  -e [ --enable-stale-production ]      Enable block production, even if the\n                                        chain is stale.\n  -x [ --pause-on-startup ]             Start this node in a state where\n                                        production is paused\n  --max-transaction-time arg (=30)      Limits the maximum time (in\n                                        milliseconds) that is allowed for a pushed\n                                        transaction's code to execute before\n                                        being considered invalid\n  --max-irreversible-block-age arg (=-1)\n                                        Limits the maximum age (in seconds) of\n                                        the DPOS Irreversible Block for a chain\n                                        this node will produce blocks on (use\n                                        negative value to indicate unlimited)\n  -p [ --producer-name ] arg            ID of producer controlled by this node\n                                        (e.g. inita; may specify multiple\n                                        times)\n  --private-key arg                     (DEPRECATED - Use signature-provider\n                                        instead) Tuple of [public key, WIF\n                                        private key] (may specify multiple\n                                        times)\n  --signature-provider arg (=EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV=KEY:5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3)\n                                        Key=Value pairs in the form\n                                        <public-key>=<provider-spec>\n                                        Where:\n                                           <public-key>    is a string form of\n                                                           a vaild EOSIO public\n                                                           key\n\n                                           <provider-spec> is a string in the\n                                                           form <provider-type>\n                                                           :<data>\n\n                                           <provider-type> is KEY, or KEOSD\n\n                                           KEY:<data>      is a string form of\n                                                           a valid EOSIO\n                                                           private key which\n                                                           maps to the provided\n                                                           public key\n\n                                           KEOSD:<data>    is the URL where\n                                                           keosd is available\n                                                           and the approptiate\n                                                           wallet(s) are\n                                                           unlocked\n  --keosd-provider-timeout arg (=5)     Limits the maximum time (in\n                                        milliseconds) that is allowed for\n                                        sending blocks to a keosd provider for\n                                        signing\n  --greylist-account arg                account that can not access extended\n                                        CPU/NET virtual resources\n  --produce-time-offset-us arg (=0)     offset of non last block producing time\n                                        in microseconds. Negative number\n                                        results in blocks to go out sooner, and\n                                        positive number results in blocks to go\n                                        out later\n  --last-block-time-offset-us arg (=0)  offset of last block producing time in\n                                        microseconds. Negative number results\n                                        in blocks to go out sooner, and\n                                        positive number results in blocks to go\n                                        out later\n                                        \n  --max-scheduled-transaction-time-per-block-ms arg (=100)\n                                        Maximum wall-clock time, in\n                                        milliseconds, spent retiring scheduled\n                                        transactions in any block before\n                                        returning to normal transaction\n                                        processing.\n  --incoming-defer-ratio arg (=1)       ratio between incoming transations and\n                                        deferred transactions when both are\n                                        exhausted\n  --producer-threads arg (=2)           Number of worker threads in producer\n                                        thread pool\n  --snapshots-dir arg (=\"snapshots\")    the location of the snapshots directory\n                                        (absolute path or relative to\n                                        application data dir)",
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
      "code": "# config.ini\nplugin = producer_plugin\n\n# nodeos startup params\n--plugin producer_plugin",
      "language": "text"
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
      "code": "# config.ini\nplugin = eosio::chain_plugin\n\n# nodeos startup params\n--plugin eosio::chain_plugin\n",
      "language": "shell"
    }
  ]
}
[/block]