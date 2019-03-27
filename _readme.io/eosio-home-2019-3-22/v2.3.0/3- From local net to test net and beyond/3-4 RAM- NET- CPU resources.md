---
title: "3.4 RAM, NET, CPU resources"
excerpt: ""
---
As mentioned earlier for a smart contract to be able to be deployed and then interacted with via its implemented actions it needs to be backed up by resources allocated on the account where the smart contract is deployed to. The three resource types an EOSIO smart contract developer needs to know about are RAM, CPU and NET.
[block:api-header]
{
  "title": "3.4.1 RAM"
}
[/block]
RAM is the memory (space, storage) where the blockchain stores data. If your contract needs to store data on the blockchain, like in a database, then it can store it in the blockchain's RAM using either a multi-index table, which can be found explained [here](https://developers.eos.io/eosio-cpp/v1.3.1/docs/db-api) and [here](https://developers.eos.io/eosio-cpp/docs/using-multi-index-tables) or a singleton, its definition can be found [here](https://github.com/EOSIO/eos/blob/master/contracts/eosiolib/singleton.hpp) and a sample of its usage [here](https://github.com/EOSIO/eos/blob/3fddb727b8f3615917707281dfd3dd3cc5d3d66d/contracts/eosio.system/eosio.system.hpp).
        The EOSIO-based blockchains are known for their high performance, which is achieved also because the data stored on the blockchain is using RAM for the storage medium, and thus access to blockchain data is very fast, helping the performance benchmarks to reach levels no other blockchain has been able to.
        RAM is a very important resource because of the following reasons: it is a limited resource, each EOSIO-based blockchain can have a different policy and rules around RAM, for example the public EOS blockchain started with 64GB of RAM and after that the block producers decided to increase the memory with 1KiB (1024 bytes) per day, thus increasing constantly the supply of RAM for the price of RAM to not grow too high because of the increased demand from blockchain applications; also RAM it is used in executing many actions that are available on the blockchain, creating a new account for example (it needs to store in the blockchain memory the new account's information), also when an account accepts a new type of token a new record has to be created somewhere in the blockchain memory that holds the balance of the new token accepted, and that memory, the storage space on the blockchain, has to be purchased either by the account that transfers the token or by the account that accepts the new token type.
        RAM is a scarce resource priced according to the unique Bancor liquidity algorithm which is implemented in the system contract [here](https://github.com/EOSIO/eos/blob/905e7c85714aee4286fa180ce946f15ceb4ce73c/contracts/eosio.system/exchange_state.hpp).
         
        Let's check now how much memory is available an how much is used right now on the contract which you created and deployed earlier:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get account eostutorial1\n\ncleos --url=https://kylin.eoscanada.com get account eostutorial1",
      "language": "shell",
      "name": "cleos get account command"
    }
  ]
}
[/block]
Note in the output of the cleos command the following:
    memory: 
            quota:     203.4 KiB    used:       203 KiB

Of course for you the numbers will be slightly different, but it should be clear, the quota is what you have as of now allocated and used indicates how much is used by the contract at the moment. The numbers should be pretty close cause you were paying attention not to buy a lot more RAM than what it was needed.

For the purpose of demonstration, if the numbers are not close to each other and there's a difference higher than 1 KiB use the below command to sell RAM and get the difference of quota and used to be under 1 KiB, that is, execute the below commands until you see the wanted difference between them:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 system sellram eostutorial1 1024\ncleos --url=https://jungle2.cryptolions.io:443 get account eostutorial1\n\ncleos --url=https://kylin.eoscanada.com system sellram eostutorial1 1024\ncleos --url=https://kylin.eoscanada.com get account eostutorial1",
      "language": "shell"
    }
  ]
}
[/block]
Let's now execute the action that will add a new entry in the address book, the upsert action, this action will require more RAM to be used in order to store the new information for eostutorial1 account.
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 push action eostutorial1 upsert '[eostutorial1, \"alice\", \"liddell\", 22, \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p eostutorial1@active\n\ncleos --url=https://kylin.eoscanada.com push action eostutorial1 upsert '[eostutorial1, \"alice\", \"liddell\", 22, \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p eostutorial1@active",
      "language": "shell",
      "name": "cleos push action command"
    }
  ]
}
[/block]
But instead you will observe an error message saying:
[block:code]
{
  "codes": [
    {
      "code": "Error 3050000: Action validate exception\nError Details:\ninline action's code account abcounter does not exist\npending console output: \n",
      "language": "text"
    }
  ]
}
[/block]
This means the action you pushed on the blockchain could not be executed because an inline action's code "abcounter" does not exist. Does it ring any bells? If you followed the tutorial mentioned earlier, in which you created the addressbook smart contract you also created the abcounter smart contract which addressbook is using by sending an inline action to it, and since you did not deployed the abcounter smart contract on the blockchain the current addressbook action uspert it fails when is sending the inline action to abcounter contract, because the contract doesn't exist on the blockchain. 
You have two choices here, either you deploy the abcounter as well, or you modify the addressbook contract code to not use the abcounter actions.
For the purpose of demonstration and because, arguably, it is easier let's go with the later, please open the addressbook.cpp file comment out the content of the *increment_counter* and *send_summary* methods to look just like the ones below:
[block:code]
{
  "codes": [
    {
      "code": "void increment_counter(name user, std::string type) {\n    \n    // action counter = action(\n    //   permission_level{get_self(),\"active\"_n},\n    //   \"abcounter\"_n,\n    //   \"count\"_n,\n    //   std::make_tuple(user, type)\n    // );\n\n    // counter.send();\n}\nvoid send_summary(name user, std::string message) {\n    // action(\n    //   permission_level{get_self(),\"active\"_n},\n    //   get_self(),\n    //   \"notify\"_n,\n    //   std::make_tuple(user, name{user}.to_string() + message)\n    // ).send();\n};\n",
      "language": "cplusplus"
    }
  ]
}
[/block]
Also modify the upsert method to have the first line commented out, just like this:
[block:code]
{
  "codes": [
    {
      "code": "[[eosio::action]]\nvoid upsert(name user, std::string first_name, std::string last_name, uint64_t age, std::string street, std::string city, std::string state) {\n    \n    //require_auth(user);\n\n    ...",
      "language": "cplusplus"
    }
  ]
}
[/block]
This change makes it so the smart contract is not requesting authorization from the account you are inserting or updating in the addressbook because later you'll add many entries to the address book so it will take too long to generate keys and use them in this tutorial for each of the new inserted accounts. Also, the addressbook contract is coded at the moment so the payer of the RAM needed to store a new record is the new account added to the addressbook, that is the account sent in as user parameter to the upsert action. Also, in order to use the RAM of the account that is added to the address book, its keys are needed and you do not have them, and again that would be too much to handle for this tutorial.
Therefore the next changes alter the contract so the account that pays for the storage/RAM, where the new entries in the address book are saved is the owner of the contract, the eostutorial1 account, thus we need only one account's permission, the eostutorial1 permissions.
To accomplish this you need to modify the invocations of emplace and the modify methods as shown below:
[block:code]
{
  "codes": [
    {
      "code": "addresses.emplace(get_self(), [&]( auto& row ){\n\naddresses.modify(iterator, get_self(), [&]( auto& row ) {\n",
      "language": "text"
    }
  ]
}
[/block]
Notice the `get_self()` is used instead of the `user` for the `payer` parameter on both methods. The detailed reference documentation for both of these methods can be found [here](https://developers.eos.io/eosio-cpp/reference#emplace) and [here](https://developers.eos.io/eosio-cpp/reference#modify)

Save the addressbook.cpp file, compile the contract again and re-deploy it to the blockchain:
[block:code]
{
  "codes": [
    {
      "code": "cd CONTRACTS_DIR/addressbook/\neosio-cpp -o addressbook.wasm addressbook.cpp --abigen\n",
      "language": "shell"
    }
  ]
}
[/block]
Re-deploy the contract on the chosen test net with one of the following commands:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active\n\ncleos --url=https://kylin.eoscanada.com set contract eostutorial1 CONTRACTS_DIR/addressbook/ -p eostutorial1@active\n",
      "language": "shell",
      "name": "cleos set contract command"
    }
  ]
}
[/block]
Now let's try again to execute the upsert action for the addressbook contract, please note that addressbook is not present in the command line at all, it is the name of the class that implements the contract, but it has been deployed to the eostutorial1 account, so we communicate with it via the account name not via the class name that implements the contract:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 push action eostutorial1 upsert '[eostutorial1, \"alice\", \"liddell\", 22, \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p eostutorial1@active\n\ncleos --url=https://kylin.eoscanada.com push action eostutorial1 upsert '[eostutorial1, \"alice\", \"liddell\", 22, \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p eostutorial1@active\n",
      "language": "shell",
      "name": "cleos push action command"
    }
  ]
}
[/block]
Now the command should be successful, and you should see a message like one below:
[block:code]
{
  "codes": [
    {
      "code": "#  eostutorial1 <= eostutorial1::upsert         {\"user\":\"eostutorial1\",\"first_name\":\"alice\",\"last_name\":\"liddell\",\"age\":22,\"street\":\"123 drink me wa...\n#  eostutorial1 <= eostutorial1::notify         {\"user\":\"eostutorial1\",\"msg\":\"eostutorial1 successfully modified record in addressbook. Fields chang...\nwarning: transaction executed locally, but may not be confirmed by the network yet         ]         \n",
      "language": "text"
    }
  ]
}
[/block]
In order to see the entries stored in the addressbook table you can run the following command:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get table eostutorial1 eostutorial1 people\n\ncleos --url=https://kylin.eoscanada.com get table eostutorial1 eostutorial1 people",
      "language": "shell",
      "name": "cleos get table command"
    }
  ]
}
[/block]
Let's demonstrate now how the available RAM will get consumed when more rows are added to the table.
Let's make note of the available RAM and the total used currently:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get account eostutorial1\n\ncleos --url=https://kylin.eoscanada.com get account eostutorial1",
      "language": "shell",
      "name": "cleos get account command"
    }
  ]
}
[/block]
If the difference between `quota` and `used` is higher than 1 KiB, then run below commands to make the difference smaller, first commands sells some of the available RAM and second command is showing the status of the account so you can inspect the difference between `quota` and `used` RAM:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 system sellram eostutorial1 1024\ncleos --url=https://jungle2.cryptolions.io:443 get account eostutorial1\n\ncleos --url=https://kylin.eoscanada.com system sellram eostutorial1 1024\ncleos --url=https://kylin.eoscanada.com get account eostutorial1\n",
      "language": "text",
      "name": "cleos sell ram command"
    }
  ]
}
[/block]
Repeat the above commands until the difference is smaller than 1 KiB (1024 bytes).

Now execute the below command which will attempt to add to the address book a bigger number of new entries, which should fail pretty quickly complaining about RAM insufficiency for account eostutorial1, when you see the errors on the command prompt you can hit CTRL+C to stop the command execution:
[block:code]
{
  "codes": [
    {
      "code": "# for Jungle test network\nfor i in `seq 1 5`; do \\\nfor j in `seq 1 5`; do \\\nfor k in `seq 1 5`; do \\\nfor l in `seq 1 5`; do \\\necho \"cleos --url=https://jungle2.cryptolions.io:443 push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"; \\\n$(eval \"cleos --url=https://jungle2.cryptolions.io:443 push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"); \\\ndone \\\ndone \\\ndone \\\ndone\n\n# for Cryptokilin test network\nfor i in `seq 1 5`; do \\\nfor j in `seq 1 5`; do \\\nfor k in `seq 1 5`; do \\\nfor l in `seq 1 5`; do \\\necho \"cleos --url=https://kylin.eoscanada.com push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"; \\\n$(eval \"cleos --url=https://kylin.eoscanada.com push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"); \\\ndone \\\ndone \\\ndone \\\ndone",
      "language": "shell",
      "name": "add more entries command"
    }
  ]
}
[/block]
You'' notice at some point the errors are looking similar to the one below:
[block:code]
{
  "codes": [
    {
      "code": "Error 3080001: Account using more than allotted RAM usage\nError Details:\naccount eostutorial1 has insufficient ram; needs 278630 bytes has 278565 bytes",
      "language": "text"
    }
  ]
}
[/block]
In order to solve the problem now you'll have to buy more RAM, so let's do it:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 system buyram eostutorial1 eostutorial1 \"0.1 EOS\" -p eostutorial1@active\n\ncleos --url=https://kylin.eoscanada.com system buyram eostutorial1 eostutorial1 \"0.1 EOS\" -p eostutorial1@active",
      "language": "shell",
      "name": "cleos buy ram command"
    }
  ]
}
[/block]
You bought RAM in value of 0.1 EOS which should be sufficient to execute the previous command and add one or more entry into the address book:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 push action eostutorial1 upsert '[lastuer11111, \"alice\", \"liddell\", 22, \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p eostutorial1@active\n\ncleos --url=https://kylin.eoscanada.com push action eostutorial1 upsert '[lastuer11111, \"alice\", \"liddell\", 22, \"123 drink me way\", \"wonderland\", \"amsterdam\"]' -p eostutorial1@active",
      "language": "shell",
      "name": "cleos push action command"
    }
  ]
}
[/block]
Let's now execute below command which adds ten more entries in the address book:
[block:code]
{
  "codes": [
    {
      "code": "# for Jungle test network\nfor i in `seq 1 5`; do \\\nfor j in `seq 1 2`; do \\\necho \"cleos --url=https://jungle2.cryptolions.io:443 push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"; \\\n$(eval \"cleos --url=https://jungle2.cryptolions.io:443 push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"); \\\ndone \\\ndone\n\n# for Cryptokilin test network\nfor i in `seq 1 5`; do \\\nfor j in `seq 1 2`; do \\\necho \"cleos --url=https://kylin.eoscanada.com push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"; \\\n$(eval \"cleos --url=https://kylin.eoscanada.com push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"); \\\ndone \\\ndone\n",
      "language": "shell",
      "name": "Add ten more entries in the address book"
    }
  ]
}
[/block]
If again you face not sufficient RAM while executing the above command please proceed by buying more RAM and then execute the above command until it executes without RAM related error.

Let's list all the entries in the addressbook again:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get table eostutorial1 eostutorial1 people\n\ncleos --url=https://kylin.eoscanada.com get table eostutorial1 eostutorial1 people",
      "language": "shell",
      "name": "cleos get table command"
    }
  ]
}
[/block]
It will show only 10 entries and then at the end the output will contain a line like this: `"more": true`.
Which means there are more rows available which can be shown with a special command line argument `-l 100`, see the command below:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get table eostutorial1 eostutorial1 people -l 100\n\ncleos --url=https://kylin.eoscanada.com get table eostutorial1 eostutorial1 people -l 100\n",
      "language": "shell",
      "name": "cleos get table with -l param"
    }
  ]
}
[/block]
The`-l 100` informs cleos command that you want to retrieve 100 elements and then if you see `"more": true` again you can increase the number of retrieved elements until more if false or you can ask for a high number of elements from the beginning:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get table eostutorial1 eostutorial1 people -l 999999999999\n\ncleos --url=https://kylin.eoscanada.com get table eostutorial1 eostutorial1 people -l 999999999999\n",
      "language": "shell",
      "name": "cleos command with -l param"
    }
  ]
}
[/block]
Be careful with this last one because if you have a huge number of elements in storage it might time out or it might take a long time.

Another way to retrieve efficiently all items in the table is to use the lower bound by specifying `-L parameter`, so first time you issue the command and you ask to get 100 elements:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get table eostutorial1 eostutorial1 people -l 100\n\ncleos --url=https://kylin.eoscanada.com get table eostutorial1 eostutorial1 people -l 100\n",
      "language": "shell",
      "name": "cleos get table with -l param"
    }
  ]
}
[/block]
If it shows `"more": true` then make note of the last element's key, let's say it is user1112, and issue this command:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get table eostutorial1 eostutorial1 people -l 100 -L user1112\n\ncleos --url=https://kylin.eoscanada.com get table eostutorial1 eostutorial1 people -l 100 -L user1112",
      "language": "shell",
      "name": "cleos get table with -l and -L param"
    }
  ]
}
[/block]
And now you'll get back next 100 elements including and starting with the one that has the key user1112
[block:api-header]
{
  "title": "3.4.2 CPU"
}
[/block]
CPU is another resource that is very important in the EOSIO-based blockchains space. 

CPU is processing power, the amount of CPU an account has is measured in microseconds, it is referred to as "cpu bandwidth" on the cleos get account command output and represents the amount of processing time a contract has at its disposal when executing its actions.

Each account has available an amount of CPU proportions to the number of system tokens staked for resources. That is, an account has to stake system tokens to get access to the CPU and NET resources (this tutorial will cover the NET resource in the next chapter). Once staked, the tokens can't be unstaked, and thus recovered in full amount, only after three days, so staking can be seen as a commitment of at least three days. It is a commitment of holding the system core tokens blocked (not been able to trade them or used them in any other purpose), while the system token value is constantly depreciating its value because of the block producers daily rewards, in exchange for CPU and NET resources which once allocated are free to be used in the amount allocated.

The CPU is allocated proportional to the amount of tokens staked, for example, if total CPU capacity of the network is 100 units, and if during a 3 days window you want to be able to access 1 unit of CPU, you need to have staked by your account 1% of all staked system tokens, in that 3 days window.

You are competing with all the other accounts that staked system tokens for the CPU capacity, the more you stake relative to the other accounts the more CPU capacity you get, and also the CPU allocated to your account varies depending on what the other accounts stake as well.

Because of all these aspects, the amount of CPU allocated to your account based on your staked tokens varies all the time. In reality after each block is produced the amount of "virtual_cpu_limit" is recalculated, and each account's available CPU is thus affected. Because the formula used to calculate the max CPU available for an account is this one below, and it relies on the "virtual_cpu_limit":
[block:code]
{
  "codes": [
    {
      "code": "CPU allocated = (virtual_cpu_capacity_in_window x user_weight) / all_user_weight \n              = virtual_cpu_limit x 2x24x60x60 x user_weight / all_user_weight \n              = virtual_cpu_limit x 172800 x (\"how much I staked for CPU\" / \"how much every user staked for CPU\")",
      "language": "text"
    }
  ]
}
[/block]
It can be found [here](https://github.com/EOSIO/eos/blob/f9a3d023c05d6b7984cbd7263a5a39e650c87e90/libraries/chain/resource_limits.cpp#L371).

Once a smart contract consumed the amount of CPU bandwidth it has allocated it can not execute another action until the amount of CPU bandwidth grows back to a level that allows the contract to execute one or more actions. So another aspect of the CPU resources is that it gets consumed, and it can get consumed completely, but after three days it gets replenished to the maximum amount allowed by the staked system tokens.

Let's inspect how much CPU the current addressbook contract has available at the moment:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get account eostutorial1\ncleos --url=https://kylin.eoscanada.com get account eostutorial1",
      "language": "shell",
      "name": "cleos get account command"
    }
  ]
}
[/block]
Notice the output values for CPU:
[block:code]
{
  "codes": [
    {
      "code": "cpu bandwidth:\n    staked:          1.0000 EOS           (total stake delegated from account to self)\n    delegated:       0.0000 EOS           (total staked delegated to account from others)\n    used:              35.2 ms   \n    available:        13.59 ms   \n    limit:            48.79 ms   ",
      "language": "text"
    }
  ]
}
[/block]
You numbers will show different values, but important is to understand that based on the amount of system token, in this case 1 EOS, you get a maximum CPU limit of 48.79 milliseconds, out of which you used already 35.2 milliseconds and of course the difference between these two makes it for the total available at the moment of 13.59 milliseconds.

For the purpose of demonstration let's consume the CPU available and see how the contract behaves afterwards. You will accomplish this buy running the upsert action again for the existing entries in the table, thus you will not need more RAM, you will only need CPU, because the upsert now does not add new entries it just updates the existing ones:
[block:code]
{
  "codes": [
    {
      "code": "# for Jungle test network\nfor i in `seq 1 5`; do \\\nfor j in `seq 1 5`; do \\\nfor k in `seq 1 5`; do \\\nfor l in `seq 1 5`; do \\\necho \"cleos --url=https://jungle2.cryptolions.io:443 push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"; \\\n$(eval \"cleos --url=https://jungle2.cryptolions.io:443 push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"); \\\ndone \\\ndone \\\ndone \\\ndone\n\n# for Cryptokilin test network\nfor i in `seq 1 5`; do \\\nfor j in `seq 1 5`; do \\\nfor k in `seq 1 5`; do \\\nfor l in `seq 1 5`; do \\\necho \"cleos --url=https://kylin.eoscanada.com push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"; \\\n$(eval \"cleos --url=https://kylin.eoscanada.com push action eostutorial1 upsert '[user$i$j$k$l, \\\"aka\\\", \\\"liddell\\\", 25, \\\"123 drink me way\\\", \\\"wonderlands\\\", \\\"amsterdam\\\"]' -p eostutorial1@active\"); \\\ndone \\\ndone \\\ndone \\\ndone",
      "language": "shell",
      "name": "update existing entries command"
    }
  ]
}
[/block]
After running several upserts actions you shall see the following message printed:
[block:code]
{
  "codes": [
    {
      "code": "Error 3080004: Transaction exceeded the current CPU usage limit imposed on the transaction\nError Details:\nbilled CPU time (239 us) is greater than the maximum billable CPU time for the transaction (130 us)",
      "language": "text"
    }
  ]
}
[/block]
And if you inspect the account status with the following command:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get account eostutorial1\ncleos --url=https://kylin.eoscanada.com get account eostutorial1",
      "language": "shell",
      "name": "cleos get account command"
    }
  ]
}
[/block]
You will notice that the available CPU is small, smaller than the amount needed to run the upsert action.

At this point you have three choices, wait until the maximum available CPU for your account which is based on the amount of your staked tokens relative with the total amount of staked tokens is growing, wait three days when the maximum amount of CPU will be replenished based on your staked tokens, or stake more tokens.

Let's do the later for demonstration purpose, in the output of the last command, you can also notice liquid amount of system tokens, if there are still available you can stake them for CPU. If there aren't any left, you can transfer from eostutorial2 to eostutorial1 and then run the staking command:
[block:code]
{
  "codes": [
    {
      "code": "# transfer command if needed more EOS\ncleos --url=https://jungle2.cryptolions.io:443 transfer eostutorial2  eostutorial1 \"1.0000 EOS\" \"initial transfer to enable contract deployment\"\n# stake command\ncleos --url=https://jungle2.cryptolions.io:443 system delegatebw eostutorial1 eostutorial1 \"0.0000 EOS\" \"1.0000 EOS\" -p eostutorial1@active\n\n# transfer command if needed more EOS\ncleos --url=https://kylin.eoscanada.com transfer eostutorial2  eostutorial1 \"1.0000 EOS\" \"initial transfer to enable contract deployment\"\n# stake command\ncleos --url=https://kylin.eoscanada.com system delegatebw eostutorial1 eostutorial1 \"0.0000 EOS\" \"1.0000 EOS\" -p eostutorial1@active\n",
      "language": "shell",
      "name": "transfer and stake to itself commands"
    }
  ]
}
[/block]
On this second command you delated bandwidth from eostutorial1 to receiver eostutorial1, net in the amount 0.0000 EOS, cpu in the amount of 1.0000 EOS and you used the eostutorial1@active permission to sign this transaction.

An alternative, instead of executing two commands you can execute only one, by delegating directly from eostutorial2 for eostutorial1 account, so this way you do not transfer the EOS tokens to the eostutorial1 account, you just stake them on behalf of that account, so when you unstake them they return to eostutorial2 account:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 system delegatebw eostutorial2 eostutorial1 \"0.0000 EOS\" \"1.0000 EOS\" -p eostutorial2@active\n\ncleos --url=https://kylin.eoscanada.com system delegatebw eostutorial2 eostutorial1 \"0.0000 EOS\" \"1.0000 EOS\" -p eostutorial2@active",
      "language": "shell",
      "name": "cleos stake command for another account"
    }
  ]
}
[/block]
On this command you delegated bandwidth, from eostutorial2 to receiver eostutorial1, for net in the amount 0.0000 EOS, for cpu in the amount of 1.0000 EOS and you used the eostutorial2@active permission to sign this transaction.

And now that you have more CPU bandwidth you can go ahead and execute the upsert action again successfully.
[block:api-header]
{
  "title": "3.4.3 NET"
}
[/block]
As CPU and RAM, NET is also a very important resource in EOSIO-based blockchains. NET is data storage measured in bytes and you need to allocate NET according to how much is needed for your transactions to be stored in the blockchain, or more if you wish so, but not less if you want your contract's actions to function. Be careful to not confuse NET with RAM, RAM stores any random data that the contract wants to store in the blockchain, whereas NET although it is also storage space, it measures the size of the transactions.

NET is also allocated based on the system tokens, staked for NET, proportional with the total system tokens staked for NET by all accounts. So it has the same rules as CPU has when it comes to its variations and it gets updated as well after each block is produced.

In order to see your maximum NET available for your account you can use the same command you used for CPU, in the output of the command look for `net bandwidth`, `used`, `available`, `limit` values.
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 get account eostutorial1\ncleos --url=https://kylin.eoscanada.com get account eostutorial1",
      "language": "text",
      "name": "cleos get account command"
    }
  ]
}
[/block]
NET bandwidth can be consumed in the same way as CPU bandwidth gets consumed, therefore you also have the same options as you had with CPU: wait until the proportion of your staked tokens for NET is getting higher thus your available NET increases, or wait for the 3 days window to pass when the full amount of NET bandwidth corresponding to your staked tokens for NET will become available again, or stake more system tokens for NET and thus increasing your maximum allowed NET bandwidth.

The command below stakes 1.0000 system token, in this case EOS, for NET bandwidth in addition to what the account has already, and adds zero tokens to CPU bandwidth:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 system delegatebw eostutorial2 eostutorial1 \"1.0000 EOS\" \"0.0000 EOS\" -p eostutorial2@active\n        \ncleos --url=https://kylin.eoscanada.com system delegatebw eostutorial2 eostutorial1 \"1.0000 EOS\" \"0.0000 EOS\" -p eostutorial2@active",
      "language": "shell",
      "name": "cleos stake command"
    }
  ]
}
[/block]
The command of staking tokens for bandwidth have a corresponding one for unstaking tokens:
[block:code]
{
  "codes": [
    {
      "code": "cleos --url=https://jungle2.cryptolions.io:443 system undelegatebw eostutorial2 eostutorial1 \"1.0000 EOS\" \"0.0000 EOS\" -p eostutorial2@active\n        \ncleos --url=https://kylin.eoscanada.com system undelegatebw eostutorial2 eostutorial1 \"1.0000 EOS\" \"0.0000 EOS\" -p eostutorial2@active",
      "language": "shell",
      "name": "cleos unstake command"
    }
  ]
}
[/block]
The previous command unstakes 1 system token (in this case EOS) that was delegated by eostutorial2 for eostutorial1 account for NET bandwidth, and of course sends in the eostutorial2 active permission because it is the eostutorial2 account that owns those tokens staked for eostutorial1 account for NET bandwidth.