---
title: "Required Knowledge"
excerpt: ""
---
## C / C++ Experience

EOSIO based blockchains execute user-generated applications and code using [WebAssembly](http://webassembly.org/) (WASM). WASM is an emerging web standard with widespread support of Google, Microsoft, Apple, and others. At the moment the most mature toolchain for building applications that compile to WASM is [clang/llvm](https://clang.llvm.org/) with their C/C++ compiler. For best compatibility, it is recommended that you use the EOSIO toolchain.

Other toolchains in development by 3rd parties include: Rust, Python, and Solidity. While these other languages may appear simpler, their performance will likely impact the scale of application you can build. We expect that C++ will be the best language for developing high-performance and secure smart contracts and plan to use C++ for the foreseeable future.

## Linux / Mac OS Experience

The EOSIO software supports the following environments:
- Amazon 2017.09 and higher
- Centos 7
- Fedora 25 and higher (Fedora 27 recommended)
- Mint 18
- Ubuntu 16.04 (Ubuntu 16.10 recommended)
- Ubuntu 18.04 LTS
- MacOS Darwin 10.12 and higher (MacOS 10.13.x recommended)

## Command Line Knowledge

There are a variety of tools provided along with EOSIO which requires you to have basic command line knowledge in order to interact with.