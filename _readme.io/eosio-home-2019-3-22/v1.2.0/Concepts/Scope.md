---
title: "Scope"
excerpt: ""
---
Scope is a region of data within a contract. Contracts can only write to regions in their own contracts but they can read from any contract's regions. Proper scoping allows transactions to run in parallel for the same contract because they do not write to the same regions. Scope is not conflated with an account name, but contracts can use the same value for both for convenience.