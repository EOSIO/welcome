---
title: "Deferred Transaction"
excerpt: ""
---
A transaction that is created by a smart contract for later execution at a specific future time. This future transaction can also create another future transaction to happen after itself. Thus, the deferred transaction opens the door to creating infinite loops. The user authorizing the deferred transaction must have the bandwidth to execute that future transaction (this is evaluated when it's scheduled), and the storage to store it until executed.