[[info]]
|
These instructions assume you are attempting to launch a producing node on a network with **system contracts loaded.** These instructions will not work on a default development node using native functionality, or one without system contracts loaded.

## Register your account as a producer
In order for your account to be eligible as a producer, you will need to register the account as a producer

## Example using `cleos system regproducer`


```shell
cleos system regproducer accountname1 EOS1234534... http://producer.site Antarctica
```

## Set Producer Name
Set the `producer-name` option in config.ini to your account, like so

```text
# ID of producer controlled by this node (e.g. inita; may specify multiple times) (eosio::producer_plugin)
producer-name = youraccount
```

## Set the Producer's signature-provider
You will need to set the private key for your producer. The public key should have an authority for the producer account defined above.

`signature-provider` is defined with a tuple
-  `public-key` - A valid EOSIO public key in form of a string.
- `provider-spec` - It's a string formatted like <provider-type>:<data>
- `provider-type` - KEY or KEOSD

## Using a Key

```text
signature-provider = PUBLIC_SIGNING_KEY=KEY:PRIVATE_SIGNING_KEY

//Example
//signature-provider = EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV=KEY:5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3

```
## Using Keosd
You can also use Keosd instead of hard-defining keys.

```text
signature-provider = KEOSD:<data>   

//Example
//EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV=KEOSD:https://127.0.0.1:88888
```

## Define a peers list


```text
# Default p2p port is 9876
p2p-peer-address = 123.255.78.9:9876
```

## Load the Required Plugins
In your [config.ini](doc:configuration-file), confirm the following plugins are loading or append them if necessary.

```text
plugin = eosio::chain_plugin
plugin = eosio::producer_plugin
```
