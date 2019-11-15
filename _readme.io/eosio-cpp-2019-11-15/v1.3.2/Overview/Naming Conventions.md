---
title: "Naming Conventions"
excerpt: ""
---
[block:api-header]
{
  "title": "Standard Account Names"
}
[/block]
- Can only contain the characters `.abcdefghijklmnopqrstuvwxyz12345`. `a-z` (lowercase), `1-5` and `.` (period) 
- Must start with a letter
- Must be 12 characters
[block:api-header]
{
  "title": "Table Names, Structs, Functions, Classes"
}
[/block]
- Can only contain up to 12 alpha characters
[block:api-header]
{
  "title": "Symbols"
}
[/block]
- Must be capitalized alpha characters between A and Z
- Must be 7 characters or less
[block:api-header]
{
  "title": "Principle"
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4188937-_2018-09-04__9.28.51.png",
        "스크린샷 2018-09-04 오후 9.28.51.png",
        2140,
        878,
        "#eeeef0"
      ]
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Tips"
}
[/block]
1. To encode a script into EOSIO name, see [eosio::string_to_name](https://developers.eos.io/eosio-cpp/reference#string_to_namebase32-str)

2. To decode from base32 and restore to string form, use `eosio::to_string()` (an alias of `std::string`) 
```c++
auto user_name_obj = eosio::name{user}; // account_name user
std::string user_name = user_name_obj.to_string();
```