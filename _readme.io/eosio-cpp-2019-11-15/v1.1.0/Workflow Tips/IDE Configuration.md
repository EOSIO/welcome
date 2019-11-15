---
title: "IDE Configuration"
excerpt: ""
---
[block:callout]
{
  "type": "info",
  "body": "This guide assumes you have already downloaded the EOS repository to your system."
}
[/block]

[block:api-header]
{
  "title": "Eclipse C++ IDE"
}
[/block]
##Downloads##
[***Java***](http://www.oracle.com/technetwork/java/javase/downloads/index.html)

[***Eclipse CDT (C/C++ Development Tooling)***](https://www.eclipse.org/cdt/)

##Shortcut / Symbolic Link##
In the `contracts` folder, in the local EOS repository, create a shortcut / symbolic link of the `eosiolib` folder and place it in the `eclipse-workspace` folder. This is done to give smart contracts access to needed header files.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/447f8c9-Screen_Shot_2018-04-17_at_6.08.32_AM.png",
        "Screen Shot 2018-04-17 at 6.08.32 AM.png",
        394,
        196,
        "#dbedf7"
      ],
      "caption": "Even though `eosiolib` is not in the `helloWorld` project folder, Eclipse's code indexer engine is able find the needed files for the `#include` statements."
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3610c39-Screen_Shot_2018-04-17_at_6.15.47_AM.png",
        "Screen Shot 2018-04-17 at 6.15.47 AM.png",
        1884,
        706,
        "#f0f0f1"
      ],
      "caption": "Notice that `eosiolib/eosio.hpp` and `eosiolib/print.hpp` are found and included."
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "More IDE Configs"
}
[/block]
Suggest an IDE configuration.