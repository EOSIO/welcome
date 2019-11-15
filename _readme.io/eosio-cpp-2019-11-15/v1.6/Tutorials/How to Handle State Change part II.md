---
title: "How to Handle State Change part II"
excerpt: ""
---
## EOS-state-history-api - community

In addition to using the block.one provided State History Plugin, the community has built a number of alternative solutions, some details of these are listed below.

### Kafka Plugin  - community

Kafka is a distributed streaming platform:

A streaming platform has three key capabilities:

  * Publish and subscribe to streams of records, similar to a message queue or enterprise messaging system.
  * Store streams of records in a fault-tolerant durable way.
  * Process streams of records as they occur.

Kafka is generally used for two broad classes of applications:

  * Building real-time streaming data pipelines that reliably get data between systems or applications
  * Building real-time streaming applications that transform or react to the streams of data

The plugin will place EOSIO data on topics which can them be accessed by your application.

https://github.com/TP-Lab/kafka_plugin


### ZMQ Plugin  - community

This plugin is doing approximately the same as history_plugin, but instead of storing history events in the shared memory database, it pushes them outside of nodeos process via ZeroMQ PUSH socket.

If wildcard filter is enabled for history_plugin, all account history is stored in the same shared memory segment as the blockchain state database. This leads to its rapid growth, up to 2GB per day, and increased risk of node crash because of exceeded memory or disk space. The ZMQ plugin allows processing and storing the history events elsewhere, such as RDBMS with truncation or archiving of old entries.

The PUSH type of socket is blocking, so if nobody is pulling from it, nodeos will wait forever. This is done in order to prevent skipping any action events in the blockchain. The receiver may also route the events to non-blocking types of sockets, such as PUB socket, in order to let other systems listen to events on the go.

https://github.com/cc32d9/eos_zmq_plugin

### ZMQ Light History API - community

The API is providing two fundamental functions for EOS blockchain:

  * Retrieve all token balances and resources for an account: http://apihost.domain/api/account/eos/ACCOUNT
  * Retrieve all accounts in all known EOS networks dependent on a public key: http://apihost.domain/api/key/KEY

In addition, adding ?pretty=1 to the URL, you get the resulting JSON sorted and formatted for human viewing.

http://apihost.domain/api/networks lists all known networks and their information.

http://apihost.domain/api/sync/eos returns a plain text delay in seconds that this server's blockchain database is behind the real time, and a status: OK if the delay is within 180 seconds, or 'OUT_OF_SYNC' otherwise.

http://apihost.domain/api/tokenbalance/eos/ACCOUNT/CONTRACT/TOKEN returns a plain text with numeric output indicating the token balance. Zero is returned if the token is not present or does not exist.

https://github.com/cc32d9/eos_zmq_light_api

### Others 
#### MongoDb
##### EOS Mongo History API - community
#### ElasticSearch  - community
#### MySQL  - community
#### SQL  - community
#### Dfuse - community