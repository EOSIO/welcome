---
title: "Crypto"
excerpt: "Defines C API for calculating and checking hash."
---
### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public void `[`assert_sha256`](#assert_sha256)`(char * data,uint32_t length,const checksum256 * hash)`            | Tests if the sha256 hash generated from data matches the provided checksum.
`public void `[`assert_sha1`](#assert_sha1)`(char * data,uint32_t length,const checksum160 * hash)`            | Tests if the sha1 hash generated from data matches the provided checksum.
`public void `[`assert_sha512`](#assert_sha512)`(char * data,uint32_t length,const checksum512 * hash)`            | Tests if the sha512 hash generated from data matches the provided checksum.
`public void `[`assert_ripemd160`](#assert_ripemd160)`(char * data,uint32_t length,const checksum160 * hash)`            | Tests if the ripemod160 hash generated from data matches the provided checksum.
`public void `[`sha256`](#sha256)`(char * data,uint32_t length,checksum256 * hash)`            | Hashes `data` using `sha256` and stores result in memory pointed to by hash.
`public void `[`sha1`](#sha1)`(char * data,uint32_t length,checksum160 * hash)`            | Hashes `data` using `sha1` and stores result in memory pointed to by hash.
`public void `[`sha512`](#sha512)`(char * data,uint32_t length,checksum512 * hash)`            | Hashes `data` using `sha512` and stores result in memory pointed to by hash.
`public void `[`ripemd160`](#ripemd160)`(char * data,uint32_t length,checksum160 * hash)`            | Hashes `data` using `ripemod160` and stores result in memory pointed to by hash.
`public int `[`recover_key`](#recover_key)`(const checksum256 * digest,const char * sig,size_t siglen,char * pub,size_t publen)`            | Calculates the public key used for a given signature and hash used to create a message.
`public void `[`assert_recover_key`](#assert_recover_key)`(const checksum256 * digest,const char * sig,size_t siglen,const char * pub,size_t publen)`            | Tests a given public key with the generated key from digest and the signature.