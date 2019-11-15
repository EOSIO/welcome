---
title: "Types"
excerpt: "Specifies builtin types, typedefs and aliases."
---
### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`define` [`ALIGNED`](#ALIGNED)            |
`define` [`N`](#N)            | Used to generate a compile time uint64_t from the base32 encoded string interpretation of X.
`public struct` [`ALIGNED`](#ALIGNED)`(checksum256)`            | 256-bit hash
`public struct` [`ALIGNED`](#ALIGNED)`(checksum160)`            | 160-bit hash
`public struct` [`ALIGNED`](#ALIGNED)`(checksum512)`            | 512-bit hash
`public static constexpr char` [`char_to_symbol`](#char_to_symbol)`(char c)`            | Converts a base32 symbol into its binary representation, used by string_to_name()
`public static constexpr uint64_t` [`string_to_name`](#string_to_name)`(const char * str)`            | Converts a base32 string to a uint64_t.
`class` [`eosio::fixed_key`](docs2/types.md#classeosio_1_1fixed__key) | Fixed size key sorted lexicographically for Multi Index Table.
`struct` [`public_key`](docs2/types.md#structpublic__key) | EOSIO Public Key.
`struct` [`signature`](docs2/types.md#structsignature) | EOSIO Signature.
`struct` [`account_permission`](docs2/types.md#structaccount__permission) |
`struct` [`eosio::name`](docs2/types.md#structeosio_1_1name) | wraps a uint64_t to ensure it is only passed to methods that expect a Name