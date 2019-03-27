---
title: "1.6 Create Development Wallet"
excerpt: ""
---
[block:api-header]
{
  "title": "Step 1: Create a Wallet"
}
[/block]
The first step is to create a wallet. Use [cleos wallet create]() to create a new "default" wallet using the option `--to-console` for simplicity. If using cleos in production, it's wise to instead use `--to-file` so your wallet password is not in your bash history. For development purposes and because these are **development and not production keys** `--to-console` poses no security threat. 
[block:code]
{
  "codes": [
    {
      "code": "cleos wallet create --to-console",
      "language": "shell"
    }
  ]
}
[/block]
`cleos` will return a password, save this password somewhere as you will likely need it later in the tutorial. 

```
Creating wallet: default
Save password to use in the future to unlock this wallet.
Without password imported keys will not be retrievable.
"PW5Kewn9L76X8Fpd....................t42S9XCw2"
```
[block:callout]
{
  "type": "info",
  "body": "A common misconception in cryptocurrency regarding wallets is that they store tokens. A wallet **does not** store tokens. What a wallet does is store private keys in an encrypted file and sign transactions. \n\nA user builds a transaction object, usually through an interface, sends that object to the wallet to be signed, the wallet then returns that transaction object with a signature which is then broadcast to the network. When/if the network confirms that the transaction is valid, it is included into a block on the blockchain.",
  "title": "About Wallets"
}
[/block]

[block:api-header]
{
  "title": "Step 2: Open the Wallet"
}
[/block]
Wallets are closed by default when starting a keosd instance, opening a keosd wallet with cleos is easy with

```
cleos wallet open
```

Return a list of wallets available

```
cleos wallet list
```
Should return the following at this point in the tutorial: 

```
Wallets:
[
  "default"
]
```
[block:api-header]
{
  "title": "Step 3: Unlock it"
}
[/block]
The `keosd` wallet(s) has been opened but is still locked. Moments ago you were provided a password, you're going to need that now. 

```
cleos wallet unlock
```
You will be prompted for your password, paste it and press enter. 

Now run the following command

```
cleos wallet list
```

It should now return

```
Wallets:
[
  "default *"
]
```

Pay special attention to the asterisk (*). This means that the wallet is currently **unlocked**
[block:api-header]
{
  "title": "Step 4:  Import keys into your wallet"
}
[/block]
Generate a private key, `cleos` has a helper function for this, just run the following.

```
cleos wallet create_key
```

It will return something like:

```
Created new private key with a public key of: "EOS8PEJ...GDJQY5Y"
```
[block:api-header]
{
  "title": "Step 5: Follow this tutorial series more easily"
}
[/block]
Enter the public key provided in the last step in the box below. It will persist the **development public key** you just generated public key throughout the documentation.
[block:html]
{
  "html": "<div class=\"eosio-helper-box\">\n  <form> \n    <label>Development Public Key</label>\n    <input class=\"helper-cookie\" name=\"YOUR_PUBLIC_KEY\" type=\"text\" />\n    <input type=\"submit\" />\n    <span></span>\n  </form>\n</div>"
}
[/block]

[block:api-header]
{
  "title": "Step 6: Import the Development Key"
}
[/block]
Every new EOSIO chain has a default "system" user called "eosio". This account is used to set up the chain by loading system contracts that dictate the governance and consensus of the EOSIO chain. Every new EOSIO chain comes with a development key, and this key is the same. On a production chain, the `eosio` user is forfeited once the chain is set up. Load this key to sign transactions on behalf of the system user (eosio)
[block:code]
{
  "codes": [
    {
      "code": "cleos wallet import",
      "language": "shell"
    }
  ]
}
[/block]
You'll be prompted for a private key, enter the `eosio` development key provided below

```
5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
```
[block:callout]
{
  "type": "danger",
  "title": "Important",
  "body": "Never use the development key for a production account! Doing so will most certainly result in the loss of access to your account, this private key is publicly known."
}
[/block]
The default wallet is now unlocked and a key has been loaded. You are ready to proceed.