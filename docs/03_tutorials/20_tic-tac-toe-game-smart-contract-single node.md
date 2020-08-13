---
content_title: "Tic-tac-toe Game Contract Using Single Node"
link_text: "Tic-tac-toe Game Contract Using Single Node"
---

# Your Guide to Tic-tac-toe on EOSIO 
This tic-tac-toe tutorial guides you step by step to build a tic-tac-toe game which runs on an EOSIO blockchain. You create a smart contract containing the game logic, then compile and deploy this smart contract to an EOSIO blockchain. In this tutorial we use a local [single node testnet](https://developers.eos.io/manuals/eos/latest/nodeos/usage/development-environment/local-single-node-testnet#gatsby-focus-wrapper) and show you how to play the game by calling the smart contract. [Getting Started](https://developers.eos.io/welcome/latest/getting-started/index) also uses a single node testnet.

[[note]]
| EOSIO is blockchain software platform developed by block.one. Smart contracts which run on EOSIO will run on any blockchain which is run on the EOSIO platform. EOS is a digital token, though it also refers to the first public blockchain run on the EOSIO platform, EOS or the public mainnet. In this tutorial we will use the EOSIO platform to run a blockchain on your local machine. This runs only one producing node and is commonly called a single node testnet.


We explain the purpose of each step and why it is important.

## Prerequisites for the Tutorial
This tutorial requires the following tools and knowledge:

* EOSIO platform software, specifically cleos, keosd and eosio.cdt which compiles the smart contract. Click on this link to [Install the CDT.](https://developers.eos.io/welcome/latest/getting-started/development-environment/install-the-CDT "EOSIO.CDT Installation Instructions") Click on this link for an [overview of the EOSIO platform and tool.](https://developers.eos.io/welcome/latest/overview/platform_and_toolchain)
* Knowledge of the C++ programming language
* A code editor or an IDE. Click on this link for more information [EOSIO Prerequisites](https://developers.eos.io/welcome/latest/getting-started/development-environment/introduction "Set up to use EOSIO")
   
### Tutorial Workflow

```sequence
Understand\n Game->Understand\n EOSIO : What?
Understand\n EOSIO->Create\nAccounts  : Accounts
Understand\n EOSIO->Create\nAccounts  : Actions
Understand\n EOSIO->Create\nAccounts  : Resources
Create\nAccounts->Create\nSmart Contract : How?
Create\nSmart Contract -> Compile\nDeploy : Code
Compile\nDeploy -> Play\nGame : Load
Play\nGame -> Play\nGame : Push
Play\nGame -> Play\nGame : Get
```

## The Rules of the Game
The EOSIO tic-tac-toe rules are:

* Player one (the host) makes the first move, followed by player two (the challenger). 
* The first player to complete a row or diagonal of either X’s or O’s wins the game.
* If no player completes a row or diagonal of either X’s or O’s, the game is a draw. 

## Understand how the game works
The smart contract contains the game logic, therefore this section introduces how the game works. 

The game is played by two players, so we need two blockchain accounts. This tutorial explains how to create and use these blockchain accounts on a local single node blockchain in the next step. Use these accounts to "push actions" to the blockchain. These actions 'start', 'restart', and 'close' the game. Pushing a 'move' action will place a 'marker' on the game 'board'.    

One player is the host, who starts the game, and one player is the challenger. The game board is nine squares, and each player takes a turn to place their marker in a square. A player wins the game when three markers are placed in a row.

In the example below the player who placed x has won.

| Row       | 0     | 1     | 2     |
| :-------: | :---: | :---: | :---: |
|     0     |   -   |   o   |   x   |
|     1     |   -   |   x   |   -   |
|     2     |   x   |   o   |   o   |

When all the squares contain a marker and no player has three markers in a row, then the game is a draw.

### Accounts, key pairs, and secure your private key
Accounts are stored on the blockchain with a public key. Use a private key to access the account, though be sure to secure your private key. For more information about account and permissions click on this link [Accounts and Permissions](https://developers.eos.io/welcome/latest/protocol/accounts_and_permissions "Accounts and Permissions Overview")

### Smart Contract Actions
A smart contract exposes methods or ‘actions’ that transactions use to operate business logic. Transactions may contain one or more ‘actions’. Transactions are generated dynamically outside the smart contract, within an application, or from the command line to call smart contract actions and execute business logic within a smart contract. Transactions are atomic. For example, if one action of a transaction fails the entire transaction, each action in the transaction, is rolled back. For more details about transactions and actions click on this link [Transaction Protocol.](https://developers.eos.io/welcome/latest/protocol/transactions_protocol "Tranasctions Protocol") You can use cleos to create transactions and push transactions to the blockchain. Transactions contain one or more actions. You can also use Cleos to call actions directly. Actions can call other actions and can call actions from other smart contracts.

![Transactions and Actions](./resources/tictactoe/transactions-and-actions-temp.png "Transactions and Actions")

### EOSIO Resources 
The EOSIO blockchain accounts own and consume three resources:

* RAM - This resource is the amount of RAM available to an account. RAM stores smart contracts loaded on the blockchain. Smart contacts use RAM via the multi-index table to store smart contract state. Spend TNT to purchase more RAM, RAM can be sold.
* CPU - This resource is the amount of CPU which can be used by an account in each 24 hour period. Transactions consume CPU. Stake TNT for more CPU. Unstaking returns CPU. 
* NET - This resource is the amount of data which can be written to blockchain blocks by an account in each 24 hour period. The blockchain blocks store transactions and transaction parameters, the history of blockchain . Stake TNT for more NET. Unstaking returns NET.

For more information click on this link [Core Concepts](https://developers.eos.io/welcome/latest/overview/core_concepts)

## Create the necessary accounts and key pairs
The game requires two accounts, one for each player, and each account requires at least one key pair (public and private keys.) One account 'owns' the smart contract, a blockchain account supports only one smart contract and a smart contract must be loaded by an account. Accounts then identify which player ‘pushes’ a transaction to the blockchain. An account is created by calling an EOSIO system contract and this action requires a public key which is stored on the blockchain.  The blockchain then uses asymmetric cryptography to verify that the account pushing the transaction is signed with the matching private key and has the required authority to perform an action.  

### Run a local single node testnet
Run [nodeos](https://developers.eos.io/manuals/eos/latest/nodeos/index) locally to start a blockchain running with a single node. [Configure nodeos](https://developers.eos.io/manuals/eos/latest/nodeos/usage/nodeos-configuration) with [plugins](https://developers.eos.io/manuals/eos/latest/nodeos/plugins/index) to produce blocks, store a history of the blockchain in memory, provide http rpc access to these plugins and to output running information to a file.

```shell
nodeos -e -p eosio --plugin eosio::producer_plugin --plugin eosio::producer_api_plugin --plugin eosio::chain_api_plugin --plugin eosio::http_plugin --plugin eosio::history_plugin --plugin eosio::history_api_plugin --filter-on="*" --access-control-allow-origin='*' --contracts-console --http-validate-host=false --verbose-http-errors >> nodeos.log 2>&1 &
```
Look at the nodeos.log file to ensure nodeos is running and producing blocks, the ouput will look like:

```console
info  2020-08-10T07:57:04.561 thread-0  http_plugin.cpp:895           add_handler          ] add api url: /v1/history/get_key_accounts
info  2020-08-10T07:57:04.561 thread-0  http_plugin.cpp:895           add_handler          ] add api url: /v1/history/get_transaction
info  2020-08-10T07:57:04.561 thread-0  net_plugin.cpp:3414           plugin_startup       ] my node_id is 12eac267ddd48fbda96d0cdd9e4e231d2bfd72f8c0bdbee1987d8952f8be10dc
info  2020-08-10T07:57:04.562 thread-0  net_plugin.cpp:3470           plugin_startup       ] starting listener, max clients is 25
info  2020-08-10T07:57:04.563 thread-0  http_plugin.cpp:794           operator()           ] start listening for http requests
info  2020-08-10T07:57:04.563 thread-0  http_plugin.cpp:895           add_handler          ] add api url: /v1/node/get_supported_apis
info  2020-08-10T07:57:04.902 thread-0  producer_plugin.cpp:2134      produce_block        ] Produced block 94febe2c222c42a7... #2 @ 2020-08-10T07:57:05.000 signed by eosio [trxs: 0, lib: 1, confirmed: 0]
info  2020-08-10T07:57:05.301 thread-0  producer_plugin.cpp:2134      produce_block        ] Produced block 602b3c6b86d28a20... #3 @ 2020-08-10T07:57:05.500 signed by eosio [trxs: 0, lib: 2, confirmed: 0]
info  2020-08-10T07:57:05.901 thread-0  producer_plugin.cpp:2134      produce_block        ] Produced block 320d2f4119d18816... #4 @ 2020-08-10T07:57:06.000 signed by eosio [trxs: 0, lib: 3, confirmed: 0]
info  2020-08-10T07:57:06.400 thread-0  producer_plugin.cpp:2134      produce_block        ] Produced block 3fa7c7d9f2c1c2da... #5 @ 2020-08-10T07:57:06.500 signed by eosio [trxs: 0, lib: 4, confirmed: 0]
info 
```

[[info]]
| Account creation requires a creator account; every new blockchain is created with an account called eosio. The eosio account is a special account that can be used to bootstrap a blockchain, click the following link for more information about [bootstrapping a blockchain for real world use.](https://developers.eos.io/welcome/latest/tutorials/bios-boot-sequence) In a production blockchain the eosio account keys are [resigned](https://developers.eos.io/welcome/latest/tutorials/bios-boot-sequence#3-resign-eosio-account-and-system-accounts).  To use our local single node testnet we need to add the private key of the eosio account to our wallet so that we can create other accounts. **The private key is well known and so any blockchain where the eosio acount has not been resigned is not secure.**

[[caution]]
| The eosio private key is **5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3**

### Import the eosio private key
```shell
cleos wallet import --name local 5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
``` 


### Procedure to create Accounts
1. Create a wallet - [How To Create A Wallet](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-create-a-wallet)
2. Create key pair - [How To Create Key Pairs](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-create-key-pairs)
3. Create the account - [How To Create An Account](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-create-an-account#gatsby-focus-wrapper)
4. Import the account private key to the wallet - [How To Import A Key](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-import-a-key)

For this tutorial we need to create two accounts
1. The host - the host will load the smart contract
2. The challenger - the challenger will play the game with the host.

#### Commands
To use the command line to create the accounts run the following commands. Make sure that the local wallet is [open](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/wallet/open) and [unlocked](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/wallet/unlock) and run these commands to create the accounts with the private keys stored in the local wallet.

Create a wallet called 'local'.

```shell
cleos wallet create --name local --to-console
```

This command outputs to stdout
```console
Creating wallet: local
Save password to use in the future to unlock this wallet.
Without password imported keys will not be retrievable.
"PW5K8dtLxB8q56JbT8UA5FQyDykNT24LS6i6gcBuxbYSixFgEpFa7"
```

Save the password, you will need this to unlock the wallet later.

To check the wallet run
```shell 
cleos wallet list
```

The output shows two wallets, one for each version of this tutorial, and * shows that the local wallet is unlocked.
```console
Wallets:
[
  "local *",
  "testnet"
]
```
Create two key pairs, one for each account.

```shell
cleos create key --to-console
```
```console
Private key: 5JSRUrUVbRsV2yJ2XSMtRtPzQ5UKbSYEGEjdKfGMS1xsvRZj7FH
Public key: EOS5p55prHwrN6KosqF4NdRayVW2mqwA8RGNEbaZXRBs2SQHwBWSf
```
```shell
cleos create key --to-console
```
```console
Private key: 5JReVMTiiztAUyQGp9w7BMMm1HVUurDmEKuSL53DQww3JKVZjot
Public key: EOS7qkiVnptc8wbHzHPC9jj1YECKJgQeUktBTm8RDA64oH3e75QW5
```

Create the host account.  
```shell
cleos create account eosio host EOS5p55prHwrN6KosqF4NdRayVW2mqwA8RGNEbaZXRBs2SQHwBWSf
```

Import the matching private key to the local wallet
```shell
cleos wallet import --name local --private-key 5JSRUrUVbRsV2yJ2XSMtRtPzQ5UKbSYEGEjdKfGMS1xsvRZj7FH
```

Create the challenger account and import a private key into the local wallet. 
```shell
cleos create account eosio challenger EOS7qkiVnptc8wbHzHPC9jj1YECKJgQeUktBTm8RDA64oH3e75QW5
```

Import the matching private key to the local wallet
```shell
cleos wallet import --name local --private-key 5JReVMTiiztAUyQGp9w7BMMm1HVUurDmEKuSL53DQww3JKVZjot
```

[[note | Note]]
| You can also use three or more accounts, one for the smart contract and separate accounts for the host(s) and the challenger(s).

[[warning | Keep your keys safe]]
| Use a wallet to securely store private keys. Keep your private keys private and do not share your private keys with anyone. A private key provides full access to a blockchain account.

## Tic-tac-toe Smart Contract
Once you have your eosio accounts you can create the smart contract. Use your favorite text editor of IDE to create the .hpp and.cpp files.

### Smart Contract Requirements
The tictactoe.hpp file (or header file) contains the declarations of the smart contract. Declarations inform the smart contract compiler what data structures to use in the smart contract to represent the game board and track game play. The header file also declares the smart contract actions that operate the game.

The tictactoe.cpp file contains implementations of the smart contract actions declared in the tictactoe.hpp header file and uses the data structures declared in the header file.

The “Compile and deploy the smart contract to the blockchain” section details compilation of the files. The compiler is the eosio-cpp tool from the EOSIO.CDT. Click on this link for more information on the [EOSIO.CDT](https://developers.eos.io/manuals/eosio.cdt/latest/index "EOSIO.CDT documentation") . The EOSIO.CDT builds the smart contract and creates an ABI file. Click on this link for more information about [ABI Files](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/understanding-ABI-files "Understand ABL Files") 

### Game Board Representation
A std::vector represents the tic-tac-toe board. The number 0 marks an empty square. The number 1 denotes a movement by the host. The number 2 denotes a movement by the challenger. To make a movement, you push a  transaction to the tic-tac-toe smart contract.

Logically the board looks like:

| Row       | 0     | 1     | 2     |
| :-------: | :---: | :---: | :---: |
|     0     |   -   |   -   |   -   |
|     1     |   -   |   -   |   -   |
|     2     |   -   |   -   |   -   |

This board is represented as a std::vector of integers with the positions in the following order:
 
[0,0] [0,1] [0,2] [1,0] [1,1] [1,2] [2,0] [2,1] [2,2]

For example, in the above game board illustration 

* An empty board is represented as [0, 0, 0, 0, 0, 0, 0, 0, 0].
* The host takes the first move and marks their square with an X in row 0, column 2, which results in an array represented as [0, 0, 1, 0, 0, 0, 0, 0, 0].
* The challenger takes the next move and marks their square with an O in row 0, column 1 which results in an array represented as [0, 2, 1, 0,  0, 0, 0, 0, 0].

At the end of a drawn game, the board array may be  represented as [1, 2, 1, 1, 2, 2, 2, 1, 1] 

Array Representation

| Row       | 0     | 1     | 2     |
| :-------: | :---: | :---: | :---: |
|     0     |   1   |   2   |   1   |
|     1     |   1   |   2   |   2   |
|     2     |   2   |   1   |   1   |

Game Representation

| Row       | 0     | 1     | 2     |
| :-------: | :---: | :---: | :---: |
|     0     |   x   |   o   |   x   |
|     1     |   x   |   o   |   o   |
|     2     |   o   |   x   |   x   |

### Create tictactoe.hpp file
This section creates the tictactoe.hpp file. This header file contains the declarations of the tictactoe class, the definitions of tictactoe game data structures, and the declarations of tictactoe game methods, known as actions in EOSIO smart contracts.


#### Game Data Structures
The tic-tac-toe smart contract hpp file defines the following public data structures to store game information.  

* game - The game data structure contains game data. The structure has variables of type eosio::name, for challenger, host, turn and winner. Click on this link for a definition of [eosio::name](https://developers.eos.io/manuals/eosio.cdt/v1.7/structeosio_1_1name "eosio.cdt reference - name structure") . The structure has a vector representing the game board  
* Games - Games is a type definition that uses a class template. Games uses an eosio::muti_index template to define a type which stores a game structure in RAM. Click on this link for more information on [eosio::multi_index](https://developers.eos.io/manuals/eosio.cdt/v1.7/group__multiindex "eosio.cdt reference - multi index table") and click on this link for more general information about [multi index tables](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/data-persistence) 

#### Game Actions
The tic-tac-toe smart contract hpp file defines the following four public actions to operate the game logic.  

* Create - This action launches a new game and creates a new game board array. The host may use this command.
* Restart - This action clears data from an existing game board array. The host or the challenger may use this command.
* Close - This action deletes and removes existing game data and frees up any storage the game uses. No game data persists. The host may use this command.
* Move - This action sets a marker on the gameboard and updates the game board array. The host or the challenger may use this command.

### Procedure to create the tictactoe.hpp file
Complete the following steps to create the tictactoe.hpp file:

1. Create a tictactoe folder on your local drive.
2. Change directory into the tictactoe folder. 
3. Create the tictactoe.hpp file.
4. Open the tictactoe.hpp file with your text editor.
5. Import the eosio base library.
   Add this code to the .hpp file:

```c++
// 5. Import the eosio base library.
#include <eosio/eosio.hpp>
```

6. For convenience use the eosio namespace.
   Add this code to the .hpp file:

```c++
//6. use the eosio namespace
using namespace eosio;
```

7. Declare the class.
8. Use the [[eosio::contract(contract_name)]] attribute lets compiler know this is a smart contract and that the compiler should generate the main dispatcher and the ABI. Click on this link for more information on [generator attributes.](https://developers.eos.io/manuals/eosio.cdt/v1.6/guides/generator-attributes) 
9. Inherit from the eosio::contract public base class.
10. Introduce base class members.
11. Use the base class constructor.
    Add this code to the .hpp file:

```c++
// 7. Declare the class. 8. Use the [[eosio::contract(contract_name)]] attribute. 9. Inherit from the base class. 
class[[eosio::contract("tictactoe")]] TicTacToe : public contract
{
public:
    
    // 10 Introduce base class members. 
    using contract::contract;
    
    // 11. Use the base class constructor.
    TicTacToe(name receiver, name code, datastream<const char *> ds) : contract(receiver, code, ds) {}
};
```
12. Declare game data structure and use the [[eosio::table]] attribute to let the compiler know this uses a multi index table. Click on this link for more information on [generator attributes.](https://developers.eos.io/manuals/eosio.cdt/v1.6/guides/generator-attributes) Click on this link for more information about [Multi Index Table](https://developers.eos.io/manuals/eosio.cdt/v1.7/group__multiindex)
13. Create a **primary_key** method. This is automatically used as an index for the table.
14. Use the EOSLIB_SERIALIZE macro to define how the data is serialized / deserialized in and out of the multi index table.  Click on this link for more information about [EOSLIB_SERIALIZE](https://developers.eos.io/manuals/eosio.cdt/v1.7/group__serialize)

    Add this code to the .hpp file inside the public section of the class:

```c++
    // 12. Declare game data structure.
    struct [[eosio::table]] game
    {
        static constexpr uint16_t boardWidth = 3;
        static constexpr uint16_t boardHeight = boardWidth;
        
        game() : board(boardWidth * boardHeight, 0){}

        name challenger, host, turn; // = account name of host, challenger and turn to store whose turn it is.
        name winner = none; // = none/ draw/ name of host/ name of challenger

        std::vector<uint8_t> board;

        // Initialize the board with empty cell
        void initializeBoard(){
            board.assign(boardWidth * boardHeight, 0);
        }

        // Reset game
        void resetGame(){
            initializeBoard();
            turn = host;
            winner = "none"_n;
        }

        // 13. primary key accessor
		auto primary_key() const { return challenger.value; }

        //14. EOSLIB_SERIALIZE macro defining how the abi serializes / deserializes  
		EOSLIB_SERIALIZE( game, (challenger)(host)(turn)(winner)(board))
    };
```

15. Define the games type which uses the game data structure with the multi-index table template. Click on this link for more information about the multi-index table template used to define multi index table types [function multi_index.](https://developers.eos.io/manuals/eosio.cdt/v1.7/group__multiindex/#function-multi_index) Set the name to "games" and use the [eosio::name](https://developers.eos.io/manuals/eosio.cdt/v1.5/structeosio_1_1name) operator [_n](https://developers.eos.io/manuals/eosio.cdt/v1.5/name_8hpp#function-operator_n) to construct an [eosio::name](https://developers.eos.io/manuals/eosio.cdt/v1.5/structeosio_1_1name) with a string. The value is stored as a uint64_t. 
    Add this code to the .hpp file inside the public section of the class, after the declaration of the game structure:

```c++
    // 15. Define the game data structure using the multi-index table template.
    typedef eosio::multi_index<"games"_n, game> games;
```

16. Declare class methods and use the [[eosio::action]] attribute to let the compiler know this is a smart contract action. Click on this link for more information on [generator attributes.](https://developers.eos.io/manuals/eosio.cdt/v1.6/guides/generator-attributes) 
    Add this code to the .hpp file inside the public section of the class:

```c++
    [[eosio::action]]
    void create(const name &challenger, name &host);
    
    [[eosio::action]]
    void restart(const name &challenger, const name &host, const name &by);

    [[eosio::action]]
    void close(const name &challenger, const name &host);
    
    [[eosio::action]]   
    void move(const name &challenger, const name &host, const name &by, const uint16_t &row, const uint16_t &column);
```

17. The Move action uses the following private supporting methods to determine if a move is valid. They also check for a winning move:
    * IsEmptyCell()
    * IsValidMove()
    * GetWinner()
    Add this code to the .hpp file inside a private section of the class:

```c++
    bool IsEmptyCell(const uint8_t &cell);
    bool IsValidMove(const uint16_t &row, const uint16_t &column, const std::vector<uint8_t> &board);
    name GetWinner(const game &currentGame);
```

The complete tictactoe.hpp file can be downloaded from github here: [Tic-tac-toe tutorial hpp source](./src/tictactoe/tictactoe.hpp "tic-tac-toe example code")  

### Create tictactoe.cpp file
This section creates the tictactoe.cpp file. This file contains the implementations of the tic-tac-toe smart contract actions and the private methods used by the smart contract actions, based the declarations in the header file.

### Procedure to create the tictactoe.cpp file
Complete the following steps to create the tictactoe.cpp file:

1. Ensure you are in the tictactoe folder. 
2. Create the tictactoe.cpp file.
3. Open the tictactoe.cpp file with your text editor.
4. Import the tictactoe.hpp file and make the tictactoe definitions from the previous section available.
   Add this code to the .cpp file: 

```c++
#include "tictactoe.hpp"
```
5. Implement Create.
   * Ensure that the action has the signature from the host
   * Ensure that the challenger and host are not the same player
   * Ensure that there is no existing game
   * Store the newly created game to the multi index table

   Add this code to the .cpp file:

```c++
void tictactoe::create(const name &challenger, name &host) {
    require_auth(host);
    check(challenger != host, "Challenger should not be the same as the host.");

    // Check if game already exists
    games existingHostGames(get_self(), host.value);
    auto itr = existingHostGames.find(challenger.value);
    check(itr == existingHostGames.end(), "Game already exists.");

    existingHostGames.emplace(host, [&](auto &g) {
        g.challenger = challenger;
        g.host = host;
        g.turn = host;
    });
}
```

6. Implement Restart.
   * Ensure that the action has the signature from the host/challenger
   * Ensure that the game exists
   * Ensure that the restart action is done by host/challenger
   * Reset the game
   * Store the updated game to the multi index table

   Add this code to the .cpp file:

```c++
void tictactoe::restart(const name &challenger, const name &host, const name &by){
    check(has_auth(by), "Only " + by.to_string() + "can restart the game.");

    // Check if game exists
    games existingHostGames(get_self(), host.value);
    auto itr = existingHostGames.find(challenger.value);
    check(itr != existingHostGames.end(), "Game does not exist.");

    // Check if this game belongs to the action sender
    check(by == itr->host || by == itr->challenger, "This is not your game.");

    // Reset game
    existingHostGames.modify(itr, itr->host, [](auto &g) {
        g.resetGame();
    });
}
```


7. Implement Close.
   * Ensure that the action has the signature from the host
   * Ensure that the game exists
   * Remove the game from the db

   Add this code to the .cpp file:

```c++
void tictactoe::close(const name &challenger, const name &host){
    check(has_auth(host), "Only the host can close the game.");

    require_auth(host);

    // Check if game exists
    games existingHostGames(get_self(), host.value);
    auto itr = existingHostGames.find(challenger.value);
    check(itr != existingHostGames.end(), "Game does not exist.");

    // Remove game
    existingHostGames.erase(itr);
}
```

8. Implement Move supporting methods.
   * Implement IsValidMove.
   Add this code to the .cpp file:

```c++
bool tictactoe::IsEmptyCell(const uint8_t &cell){
    return cell == 0;
}
``` 
   * Implement IsValidMove
   Add this code to the .cpp file:

```c++
bool tictactoe::IsValidMove(const uint16_t &row, const uint16_t &column, const std::vector<uint8_t> &board){
    uint32_t movementLocation = row * game::boardWidth + column;
    bool isValid = movementLocation < board.size() && IsEmptyCell(board[movementLocation]);
    return isValid;
}
```
   * Implement getWinner. The winner is the first player who places three of their marks in a horizontal, vertical, or diagonal row.

   Add this code to the .cpp file:

```c++
name tictactoe::GetWinner(const game &currentGame)
{
    auto &board = currentGame.board;

    bool isBoardFull = true;

    // Use bitwise AND operator to determine the consecutive values of each column, row and diagonal
    // Since 3 == 0b11, 2 == 0b10, 1 = 0b01, 0 = 0b00
    std::vector<uint32_t> consecutiveColumn(game::boardWidth, 3);
    std::vector<uint32_t> consecutiveRow(game::boardHeight, 3);
    uint32_t consecutiveDiagonalBackslash = 3;
    uint32_t consecutiveDiagonalSlash = 3;

    for (uint32_t i = 0; i < board.size(); i++)
    {
        isBoardFull &= IsEmptyCell(board[i]);
        uint16_t row = uint16_t(i / game::boardWidth);
        uint16_t column = uint16_t(i % game::boardWidth);

        // Calculate consecutive row and column value
        consecutiveRow[column] = consecutiveRow[column] & board[i];
        consecutiveColumn[row] = consecutiveColumn[row] & board[i];
        // Calculate consecutive diagonal \ value
        if (row == column)
        {
            consecutiveDiagonalBackslash = consecutiveDiagonalBackslash & board[i];
        }
        // Calculate consecutive diagonal / value
        if (row + column == game::boardWidth - 1)
        {
            consecutiveDiagonalSlash = consecutiveDiagonalSlash & board[i];
        }
    }

    // Inspect the value of all consecutive row, column, and diagonal and determine winner
    std::vector<uint32_t> aggregate = {consecutiveDiagonalBackslash, consecutiveDiagonalSlash};
    aggregate.insert(aggregate.end(), consecutiveColumn.begin(), consecutiveColumn.end());
    aggregate.insert(aggregate.end(), consecutiveRow.begin(), consecutiveRow.end());

    for (auto value : aggregate)
    {
        if (value == 1)
        {
            return currentGame.host;
        }
        else if (value == 2)
        {
            return currentGame.challenger;
        }
    }
    // Draw if the board is full, otherwise the winner is not determined yet
    return isBoardFull ? draw : none;
}
```

9. Implement Move.
   * Ensure that the action has the signature from the host/ challenger
   * Ensure that the game exists
   * Ensure that the game is not finished yet
   * Ensure that the move action is done by host or challenger
   * Ensure that this is the right user's turn
   * Verify movement is valid 
   * Update board with the new move
   * Change the move_turn to the other player
   * Determine if there is a winner
   * Store the updated game to the multi index table

   Add this code to the .cpp file:

```c++
void tictactoe::move(const name &challenger, const name &host, const name &by, const uint16_t &row, const uint16_t &column){
    check(has_auth(by), "The next move should be made by " + by.to_string());

    // Check if game exists
    games existingHostGames(get_self(), host.value);
    auto itr = existingHostGames.find(challenger.value);
    check(itr != existingHostGames.end(), "Game does not exist.");

    // Check if this game hasn't ended yet
    check(itr->winner == none, "The game has ended.");
    
    // Check if this game belongs to the action sender
    check(by == itr->host || by == itr->challenger, "This is not your game.");
    // Check if this is the  action sender's turn
    check(by == itr->turn, "it's not your turn yet!");

    // Check if user makes a valid movement
    check(IsValidMove(row, column, itr->board), "Not a valid movement.");

    // Fill the cell, 1 for host, 2 for challenger
    //TODO could use constant for 1 and 2 as well
    const uint8_t cellValue = itr->turn == itr->host ? 1 : 2;
    const auto turn = itr->turn == itr->host ? itr->challenger : itr->host;
    existingHostGames.modify(itr, itr->host, [&](auto &g) {
        g.board[row * game::boardWidth + column] = cellValue;
        g.turn = turn;
        g.winner = GetWinner(g);
    });
}
```
The complete tictactoe.cpp file can be downloaded from github here: [Tic-tac-toe tutorial cpp source](./src/tictactoe/tictactoe.cpp "tic-tac-toe example code")  


## Compile and deploy the smart contract to the blockchain
To deploy the smart contract to the blockchain first use the EOSIO.CDT (EOSIO Contract Development Toolkit) eosio-cpp tool to build the .wasm file and a corresponding .abi file. Click on this link for details on [eosio-cpp tool](https://developers.eos.io/manuals/eosio.cdt/latest/command-reference/eosio-cpp "eosio-cdt reference eosio-cpp tool") and click on this link for details about the [EOSIO.CDT](https://developers.eos.io/manuals/eosio.cdt/latest/index "Contract Development Toolkit")

The .wasm file (or webassembly) is the binary code that the wasm engine in the blockchain executes. The webassembly engine currently used in eosio is [eos-vm](https://github.com/EOSIO/eos-vm "git eos-vm"). The application binary interface or .abi file defines how to pack and unpack the data used by a smart contract see [Understanding ABI Files](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/understanding-ABI-files "Getting Started - ABI files") for more information.     

### Compile the Smart Contract Code
To compile the smart contract change to the tictactoe folder  and run eosio-cpp. Click on this link for more information about using the eosio-cpp: [eosio-cpp tool](https://developers.eos.io/manuals/eosio.cdt/latest/command-reference/eosio-cpp "eosio-cpp command reference") .This tutorial uses .hpp or header files, use the “-I” option to tell the compiler where the .hpp file is located.

```shell
tictactoe$ eosio-cpp -I ./ tictactoe.cpp
```

The output from this command is:

```console
Warning, empty ricardian clause file
Warning, empty ricardian clause file
Warning, action <create> does not have a ricardian contract
Warning, action <restart> does not have a ricardian contract
Warning, action <close> does not have a ricardian contract
Warning, action <move> does not have a ricardian contract
```

For this tutorial we ignore these warnings. Click on the following link for a tutorial showing how to add the optional ricardian contracts [Prepare the Ricardian Contract](https://developers.eos.io/welcome/latest/getting-started/smart-contract-development/data-persistence#step-10-prepare-the-ricardian-contract-optional "Getting Started - Data Peristence")

The tictactoe directory now contains two new files, tictactoe.wasm and tictactoe.abi.

### Deploy the Smart Contract to the Testnet
[Deploy the smart contract](https://developers.eos.io/manuals/eos/latest/cleos/how-to-guides/how-to-deploy-a-smart-contract) on the single node testnet with the following commandline.

In the smae directory as the generated wasm and ABI files run
```shell
cleos set contract host ./ tictactoe.wasm tictactoe.abi -p host@active
```

## Play The Game
Now that the smart contract has been successfully deployed, [push smart contract actions](https://developers.eos.io/manuals/eos/latest/cleos/command-reference/push/push-action) to the blockchain to play the game.  


### Push 'create' to the single node testnet to create a game
A game requires a host and a challenger. Use the accounts created earlier in the “Create the necessary accounts and key pairs” sectio of the tutorial for these. These accounts use arbitrary names. In this example assume the host has the account name of ‘mcazyfujecke’ and the challenger has the account name of ‘vswlkiegwdsk’.

The create action takes two parameters, the "challenger" and the "host". The required payload in json format is:

```json
{
  "challenger": "challenger",
  "host": "host"
}
```

Sign the push action with host@active’, the host of the game.

```shell
cleos push action tictactoe create '{"challenger":"challenger", "host":"host"}' --permission host@active
```

### Push 'move' to the single node testnet to make game moves
Players make moves in turn by pushing ‘move’ actions to the blockchain. The host moves first, and each move must be signed by the appropriate account.

The move action takes five parameters, the "challenger", the "host", the player who makes the move or "by" and "row" and "column" parameters to show where the marker is placed.

The host makes the first move. The required payload in json format is:

```json
{
  "challenger": "challenger",
  "host": "host",
  "by": "host",
  "row": 0,
  "column": 1
}
```

Sign the push action with host@active’ - the host of the game.

```shell
cleos push action tictactoe move '{"challenger":"challenger", "host":"host", "by":"host", "row":0, "column":1}' --permission host@active
```

The challenger makes the second move. The required payload in json format is:

```json
{
  "challenger": "challenger",
  "host": "host",
  "by": "challenger",
  "row": 1,
  "column": 1
}
```

Sign the push action with challenger@active’ - the challenger.

```shell
cleos push action tictactoe move '{"challenger":"challenger", "host":"host", "by":"challenger", "row":1, "column":1}' --permission challenger@active
```

Continue to make moves until the game ends with a win or a draw.

### Check game status 
Look at the data in the multi index table to check the game status. 

```shell
cleos get table tictactoe host games
```

### Push "restart" to the Testnet to restart the Game
The restart action takes three parameters, the "challenger", the "host", and "by". The required payload in json format is:

```json
{
  "challenger": "challenger",
  "host": "host",
  "by": "host"
}
```

Sign the push action with host@active’ - the host of the game.

```shell
cleos push action tictactoe restart '{"challenger":"challenger", "host":"host", "by":"host"}' --permission host@active
```

Check the game status to see that the board has been reset.

```shell
cleos get table tictactoe host games
```

### Push "close" to the Testnet to close the game
The close action takes two parameters, the "challenger" and the "host". The required payload in json format is:

```json
{
  "challenger": "challenger",
  "host": "host"
}
```

Sign the push action with ‘host@active’ - the host of the game.

```shell
cleos push action tictactoe close '{"challenger":"challenger", "host":"host"}' --permission host@active
```

Check the game status to see that game data has been removed.  

```shell
cleos get table tictactoe host games
```

## Next Steps
Visit the [EOSIO Developer Portal](https://developers.eos.io/ "eosio developers portal") to learn more about EOSIO and try building a more advanced web based game with [Elemental Battles.](https://battles.eos.io/) 
