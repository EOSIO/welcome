---
title: "Multi-Index DB API"
excerpt: ""
---
## Overview

EOSIO provides a set of services and interfaces that enable contract developers to
persist state across actions, and consequently transactions, boundaries.  Without persistence, state that is generated during the processing of actions and transactions will be lost when processing goes out of scope.  The persistence components include:

1. Services to persist state in a database
2. Enhanced query capabilities to find and retrieve database content
3. C++ APIs to these services, intended for use by contract developers
4. C APIs for access to core services, of interest to libraries and system developers

This document covers the first three topics.

<a name="need-for-persistence-services"></a>
### The Need for Persistence Services

Actions perform the work of EOSIO contracts. Actions operate within an environment known as the action context.  As illustrated in the [Action "Apply" Context Diagram](https://files.readme.io/6d71afc-action-apply-context-diagram.png), an action context provides several things necessary for the execution of the action. One of those things is the action's working memory. This is where the action maintains its working state. Before processing an action, EOSIO sets up a clean working memory for the action. Variables that might have been set when another action executed are not available within the new action's context. The only way to pass state among actions is to persist it to and retrieve it from the EOSIO database.

<a name="eosio-multi-index-api"></a>
## The EOSIO Multi-Index API

The EOSIO Multi-Index API provides a C++ interface to the EOSIO database.  The EOSIO Multi-Index API is patterned after [Boost Multi-Index Containers](https://www.boost.org/doc/libs/1_66_0/libs/multi_index/doc/index.html).  This API provides a model for object storage with rich retrieval capabilities, enabling the use of multiple indices with different sorting and access semantics. The Multi-Index API is provided by the [`eosio::multi_index`](https://github.com/EOSIO/eos/blob/master/contracts/eosiolib/multi_index.hpp) C++ class found in the `contracts/eosiolib` folder of the [`EOSIO/eos` GitHub repository](https://github.com/EOSIO/eos/). This class enables a contract written in C++ to read and modify persistent state in the EOSIO database.

The Multi-Index container interface `eosio::multi_index` provides a homogeneous container of an arbitrary C++ type (and it does not need to be a plain-old data type or be fixed-size) that is kept sorted in multiple indices by keys of various types that are derived from the objects. It can be compared to a traditional database table with rows, columns, and indices. It can also be easily compared to [Boost Multi-index Containers](https://www.boost.org/doc/libs/1_66_0/libs/multi_index/doc/index.html). In fact many of the member function signatures of `eosio::multi_index` are modeled after `boost::multi_index`, although there are important differences.

`eosio::multi_index` can be conceptually viewed as tables in a conventional database in which the rows are the individual objects in the container, the columns are the member properties of the objects in the container, and the indices provide fast lookup of an object by a key compatible with an object member property.

Traditional database tables allow the index to be a user-defined function over some number of columns of the table. `eosio::multi_index` similarly allows the index to be any user-defined function (provided as a member function of the `class`/`struct` of the element type) but with its return value restricted to one of a limited set of supported key types.

Traditional database tables typically have a single unique primary key that allows 
unambiguously identifying a particular row in the table and also provides the standard sort order for the rows in the table. `eosio::multi_index` supports a similar semantic, but the primary key of the object in the `eosio::multi_index` container must be a unique unsigned 64-bit integer. The objects in the `eosio::multi_index` container are sorted by the primary key index in ascending order of the unsigned 64-bit integer primary key.

<a name="eosio-multi-index-iterators"></a>
### EOSIO Multi-Index Iterators

A key differentiator of the EOSIO persistence services over other blockchain infrastructures is its Multi-Index iterators. Unlike some other blockchains that only provide a key-value store, EOSIO Multi-Index tables allow a contract developer to keep a collection of objects sorted by a variety of different key types, which could be derived from the data within the object.  This enables rich retrieval capabilities.  Up to 16 secondary indices can be defined, each having its own way of ordering and retrieving table contents.

The EOSIO Multi-Index iterators follow a pattern that is common to C++ iterators.  All iterators are bi-directional `const`, either `const_iterator` or `const_reverse_iterator`.  The iterators can be dereferenced to provide access to an object in the Multi-Index table. 

<a name="putting-it-all-together"></a>
## Putting It All Together

<a name="how-to-create-your-own-table"></a>
### How to Create Your EOSIO Multi-Index Table

Here is a summary of the steps to create your own persistent data using EOSIO Multi-Index tables.

- Define your object(s) using C++ `class` or `struct`.  Each object will be in its own Multi-Index table.
- Define a `const` member function in the `class`/`struct` called `primary_key` that returns the `uint64_t` primary key value of your object.
- Determine the secondary indices. Up to 16 additional indices are supported. A secondary index
supports several key types, listed below.
    - `uint64_t` - Primitive 64-bit unsigned integer key
    - `uint128_t` - Primitive 128-bit unsigned integer key, or a 128-bit fixed-size lexicographical key
    - `eosio::checksum256` - 256-bit fixed-size lexicographical key
    - `double` - Double precision floating point key
    - `long double` - Quadruple precision floating point key
- Define a key extractor for each secondary index. The key extractor is a function used to obtain the keys from the elements of the Multi-Index table. 

<a name="how-to-use-your-own-table"></a>
### How to Use Your EOSIO Multi-Index Table

- [Instantiate your Multi-Index table.](https://developers.eos.io/eosio-cpp/reference#multi-index)
- Insert [emplace](https://developers.eos.io/eosio-cpp/reference#emplace) into, and subsequently [modify](https://developers.eos.io/eosio-cpp/reference#modify) or [erase](https://developers.eos.io/eosio-cpp/reference#erase) objects in your table as required by your contract.
- Locate and traverse objects in your table using [get](https://developers.eos.io/eosio-cpp/reference#get), [find](https://developers.eos.io/eosio-cpp/reference#find) and iterator operations.