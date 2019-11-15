---
title: "Dispatcher"
excerpt: "Defines C++ functions to dispatch action to proper action handler inside a contract."
---
### SUMMARY

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public template<>`  <br/>`bool `[`execute_action`](#execute_action)`(T * obj,void(Q::*)(Args...) func)`            | Unpack the received action and execute the correponding action handler.