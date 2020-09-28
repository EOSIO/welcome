---
content_title: "1.1: Prerequisites"
link_text: "1.1: Prerequisites"
---

## EOSIO versions

The subsequent tutorials are up to date with the following EOSIO components.

| Component | Version |
| ------ | ------ |
| eosio | 2.0.0 |
| eosio.cdt | 1.7.0 |
| eosio.contracts | 1.9.0 |



## Development Experience

EOSIO based blockchains execute user-generated applications and code using WebAssembly (WASM). WASM is an emerging web standard with widespread support from Google, Microsoft, Apple, and industry leading companies.

At the moment the most mature toolchain for building applications that compile to WASM is clang/llvm with their C/C++ compiler. For best compatibility, it is recommended that you use the EOSIO C++ toolchain.

Other toolchains in development by 3rd parties include: Rust, Python, and Solidity. While these other languages may appear simpler, their performance will likely impact the scale of application you can build. We expect that C++ will be the best language for developing high-performance and secure smart contracts and plan to use C++ for the foreseeable future.

## Operating System

The EOSIO software supports the following environments for development and/or deployment:

**Linux Distributions**
* Amazon Linux 2
* CentOS Linux 8.x
* CentOS Linux 7.x
* Ubuntu 20.04
* Ubuntu 18.04
* Ubuntu 16.04

**macOS**
* macOS 10.14 (Mojave) or later

[[info | Note]]
| If you are developing on __Windows__, we do not provide PowerShell ports and instructions at this time. You can use a VM with Ubuntu (or any supported Linux distro), and set up your development environment inside the VM. If you are an advanced Windows developer familiar with porting Linux instructions, you should encounter minimal issues.

### Command Line Knowledge

There are a variety of tools provided along with EOSIO which requires you to have basic command line knowledge in order to interact with.

## Development Tools

We can use any text editor that, preferably, supports C++ syntax highlighting. Some of the popular editors are Sublime Text and Atom. Another option is an IDE, which provides a more sophisticated code completion and more complete development experience. You are welcome to use the software of your personal preference, but if you're unsure what to use we've provided some options for you to explore.

### Potential Editors and IDEs

- [Sublime Text](https://www.sublimetext.com/)
- [Atom Editor](https://atom.io/)
- [CLion](https://www.jetbrains.com/clion/)
- [Eclipse](http://www.eclipse.org/downloads/packages/release/oxygen/1a/eclipse-ide-cc-developers)
- [Visual Studio Code](https://code.visualstudio.com/)

[[info]]
| The resources listed above are developed, offered, and maintained by third-parties and not by block.one. Providing information, material, or commentaries about such third-party resources does not mean we endorse or recommend any of these resources. We are not responsible, and disclaim any responsibility or liability, for your use of or reliance on any of these resources. Third-party resources may be updated, changed or terminated at any time, so the information below may be out of date or inaccurate. USAGE AND RELIANCE IS ENTIRELY AT YOUR OWN RISK

Alternatively, you can try out some community driven IDEs specifically developed for EOSIO:

- [EOS Studio](https://www.eosstudio.io/)

## What you'll learn

_Only a sample of what you'll learn_
- How to quickly spin up a node
- Manage wallets and keys
- Create Accounts
- Write some contracts
- Compilation and ABI
- Deploy contracts

## What's Next?
- [Before You Begin](./03_before-you-begin.md): Steps to download and install binaries on your system.
