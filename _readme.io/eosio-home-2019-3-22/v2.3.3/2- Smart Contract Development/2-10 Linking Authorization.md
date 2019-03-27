---
title: "2.10 Linking Authorization"
excerpt: ""
---
[block:api-header]
{
  "title": "Introduction"
}
[/block]
EOSIO enables for authorization of a particular action on a particular contract to be directly linked to a permission on an account. This enables all kinds of unique interactions, but the one we'll cover here is to permit a contract's action to autonomously execute without additional permission from an account. This has countless implementation possibilities, a few worth mentioning are the ability to contracts to communicate with each other autonomously, and for a contract to execute actions on a user's behalf.

With great power, comes great responsibility. This functionality poses some challenges for security, which can be addressed in the future with user-friendly GUIs that help prevent a user from making a mistake. 
[block:api-header]
{
  "title": "Step 1. Create a Custom Permission"
}
[/block]
Firstly let us create a new permission level on alice's account

cleos set action permission alice upsert EOS7ZmPRBiGisnHrojMzMT2YrHmrYBdWrjXD3GhC3Cq4cURJqs8Lz -p alice@owner
[block:api-header]
{
  "title": "Step 2. Link Authorization to Your Custom Permission"
}
[/block]
Link the authorization to invoke the upsert with the new permission we created:

cleos set action permission alice addressbook upsert upsert
[block:api-header]
{
  "title": "Step 3. Test it"
}
[/block]
cleos push action addressbook upsert '["alice", "alice", "a", 21, "Herengracht", "land", "dam"]' -p alice@upsert