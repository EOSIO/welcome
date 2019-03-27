---
title: "Configuration"
excerpt: ""
---
`nodeos` can be configured using either the command line interface (CLI) options or a configuration file, `config.ini`. All the CLI options can be found by running `$ nodeos --help`.

Each CLI option maps to a setting in `config.ini`, for example `--plugin eosio::chain_api_plugin` can be set by adding `plugin = eosio::chain_api_plugin` to `config.ini`.

A custom `config.ini` file can be used by executing `$ nodeos --config path/to/config.ini`.
[block:api-header]
{
  "title": "Configuration File Location"
}
[/block]
`config.ini` can be found at the following locations:
- Mac OS: `~/Library/Application Support/eosio/nodeos/config`
- Linux: `~/.local/share/eosio/nodeos/config`
[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "Application Config Options:\n  --plugin arg                          Plugin(s) to enable, may be specified\n                                        multiple times\n\nApplication Command Line Options:\n  -h [ --help ]                         Print this help message and exit.\n  -v [ --version ]                      Print version information.\n  --print-default-config                Print default configuration template\n  -d [ --data-dir ] arg                 Directory containing program runtime\n                                        data\n  --config-dir arg                      Directory containing configuration\n                                        files such as config.ini\n  -c [ --config ] arg (=config.ini)     Configuration file name relative to\n                                        config-dir\n  -l [ --logconf ] arg (=logging.json)  Logging configuration file name/path\n                                        for library users",
      "language": "text"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "Note",
  "body": "EOSIO Plugins often add additional configuration parameters. You can get a full list of arguments available on your install by typing `nodeos -h` ... The output will be dependent on the plugins you have loaded."
}
[/block]