---
title: "Randomization in Contracts"
excerpt: ""
---
By using `openssl`, `sha256` and `checksum256`, a value can be produced that is deterministic and effectively random. This can be achieved by hashing (sha256) `n` number of hashes and their corresponding secrets and then selecting `n` number of values from the result. The determinism and randomness comes from having an outside source supply a hash and its corresponding secret.

In the example of two users wanting to play a game with 50/50 odds, each player must first submit a hash of their secret. By submitting their hash, they then become eligible to play the game. Once both players have submitted the hash of their secret, they are effectively engaged in the game. It's only when both players reveal their secrets that both of their submitted hashes and recently submitted secrets are hashed. From the result of this hash, two numbers are selected to determine a winner and a loser.
[block:api-header]
{
  "title": "Step 1: Generate Secrets"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "openssl rand -hex 32\n28349b1d4bcdc9905e4ef9719019e55743c84efa0c5e9a0b077f0b54fcd84905\n\nopenssl rand -hex 32\n15fe76d25e124b08feb835f12e00a879bd15666a33786e64b655891fba7d6c12",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 2: Generate sha256 hashes"
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
  "title": "Step 3: Submit Hash of Secret"
}
[/block]
Alice and Bob each submit their hash of their secret.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action chance submithash '[ \"alice\", \"d533f24d6f28ddcef3f066474f7b8355383e485681ba8e793e037f5cf36e4883\" ]' -p alice@active\t\n\ncleos push action chance submithash '[ \"bob\", \"50ed53fcdaf27f88d51ea4e835b1055efe779bb87e6cfdff47d28c88ffb27129\" ]' -p bob@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 4: Submit Secret"
}
[/block]
Alice and Bob each submit the hash of their secret and the secret itself.
[block:code]
{
  "codes": [
    {
      "code": "cleos push action chance submitboth '[ \"d533f24d6f28ddcef3f066474f7b8355383e485681ba8e793e037f5cf36e4883\", \"28349b1d4bcdc9905e4ef9719019e55743c84efa0c5e9a0b077f0b54fcd84905\" ]' -p alice@active\n\ncleos push action chance submitboth '[ \"50ed53fcdaf27f88d51ea4e835b1055efe779bb87e6cfdff47d28c88ffb27129\", \"15fe76d25e124b08feb835f12e00a879bd15666a33786e64b655891fba7d6c12\" ]' -p bob@active",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 5: Conclusion"
}
[/block]
The simplest data type that can be used to store the secret and the hash of the secret is a struct.
[block:code]
{
  "codes": [
    {
      "code": "struct player {\n  checksum256 hash;\n  checksum256 secret;\n};",
      "language": "cplusplus"
    }
  ]
}
[/block]
When the players of the game are being instantiated, it is important to do so in succession. This is done so that the secrets and hashes for all the players are contiguously stored in memory.
[block:code]
{
  "codes": [
    {
      "code": "struct game {\n\tuint64_t id;\n  player player1;\n  player player2;\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
Once the secret and the hash of the secret are received for all the players, the hashing of it all can be done.
[block:code]
{
  "codes": [
    {
      "code": "// variable to get result from hashing all players hashes and secrets\nchecksum256 result;\n\n// hash the contents in memory, starting at game.player1 and spanning for \n// sizeof(player)*2 bytes\nsha256( (char *)&game.player1, sizeof(player)*2, &result);\n\n// compares first and second 4 byte chunks in result to determine a winner\nint winner = result.hash[1] < result.hash[0] ? 0 : 1;\n\n// report appropriate winner\nif( winner ) {\n  report_winner(game.player1);\n} else {\n  report_winner(game.player2);\n}",
      "language": "cplusplus"
    }
  ]
}
[/block]
It's important to note that sha256 is 32 bytes and that there are 8 chunks of uint32_t in it. In the above example, the first two are considered, but it could have been any of them.