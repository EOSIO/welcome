---
title: "Autobuild Script"
excerpt: ""
---
There is an automated build script that can install all dependencies and build EOSIO.  The script supports the following operating systems.  
We are working on supporting other Linux/Unix distributions in future releases.

1. Amazon 2017.09 and higher.  
2. Centos 7.  
3. Fedora 25 and higher (Fedora 27 recommended).  
4. Mint 18.  
5. Ubuntu 16.04 (Ubuntu 16.10 recommended).  
6. MacOS Darwin 10.12 and higher (MacOS 10.13.x recommended).  

Run the build script from the `eos` folder.

```bash
cd eos
./eosio_build.sh
```

After the script has completed, install EOSIO 

```bash
sudo ./eosio_install.sh
```