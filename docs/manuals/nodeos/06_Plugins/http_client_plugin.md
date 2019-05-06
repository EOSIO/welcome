---
title: "http_client_plugin"
excerpt: ""
---
## Description
**http_client_plugin**  is an internal utility plugin, providing the producer_plugin the ability to securely use an external keosd instance as its' block signer. It can only be used when the producer plugin is configured to produce blocks.

## Options


```shell
  --https-client-root-cert arg          PEM encoded trusted root certificate 
                                        (or path to file containing one) used 
                                        to validate any TLS connections made.  
                                        (may specify multiple times)
                                        
  --https-client-validate-peers arg (=1)
                                        true: validate that the peer 
                                        certificates are valid and trusted, 
                                        false: ignore cert errors

```

## Usage


```text
# config.ini
plugin = eosio::http_client_plugin
https-client-root-cert = path/to/my/certificate.pem 
https-client-validate-peers = 1

```

## Dependencies
