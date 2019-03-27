---
title: "2.10 Linking Authorization"
excerpt: ""
---
TODO: Migrate from MacDown! (for Sean) 
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

[block:api-header]
{
  "title": "Step 2. Link Authorization to Your Custom Permission"
}
[/block]

[block:api-header]
{
  "title": "Step 3. Test it"
}
[/block]