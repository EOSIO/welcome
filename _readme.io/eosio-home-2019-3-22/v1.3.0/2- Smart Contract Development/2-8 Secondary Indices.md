---
title: "2.8 Secondary Indices"
excerpt: ""
---
EOSIO has the ability to sort tables by up to 16 indices. In the following section, we're going to add another index to the `addressbook` contract, so we can iterate through the records in a different way. As mentioned earlier, **a table's struct cannot be modified when it has data in it.** The first step, will be to remove the data we've already added. Let's begin.
[block:api-header]
{
  "title": "Step 1: Remove existing data from table"
}
[/block]

[block:api-header]
{
  "title": "Step 2: Add new index member and getter"
}
[/block]

[block:api-header]
{
  "title": "Step 3: Add secondary index to `addresses` table configuration"
}
[/block]

[block:api-header]
{
  "title": "Step 4: Compile and Deploy"
}
[/block]

[block:api-header]
{
  "title": "Step 5: Test it"
}
[/block]