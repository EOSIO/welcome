---
title: "Assumptions"
excerpt: ""
---
EOSIO documentation enforces several assumptions on the end-user in order to create a more consistent documentation experience.

* **Your development environment exists within some flavor of nix**, this includes Mac OS. The majority of development at the core levels of EOSIO require that the user utilize command line. Windows' `cmd` is an edge case in the computing world, utilizing syntax inspired by DOS not compatible with the vast majority of software in the wild. Until Windows adopts a Linux Platform (it does appear this might happen eventually), we regret to inform you that none of our documentation support windows. If you develop on Windows, you've likely dealt with this in the past, and may possess the skill to take the information provided, and port it for your needs.

* **You are running the Docker image**. There are many different ways to build and compile EOSIO, this is to create support for every possible configuration developers may need, but if we wrote documentation for every possible situation, we would have to write the same tutorial, 3 or 4 times. This would result in inconsistent documentation, and make maintenance a slow and arduous process. For this reason, we have decided to conform our documentation around the platform-agnostic configuration with the shortest time to install and get running. If you are developing from a local build, you also likely possess the skills to recognize where these _gotchyas_ exist, and can modify the instructions to suit your needs.