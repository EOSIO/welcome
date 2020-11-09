 ---
content_title: Development Environment
link_text: Development Environment
---

EOSIO based blockchains execute user-generated applications and code using WebAssembly (WASM). WASM is an emerging web standard with widespread support from Google, Microsoft, Apple, and industry leading companies.

Currently the toolchain for building applications that compile to WASM is clang/llvm with their C/C++ compiler. These tools can be found in the `EOSIO.CDT`, the `EOSIO.CDT` provides EOSIO libraries and tools used to compile the smart contract before it can be deployed to the blockchain. For best compatibility, it is recommended that you use the EOSIO C++ toolchain.

Other toolchains in development by 3rd parties include: Rust, Python, and Solidity. While these other languages may appear simpler, their performance will likely impact the scale of application you can build. We expect that C++ will be the best language for developing high-performance and secure smart contracts and plan to use C++ for the foreseeable future.

[EOSIO software versions and supported environments.](../10_installation-guides/05_versions-and-operating-systems.md) 

## Example Editors and IDEs

- [Sublime Text](https://www.sublimetext.com/)
- [Atom Editor](https://atom.io/)
- [CLion](https://www.jetbrains.com/clion/)
- [Eclipse](http://www.eclipse.org/downloads/packages/release/oxygen/1a/eclipse-ide-cc-developers)
- [Visual Studio Code](https://code.visualstudio.com/)

Alternatively, you can use IDEs specifically developed for EOSIO:

- [EOS Studio](https://www.eosstudio.io/)

[[info]]
| The resources listed above are developed, offered, and maintained by third-parties and not by block.one. Providing information, material, or commentaries about such third-party resources does not mean we endorse or recommend any of these resources. We are not responsible, and disclaim any responsibility or liability, for your use of or reliance on any of these resources. Third-party resources may be updated, changed or terminated at any time, so the information below may be out of date or inaccurate. USAGE AND RELIANCE IS ENTIRELY AT YOUR OWN RISK
