---
title: "Using HTTP Sandbox and Code Samples"
excerpt: ""
---
Our HTTP RPC documentation includes an API Sandbox that can be utilized by a local node when correctly configured. 
[block:api-header]
{
  "title": "Port"
}
[/block]
At this moment in time, the HTTP API sandbox only supports the default port, 8888. 
[block:api-header]
{
  "title": "Cors"
}
[/block]
In order to utilize the HTTP sandbox, you'll need set the `access control allow origin` parameter on Nodeos or Keosd for **localhost**. If you do not start with this method, you will get a 404 not found when using the sandbox.  
[block:code]
{
  "codes": [
    {
      "code": "--access-control-allow-origin=localhost\n",
      "language": "shell",
      "name": "Nodeos Boot Flags"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "The [Docker Quickstart](https://eosio.readme.io/eosio-nodeos/docs/docker-quickstart) guide includes this configuration by default."
}
[/block]

[block:callout]
{
  "type": "danger",
  "title": "WARNING",
  "body": "**NEVER** enable CORS on Keosd or Nodeos with loaded wallet api plugin **where you have production keys**. This would be an unnecessary security risk. This option should only be utilized for development reasons or if you know what you are doing."
}
[/block]

[block:api-header]
{
  "title": "Loading the Required Plugins"
}
[/block]
Any endpoint requires loading the corresponding plugin to Nodeos. The only exception to this is Keosd, which loads the Wallet API Plugin by default.
[block:api-header]
{
  "title": "Hitting an Endpoint Method with the Sandbox"
}
[/block]
Some methods require parameters, for these methods there is a provided input area. There are several types of input areas, we'll cover the different types utilized by the EOSIO HTTP API. 

## Text (string) 
_Accepts any string_
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/474f682-Screen_Shot_2018-06-06_at_10.56.55_AM.png",
        "Screen Shot 2018-06-06 at 10.56.55 AM.png",
        718,
        117,
        "#fcfcfc"
      ]
    }
  ]
}
[/block]
## Numbers (int32)
_Only accepts numbers_
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1bc221a-Screen_Shot_2018-06-06_at_10.57.53_AM.png",
        "Screen Shot 2018-06-06 at 10.57.53 AM.png",
        727,
        62,
        "#fbfbfb"
      ]
    }
  ]
}
[/block]
## Array of Strings
_A helper field, enter a string and press enter to add it to the array_
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1824a93-Screen_Shot_2018-06-06_at_10.58.43_AM.png",
        "Screen Shot 2018-06-06 at 10.58.43 AM.png",
        724,
        118,
        "#f3f4f6"
      ]
    }
  ]
}
[/block]
## JSON
_JSON fields are currently buggy and will not function as anticipated, see notice below_ 
[block:callout]
{
  "type": "warning",
  "body": "There are some incompatibilities between the Sandbox and our API that we are presently working through. We appreciate your patience on this matter."
}
[/block]