---
title: "3.5 Resource planning"
excerpt: ""
---
How much RAM do I need? This is not an easy question and there's no perfect generic answer for it. You need to find out by measuring your contracts' actions and also by planning accordingly based on your predictions on how fast and how much your bockchain application will grow. If your blockchain application growth is requiring more storage capacity you'll need to by more RAM, if it requires more actions to be executed in the 3 days window (the staking time) you stake more tokens for CPU bandwidth and if your blockchain application growth means also more actions to be stored on the blockchain then you need to also expand your NET bandwidth maximum limit by staking more tokens for NET bandwidth.

*Ok, you'd say, but how much?*

You need to test it, simulate various business scenarios that apply to your blockchain application and measure, hence the existence of public test networks. It allows you to test, to measure how much each action consumes, on worse case business scenario and best case business scenario, for CPU, NET and RAM. Then extrapolate and build a fairly good view of your blockchain application's resources needs based on all your business scenarios combined.

Once you have a fair idea of how your contract, blockchain application and user based are consuming blockchain resources on a public test net you can estimate what you'll need to start with on any EOSIO-based networks, public or private. And from that point onward as with any other application it is advisable to have monitors that tell you statistics and metrics about your application performance.

Of course some aspects might differ from network to network, because each network might have altered its system contracts, EOSIO code base is open sourced and it can be tailored to each network's requirements. You need to be aware of these differences and take them into account if it is the case.

The EOSIO community is also providing tools that can help you in this endeavor. One example is the https://www.eosrp.io
Because the RAM price varies and because the CPU and NET bandwidth allocations vary too as we explained in the previous section, this tool can help you estimate how many resources you can allocate based on a specific amount of tokens and vice-versa.

Another aspect of resource planning involves making sure your contract is very efficient, that is, not consuming resources when not necessary. Therefore it is beneficial for you to find answers to the following questions applied of course to your smart contracts and your blockchain application as well:

- Is your smart contract storing on blockchain only the information that is necessary to be stored in blockchain and for the rest is using alternative ways for storing data (e.g. IPFS)?

- If you have multiple smart contracts, are they communicating between them too much via inline actions? Could some of the smart contracts be merged into one and thus eliminate the need to spawn inline actions between them, reducing the overall inline actions count and thus resource consumption?

- Could you change your smart contracts so your clients pay for some parts of the RAM used? Remember previously how originally the addressbook contract was making each new account added to the book pay for the RAM needed to store its individual data? 

- Or the other way around, are you making your clients pay too much RAM or CPU in order to access your contracts actions, to the point where you are either prohibitive or chasing them away? Would it be better for your blockchain application's growth and success to take on your side some of those costs?