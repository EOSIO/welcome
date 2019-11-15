---
title: "permission_level (struct)"
excerpt: "Packed representation of a permission level (Authorization)"
---
## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public `[`account_name`](#account_name)` `[`actor`](#actor) | Name of the account who owns this permission.
`public `[`permission_name`](#permission_name)` `[`permission`](#permission) | Name of the permission.
`public inline  `[`permission_level`](#permission_level)`(`[`account_name`](#account_name)` a,`[`permission_name`](#permission_name)` p)` | Construct a new permission level object.
`public inline  `[`permission_level`](#permission_level)`()` | Construct a new permission level object.

## Members

### `public `[`account_name`](#account_name)` `[`actor`](#actor)

Name of the account who owns this permission.

### `public `[`permission_name`](#permission_name)` `[`permission`](#permission)

Name of the permission

### `public inline  `[`permission_level`](#permission_level)`(`[`account_name`](#account_name)` a,`[`permission_name`](#permission_name)` p)`

Construct a new permission level object with actor name and permission name

#### Parameters
* `a` - Name of the account who owns this authorization
* `p` - Name of the permission

### `public inline  `[`permission_level`](#permission_level)`()`

Construct a new permission level object. (Default Constructor)