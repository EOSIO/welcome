Previously, we sent an external inline action in the addressbook contract. In this tutorial we’ll explore sending a deferred transaction, which will include the inline action we sent in the previous tutorial.
## Using deferred transaction to replace inline action
Open the `addressbook.cpp` file in your favorite editor and use the following code to replace the `increment_counter` function.

```cpp
  void increment_counter(name user, std::string type) {
    eosio::transaction deferred;
    
    deferred.actions.emplace_back(
      permission_level{get_self(),"active"_n},
      get_self(), "notify"_n, 
      std::make_tuple(user, type)
    );

    deferred.send(user.value, get_self());
  }
```
The code listing above does the following:

1. Initializes a transaction object.
2. Creates an action with the same parameters in the previous addressbook example.
3. Adds the action into the transaction.
4. Sends the transaction with two parameters. The first parameter is the sender id which will be useful in the later section of this tutorial. The second parameter is the account which will pay for the RAM costs associated with the deferred transaction. 
## Canceling a deferred transaction
To cancel a deferred transaction, call `cancel_deferred` with the sender id specified when the deferred transaction was created. In our case this is the name variable user's value.

See the example below:

```cpp
cancel_deferred(user.value);
```

## Executing the deferred transaction
To test if the deferred transaction invokes the notify action, run the below command: 

```shell
cleos push action addressbook upsert '["alice", "alice", "liddell", 19, "123 drink me way", "wonderland", "amsterdam"]' -p alice@active
```
Since the transaction was deferred, you will not see output related to the deferred transaction in the console, even though the `upsert` transaction was successfully invoked.

```text
executed transaction: f1143e224c9809aafb6e7274096521168ecfe1e21feb86ca2d4794c4a4929fd5  208 bytes  428 us
#   addressbook <= addressbook::upsert          {"user":"alice","first_name":"alice","last_name":"liddell","age":19,"street":"123 drink me way","cit...
warning: transaction executed locally, but may not be confirmed by the network yet         ]
```
Although you will not see the deferred transaction output in the console, you can check the nodeos logs to see if the transaction executed successfully. To check the nodeos logs, execute the following command:

```shell
tail -f nodeos.log
```

[[info]]
| The `nodeos.log` was created when you started the nodeos.


```shell
info  2019-04-08T12:52:34.000 thread-0  producer_plugin.cpp:1596      produce_block        ] Produced block 00081d73bfb74c06... #531827 @ 2019-04-08T12:52:34.000 signed by eosio [trxs: 0, lib: 531826, confirmed: 0]

info  2019-04-08T12:52:34.502 thread-0  producer_plugin.cpp:1596      produce_block        ] Produced block 00081d7447279fcf... #531828 @ 2019-04-08T12:52:34.500 signed by eosio [trxs: 1, lib: 531827, confirmed: 0]
info  2019-04-08T12:52:35.004 thread-0  producer_plugin.cpp:1596      produce_block        ] Produced block 00081d758add241e... #531829 @ 2019-04-08T12:52:35.000 signed by eosio [trxs: 1, lib: 531828, confirmed: 0]

info  2019-04-08T12:52:35.503 thread-0  producer_plugin.cpp:1596      produce_block        ] Produced block 00081d76113974b9... #531830 @ 2019-04-08T12:52:35.500 signed by eosio [trxs: 0, lib: 531829, confirmed: 0]

```
You can see the there are two transactions ( trxs ) executed consecutively. This means the deferred transaction was executed by nodeos.
## Err on the side of caution
When contract code raises an exception it can be handled with error handling code. You can define your own error handling code as follows:

```cpp
void onError() {
   print("onError is called");
}
```

With the following notify attribute:

```cpp
[[eosio::on_notify("eosio::onerror")]]
void onError() {
   print("onError is called");
}
```
Using the above onerror function you can handle various exceptions. This allows you to fail safely when necessary.

For more detail on how onerror works internally see [here](https://developers.eos.io/eosio-nodeos/v1.7.0/docs/communication-model)
## Nondeterministic
Because you can schedule a deferred transaction at a future point in time, the **execution of a deferred transaction is indeterministic**

It may be that no nodes on an EOSIO network ever attempt to execute a scheduled deferred transaction. Since all users of an EOSIO blockchain network can schedule a deferred transaction, the to-be-executed transactions can accumulate in a backlog. It is possible that the expiration time of a deferred transaction has been reached before a deferred transaction has been scheduled to execute.

Due to this behavior and other subjective reasons you should never design your application based the deterministic execution of a deferred transaction.

For more detail on how a deferred transaction works see [here](https://developers.eos.io/eosio-nodeos/v1.7.0/docs/communication-model)