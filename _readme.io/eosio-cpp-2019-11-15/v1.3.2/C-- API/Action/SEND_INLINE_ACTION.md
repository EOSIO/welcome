---
title: "SEND_INLINE_ACTION"
excerpt: "Send inline action."
---
A macro that simplifies the constructing and sending of an `action`. Best used to send an action to another contract.

#### Parameters
* `CONTRACT` - The account this action is intended for
* `NAME` - The name of the action
* `...` - The member of the action specified as ("action_member1_name", action_member1_value)("action_member2_name", action_member2_value)