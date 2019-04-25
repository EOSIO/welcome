---
title: "Monitoring with 3rd Party plugins"
excerpt: ""
---
[block:callout]
{
  "type": "warning",
  "body": "The resources listed below are developed, offered, and maintained by third-parties and not by block.one. Providing information, material, or commentaries about such third-party resources does not mean we endorse or recommend any of these resources. We are not responsible, and disclaim any responsibility or liability, for your use of or reliance on any of these resources. Third-party resources may be updated, changed or terminated at any time, so the information below may be out of date or inaccurate. USAGE AND RELIANCE IS ENTIRELY AT YOUR OWN RISK."
}
[/block]
In part I [How to monitor state](doc:how-to-monitor-state) we discussed the states of a transaction.

In part II [Monitoring with State History Plugin](doc:monitoring-with-state-history) we discussed monitoring state using the state history plugin.

In this article we will take a brief look at some of the 3rd party options which are available for monitoring the state of the blockchain. There may be other solutions for monitoring state not present in this document so please research what is currently the best option for you.   

This information comes from `https://github.com/EOSIO/eos/blob/master/plugins/COMMUNITY.md`. These are plugins developed by the community, in no particular order, which can be added to Nodeos by compiling Nodeos with those plugins included. In this article we only show the plugins related to monitoring transactions.

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
[block:callout]
{
  "type": "warning",
  "body": "These are in no particular order.\nDescriptions of each plugin have been provided by the plugin authors.",
  "title": ""
}
[/block]

[block:api-header]
{
  "title": "Elastic Search Plugin"
}
[/block]
The Elasticsearch plugin is a nodeos plugin for archiving blockchain data into Elasticsearch. It is designed to transfer nodeos data structures to json documents, and to post these documents to an  Elasticsearch cluster, using bulk requests. It speeds up the processing progress by using a thread pool to handle the serialisation and the bulk request jobs.

Please refer to https://github.com/EOSLaoMao/elasticsearch_plugin for more information.
[block:api-header]
{
  "title": "Kafka Plugin"
}
[/block]
EOSIO Kafka Plugin is used to receive the transaction data from the blockchain and to send out the transaction through a kafka producer. Developers can receive the transaction data through a kafka consumer in the back-end application.

Please refer to https://github.com/TP-Lab/kafka_plugin for more information.
[block:api-header]
{
  "title": "Eosio MySQLdb Plugin"
}
[/block]
The mysqldb_plugin is a plug-in to store block, transaction and action data in a MySQL database.

Please refer to https://github.com/eosBLACK/eosio_mysqldb_plugin for more information.
[block:api-header]
{
  "title": "SQL"
}
[/block]
Please refer to https://github.com/asiniscalchi/eosio_sql_plugin for more information.
[block:api-header]
{
  "title": "EOSIO Watcher"
}
[/block]
EOSIO Watcher plugin is a simple plugin to watch for specific actions on chain and send them as HTTP POSTs to a url in real-time.

Please refer to https://github.com/eosauthority/eosio-watcher-plugin for more information.
[block:api-header]
{
  "title": "ZMQ / history"
}
[/block]
The ZMQ / history plugin collects EOS action traces, converting them into JSON format, and exporting them via a ZeroMQ socket. It may export all action traces, or only those relevant to a number of whitelisted accounts. A receiver for this data can be implemented in any modern programming language that supports the ZeroMQ library.

Please refer to https://github.com/cc32d9/eos_zmq_plugin for more information.
[block:api-header]
{
  "title": "ZMQ Light History API"
}
[/block]
The ZMQ Light History API receives data from the `nodeos`  ZMQ / history plugin. This stores the latest state of each account and account token balances. It is called Light because does not store historic data. 

Please refer to https://github.com/cc32d9/eos_zmq_light_api for more information.

[block:api-header]
{
  "title": "Mongo History API"
}
[/block]
The Mongo History API Plugin was developed as a gateway to the MongoDB Plugin which may be used in place of the history plugin and state history plugin.  The API requests are the same, however, there are some additional API requests.

 Please refer to https://github.com/CryptoLions/EOS-mongo-history-API for more information and to  https://history.cryptolions.io/ for documentation.
[block:api-header]
{
  "title": "Chintai ZMQ Watcher Plugin"
}
[/block]
This plugin is designed to allow a blockchain application developer to easily monitor actions from the blockchain. It is originally forked from EOSIO Watcher but modified to use ZeroMQ instead of HTTP requests, as using ZMQ guarantees ordering. When building a blockchain application that requires an exact ordering of block events and a guarantee that no blocks will be (easily) lost during a replay, a message queue like ZeroMQ is a great solution.
 
- While this plugin does allow for the monitoring of on-chain events, it does not include a ZeroMQ receiver component which would receive the events from the plugin. The receiver is generally proprietary to the specific implementation of your blockchain application's web backend, however, there are ZeroMQ libraries available for most programming languages. This plugin puts blockchain events onto a ZeroMQ messaging queue, and any language using the ZeroMQ library can connect to the queue and process events from it. 
- This plugin listens to head block signals and is therefore subject to periodic microforks in the network. The handling of these forks must be done in your ZMQ receiver component. If you prefer, you can modify the plugin to use irreversible blocks, however, there would be a 2-3 minute delay in receiving transactions. 
- The plugin is currently setup to filter on actions specific to the Chintai smart contract. The filtering function should be updated to your dApps's specific implementation. 

Please refer to https://github.com/acoutts/chintai-zeromq-watcher-plugin for more information
[block:api-header]
{
  "title": "State History API"
}
[/block]
The State History API is intended as a public API interface which matches the history plugin api, but uses the data stored by the state history plugin in a Postgresql database, by using fill-postgresql, please see [Monitoring with State History Plugin](doc:monitoring-with-state-history)

Please refer to https://github.com/acoutts/EOS-state-history-API for more information. 
[block:callout]
{
  "type": "warning",
  "body": "These are in no particular order.\nDescriptions of each tool have been provided by the tool authors."
}
[/block]

[block:api-header]
{
  "title": "Additional Monitoring Tools"
}
[/block]
In addition to the plugins discussed above these are some other tools that are available for monitoring transactions on the blockchain:

| Description | URL |
| ----------- | --- |
| Chronicle |  https://github.com/EOSChronicleProject/eos-chronicle |
| eos zmq plugin receiver |  https://github.com/cc32d9/eos_zmq_plugin_receiver |
| Hyperion History  |  https://github.com/eosrio/Hyperion-History-API |
| dfuse |  https://www.dfuse.io/en/technology |
[block:api-header]
{
  "title": "Chronicle"
}
[/block]
The chronicle project aims to build a toolset for EOSIO history databases. Currently Chronicle Receiver is released, and this tool will read the data from the state history plugin, decoding it into JSON format, and exporting this json to downstream consumers. 

Please refer to https://github.com/EOSChronicleProject/eos-chronicle for more information.
[block:api-header]
{
  "title": "eos zmq plugin receiver"
}
[/block]
This is a set of tools written in Perl for receiving and processing the EOSIO network events exported by the ZMQ / history plugin (see above). They can be useful for dispatching and troubleshooting  message flow, and there is a ready-made solution for storing action data in MySQL database.

Please refer to https://github.com/cc32d9/eos_zmq_plugin_receiver for more information.
[block:api-header]
{
  "title": "Hyperion History"
}
[/block]
Hyperion History uses a multi-threaded indexer to extract data from the state history plugin, storing data in an Elasticsearch cluster. Optimising the data structures used to store data has reduced the amount of storage required by up to 85%, and has meant lower response times when responding to queries whilst also reducing data transfer overhead.

Access to this data is provided by a javascript library, the Hyperion HTTP API, and next steps include implementing a WebSocket API for action streaming. 

Please refer to https://medium.com/@eosriobrazil/presenting-hyperion-history-api-solution-f8a8fda5865b for more information. 
The source code can be located here https://github.com/eosrio/Hyperion-History-API 
For more information about the Hyperion HTTP API  Javascript library please refer to https://eos.hyperion.eosrio.io/v2/docs/index.html and the source code for this library can be found here https://github.com/eoscafe/hyperion-api
[block:api-header]
{
  "title": "dfuse"
}
[/block]
dfuse will cache blockchain data and then serve this data to users via WebSocket and REST API. This allows a developer to access data and send transactions to the blockchain. dfuse is split into three modules: 
 - `Stream` provides real-time updates reflecting the state of any table on the blockchain
 - `Lifecycle` allows a developer to submit transactions to the blockchain.
 - `Search` allows you to search the entire transaction history of the blockchain using a simple but powerful query language.

dfuse is closed source, for an overview of dfuse go to https://www.dfuse.io/en/technology , for the product documentation go to https://docs.dfuse.io/#introduction