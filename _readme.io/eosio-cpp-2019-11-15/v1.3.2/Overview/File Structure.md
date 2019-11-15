---
title: "File Structure"
excerpt: ""
---
[block:callout]
{
  "type": "warning",
  "title": "Deprecation alert!",
  "body": "**eosiocpp** is deprecated from v1.2.0 and will be removed in v1.3.0 . It will be replaced into **eosio-cpp** of [eosio.wasmsdk](https://github.com/EOSIO/eosio.wasmsdk) repository.\nParameters and arguments could be changed accordingly."
}
[/block]
The eosio-cpp tool bundled with **[the Contract Development Toolkit](https://github.com/EOSIO/eosio.cdt)* simplifies the work required to bootstrap a new contract. `eosio-cpp` will create the two smart contract files with the basic skeleton to get you started. These skeleton files are the same `.hpp` and `.cpp` files for the `hello` contract covered in the **[hello world contract tutorial](hello-world)**.

```base
$ eosio-cpp -o contract.wasm contract.cpp
```

The above will create a new empty project in the `./${contract}` folder with two files:
```base
contract.hpp ${contract}.cpp
```

### hpp

`${contract}.hpp` is the header file that contain the variables, constants, and functions referenced by the `.cpp` file.

### cpp

`${contract}.cpp` is the source file that contains the implementations of the functions of the contract.

If you generate the `.cpp` file using the [eosio-cpp](https://github.com/EOSIO/eosio.cdt#eosio-cpp) tool, the generated .cpp file would look similar to the following:

```cpp
#include <eosiolib/eosio.hpp>
  
using namespace eosio;

class hello : public eosio::contract {
  public:
      using contract::contract;

      /// @abi action
      void hi( account_name user ) {
         print( "Hello, ", name{user} );
      }
};

EOSIO_ABI( hello, (hi) )
```
The generated skeleton file has one function, hi, that prints the name of the user data parameter passed in the command request.