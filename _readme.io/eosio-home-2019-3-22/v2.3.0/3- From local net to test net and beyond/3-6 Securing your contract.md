---
title: "3.6 Securing your contract"
excerpt: ""
---
These are basic recommendations that should be the foundation of your work of securing your smart contract.

Master the `has_auth`, `require_auth`, `require_auth2` and `require_recipient` methods available in the EOSIO library, they can be found in details [here](https://developers.eos.io/eosio-cpp/reference#require_auth) and implemented [here](https://github.com/EOSIO/eos/blob/3fddb727b8f3615917707281dfd3dd3cc5d3d66d/libraries/chain/apply_context.cpp#L144) (they end up calling the methods implemented in the `apply_context` class).

Understand very well how each of your contracts' actions is impacting the RAM, CPU and NET consumption, and what account ends up paying for these resources, you saw earlier how changing one parameter value for the multi-index `emplace` and `modify` methods changed also the account that is billed for the RAM and CPU needed to execute that action.

Have a solid and comprehensive development process that includes security considerations from day one of the product planning and development.

Test your smart contracts with every update announced for the blockchain you have it deployed. To ease your work automate as much as possible the tests so you can run them with ease anytime is needed and improve them periodically.

Conduct independent smart contract audits, at least two from different organizations.

Host periodic bug bounties on your smart contracts and keep a continuous commitment to reward real security problems reported at any time.

It is an ongoing effort because the whole landscape is always changing to the requirements of the real world needs.