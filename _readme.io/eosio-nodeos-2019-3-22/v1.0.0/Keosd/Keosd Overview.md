---
title: "Keosd Overview"
excerpt: ""
---
The program `keosd`, located in the `eos/build/programs/keosd` folder within the EOSIO/eos repository, can be used to store private keys that cleos will use to sign transactions sent to the block chain. `keosd` runs on your local machine and stores your private keys locally.

For most users the easiest way to use keosd is to have cleos launch it automatically. Wallet files (named `foo.wallet` for example) will also be created in this directory by default.

## Auto locking

By default keosd is set to auto lock your wallets after 15 minutes of inactivity. This is configurable in the `config.ini`. Be aware if you need to disable this feature you will have to set an enormous number -- setting it to 0 will cause keosd to always lock your wallet.

## Launching keosd manually

It is possible to launch `keosd` manually simply with

```
$ keosd 
```

By default, `keosd` creates the folder `~/eosio-wallet` and populates it with a basic `config.ini` file.  The location of the config file can be specified on the command line using the `--config-dir` argument.  The configuration file contains the http server endpoint for incoming http connections and other parameters for cross origin resource sharing. Be aware that if you allowed cleos to auto launch keosd, a config.ini will be generated that will be sightly different than if you had launched keosd manually.

The location of the wallet data folder can be specified on the command line using the --data-dir argument.

## Stopping keosd

The most effective way to stop `keosd` is to find the keosd process and send a SIGTERM signal to it.  Note that because `cleos` auto-launches `keosd`, it is possible to end up with multiple instances of the `keosd` running.  The following will find and terminate all instances.
```
$ pgrep keosd
3178
24991
$ pkill keosd
```

## Other options

For a full list of possible options you can run `keosd --help`:
[block:code]
{
  "codes": [
    {
      "code": "$ keosd --help\nApplication Options:\n\nConfig Options for eosio::http_plugin:\n  --http-server-address arg (=127.0.0.1:8888)\n                                        The local IP and port to listen for\n                                        incoming http connections; set blank to\n                                        disable.\n  --https-server-address arg            The local IP and port to listen for\n                                        incoming https connections; leave blank\n                                        to disable.\n  --https-certificate-chain-file arg    Filename with the certificate chain to\n                                        present on https connections. PEM\n                                        format. Required for https.\n  --https-private-key-file arg          Filename with https private key in PEM\n                                        format. Required for https\n  --access-control-allow-origin arg     Specify the Access-Control-Allow-Origin\n                                        to be returned on each request.\n  --access-control-allow-headers arg    Specify the Access-Control-Allow-Header\n                                        s to be returned on each request.\n  --access-control-allow-credentials    Specify if Access-Control-Allow-Credent\n                                        ials: true should be returned on each\n                                        request.\n\nConfig Options for eosio::wallet_plugin:\n  --wallet-dir arg (=\".\")               The path of the wallet files (absolute\n                                        path or relative to application data\n                                        dir)\n  --unlock-timeout arg (=900)           Timeout for unlocked wallet in seconds\n                                        (default 900 (15 minutes)). Wallets\n                                        will automatically lock after specified\n                                        number of seconds of inactivity.\n                                        Activity is defined as any wallet\n                                        command e.g. list-wallets.\n  --eosio-key arg                       eosio key that will be imported\n                                        automatically when a wallet is created.\n\nApplication Config Options:\n  --plugin arg                          Plugin(s) to enable, may be specified\n                                        multiple times\n\nApplication Command Line Options:\n  -h [ --help ]                         Print this help message and exit.\n  -v [ --version ]                      Print version information.\n  --print-default-config                Print default configuration template\n  -d [ --data-dir ] arg                 Directory containing program runtime\n                                        data\n  --config-dir arg                      Directory containing configuration\n                                        files such as config.ini\n  -c [ --config ] arg (=config.ini)     Configuration file name relative to\n                                        config-dir\n  -l [ --logconf ] arg (=logging.json)  Logging configuration file name/path\n                                        for library users",
      "language": "text"
    }
  ]
}
[/block]