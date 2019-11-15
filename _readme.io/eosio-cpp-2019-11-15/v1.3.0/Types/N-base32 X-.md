---
title: "N(base32 X)"
excerpt: "Used to generate a compile time uint64_t from the base32 encoded string interpretation of X."
---
[block:code]
{
  "codes": [
    {
      "code": "#define N(X) eosio::string_to_name(#X)",
      "language": "cplusplus"
    }
  ]
}
[/block]