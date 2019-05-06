[[info]]
|
This article assumes you have [Nodeos installed somewhere](doc:install-nodeos)

## Non-Producing Node
A non-producing node is a node that is not configured to produce blocks. An example use case would be to provide a synchronized node that provides a public HTTP-RPC API for developers or as a dedicated private endpoint for your app.

To setup a non-producing node is simple.
## Set Peers
You need to set some peers in your config ini, for example

```text
p2p-peer-address = 106.10.42.238:9876
```
Or you can include the peer in as a boot flag, like so

```text
--p2p-peer-address=106.10.42.238:9876
```
