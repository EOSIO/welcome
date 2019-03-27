---
title: "http_client_plugin"
excerpt: ""
---
[block:api-header]
{
  "title": "Description"
}
[/block]
**http_client_plugin**  is an internal utility plugin, providing the producer_plugin the ability to securely use an external keosd instance as its' block signer. It can only be used when the producer plugin is configured to produce blocks.

[block:api-header]
{
  "title": "Options"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "  --https-client-root-cert arg          PEM encoded trusted root certificate \n                                        (or path to file containing one) used \n                                        to validate any TLS connections made.  \n                                        (may specify multiple times)\n                                        \n  --https-client-validate-peers arg (=1)\n                                        true: validate that the peer \n                                        certificates are valid and trusted, \n                                        false: ignore cert errors\n",
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
      "code": "# config.ini\nplugin = eosio::http_client_plugin\nhttps-client-root-cert = path/to/my/certificate.pem \nhttps-client-validate-peers = 1\n",
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