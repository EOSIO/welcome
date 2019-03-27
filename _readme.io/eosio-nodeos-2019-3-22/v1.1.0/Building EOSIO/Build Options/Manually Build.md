---
title: "Manually Build"
excerpt: ""
---
To manually build, use the following steps to create a `build` folder within your `eos` folder and then perform the build.  The steps below assume the `eos` repository was cloned into your home (i.e., `~`) folder.  It is also assumes that the necessary dependencies have been installed.  See [Manual Installation of the Dependencies](#manualdep).

```bash
cd ~
mkdir -p ~/eos/build && cd ~/eos/build
```

On Linux platforms, use this `cmake` command:
``` bash
cmake -DBINARYEN_BIN=~/binaryen/bin -DWASM_ROOT=~/wasm-compiler/llvm -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl -DOPENSSL_LIBRARIES=/usr/local/opt/openssl/lib -DBUILD_MONGO_DB_PLUGIN=true ..
```

On MacOS, use this `cmake` command:
``` bash
cmake -DBINARYEN_BIN=~/binaryen/bin -DWASM_ROOT=/usr/local/wasm -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl -DOPENSSL_LIBRARIES=/usr/local/opt/openssl/lib -DBUILD_MONGO_DB_PLUGIN=true ..
```

Then on all platforms:
``` bash
make -j$( nproc )
```

Out-of-source builds are also supported. To override clang's default choice in compiler, add these flags to the CMake command:

`-DCMAKE_CXX_COMPILER=/path/to/c++ -DCMAKE_C_COMPILER=/path/to/cc`

For a debug build, add `-DCMAKE_BUILD_TYPE=Debug`. Other common build types include `Release` and `RelWithDebInfo`.