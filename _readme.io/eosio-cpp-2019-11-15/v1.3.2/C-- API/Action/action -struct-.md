---
title: "action [struct]"
excerpt: "Packed representation of an action."
---
This is the packed representation of an action along with meta-data about the authorization levels.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`account_name`](#account_name)` `[`account`](#account) | Name of the account the action is intended for.
`public `[`action_name`](#action_name)` `[`name`](#name) | Name of the action.
`public vector< `[`permission_level`](#permission_level)` > `[`authorization`](#authorization) | List of permissions that authorize this action.
`public `[`bytes`](#bytes)` `[`data`](#data) | Payload data.
`public  `[`action`](#action)`() = default` | Construct a new action object.
`public template<>`  <br/>`inline  `[`action`](#action)`(vector< `[`permission_level`](#permission_level)` > && auth,const Action & value)` | Construct a new action object with the given permission and action struct.
`public template<>`  <br/>`inline  `[`action`](#action)`(const `[`permission_level`](#permission_level)` & auth,const Action & value)` | Construct a new action object with the given list of permissions and action struct.
`public template<>`  <br/>`inline  `[`action`](#action)`(const Action & value)` | Construct a new action object with the given action struct.
`public template<>`  <br/>`inline  `[`action`](#action)`(const `[`permission_level`](#permission_level)` & auth,`[`account_name`](#account_name)` a,`[`action_name`](#action_name)` n,T && value)` | Construct a new action object with the given permission, action receiver, action name, action struct.
`public template<>`  <br/>`inline  `[`action`](#action)`(vector< `[`permission_level`](#permission_level)` > auths,`[`account_name`](#account_name)` a,`[`action_name`](#action_name)` n,T && value)` | Construct a new action object with the given list of permissions, action receiver, action name, action struct.
`public inline  `[`EOSLIB_SERIALIZE`](#EOSLIB_SERIALIZE)`(`[`action`](#action)`,(`[`account](#account))([name](#name))([authorization](#authorization))([data`](#data))`) const` | Send the action as inline action.
`public inline void `[`send_context_free`](#send_context_free)`() const` | Send the action as inline context free action.
`public template<>`  <br/>`inline T `[`data_as`](#data_as)`()` | Retrieve the unpacked data as T.

## Members

### `public `[`account_name`](#account_name)` `[`account`](#account)

Name of the account the action is intended for.

Name of the account the action is intended for

### `public `[`action_name`](#action_name)` `[`name`](#name)

Name of the action.

Name of the action

### `public vector< `[`permission_level`](#permission_level)` > `[`authorization`](#authorization)

List of permissions that authorize this action.

List of permissions that authorize this action

### `public `[`bytes`](#bytes)` `[`data`](#data)

Payload data.

Payload data

### `public  `[`action`](#action)`() = default`

Construct a new action object.

Default Constructor

### `public template<>`  <br/>`inline  `[`action`](#action)`(vector< `[`permission_level`](#permission_level)` > && auth,const Action & value)`

Construct a new action object with the given permission and action struct.

Construct a new action object with the given permission and action struct

#### Parameters
* `Action` - Type of action struct

#### Parameters
* `auth` - The permission that authorizes this action

* `value` - The action struct that will be serialized via pack into data

### `public template<>`  <br/>`inline  `[`action`](#action)`(const `[`permission_level`](#permission_level)` & auth,const Action & value)`

Construct a new action object with the given list of permissions and action struct.

Construct a new action object with the given list of permissions and action struct

#### Parameters
* `Action` - Type of action struct

#### Parameters
* `auth` - The list of permissions that authorizes this action

* `value` - The action struct that will be serialized via pack into data

### `public template<>`  <br/>`inline  `[`action`](#action)`(const Action & value)`

Construct a new action object with the given action struct.

Construct a new action object with the given action struct

#### Parameters
* `Action` - Type of action struct

#### Parameters
* `value` - The action struct that will be serialized via pack into data

### `public template<>`  <br/>`inline  `[`action`](#action)`(const `[`permission_level`](#permission_level)` & auth,`[`account_name`](#account_name)` a,`[`action_name`](#action_name)` n,T && value)`

Construct a new action object with the given permission, action receiver, action name, action struct.

Construct a new action object with the given action struct

#### Parameters
* `T` - Type of action struct

#### Parameters
* `auth` - The permissions that authorizes this action

* `a` - The name of the account this action is intended for (action receiver)

* `n` - The name of the action

* `value` - The action struct that will be serialized via pack into data

### `public template<>`  <br/>`inline  `[`action`](#action)`(vector< `[`permission_level`](#permission_level)` > auths,`[`account_name`](#account_name)` a,`[`action_name`](#action_name)` n,T && value)`

Construct a new action object with the given list of permissions, action receiver, action name, action struct.

Construct a new action object with the given action struct

#### Parameters
* `T` - Type of action struct

#### Parameters
* `auths` - The list of permissions that authorize this action

* `a` - The name of the account this action is intended for (action receiver)

* `n` - The name of the action

* `value` - The action struct that will be serialized via pack into data

### `public inline  `[`EOSLIB_SERIALIZE`](#EOSLIB_SERIALIZE)`(`[`action`](#action)`,(`[`account](#account))([name](#name))([authorization](#authorization))([data`](#data))`) const`

Send the action as inline action.

Send the action as inline action

### `public inline void `[`send_context_free`](#send_context_free)`() const`

Send the action as inline context free action.

Send the action as inline context free action

#### Precondition
This action should not contain any authorizations

### `public template<>`  <br/>`inline T `[`data_as`](#data_as)`()`

Retrieve the unpacked data as T.

Retrieve the unpacked data as T

#### Parameters
* `T` expected type of data

#### Returns
the action data


Base class to derive a new defined action from.

Base class to derive a new defined action from so it can take advantage of the dispatcher

#### Parameters
* `Account` - The account this action is intended for

* `Name` - The name of the action