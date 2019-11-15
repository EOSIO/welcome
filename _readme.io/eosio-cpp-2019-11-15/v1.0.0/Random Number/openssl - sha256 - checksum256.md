---
title: "openssl + sha256 + checksum256"
excerpt: "Produce a deterministic and random value."
---
[block:api-header]
{
  "title": "Description"
}
[/block]
By using `openssl`, `sha256` and `checksum256`, a value can be produced that is deterministic and effectively random. This can be achieved by hashing (sha256) `n` number of hashes and their corresponding secrets and then selecting `n` number of values from the result. The determinism and randomness comes from having an outside source supply a hash and its corresponding secret.

In the example of two users wanting to play a game with 50/50 odds, each player must first submit a hash of their secret. By submitting their hash, they then become eligible to play the game. Once both players have submitted the hash of their secret, they are effectively engaged in the game. It's only when both players reveal their secrets that both of their submitted hashes and recently submitted secrets are hashed. From the result of this hash, two numbers are selected to determine a winner and a loser.
[block:api-header]
{
  "title": "Generate Secrets"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "openssl rand 32 -hex\n28349b1d4bcdc9905e4ef9719019e55743c84efa0c5e9a0b077f0b54fcd84905\n\nopenssl rand 32 -hex\n15fe76d25e124b08feb835f12e00a879bd15666a33786e64b655891fba7d6c12",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Generate sha256(secret)s"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "echo -n '28349b1d4bcdc9905e4ef9719019e55743c84efa0c5e9a0b077f0b54fcd84905' | xxd -r -p | sha256sum -b | awk '{print $1}'\nd533f24d6f28ddcef3f066474f7b8355383e485681ba8e793e037f5cf36e4883\n\necho -n '15fe76d25e124b08feb835f12e00a879bd15666a33786e64b655891fba7d6c12' | xxd -r -p | sha256sum -b | awk '{print $1}'\n50ed53fcdaf27f88d51ea4e835b1055efe779bb87e6cfdff47d28c88ffb27129",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Submit Hash of Secret"
}
[/block]
Alice and Bob each submit their hash of their secret.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action chance submithash '[ \"alice\", \"d533f24d6f28ddcef3f066474f7b8355383e485681ba8e793e037f5cf36e4883\" ]' -p alice\n\ncleos push action chance submithash '[ \"bob\", \"50ed53fcdaf27f88d51ea4e835b1055efe779bb87e6cfdff47d28c88ffb27129\" ]' -p bob",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Submit Secret"
}
[/block]
Alice and Bob each submit the hash of their secret and the secret itself.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action chance submitboth '[ \"d533f24d6f28ddcef3f066474f7b8355383e485681ba8e793e037f5cf36e4883\", \"28349b1d4bcdc9905e4ef9719019e55743c84efa0c5e9a0b077f0b54fcd84905\" ]' -p alice\n\ncleos push action dice submitboth '[ \"50ed53fcdaf27f88d51ea4e835b1055efe779bb87e6cfdff47d28c88ffb27129\", \"15fe76d25e124b08feb835f12e00a879bd15666a33786e64b655891fba7d6c12\" ]' -p bob",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Random Outcome"
}
[/block]