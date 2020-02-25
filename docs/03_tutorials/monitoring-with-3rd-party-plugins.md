
[block:callout]
{
  "type": "warning",
  "body": "The resources listed below are developed, offered, and maintained by third-parties and not by block.one. Providing information, material, or commentaries about such third-party resources does not mean we endorse or recommend any of these resources. We are not responsible, and disclaim any responsibility or liability, for your use of or reliance on any of these resources. Third-party resources may be updated, changed or terminated at any time, so the information below may be out of date or inaccurate. USAGE AND RELIANCE IS ENTIRELY AT YOUR OWN RISK."
}
[/block]
In part I, [How to monitor state](doc:how-to-monitor-state), we discussed the states of a transaction.

In part II, [Monitoring with State History Plugin](doc:monitoring-with-state-history), we discussed monitoring state using the state history plugin.

In this article, we will take a brief look at some of the 3rd party options which are available for monitoring the state of the blockchain. There may be other solutions for monitoring state not present in this document, so please research what is currently the best option for you.   

This information here is extractd from the [Community Plugin List](https://github.com/EOSIO/eos/blob/master/plugins/COMMUNITY.md) page. These are plugins developed by the community, in no particular order, which can be added to Nodeos by compiling Nodeos with those plugins included. In this article, we only show the plugins related to monitoring transactions.

| Description | URL |
| ----------- | --- |
| ElasticSearch | https://github.com/EOSLaoMao/elasticsearch_plugin |
| Kafka | https://github.com/TP-Lab/kafka_plugin |
| Eosio MySQLdb Plugin | https://github.com/eosBLACK/eosio_mysqldb_plugin |
| SQL | https://github.com/asiniscalchi/eosio_sql_plugin |
| EOSIO Watcher - Watch for specific actions and send them to an HTTP URL | https://github.com/eosauthority/eosio-watcher-plugin |
| ZMQ / history | https://github.com/cc32d9/eos_zmq_plugin |
| ZMQ Light History API | https://github.com/cc32d9/eos_zmq_light_api |
| Mongo History API | https://github.com/CryptoLions/EOS-mongo-history-API |
| Chintai ZMQ Watcher | https://github.com/acoutts/chintai-zeromq-watcher-plugin |
| State History API | https://github.com/acoutts/EOS-state-history-API |
| Chronicle |  https://github.com/EOSChronicleProject/eos-chronicle |
| Hyperion History  |  https://github.com/eosrio/Hyperion-History-API |
| eos zmq plugin receiver |  https://github.com/cc32d9/eos_zmq_plugin_receiver |
| dfuse (commercial) |  https://www.dfuse.io/en/technology |
[block:callout]
{
  "type": "warning",
  "body": "These are in no particular order. Descriptions of each tool have been provided by the tool authors."
}
[/block]

[block:api-header]
{
  "title": "Elastic Search Plugin"
}
[/block]
The Elasticsearch plugin is a nodeos plugin for archiving blockchain data into Elasticsearch. It is designed to transfer nodeos data structures to JSON documents, and to post these documents to an  Elasticsearch cluster using bulk requests. It speeds up the processing progress by using a thread pool to handle the serialization and the bulk request jobs.

For more information, see the [Elastic Search Plugin](https://github.com/EOSLaoMao/elasticsearch_plugin) page on Github.

[block:api-header]
{
  "title": "Kafka Plugin"
}
[/block]
The EOSIO Kafka Plugin is used to receive the transaction data from the blockchain and to send out the transaction through a kafka producer. Developers can receive the transaction data through a kafka consumer in the back-end application.

For more information, see the [Kafka Plugin](https://github.com/TP-Lab/kafka_plugin) page on Github. 

[block:api-header]
{
  "title": "EOSIO MySQLdb Plugin"
}
[/block]
The mysqldb_plugin is a plug-in to store block, transaction and action data in a MySQL database.

For more information, see the [EOSIO MySQL Plugin](https://github.com/eosBLACK/eosio_mysqldb_plugin) page on Github. 


[block:api-header]
{
  "title": "SQL Plugin"
}
[/block]
For more information, see the [SQL Plugin](https://github.com/asiniscalchi/eosio_sql_plugin) page on Github. 



[block:api-header]
{
  "title": "EOSIO Watcher Plugin"
}
[/block]
The EOSIO Watcher plugin is a simple plugin to watch for specific actions on chain and send them as HTTP POSTs to a url in real-time.

For more information, see the [EOSIO Watcher Plugin](https://github.com/eosauthority/eosio-watcher-plugin) page on Github. 


[block:api-header]
{
  "title": "ZMQ Plugin"
}
[/block]
The ZMQ / history plugin collects EOS action traces, converting them into JSON format, and exporting them via a ZeroMQ socket. It may export all action traces, or only those relevant to a number of whitelisted accounts. A receiver for this data can be implemented in any modern programming language that supports the ZeroMQ library.

For more information, see the [ZMQ Plugin](https://github.com/cc32d9/eos_zmq_plugin) page on Github.

[block:api-header]
{
  "title": "ZMQ Light History API"
}
[/block]
The ZMQ Light History API receives data from the `nodeos`  ZMQ / history plugin. This stores the latest state of each account and account token balances. It is called **Light** because it does not store historic data. 


For more information, see the [ZMQ Light History API](https://github.com/cc32d9/eosio_light_api) page on Github.
 
 
[block:api-header]
{
  "title": "Chintai ZMQ Watcher Plugin"
}
[/block]
The Chintai ZMQ Watcher plugin is designed to allow a blockchain application developer to easily monitor actions from the blockchain. It is originally forked from EOSIO Watcher, but modified to use ZeroMQ instead of HTTP requests, as using ZMQ guarantees ordering. When building a blockchain application that requires an exact ordering of block events and a guarantee that no blocks will be (easily) lost during a replay, a message queue like ZeroMQ is a great solution.
 
- While this plugin does allow for the monitoring of on-chain events, it does not include a ZeroMQ receiver component which would receive the events from the plugin. The receiver is generally proprietary to the specific implementation of your blockchain application's web backend, however, there are ZeroMQ libraries available for most programming languages. This plugin puts blockchain events onto a ZeroMQ messaging queue, and any language using the ZeroMQ library can connect to the queue and process events from it. 
- This plugin listens to head block signals and is therefore subject to periodic microforks in the network. The handling of these forks must be done in your ZMQ receiver component. If you prefer, you can modify the plugin to use irreversible blocks, however, there would be a 2-3 minute delay in receiving transactions. 
- The plugin is currently setup to filter on actions specific to the Chintai smart contract. The filtering function should be updated to your dApps's specific implementation. 

For more information, see the [Chintai ZMQ Watcher Plugin](https://github.com/acoutts/chintai-zeromq-watcher-plugin) page on Github.
[block:api-header]
{
  "title": "State History API"
}
[/block]
The State History API is intended as a public API interface which matches the history plugin api, but uses the data stored by the state history plugin in a Postgresql database, by using fill-postgresql, please see [Monitoring with State History Plugin](doc:monitoring-with-state-history)

For more information, see the [State History API](https://github.com/acoutts/EOS-state-history-API) page on Github.
[block:api-header]
{
  "title": "Chronicle Project"
}
[/block]
The Chronicle project aims to build a toolset for EOSIO history databases. Currently, Chronicle Receiver is released, and this tool will read the data from the state history plugin, decoding it into JSON format, and exporting this JSON to downstream consumers. 

For more information, see the [Chronicle Project](https://github.com/EOSChronicleProject/eos-chronicle) page on Github.

[block:api-header]
{
  "title": "Hyperion History API"
}
[/block]
The Hyperion History API uses a multi-threaded indexer to extract data from the state history plugin, storing data in an Elasticsearch cluster. Optimizing the data structures used to store data has reduced the amount of storage required by up to 85%, and has meant lower response times when responding to queries whilst also reducing data transfer overhead.

Access to this data is provided by a javascript library, the Hyperion HTTP API, and next steps include implementing a WebSocket API for action streaming. 

For more information on **Hyperion History**, see the [Hyperion History](https://github.com/eosrio/Hyperion-History-API) page on Github.

For more information on the **Hyperion HTTP API Javascript library**, see the [Hyperion HTTP API](https://github.com/eoscafe/hyperion-api) page on Github.

For additional information, see this [Medium](https://medium.com/@eosriobrazil/presenting-hyperion-history-api-solution-f8a8fda5865b) article. 




[block:api-header]
{
  "title": "EOS ZMP plugin receiver"
}
[/block]
This is a set of tools written in Perl for receiving and processing the EOSIO network events exported by the ZMQ / history plugin (see above). They can be useful for dispatching and troubleshooting  message flow, and there is a ready-made solution for storing action data in MySQL database.

For more information, see the [EOS ZMQ Plugin](https://github.com/cc32d9/eos_zmq_plugin_receiver) page on Github.

[block:api-header]
{
  "title": "dfuse"
}
[/block]
dfuse offers powerful streaming APIs, GraphQL queries and subscriptions, server-side navigation of forks, and some of the deepest insight of on-chain data, like action-level database operations. dfuse also allows querying of the blockchain state (contract tables) at any past block height, providing a consistent view of tables even when they hold millions of rows. dfuse Search allows you to find transactions through the full blockchain history in under a second, with granular search criterias. dfuse Events allows you to index special fields directly from your smart contracts, making them available instantaneously through dfuse Search.

dfuse is a commercial offering by the team at EOS Canada. For product overview, see the [dfuse technology]
(https://www.dfuse.io/en/technology) page and for product documentation, see [dfuse API Documentation](https://docs.dfuse.io/).
