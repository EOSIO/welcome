---
title: "The \"Hello World\" Contract"
excerpt: ""
---
## Hello World Contract
**This tutorial assumes that you have completed tutorials [Getting Started With Contracts](introduction-to-smart-contracts) and [ntroduction to the EOSIO Token Contract](token-tutorial).**

We will now create our first "hello world" contract.  Create a new folder called "hello", cd into the folder, then create a file "hello.cpp" with the following contents:

### hello/hello.cpp
```
#include <eosiolib/eosio.hpp>
#include <eosiolib/print.hpp>
using namespace eosio;

class hello : public eosio::contract {
  public:
      using contract::contract;

      /// @abi action 
      void hi( account_name user ) {
         print( "Hello, ", name{user} );
      }
};

EOSIO_ABI( hello, (hi) )
```

You can compile your code to web assembly (.wast) as follows:
```
$ eosiocpp -o hello.wast hello.cpp
```
**NOTE:**  The compiler might generate warnings.  These can be safely ignored.

Now generate the abi:

```
$ eosiocpp -g hello.abi hello.cpp
Generated hello.abi
```

Create an account and upload the contract:

```
$ cleos create account eosio hello.code EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4 EOS7ijWCBmoXBi3CgtK7DJxentZZeTkeUnaSDvyro9dq7Sd1C3dC4
...
$ cleos set contract hello.code ../hello -p hello.code@active
...
```

Now we can run the contract:

```
$ cleos push action hello.code hi '["user"]' -p user@active
executed transaction: 4c10c1426c16b1656e802f3302677594731b380b18a44851d38e8b5275072857  244 bytes  1000 cycles
#    hello.code <= hello.code::hi               {"user":"user"}
>> Hello, user
```
If you're observing the output from `nodeos`, you probably did not see any output from `nodeos` indicating that anything happened.  You can restart `nodeos` with the `--contracts-console` option to cause printed debug output to be sent to the console.  Output will look like the following:
```
1025500ms thread-0   producer_plugin.cpp:944       produce_block        ] Produced block 00004de945a23f63... #19945 @ 2018-05-25T19:17:05.500 signed by eosio [trxs: 0, lib: 19944, confirmed: 0]
1025830ms thread-0   apply_context.cpp:28          print_debug          ] 
[(hello.code,hi)->hello.code]: CONSOLE OUTPUT BEGIN =====================
Hello, user
[(hello.code,hi)->hello.code]: CONSOLE OUTPUT END   =====================
1026000ms thread-0   producer_plugin.cpp:944       produce_block        ] Produced block 00004deaebee2dc5... #19946 @ 2018-05-25T19:17:06.000 signed by eosio [trxs: 1, lib: 19945, confirmed: 0]
```

At this time the contract allows anyone to authorize it, we could also say:

```
$ cleos push action hello.code hi '["user"]' -p tester@active
executed transaction: 28d92256c8ffd8b0255be324e4596b7c745f50f85722d0c4400471bc184b9a16  244 bytes  1000 cycles
#    hello.code <= hello.code::hi               {"user":"user"}
>> Hello, user
```

In this case tester is the one who authorized it and user is just an argument.  If we want our contact to authenticate the user we are saying "hi" to, then we need to modify the contract to require authentication.

Modify the hi() function in hello.cpp as follows:
```
void hi( account_name user ) {
   require_auth( user );
   print( "Hello, ", name{user} );
}
```
Repeat the steps to compile the wast file and generate the abi, then set the contract again to deploy the update.

Now if we attempt to mismatch the user and the authority, the contract will throw an error:
```
$ cleos push action hello.code hi '["tester"]' -p user@active
Error 3030001: missing required authority
Ensure that you have the related authority inside your transaction!;
If you are currently using 'cleos push action' command, try to add the relevant authority using -p option.
Error Details:
missing authority of tester
```

The debug output will look similar to this:
```
1340500ms thread-0   producer_plugin.cpp:944       produce_block        ] Produced block 0000505f9de7f4b9... #20575 @ 2018-05-25T19:22:20.500 signed by eosio [trxs: 0, lib: 20574, confirmed: 0]
1340515ms thread-0   http_plugin.cpp:369           handle_exception     ] FC Exception encountered while processing chain.push_transaction: 3090004 missing_auth_exception: missing required authority
missing authority of user
    {"account":"user"}
    thread-0  apply_context.cpp:123 require_authorization

    {"_pending_console_output.str()":""}
    thread-0  apply_context.cpp:53 exec_one
1341005ms thread-0   producer_plugin.cpp:944       produce_block        ] Produced block 000050601ffc5bd9... #20576 @ 2018-05-25T19:22:21.000 signed by eosio [trxs: 0, lib: 20575, confirmed: 0]
```

We can fix this by giving the permission of tester:

```
$ cleos push action hello.code hi '["tester"]' -p tester@active
executed transaction: 235bd766c2097f4a698cfb948eb2e709532df8d18458b92c9c6aae74ed8e4518  244 bytes  1000 cycles
#    hello.code <= hello.code::hi               {"user":"tester"}
>> Hello, tester
```

## Hello World Ricardian Contract
Every smart contract must have a matching Ricardian contract.  The Ricardian Contract specifies the legally binding behavior associated with each action of the smart contract.  The Ricardian Contract for the Hello World Contract is listed here.

```markdown
## CONTRACT FOR HELLO WORLD

### Parameters
Input parameters: NONE

Implied parameters: 

* _**account_name**_ (name of the party invoking and signing the contract)

### Intent
INTENT. The intention of the author and the invoker of this contract is to print output. It shall have no other effect.

### Term
TERM. This Contract expires at the conclusion of code execution.

### Warranty
WARRANTY. {{ account_name }} shall uphold its Obligations under this Contract in a timely and workmanlike manner, using knowledge and recommendations for performing the services which meet generally acceptable standards set forth by EOSIO Blockchain Block Producers.
  
### Default
DEFAULT. The occurrence of any of the following shall constitute a material default under this Contract: 

### Remedies
REMEDIES. In addition to any and all other rights a party may have available according to law, if a party defaults by failing to substantially perform any provision, term or condition of this Contract, the other party may terminate the Contract by providing written notice to the defaulting party. This notice shall describe with sufficient detail the nature of the default. The party receiving such notice shall promptly be removed from being a Block Producer and this Contract shall be automatically terminated. 
  
### Force Majeure
FORCE MAJEURE. If performance of this Contract or any obligation under this Contract is prevented, restricted, or interfered with by causes beyond either party's reasonable control ("Force Majeure"), and if the party unable to carry out its obligations gives the other party prompt written notice of such event, then the obligations of the party invoking this provision shall be suspended to the extent necessary by such event. The term Force Majeure shall include, without limitation, acts of God, fire, explosion, vandalism, storm or other similar occurrence, orders or acts of military or civil authority, or by national emergencies, insurrections, riots, or wars, or strikes, lock-outs, work stoppages, or supplier failures. The excused party shall use reasonable efforts under the circumstances to avoid or remove such causes of non-performance and shall proceed to perform with reasonable dispatch whenever such causes are removed or ceased. An act or omission shall be deemed within the reasonable control of a party if committed, omitted, or caused by such party, or its employees, officers, agents, or affiliates. 
  
### Dispute Resolution
DISPUTE RESOLUTION. Any controversies or disputes arising out of or relating to this Contract will be resolved by binding arbitration under the default rules set forth by the EOSIO Blockchain. The arbitrator's award will be final, and judgment may be entered upon it by any court having proper jurisdiction. 
  
### Entire Agreement
ENTIRE AGREEMENT. This Contract contains the entire agreement of the parties, and there are no other promises or conditions in any other agreement whether oral or written concerning the subject matter of this Contract. This Contract supersedes any prior written or oral agreements between the parties. 

### Severability
SEVERABILITY. If any provision of this Contract will be held to be invalid or unenforceable for any reason, the remaining provisions will continue to be valid and enforceable. If a court finds that any provision of this Contract is invalid or unenforceable, but that by limiting such provision it would become valid and enforceable, then such provision will be deemed to be written, construed, and enforced as so limited. 

### Amendment
AMENDMENT. This Contract may be modified or amended in writing by mutual agreement between the parties, if the writing is signed by the party obligated under the amendment. 

### Governing Law
GOVERNING LAW. This Contract shall be construed in accordance with the Maxims of Equity. 

### Notice
NOTICE. Any notice or communication required or permitted under this Contract shall be sufficiently given if delivered to a verifiable email address or to such other email address as one party may have publicly furnished in writing, or published on a broadcast contract provided by this blockchain for purposes of providing notices of this type. 
  
### Waiver of Contractual Right
WAIVER OF CONTRACTUAL RIGHT. The failure of either party to enforce any provision of this Contract shall not be construed as a waiver or limitation of that party's right to subsequently enforce and compel strict compliance with every provision of this Contract. 

### Arbitrator's Fees to Prevailing Party
ARBITRATOR’S FEES TO PREVAILING PARTY. In any action arising hereunder or any separate action pertaining to the validity of this Agreement, both sides shall pay half the initial cost of arbitration, and the prevailing party shall be awarded reasonable arbitrator's fees and costs.
  
### Construction and Interpretation
CONSTRUCTION AND INTERPRETATION. The rule requiring construction or interpretation against the drafter is waived. The document shall be deemed as if it were drafted by both parties in a mutual effort. 
  
### In Witness Whereof
IN WITNESS WHEREOF, the parties hereto have caused this Agreement to be executed by themselves or their duly authorized representatives as of the date of execution, and authorized as proven by the cryptographic signature on the transaction that invokes this contract.

```