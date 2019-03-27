---
title: "Wallet"
excerpt: ""
---
Wallets are clients that store keys that may or may not be associated with the permissions of one or more accounts. Ideally a wallet has a locked (encrypted) and unlocked (decrypted) state that is protected by a high entropy password. 

The `EOSIO/eos` repository comes bundled with a command line interface client called `cleos` that interfaces with a lite-client called `walleos` and together, they demonstrate this pattern.