---
title: "http_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
The **http_plugin** is a core plugin required to enable any RPC API on an EOSIO node. 
[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": " --http-server-address arg (=127.0.0.1:8888)\n                                        The local IP and port to listen for\n                                        incoming http connections; set blank to\n                                        disable.\n  --https-server-address arg            The local IP and port to listen for\n                                        incoming https connections; leave blank\n                                        to disable.\n  --https-certificate-chain-file arg    Filename with the certificate chain to\n                                        present on https connections. PEM\n                                        format. Required for https.\n  --https-private-key-file arg          Filename with https private key in PEM\n                                        format. Required for https\n  --access-control-allow-origin arg     Specify the Access-Control-Allow-Origin\n                                        to be returned on each request.\n  --access-control-allow-headers arg    Specify the Access-Control-Allow-Header\n                                        s to be returned on each request.\n  --access-control-max-age arg          Specify the Access-Control-Max-Age to\n                                        be returned on each request.\n  --access-control-allow-credentials    Specify if Access-Control-Allow-Credent\n                                        ials: true should be returned on each\n                                        request.\n  --max-body-size arg (=1048576)        The maximum body size in bytes allowed\n                                        for incoming RPC requests\n  --verbose-http-errors                 Append the error log to HTTP responses\n  --http-validate-host arg (=1)         If set to false, then any incoming\n                                        \"Host\" header is considered valid\n  --http-alias arg                      Additionaly acceptable values for the\n                                        \"Host\" header of incoming HTTP\n                                        requests, can be specified multiple\n                                        times.  Includes http/s_server_address\n                                        by default.",
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
      "code": "# config.ini\nplugin = eosio::http_plugin\n\n# nodeos startup params\n--plugin eosio::http_plugin",
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
None