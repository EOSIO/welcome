---
content_title: "2.10 Creating a Tic-Tac-Toe Smart Contract"
link_text: "2.10 Creating a Tic-Tac-Toe Smart Contract"
---

## Goal

The following tutorial will guide the user to build a sample Player vs Player game contract. We will use tic tac toe game to demonstrate this. The final result of this tutorial can be found at the end of this tutorial.

## Assumption

For this game, we are using a standard 3x3 tic tac toe board. Players are divided into two roles: **host** and **challenger**. The host always makes the first move. Each pair of players can **ONLY** have up to two games at the same time, one where the first player becomes the host and the other one where the second player becomes the host.

### Board

Instead of using `o` and `x` as in the traditional tic tac toe game. We use `1` to denote movement by host, `2` to denote movement by challenger, and `0` to denote empty cell. Furthermore, we will use one dimensional array to store the board. Hence:

|           | (0,0) | (1,0) | (2,0) |
| :-------: | :---: | :---: | :---: |
| **(0,0)** | -     | o     | x     |
| **(0,1)** | -     | x     | -     |
| **(0,2)** | x     | o     | o     |

Assuming x is host, the above board is equal to `[0, 2, 1, 0, 1, 0, 1, 2, 2]`

### Action

A user will have the following actions to interact with this contract:

- create: create a new game
- restart: restart an existing game, host or challenger is allowed to do this
- close: close an existing game, which frees up the storage used to store the game, only host is allowed to do this
- move: make a movement

### Contract account

For the following guide, we are going to push the contract to an account called `tic.tac.toe`.

```bash
cleos create account eosio tic.tac.toe EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
```

Ensure that you have your wallet unlocked and the creator's private active key in the wallet imported, otherwise the above command will fail.

For instructions on wallet unlocking and keys importing, see section [Create Development Wallet](../02_development-environment/05_create-development-wallet.md). 



## Start

We are going to create two files here:

1. **tic.tac.toe.hpp** => header file where the structure of the contract is defined
2. **tic.tac.toe.cpp** => main part of the contract where the action handler is defined

## Defining Structure

Let's first start with the header file and define the structure of the contract. Open **tic.tac.toe.hpp** and start with the following boilerplate:

```cpp
// Import necessary library
#include <eosio/eosio.hpp>

// Generic eosio library, i.e. print, type, math, etc
using namespace eosio;


class[[eosio::contract("tic.tac.toe")]] tic_tac_toe : public contract
{
public:
    using contract::contract;
    tic_tac_toe(name receiver, name code, datastream<const char *> ds) : contract(receiver, code, ds) {}
};
```

### Games Table

For this contract, we will need to have a table that stores a list of games. Let's define it:

```cpp
...
class [[eosio::contract("tictactoe")]] tic_tac_toe : public contract {
   public:
    ...
    typedef eosio::multi_index<"games"_n, game> games;
};
```

- First template parameter  defines the name of the table
- Second template parameter defines the structure that it stores (will be defined in the next section)

### Game Structure

Let's define the structure for the game. Please ensure that this struct definition appears before the table definition in the code.

```cpp
...
class tic_tac_toe : public eosio::contract {
   public:
   ...
    struct [[eosio::table]] game
    {

        static const uint16_t board_width = 3;
        static const uint16_t board_height = board_width;

        game()
        {
            initialize_board();
        }

        name challenger;
        name host;
        name turn;              // = account name of host/ challenger
        name winner = "none"_n; // = none/ draw/ name of host/ name of challenger

        std::vector<uint8_t> board;

        // Initialize board with empty cell
        void initialize_board()
        {
            board = std::vector<uint8_t>(board_width * board_height, 0);
        }

        // Reset game
        void reset_game()
        {
            initialize_board();
            turn = host;
            winner = "none"_n;
        }

        auto primary_key() const { return challenger.value; }
        EOSLIB_SERIALIZE( game, (challenger)(host)(turn)(winner)(board))
    };
};
```

The **primary_key** method is required by the above table definition for games. That is how the table knows what field is the lookup key for the table.

### Action Structure

#### Create

To create the game, we need host account name and challenger's account name.

```cpp
[[eosio::action]]
void create(const name &challenger, name host);
```

#### Restart

To restart the game, we need host account name and challenger's account name to identify the game. Furthermore, we need to specify who wants to restart the game, so we can verify the correct signature is provided.

```cpp
[[eosio::action]]
void restart(const name &challenger, const name &host, const name &by);

```

#### Close

To close the game, we need host account name and challenger's account name to identify the game.

```cpp
[[eosio::action]]
void close(const name &challenger, const name &host);
```

#### Move

To make a move, we need host account name and challenger's account name to identify the game. Furthermore, we need to specify who makes this move and the movement he is making.

```cpp
[[eosio::action]]   
void move(const name &challenger, const name &host, const name &by, const uint16_t &row, const uint16_t &column);
```

### Action Handler

Let's declare the action handler which will be defined in **tic.tac.toe.cpp** later

```cpp
void create(const name &challenger, name host);
void restart(const name &challenger, const name &host, const name &by);
void close(const name &challenger, const name &host);
void move(const name &challenger, const name &host, const name &by, const uint16_t &row, const uint16_t &column);
```

You can see the final tic.tac.toe.hpp in the next section.

## Final Contract Header File

The final state of the tic.tac.toe.hpp should be:

```cpp
// Import necessary library
#include <eosio/eosio.hpp>

// Generic eosio library, i.e. print, type, math, etc
using namespace eosio;

class[[eosio::contract("tic.tac.toe")]] tic_tac_toe : public contract
{
public:
    using contract::contract;
    tic_tac_toe(name receiver, name code, datastream<const char *> ds) : contract(receiver, code, ds) {}

    struct [[eosio::table]] game
    {

        static const uint16_t board_width = 3;
        static const uint16_t board_height = board_width;

        game()
        {
            initialize_board();
        }

        name challenger;
        name host;
        name turn;              // = account name of host/ challenger
        name winner = "none"_n; // = none/ draw/ name of host/ name of challenger

        std::vector<uint8_t> board;

        // Initialize board with empty cell
        void initialize_board()
        {
            board = std::vector<uint8_t>(board_width * board_height, 0);
        }

        // Reset game
        void reset_game()
        {
            initialize_board();
            turn = host;
            winner = "none"_n;
        }

        auto primary_key() const { return challenger.value; }
        EOSLIB_SERIALIZE( game, (challenger)(host)(turn)(winner)(board))
    };

    typedef eosio::multi_index<"games"_n, game> games;

    [[eosio::action]]
    void create(const name &challenger, name host);
    
    [[eosio::action]]
    void restart(const name &challenger, const name &host, const name &by);
    
    [[eosio::action]]
    void close(const name &challenger, const name &host);
 
    [[eosio::action]]   
    void move(const name &challenger, const name &host, const name &by, const uint16_t &row, const uint16_t &column);
};
```

## Contract Implementation

Let's open tic.tac.toe.cpp and set up the boilerplate

```cpp
#include "tic.tac.toe.hpp"
```

### Action Handler

We want tic_tac_toe contract to only react to actions sent to the `tic.tac.toe` account and react differently according to the type of the action. The actions that we want to support are ***create***, ***move***, ***restart***, and ***close***. Let's define the individual action handlers in the next section.

### "create" Action Handler

For the ***create*** action handler, we want to:

1. Ensure that the action has the signature from the host
2. Ensure that the challenger and host are not the same player
3. Ensure that there is no existing game
4. Store the newly created game to the db

```cpp
void tic_tac_toe::create(const name &challenger, name host) {
    require_auth(host);
    check(challenger != host, "challenger shouldn't be the same as host");

    // Check if game already exists
    games existing_host_games(get_self(), host.value);
    auto itr = existing_host_games.find(challenger.value);
    check(itr == existing_host_games.end(), "game already exists");

    existing_host_games.emplace(host, [&](auto &g) {
        g.challenger = challenger;
        g.host = host;
        g.turn = host;
   });
}
```

### "restart" Action Handler

For the ***restart*** action handler, we want to:

1. Ensure that the action has the signature from the host/challenger
2. Ensure that the game exists
3. Ensure that the restart action is done by host/challenger
4. Reset the game
5. Store the updated game to the db

```cpp
void tic_tac_toe::restart(const name &challenger, const name &host, const name &by)
{
    require_auth(by);
    // Check if game exists
    games existing_host_games(get_self(), host.value);
    auto itr = existing_host_games.find(challenger.value);
    check(itr != existing_host_games.end(), "game doesn't exists");

    // Check if this game belongs to the action sender
    check(by == itr->host || by == itr->challenger, "this is not your game!");

    // Reset game
    existing_host_games.modify(itr, itr->host, [](auto &g) {
        g.reset_game();
   });
}
```

### "close" Action Handler

For the ***close*** action handler, we want to:

1. Ensure that the action has the signature from the host
2. Ensure that the game exists
3. Remove the game from the db

```cpp
void tic_tac_toe::close(const name &challenger, const name &host)
{
    require_auth(host);

    // Check if game exists
    games existing_host_games(get_self(), host.value);
    auto itr = existing_host_games.find(challenger.value);
    check(itr != existing_host_games.end(), "game doesn't exists");

    // Remove game
    existing_host_games.erase(itr);
}
```

### "move" Action Handler 

For the ***move*** action handler, we want to:

1. Ensure that the action has the signature from the host/ challenger
2. Ensure that the game exists
3. Ensure that the game is not finished yet
4. Ensure that the move action is done by host/ challenger
5. Ensure that this is the right user's turn
6. Verify movement is valid
7. Update board with the new move
8. Change the move_turn to the other player
9. Determine if there is a winner
10. Store the updated game to the db

```cpp
void tic_tac_toe::move(const name &challenger, const name &host, const name &by, const uint16_t &row, const uint16_t &column)
{
    require_auth(by);

    // Check if game exists
    games existing_host_games(get_self(), host.value);
    auto itr = existing_host_games.find(challenger.value);
    check(itr != existing_host_games.end(), "game doesn't exists");

    // Check if this game hasn't ended yet
    check(itr->winner == "none"_n, "the game has ended!");
    // Check if this game belongs to the action sender
    check(by == itr->host || by == itr->challenger, "this is not your game!");
    // Check if this is the  action sender's turn
    check(by == itr->turn, "it's not your turn yet!");

    // Check if user makes a valid movement
    check(is_valid_movement(row, column, itr->board), "not a valid movement!");

    // Fill the cell, 1 for host, 2 for challenger
    const uint8_t cell_value = itr->turn == itr->host ? 1 : 2;
    const auto turn = itr->turn == itr->host ? itr->challenger : itr->host;
    existing_host_games.modify(itr, itr->host, [&](auto &g) {
        g.board[row * tic_tac_toe::game::board_width + column] = cell_value;
        g.turn = turn;
        g.winner = get_winner(g);
   });
}
```

### Movement Validation

Valid movement is defined as movement done inside the board on an empty cell:

```cpp
bool is_empty_cell(const uint8_t &cell)
{
    return cell == 0;
}

bool is_valid_movement(const uint16_t &row, const uint16_t &column, const std::vector<uint8_t> &board)
{
    uint32_t movement_location = row * tic_tac_toe::game::board_width + column;
    bool is_valid = movement_location < board.size() && is_empty_cell(board[movement_location]);
    return is_valid;
}
```

### Get Winner

Winner is defined as the first player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row.

```cpp
...
name get_winner(const tic_tac_toe::game &current_game)
{
    auto &board = current_game.board;

    bool is_board_full = true;

    // Use bitwise AND operator to determine the consecutive values of each column, row and diagonal
    // Since 3 == 0b11, 2 == 0b10, 1 = 0b01, 0 = 0b00
    std::vector<uint32_t> consecutive_column(tic_tac_toe::game::board_width, 3);
    std::vector<uint32_t> consecutive_row(tic_tac_toe::game::board_height, 3);
    uint32_t consecutive_diagonal_backslash = 3;
    uint32_t consecutive_diagonal_slash = 3;

    for (uint32_t i = 0; i < board.size(); i++)
    {
        is_board_full &= is_empty_cell(board[i]);
        uint16_t row = uint16_t(i / tic_tac_toe::game::board_width);
        uint16_t column = uint16_t(i % tic_tac_toe::game::board_width);

        // Calculate consecutive row and column value
        consecutive_row[column] = consecutive_row[column] & board[i];
        consecutive_column[row] = consecutive_column[row] & board[i];
        // Calculate consecutive diagonal \ value
        if (row == column)
        {
            consecutive_diagonal_backslash = consecutive_diagonal_backslash & board[i];
        }
        // Calculate consecutive diagonal / value
        if (row + column == tic_tac_toe::game::board_width - 1)
        {
            consecutive_diagonal_slash = consecutive_diagonal_slash & board[i];
        }
    }

    // Inspect the value of all consecutive row, column, and diagonal and determine winner
    std::vector<uint32_t> aggregate = {consecutive_diagonal_backslash, consecutive_diagonal_slash};
    aggregate.insert(aggregate.end(), consecutive_column.begin(), consecutive_column.end());
    aggregate.insert(aggregate.end(), consecutive_row.begin(), consecutive_row.end());

    for (auto value : aggregate)
    {
        if (value == 1)
        {
            return current_game.host;
        }
        else if (value == 2)
        {
            return current_game.challenger;
        }
    }
    // Draw if the board is full, otherwise the winner is not determined yet
    return is_board_full ? "draw"_n : "none"_n;
}
```

You can see the final tic.tac.toe.cpp below:

## Final Contract Code
The final state of the tic.tac.toe.cpp file:

```cpp
// Import necessary library
#include "tic.tac.toe.hpp"

// Generic eosio library, i.e. print, type, math, etc
using namespace eosio;

bool is_empty_cell(const uint8_t &cell)
{
    return cell == 0;
}

bool is_valid_movement(const uint16_t &row, const uint16_t &column, const std::vector<uint8_t> &board)
{
    uint32_t movement_location = row * tic_tac_toe::game::board_width + column;
    bool is_valid = movement_location < board.size() && is_empty_cell(board[movement_location]);
    return is_valid;
}

void tic_tac_toe::create(const name &challenger, name host) {
    require_auth(host);
    check(challenger != host, "challenger shouldn't be the same as host");

    // Check if game already exists
    games existing_host_games(get_self(), host.value);
    auto itr = existing_host_games.find(challenger.value);
    check(itr == existing_host_games.end(), "game already exists");

    existing_host_games.emplace(host, [&](auto &g) {
        g.challenger = challenger;
        g.host = host;
        g.turn = host;
    });
}

void tic_tac_toe::restart(const name &challenger, const name &host, const name &by)
{
    require_auth(by);
    // Check if game exists
    games existing_host_games(get_self(), host.value);
    auto itr = existing_host_games.find(challenger.value);
    check(itr != existing_host_games.end(), "game doesn't exists");

    // Check if this game belongs to the action sender
    check(by == itr->host || by == itr->challenger, "this is not your game!");

    // Reset game
    existing_host_games.modify(itr, itr->host, [](auto &g) {
        g.reset_game();
    });
}

void tic_tac_toe::close(const name &challenger, const name &host)
{
    require_auth(host);

    // Check if game exists
    games existing_host_games(get_self(), host.value);
    auto itr = existing_host_games.find(challenger.value);
    check(itr != existing_host_games.end(), "game doesn't exists");

    // Remove game
    existing_host_games.erase(itr);
}

void tic_tac_toe::move(const name &challenger, const name &host, const name &by, const uint16_t &row, const uint16_t &column)
{
    require_auth(by);

    // Check if game exists
    games existing_host_games(get_self(), host.value);
    auto itr = existing_host_games.find(challenger.value);
    check(itr != existing_host_games.end(), "game doesn't exists");

    // Check if this game hasn't ended yet
    check(itr->winner == "none"_n, "the game has ended!");
    // Check if this game belongs to the action sender
    check(by == itr->host || by == itr->challenger, "this is not your game!");
    // Check if this is the  action sender's turn
    check(by == itr->turn, "it's not your turn yet!");

    // Check if user makes a valid movement
    check(is_valid_movement(row, column, itr->board), "not a valid movement!");

    // Fill the cell, 1 for host, 2 for challenger
    const uint8_t cell_value = itr->turn == itr->host ? 1 : 2;
    const auto turn = itr->turn == itr->host ? itr->challenger : itr->host;
    existing_host_games.modify(itr, itr->host, [&](auto &g) {
        g.board[row * tic_tac_toe::game::board_width + column] = cell_value;
        g.turn = turn;
        g.winner = get_winner(g);
    });
}

name get_winner(const tic_tac_toe::game &current_game)
{
    auto &board = current_game.board;

    bool is_board_full = true;

    // Use bitwise AND operator to determine the consecutive values of each column, row and diagonal
    // Since 3 == 0b11, 2 == 0b10, 1 = 0b01, 0 = 0b00
    std::vector<uint32_t> consecutive_column(tic_tac_toe::game::board_width, 3);
    std::vector<uint32_t> consecutive_row(tic_tac_toe::game::board_height, 3);
    uint32_t consecutive_diagonal_backslash = 3;
    uint32_t consecutive_diagonal_slash = 3;

    for (uint32_t i = 0; i < board.size(); i++)
    {
        is_board_full &= is_empty_cell(board[i]);
        uint16_t row = uint16_t(i / tic_tac_toe::game::board_width);
        uint16_t column = uint16_t(i % tic_tac_toe::game::board_width);

        // Calculate consecutive row and column value
        consecutive_row[column] = consecutive_row[column] & board[i];
        consecutive_column[row] = consecutive_column[row] & board[i];
        // Calculate consecutive diagonal \ value
        if (row == column)
        {
            consecutive_diagonal_backslash = consecutive_diagonal_backslash & board[i];
        }
        // Calculate consecutive diagonal / value
        if (row + column == tic_tac_toe::game::board_width - 1)
        {
            consecutive_diagonal_slash = consecutive_diagonal_slash & board[i];
        }
    }

    // Inspect the value of all consecutive row, column, and diagonal and determine winner
    std::vector<uint32_t> aggregate = {consecutive_diagonal_backslash, consecutive_diagonal_slash};
    aggregate.insert(aggregate.end(), consecutive_column.begin(), consecutive_column.end());
    aggregate.insert(aggregate.end(), consecutive_row.begin(), consecutive_row.end());

    for (auto value : aggregate)
    {
        if (value == 1)
        {
            return current_game.host;
        }
        else if (value == 2)
        {
            return current_game.challenger;
        }
    }
    // Draw if the board is full, otherwise the winner is not determined yet
    return is_board_full ? "draw"_n : "none"_n;
}

```

## Compile

Let's compile our contract, using eosio-cpp

```bash
eosio-cpp -o tic_tac_toe.wasm tic.tac.toe.cpp
```

## Deploy

Now the wasm file and abi file are ready. Time to deploy!
Create a directory (let's call it tic.tac.toe) and copy your generated tic.tac.toe.wasm tic_tac_toe.abi files.

```bash
cleos set contract tic.tac.toe tic.tac.toe
```

Ensure that your wallet is unlocked and you have `tic.tac.toe` key imported.

## Play

After the deployment and the transaction is confirmed, the contract is already available in the blockchain. You can play with it now!

### Create

Assuming you are using two accounts `bob` and `alice` (for the following commands as well):

[[info | Test Account]]
| Refer to this article for creating test accounts [Create Test Accounts](../02_development-environment/07_create-test-accounts.md)

```bash
cleos push action tic.tac.toe create '{"challenger":"bob", "host":"alice"}' --permission alice@active
```

### Move

```bash
cleos push action tic.tac.toe move '{"challenger":"bob", "host":"alice", "by":"alice", "row":0, "column":0}' --permission alice@active

cleos push action tic.tac.toe move '{"challenger":"bob", "host":"alice", "by":"bob", "row":1, "column":1}' --permission bob@active
```

### Restart

```bash
cleos push action tic.tac.toe restart '{"challenger":"bob", "host":"alice", "by":"alice"}' --permission alice@active
```

### Close

```bash
cleos push action tic.tac.toe close '{"challenger":"bob", "host":"alice"}' --permission alice@active
```

### See the game status

```bash
$ cleos get table tic.tac.toe alice games
{
  "rows": [{
      "challenger": "bob",
      "host": "alice",
      "turn": "bob",
      "winner": "none",
      "board": [
        1,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        0
      ]
    }
  ],
  "more": false
}
```
