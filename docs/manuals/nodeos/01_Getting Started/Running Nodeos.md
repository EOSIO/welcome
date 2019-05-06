`Nodeos` can be run from the command line.  The behaviour of `nodeos` is determined by which plugins are used and the configuration options for each plugin. `Nodeos` itself has a few options, these allow you to set the data directory, where the blockchain data is stored, and point to configuration files for the plugins and for logging. 

For example:

```shell
nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::state_history_plugin --data-dir /Users/mydir/eosio/data --config-dir /Users/mydir/eosio/config --access-control-allow-origin='*' --contracts-console --http-validate-host=false --state-history-dir /shpdata --trace-history --chain-state-history --verbose-http-errors --filter-on='*' --disable-replay-opts >> nodeos.log 2>&1 &
```

## Nodeos Configuration
`Nodeos` can be configured using either the command line interface (CLI) options or a configuration file, `config.ini`. All the CLI options can be found by running `$ nodeos --help`.

Each CLI option maps to a setting in `config.ini`, for example `--plugin eosio::chain_api_plugin` can be set by adding `plugin = eosio::chain_api_plugin` to `config.ini`.

A custom `config.ini` file can be used by executing `$ nodeos --config path/to/config.ini`.
## Configuration File Location
`config.ini` can be found in the following locations:
- Mac OS: `~/Library/Application Support/eosio/nodeos/config`
- Linux: `~/.local/share/eosio/nodeos/config`
## Nodeos Options
An example of the output from running  `$ nodeos --help` output is show below, the actual output will include options for plugins, though these have been excluded for clarity.

```text
Application Options:

Application Config Options:
  --plugin arg                          Plugin(s) to enable, may be specified
                                        multiple times

Application Command Line Options:
  -h [ --help ]                         Print this help message and exit.
  -v [ --version ]                      Print version information.
  --print-default-config                Print default configuration template
  -d [ --data-dir ] arg                 Directory containing program runtime
                                        data
  --config-dir arg                      Directory containing configuration
                                        files such as config.ini
  -c [ --config ] arg (=config.ini)     Configuration file name relative to
                                        config-dir
  -l [ --logconf ] arg (=logging.json)  Logging configuration file name/path
                                        for library users
```

## Plugins Options
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
