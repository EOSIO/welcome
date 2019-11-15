---
title: "assert_recover_key"
excerpt: "Tests a given public key with the generated key from digest and the signature."
---
#### Parameters
* `digest` - What the key will be generated from 

* `sig` - Signature 

* `siglen` - Signature length 

* `pub` - Public key 

* `publen` - Public key length

#### Precondition
**assert recovery key** of `pub` equals the key generated from the `digest` parameter 

#### Post Condition
Executes next statement. If was not `true`, hard return.

#### Example

```cpp
checksum digest;
char sig;
size_t siglen;
char pub;
size_t publen;
assert_recover_key( digest, sig, siglen, pub, publen )
// If the given public key does not match with the generated key from digest and the signature, anything below will never fire.
eosio::print("pub key matches the pub key generated from digest");
```