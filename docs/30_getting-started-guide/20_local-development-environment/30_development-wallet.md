---
content_title: "Create Development Wallet"
link_text: "Create Development Wallet"
---

Private keys are stored locally in [Keosd](../../glossary/index#keosd). Private keys are one half of public-private key pairs which are used by asymmetric cryptography. The corresponding public keys is stored on the blockchain and associated with an account. It is these keys that are used to secure accounts and to sign transactions. 

Use [Cleos](../../glossary/index#cleos) to run commands on the blockchain and to interact with accounts and keys via [wallet](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/wallet/index) and other [commands.](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/index)    

## Create a Wallet
The first step is to create a wallet. Use [cleos wallet create](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/wallet/create) to create a new "default" wallet using the option `--to-console` for simplicity. If using cleos in production, it's wise to instead use `--file` so your wallet password is not in your bash history. For development purposes and because these are **development and not production keys** `--to-console` poses no security threat.

```shell
cleos wallet create --to-console
```
`cleos` will return a password, save this password somewhere as you will likely need it later in the tutorial.

```
Creating wallet: default
Save password to use in the future to unlock this wallet.
Without password imported keys will not be retrievable.
"PW5Kewn9L76X8Fpd....................t42S9XCw2"
```
[[info | About Wallets]]
| A common misconception in cryptocurrency regarding wallets is that they store tokens. However, in reality, a wallet is used to store private keys in an encrypted file to sign transactions. Wallets do not serve as a storage medium for tokens.

A user builds a transaction object, usually through an interface, sends that object to the wallet to be signed, the wallet then returns that transaction object with a signature which is then broadcast to the network. When/if the network confirms that the transaction is valid, it is included into a block on the blockchain.

## Open the Wallet
Wallets are closed by default when starting a keosd instance, to begin, run the following


```shell
cleos wallet open
```
Run the following to return a list of wallets.


```text
cleos wallet list
```
and it will return

```
Wallets:
[
  "default"
]
```
## Unlock a Wallet
The `keosd` wallet(s) have been opened, but is still locked. Moments ago you were provided a password, you're going to need that now.

```text
cleos wallet unlock
```
You will be prompted for your password, paste it and press enter.

Now run the following command

```text
cleos wallet list
```
It should now return

```
Wallets:
[
  "default *"
]
```

Pay special attention to the asterisk (\*). This means that the wallet is currently **unlocked**

## Import keys into a Wallet
Generate a private key, `cleos` has a helper function for this, just run the following.


```text
cleos wallet create_key
```
It will return something like..

```
Created new private key with a public key of: "EOS8PEJ5FM42xLpHK...X6PymQu97KrGDJQY5Y"
```

## Import the Development Key
Every new EOSIO chain has a default "system" user called "eosio". This account is used to setup the chain by loading system contracts that dictate the governance and consensus of the EOSIO chain. Every new EOSIO chain comes with a development key, and this key is the same. Load this key to sign transactions on behalf of the system user (eosio)

```shell
cleos wallet import
```
You'll be prompted for a private key, enter the `eosio` development key provided below

```
5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
```

[[warning | Important]]
| Never use the development key for a production account! Doing so will most certainly result in the loss of access to your account, this private key is publicly known.
Wonderful, you now have a default wallet unlocked and loaded with a key, and are ready to proceed.


## Use these to help follow the tutorial series easily
Enter the public key provided in the last step in the box below. It will persist the **development public key** you just generated throughout the documentation.

<div class="eosio-helper-box"><form id="YOUR_PUBLIC_KEY"><label>Development Public Key</label><input class="helper-cookie" name="YOUR_PUBLIC_KEY" type="text" /><input type="submit" /><span></span></form></div>

## What's Next?
[Start Keosd and Nodeos](40_start-nodeos-keosd.md): Steps to start Keosd and Nodeos.

