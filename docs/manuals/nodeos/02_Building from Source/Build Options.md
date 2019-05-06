---
title: "Build Options"
excerpt: ""
---
[[info]]
|Building EOSIO is Recommended for Advanced Developers
If you are new to EOSIO it's suggested you use the [Getting Started Guide](doc:docker-quickstart)
EOSIO can be built on several platforms with various paths to building. The majority of users will prefer to use the autobuild script or docker, while more advanced users, or users wishing to deploy a public node may desire manual methods. The build places content in the `eos/build` folder. The executables can be found in subfolders within the `eos/build/programs` folder.

- [Autobuild Script](doc:autobuild-script)  - Suitable for the majority of developers, this script builds on Mac OS and many flavors of Linux.

- [Docker Compose](doc:docker) - By far the fastest installation method, you can have a node up and running in a couple minutes. That said, it requires some additional local configuration for development to run smoothly and follow our provided tutorials.

- [Manual Build](doc:manually-build)  - Suitable for those who have environments that may be hostile to the autobuild script or for operators who wish to exercise more control over their build.

- [Install Executables](doc:install-executables)  - An optional `make install` step that makes local development a bit more developer friendly.
## System Requirements (all platforms)
- 7GB RAM free required
- 20GB Disk free required