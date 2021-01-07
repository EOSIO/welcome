---
content_title: "Hello World Contract"
link_text: "Hello World Contract"
---
This tutorial introduces the concept of smart contracts; building smart contracts; deploying smart contracts to a blockchain and then uses `cleos` to call smart contract actions. 

## Create the Contract

Create a new directory called **hello** in the **contracts** directory you previously created and enter the newly created directory.:

```shell
cd CONTRACTS_DIR
mkdir hello
cd hello
```

Create a new file, **hello.cpp**, and open it in your preferred text editor:

```shell
touch hello.cpp
```

Below the `eosio.hpp` header file is included. The `eosio.hpp` file includes a few classes required to write a smart contract.

```cpp
#include <eosio/eosio.hpp>
```

Using the `eosio` namespace will reduce clutter in your code. For example, by setting `using namespace eosio;`, `eosio::print("foo")` can be written `print("foo")`

```cpp
using namespace eosio;
```

Create a standard C++11 class. The contract class needs to extend `eosio::contract` class which is included earlier from the eosio.hpp header:

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract]] hello : public contract {};
```

An empty contract is not enough. Add a public access specifier and a using-declaration. The `using` declaration will allow us to write more concise code:

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract]] hello : public contract {
  public:
    using contract::contract;
};
```

This contract needs to do something. In the spirit of **hello world** write an action that accepts a "name" parameter, and then prints that parameter out:

<!--Links to virtual directory created by glossary generator-->
[Actions](../../glossary/index/#action) implement the behavior of a contract

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract]] hello : public contract {
  public:
      using contract::contract;

      void hi( name user ) {
         print( "Hello, ", user);
      }
};
```

The above action accepts a parameter called `user`, that's a [`name`](https://developers.eos.io/manuals/eosio.cdt/latest/structeosio_1_1name) type. EOSIO comes with a number of typedefs, one of the most common typedefs you'll encounter is `name`. Using the `eosio::print` library previously included, concatenate a string and print the `user` parameter. Use the braced initialization of `name{user}` to make the `user` parameter printable.

As is, the [ABI](../../glossary/index/#application-binary-interface) <!-- (hiding for now) <<glossary:ABI>> (unhide after tooltip feature implemented) --> generator in `eosio.cdt` won't know about the `hi()` action without an attribute. Add a C++11 style attribute above the action, this way the abi generator can produce more reliable output:

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract]] hello : public contract {
  public:
      using contract::contract;

      [[eosio::action]]
      void hi( name user ) {
         print( "Hello, ", user);
      }
};
```

Everything together, here's the completed hello world contract:

```cpp
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract]] hello : public contract {
  public:
      using contract::contract;

      [[eosio::action]]
      void hi( name user ) {
         print( "Hello, ", user);
      }
};
```

## Compile the Contract

[[info]]
| The ABI Generator in eosio.cdt supports several different style of attributes, see the ABI usage guide [here](./30_understanding-ABI-files.md).

Compile your code to web assembly (.wasm) as follows:

```shell
eosio-cpp hello.cpp -o hello.wasm
```

## Deploy the Contract

When you deploy a contract, it is deployed to an account, and the account becomes the interface for the contract. As mentioned earlier these tutorials use the same public key for all of the accounts to keep things simple.

View the wallet keys by:

```shell
cleos wallet keys
```

Create an account for the contract using [cleos create account](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/create/account):

```shell
cleos create account eosio hello YOUR_PUBLIC_KEY -p eosio@active
```

Deploy the compiled `wasm` to the blockchain with [cleos set contract](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/set/set-contract).

<div class="no-contracts-helper">In previous steps you should have created a `contracts` directory and obtained the absolute path and then saved it into a cookie. Replace "CONTRACTS_DIR" in the command below with the absolute path to your `contracts` directory.</div>

```shell
cleos set contract hello CONTRACTS_DIR/hello -p hello@active
```

[[info | Get an error?]]
| Check if your wallet needs to be unlocked.

## Execute the Contract

Great! Now the contract is set. Push an action to it.

```shell
cleos push action hello hi '["bob"]' -p bob@active
```

```shell
executed transaction: 4c10c1426c16b1656e802f3302677594731b380b18a44851d38e8b5275072857  244 bytes  1000 cycles
#    hello.code <= hello.code::hi               {"user":"bob"}
>> Hello, bob
```

As written, the contract will allow any account to say **hi** to any user:

```shell
cleos push action hello hi '["bob"]' -p alice@active

```

```shell
executed transaction: 28d92256c8ffd8b0255be324e4596b7c745f50f85722d0c4400471bc184b9a16  244 bytes  1000 cycles
#    hello.code <= hello.code::hi               {"user":"bob"}
>> Hello, bob
```

As expected, the console output is **Hello, bob**

In this case "alice" is the one who authorized it and `user` is just an argument. Modify the contract so that the authorizing user, "alice" in this case, must be the same as the user the contract is responding "hi" to. Use the `require_auth` method. This method takes a `name` as a parameter, and will check if the user executing the action matches the provided parameter.

```cpp
void hi( name user ) {
   require_auth( user );
   print( "Hello, ", name{user} );
}
```

Recompile the contract

```shell
eosio-cpp -abigen -o hello.wasm hello.cpp

```

And then update it

```shell
cleos set contract hello CONTRACTS_DIR/hello -p hello@active
```

Try to execute the action again, but this time with mismatched authorization.

```shell
cleos push action hello hi '["bob"]' -p alice@active
```

As expected, `require_auth` halted the transaction and threw an error.

```shell
Error 3090004: Missing required authority
Ensure that you have the related authority inside your transaction!;
If you are currently using 'cleos push action' command, try to add the relevant authority using -p option.
```

Now, with our change, the contract verifies the provided `name user` is the same as the authorising user. Try it again, but this time, with the authority of the "alice" account.

```shell
cleos push action hello hi '["alice"]' -p alice@active
```

```shell
executed transaction: 235bd766c2097f4a698cfb948eb2e709532df8d18458b92c9c6aae74ed8e4518  244 bytes  1000 cycles
#    hello <= hello::hi               {"user":"alice"}
>> Hello, alice
```

## What's Next

- [Deploy, Issue and Transfer Tokens](./20_deploy-issue-and-transfer-tokens.md): Learn how to deploy, issue and transfer tokens.
