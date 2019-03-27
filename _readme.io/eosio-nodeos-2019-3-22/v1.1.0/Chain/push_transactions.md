---
title: "push_transactions"
excerpt: "This method expects a transactions in JSON format and will attempt to apply it to the blockchain. This method push multiple transactions at once."
---
[block:callout]
{
  "type": "info",
  "body": "The **ref_block_num** and **ref_block_prefix** here are provided as a result of [/v1/chain/get_block](#get_block) of the **last_irreversible_block**. The **last_irreversible_block** can be found by calling [/v1/chain/get_info](#get_info). You also need to use [/v1/wallet/sign_transaction](#sign_transaction) to get the right signature."
}
[/block]