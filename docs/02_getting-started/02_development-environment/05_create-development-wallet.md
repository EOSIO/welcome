---
content_title: "1.4: Create Development Wallet"
link_text: "1.4 Create Development Wallet"
---

Wallets are repositories of public-private key pairs. Private keys are needed to sign operations performed on the blockchain. Wallets are accessed using cleos.
## Step 1: Create a Wallet
The first step is to create a wallet. Use [cleos wallet create]() to create a new "default" wallet using the option `--to-console` for simplicity. If using cleos in production, it's wise to instead use `--to-file` so your wallet password is not in your bash history. For development purposes and because these are **development and not production keys** `--to-console` poses no security threat.

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

## Step 2: Open the Wallet
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
## Step 3: Unlock it
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
## Step 4:  Import keys into your wallet
Generate a private key, `cleos` has a helper function for this, just run the following.


```text
cleos wallet create_key
```
It will return something like..

```
Created new private key with a public key of: "EOS8PEJ5FM42xLpHK...X6PymQu97KrGDJQY5Y"
```
## Step 5: Follow this tutorial series more easily
Enter the public key provided in the last step in the box below. It will persist the **development public key** you just generated throughout the documentation.

<div class="eosio-helper-box"><form id="YOUR_PUBLIC_KEY"><label>Development Public Key</label><input class="helper-cookie" name="YOUR_PUBLIC_KEY" type="text" /><input type="submit" /><span></span></form></div>

## Step 6: Import the Development Key
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

## What's Next? 
- [Start Your Node](https://developers.eos.io/getting-started/development-environment/start-your-node-setup): Steps to start `keosd` and `nodeos`.
