---
title: "Running Nodeos"
excerpt: ""
---
`Nodeos` can be run from the command line.  The behaviour of `nodeos` is determined by which plugins are used and the configuration options for each plugin. `Nodeos` itself has a few options, these allow you to set the data directory, where the blockchain data is stored, and point to configuration files for the plugins and for logging. 

For example:
[block:code]
{
  "codes": [
    {
      "code": "nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::state_history_plugin --data-dir /Users/mydir/eosio/data --config-dir /Users/mydir/eosio/config --access-control-allow-origin='*' --contracts-console --http-validate-host=false --state-history-dir /shpdata --trace-history --chain-state-history --verbose-http-errors --filter-on='*' --disable-replay-opts >> nodeos.log 2>&1 &",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Nodeos Configuration"
}
[/block]
`Nodeos` can be configured using either the command line interface (CLI) options or a configuration file, `config.ini`. All the CLI options can be found by running `$ nodeos --help`.

Each CLI option maps to a setting in `config.ini`, for example `--plugin eosio::chain_api_plugin` can be set by adding `plugin = eosio::chain_api_plugin` to `config.ini`.

A custom `config.ini` file can be used by executing `$ nodeos --config path/to/config.ini`.
[block:api-header]
{
  "title": "Configuration File Location"
}
[/block]
`config.ini` can be found in the following locations:
- Mac OS: `~/Library/Application Support/eosio/nodeos/config`
- Linux: `~/.local/share/eosio/nodeos/config`
[block:api-header]
{
  "title": "Nodeos Options"
}
[/block]
An example of the output from running  `$ nodeos --help` output is show below, the actual output will include options for plugins, though these have been excluded for clarity. 
[block:code]
{
  "codes": [
    {
      "code": "Application Options:\n\nApplication Config Options:\n  --plugin arg                          Plugin(s) to enable, may be specified \n                                        multiple times\n\nApplication Command Line Options:\n  -h [ --help ]                         Print this help message and exit.\n  -v [ --version ]                      Print version information.\n  --print-default-config                Print default configuration template\n  -d [ --data-dir ] arg                 Directory containing program runtime \n                                        data\n  --config-dir arg                      Directory containing configuration \n                                        files such as config.ini\n  -c [ --config ] arg (=config.ini)     Configuration file name relative to \n                                        config-dir\n  -l [ --logconf ] arg (=logging.json)  Logging configuration file name/path \n                                        for library users",
      "language": "text"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Plugins Options"
}
[/block]
For details on options for each plugin please see the documentation for each plugin:

[bnet_plugin](doc:bnet_plugin) 
[chain_plugin](doc:chain_plugin)
[history_plugin](doc:history_plugin) 
[http_client_plugin](doc:http_client_plugin)
[http_plugin](doc:http_plugin) 
[login_plugin](doc:login_plugin)
[mongo_db_plugin](doc:mongo_db_plugin)
[net_plugin](doc:net_plugin)
[producer_plugin](doc:producer_plugin)
[state_history_plugin](doc:state_history_plugin)
[txn_test_gen_plugin](doc:txn_test_gen_plugin)