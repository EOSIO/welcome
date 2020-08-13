# **Abstract**

This guide is for users who intend to use the EOSIO Testnet for building blockchain applications on EOSIO. This guide also supports EOSIO-based documentation tutorials that use the Testnet to perform various smart contract operations including pushing permission-based actions. 

# Getting Started with Testnet
This chapter provides instructions for registering a new EOSIO Testnet developer account and steps to log in to the Testnet web interface. 

When you register on the EOSIO Testnet, we will create a new developer account for you - a login credential for you to log into the Testnet. With the new developer account, a new blockchain account is also provisioned to interact with the blockchain by deploying smart contracts or pushing actions.

**Note**: The developer account is only used for login purposes and should not be confused with a blockchain account. 

## Testnet Sign Up
This section outlines the steps for creating a new Testnet developer account. 


Complete the following steps to create a Testnet developer account:

1. Visit the sign-up page on the Testnet website and enter the requested details. 
2. Read the Testnet terms and conditions and click the checkboxes to indicate your agreement to the terms and conditions.
3. Click the checkbox in the **I’m not a robot** captcha clicker and then click **Register**. 
4. Visit your inbox to verify your email address.
5. Click **VERIFY ACCOUNT** in the verification email.
6. Once your email address is verified, enter your login details and click **Log in**.

**Note**: After you click Log In, the welcome page invites you to a getting started tour. Complete the getting started tour, or optionally, click Skip tour at the bottom. 

## Testnet Login
If you already have a Developer Testnet account, log in at EOSIO Testnet Login. 

# Blockchain Account Configuration
This section provides instructions on creating new blockchain accounts within the Testnet and additional administrative actions such as requesting new Temporary Network Tokens (TNTs) for staking and unstaking system resources. 

An account is a collection of authorizations, is stored on the blockchain, and is used to identify a sender/recipient. The flexible authorization structure of an account enables it to be owned either by an individual or group of individuals dependant on how permissions are configured. An account sends or receives a valid transaction to the blockchain.

For more information on EOSIO accounts and associated permissions, see the Accounts and Permissions page on the EOSIO Developers Portal.

## Create New Account
The EOSIO Testnet provisions a new EOSIO blockchain account every time you sign up for a new EOSIO Testnet developer account. If you require more EOSIO blockchain accounts, follow the steps below. 

**Complete the following steps to create a new account:**

1. Log in to the Testnet interface and navigate to Blockchain Accounts from the top navigation menu.
2. To create a new account, click the create another account button (outlined in red below) next to the existing account name in the drop down menu.
   
**Note**: You can see your existing blockchain accounts in the drop-down menu.
   
**Result**

The previous action creates a new blockchain account as show below:

After creating new accounts, request Temporary Network Tokens (TNTs) as outlined in the next section Request Tokens.

## Request Tokens
Temporary Network Tokens (TNTs) are the native tokens of the EOSIO Testnet. By default, each account contains 32 TNTs. Tokens allow you to get more system resources on Testnet to deploy contracts, interact with smart contracts, and store data on the blockchain.

To request new TNTs, In the TNT Balances block, click the Request Tokens button to replenish your account by 10 tokens.

Result

This action replenishes your account by 10 tokens and disables the Request Tokens button for the next 60 minutes as show below:

Note: TNTs are replenished every hour by the system. After requesting the first set of tokens, wait for an hour before requesting another round of tokens. 

## Buy and Stake System Resources

For more information on staking, see the Staking on EOSIO Based Blockchains section on the EOSIO Developers Portal. 

Complete the following steps to buy and stake system resources:

1. On the Blockchain Accounts page, scroll down to Request Resources.
2. To buy RAM resource, enter the amount in bytes and click on the Get RAM button.
3. To stake CPU resource, enter the TNT amount and click the Stake button.
4. To stake NET resource, enter the TNT amount and click the Stake button.


To learn more about EOSIO system resources see the following documentation on the EOSIO Developers Portal:


* RAM as Resource
* CPU as Resource 
* NET as Resource 

## View Account Details
Once your new blockchain account is created, you can view the following account details in the Testnet:

* **TNT Balances**: This detail displays the Temporary Network Token (TNT) total balance, available balance, and the staked balance for the specific account. Use tokens to purchase system resources. 
* **Resource Usage**: This detail displays the percentage utilization of system resources and the amount of resources available. 
* **Keys**: This detail displays automatically generated public and private keys pairs. 
* **Transaction list**: the number of transactions performed on behalf of the account.

Complete the following steps to view account details:

1. Log in to the Testnet interface and navigate to Blockchain Accounts from the top navigation menu.
2. From the drop-down menu, select the blockchain account.
3. Click on the account name.


**Result**
The account details are displayed. 

# Smart Contract Deployment

This chapter provides instructions on how to upload and deploy a compiled smart contract using the Testnet GUI.





## Prerequisites
You must have the following prerequisites before uploading and deploying a smart contract:


1. EOSIO CDT-compiled smart contract files. 
The WASM file
The ABI file
2. Testnent blockchain account with sufficient system resources. See the previous section of this guide **Buy and Stake System Resources** for information on staking and unstaking in the Testnent. 

**Note**: For more information on how to build and compile smart contract source files, see the Hello World Contract section on the EOSIO Developers Portal. 

## Upload and Deploy
Upload and deploy your smart contract on the EOSIO blockchain in a 3-step sequential process. 

**Complete the following steps to upload and deploy your smart contract:**

1. Click the **Browse** button to select the compiled WASM file.
2. Click the **Browse** button to select the generated ABI file.
3. From the drop down menu, select the blockchain account with sufficient system resources and click the **Deploy** button.

**Result**
The smart contract successfully deploys to the selected account. 

**Note**: If you encounter an unsuccessful deploy error message, make sure you have sufficient RAM on your account. 

# Push Actions
An action is authorized by one or more actors created on the blockchain. Actions are created explicitly within a smart contract, or generated implicitly by application code.

For more information on Actions in EOSIO, see the Transactions Protocol section on the EOSIO Developers Portal. 

Complete the following steps to push actions on the Testnet:

1. Navigate to the **Push Action** page from the top navigation menu.
2. Enter the account name to which the smart contract is deployed and select the action type in the **Action Type** dropdown menu. 
3. Enter the JSON payload containing the data or parameters implemented in the source files. 
4. Select the relevant permission associated with the account and click **Push**.

# View Transactions
A transaction instance contains a transaction header and the list of action instances and transaction extensions that make the actual transaction.

For more information on Transactions in EOSIO, see the Transactions Protocol section on the EOSIO Developers Portal. 

Complete the following steps to view transactions on the Testnet:

1. Navigate to the Transactions page form the top navigation menu. 
2. From the Transactions list, click on a transaction. 
3. View the transaction details with the associated metadata including the number of actions part of the transaction. 
