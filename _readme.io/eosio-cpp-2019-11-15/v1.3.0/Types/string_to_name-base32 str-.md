---
title: "string_to_name(base32 str)"
excerpt: "Converts a base32 string to a uint64_t."
---
Converts a base32 string to a uint64_t. This is a constexpr so that this method can be used in template arguments as well.

#### Parameters
* `str` - String representation of the name

#### Returns
constexpr uint64_t - 64-bit unsigned integer representation of the name

#### Example


[block:code]
{
  "codes": [
    {
      "code": "void token::test( std::string user ){\n....\n    account_name eosio_name = eosio::string_to_name(user); // convert to EOSIO name from variable\n    account_name eosiotoken_name = N(eosio.token); // convert to EOSIO name from fixed name\n....\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]