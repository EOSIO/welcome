---
content_title: "Hello World Contract"
link_text: "Build and Deploy Hello World Smart Contract"
---

You deploy and execute smart contracts on the blockchain. A record of each transaction is immutably stored on the blockchain and smart contracts store and update state on the blockchain. A blockchain application is composed of clients, which utilize EOSIO client libraries, and call smart contract actions, which execute on the blockchain.    

Let's start with a simple smart contract that produces the traditional **_Hello World_**. 

This tutorial introduces the following key concepts:
* [EOSIO Contract Development Toolkit](https://developers.eos.io/manuals/eosio.cdt/latest/index): The toolchain and libraries used to build smart contracts
* [Webassembly](../glossary/index#webassembly) (WASM): The virtual machine used to execute a portable binary-code format, hosted in [nodeos](../glossary/index#nodeos)
* [Application Binary Interfaces](https://developers.eos.io/manuals/eosio.cdt/latest/best-practices/abi/understanding-abi-files) (ABI): The interface that defines how data is marshalled to and from the webassembly virtual machine
* [Smart Contracts](../glossary/index/#smart-contract): The code that defines actions and transactions which may be executed on a blockchain

**This tutorial shows how to**:
* Create a simple smart contract with a `hi` [action](../glossary/index/#action) to the smart contract
* Compile and deploy the smart contract to an EOSIO blockchain
* Use the command line to call the `hi` action of the smart contract

## Before you Begin
This tutorial requires the following:
* Knowledge of the C++ programming language
* A preferred code editor or an IDE
* A fully configured [local development environment](20_local-development-environment) 

Once you complete the tutorial, you should have a basic **_Hello World_** smart contract created and deployed.

## EOSIO Contract Development Toolkit

Create EOSIO smart contracts using the C++ programming language. The EOSIO Contract Development Toolkit or [EOSIO.CDT](../glossary/index/#eosio.cdt) provides the libraries and tools you can use to build a smart contract. See the [EOSIO.CDT](https://developers.eos.io/manuals/eosio.cdt/latest/index) manual for instructions on how to get started.

To deploy the smart contract to the blockchain, use the [eosio-cpp](https://developers.eos.io/manuals/eosio.cdt/v1.7/command-reference/eosio-cpp) tool to compile the smart contract. The compilation using the `eosio-cpp` tool builds the webassembly file and creates a corresponding application binary interface (ABI) file.

The webassembly or `.wasm` file is the binary code that the webassembly engine in the blockchain executes. The webassembly engine or wasm engine is the engine in the blockchain which executes smart contracts. The application binary interface or `.abi` file defines how data is marshalled to and from the wasm engine.

## Create the Contract

This section creates the Hello World smart contract. Normally, you create two files - the header  or `.hpp` file which contains the declarations for the smart contract class and the `.cpp` file, which contains the implementation of the smart contract actions. In this simple example, you only create a `.cpp` file.


### Procedure to create hello.cpp 

1. Create a new directory called **hello** to store your smart contract file:

```shell
mkdir hello
```
Go to the new  directory

```shell
cd hello
```

2. Create a new file, `hello.cpp`, and open it in your preferred text editor:

```shell
touch hello.cpp
```

3. Write the smart contract code:

Follow these four steps and add this code to the `hello.cpp` file.

a. Import the eosio base library with the include directive.
Add the line:

```cpp
#include <eosio/eosio.hpp>
```

b. The `eosio.hpp` contains classes required to write a smart contract, including `eosio::contract`. Create a standard C++11 class and inherit from the `eosio::contract` class. Use the `[[eosio::contract]]` attribute to inform the EOSIO.CDT compiler this is a smart contract. 

Add the line:

```cpp
class [[eosio::contract]] hello : public eosio::contract {};
```

The `EOSIO.CDT` compiler automatically generates the main dispatcher and the `ABI file`.
The [dispatcher](https://developers.eos.io/manuals/eosio.cdt/v1.7/group__dispatcher/?query=dispatcher&page=1#dispatcher) routes action calls to the correct smart contract action. The compiler will create one when using the `eosio::contract` attribute. Advanced programmers can customize this behaviour by defining their own dispatcher.

c. Add a public access specifier and a using-declaration to introduce base class members from `eosio::contract`. You can now use the default base class constructor.

Add these lines:

```cpp
public:
	using eosio::contract::contract;
```

d. Add a `hi` public action. This action accepts an `eosio::name` parameter, and prints **Hello** concatenated with the `eosio::name` parameter. 

Add these lines:

```cpp
	[[eosio::action]] void hi( eosio::name user ) {
		print( "Hello, ", user);
	}
```

The `[[eosio::action]]` attribute lets the compiler know this is an action.

The `hello.cpp` file should now look like this:

```cpp
#include <eosio/eosio.hpp>
class [[eosio::contract]] hello : public eosio::contract {
  public:
      using eosio::contract::contract;
      [[eosio::action]] void hi( eosio::name user ) {
         print( "Hello, ", user);
      }
};
```

`eosio::print` is included by eosio/eosio.hpp. The smart contract uses this function to print **Hello** and concatenate the `string` **Hello** with the passed in user.

4. Save the file.

## Compile and Deploy

Now that the smart contract is successfully created, follow this section to
compile and deploy the smart contract to the blockchain. Use the EOSIO.CDT [eosio-cpp](https://developers.eos.io/manuals/eosio.cdt/latest/command-reference/eosio-cpp) command to build the `.wasm` file and a corresponding `.abi` file. 

### Procedure to Compile and Deploy

1. Use the `eosio-cpp` command to compile the `hello.cpp` file.  Run the `eosio-cpp` command in the same folder as the hello.cpp file (or refer to the file with an absolute or relative path):

```shell
eosio-cpp -abigen -o hello.wasm hello.cpp
```

The eosio-cpp command creates two new files - `hello.wasm` and `hello.abi`.

2. Deploy the compiled `hello.wasm` and `hello.abi` files to a **hello** account on the blockchain. **If you do not have a "hello" account** see [accounts and permissions.](../40_smart-contract-guides/01_before-you-begin/20_accounts-and-permissions.md) Run the command outside the folder containing the `hello.wasm` and `hello.abi` and use the `contract-dir` positional to specify the path to the directory containing the `.wasm` and the `.abi`:

```shell
cleos set contract hello ./hello -p hello@active
```

[[info]]
| Check that your wallet is unlocked. The cleos command needs to be authorized by signing the transaction with the private key stored in the wallet. Cleos will look for an open and unlocked wallet containing the private key for the permission you used, in this case -p hello@active. Use `cleos set contract --help` to get commmand line help.  

## Calling a Smart Contract Action

Now that the smart contract is successfully deployed, follow this section to [push smart contract actions](https://developers.eos.io/manuals/eos/v2.0/cleos/command-reference/push/push-action) to the blockchain and test the `hi` action.

### Procedure to call the Hi Action

1. Use `cleos push action`:

```shell
cleos push action hello hi '["bob"]' -p bob@active
```

This should produce:

```console
executed transaction: 4c10c1426c16b1656e802f3302677594731b380b18a44851d38e8b5275072857  244 bytes  1000 cycles
#    hello.code <= hello.code::hi               {"user":"bob"}
>> Hello, bob
```

2. The contract allows any account to say hi to any user, push the action using a different account:

```shell
cleos push action hello hi '["alice"]' -p alice@active
```

This should produce:

```console
executed transaction: 28d92256c8ffd8b0255be324e4596b7c745f50f85722d0c4400471bc184b9a16  244 bytes  1000 cycles
#    hello.code <= hello.code::hi               {"user":"alice"}
>> Hello, alice
```

This version of the Hello World smart contract is a simple example. The `hi` action may be called by any user. Smart contracts should be secure so extend the code to add authorization. This forces the smart contract to check which account is used to call the action.

## Authorization

The EOSIO blockchain uses asymmetric cryptography to verify that the account pushing a transaction has signed the transaction with the matching private key. EOSIO blockchains use account authority tables to check the account has the required authority to perform an action. Using authorization is the first step towards [securing your smart contract.](https://developers.eos.io/manuals/eosio.cdt/v1.7/best-practices/securing_your_contract) Follow this link [for more information about authorization checks.](https://developers.eos.io/manuals/eosio.cdt/v1.8/how-to-guides/authorization/how_to_restrict_access_to_an_action_by_user)

Add [require_auth](https://developers.eos.io/manuals/eosio.cdt/latest/group__action#function-require_auth) to the smart contract, the `require_auth` function checks authorization and ensures the name parameter matches the user executing and authorizing the action. 

### Procedure to add authorization

1. Update the "hi" action in the `hello.cpp` to use `require_auth`:

```cpp
void hi( name user ) {
   require_auth( user );
   print( "Hello, ", name{user} );
}
```

2. Recompile the contract (remember to run the `eosio-cpp` command in the same folder as the `hello.cpp` file, or refer to the file with an absolute or relative path):

```shell
eosio-cpp -abigen -o hello.wasm hello.cpp
```

3. Redeploy the updated smart contract to the blockchain (run this command outside the folder containing the `hello.wasm` and `hello.abi`):

```shell
cleos set contract hello ./hello -p hello@active
```

4. Call the action again, but this time with mismatched authorization. This command tells the action that **bob** is saying hi, whilst **alice** is signing the transaction:

```shell
cleos push action hello hi '["bob"]' -p alice@active
```
`require_auth` should halt the transaction and the output should be:

```console
Error 3090004: Missing required authority
Ensure that you have the related authority inside your transaction!;
```

The contract now verifies the provided name user is the same as the authorizing user.

5. Try it again, but this time, make **alice** say hi, with the authority of the **alice** account:

```shell
cleos push action hello hi '["alice"]' -p alice@active
```

This should now produce:

```console
235bd766c2097f4a698cfb948eb2e709532df8d18458b92c9c6aae74ed8e4518  244 bytes  1000 cycles
#    hello <= hello::hi               {"user":"alice"}
>> Hello, alice
```

The action should execute successfully, after checking that the account calling the action has the same authorizing account as the user name passed to the action. 

## What's Next?

You have looked at how to write and deploy smart contracts. In the [Smart Contract Guides](../40_smart-contract-guides) we will look at writing and using more complex smart contracts.
