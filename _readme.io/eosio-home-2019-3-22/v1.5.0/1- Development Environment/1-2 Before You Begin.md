---
title: "1.2 Before You Begin"
excerpt: ""
---
[block:api-header]
{
  "title": "Step 1: Download Dependencies"
}
[/block]
- [Download Docker](https://www.docker.com/get-started) - This tutorial is going to be using Docker. For you to get started as quickly as possible this is the best option at the moment. Building from source is an option, but will set you back an hour or more and you may encounter build errors. 
[block:api-header]
{
  "title": "Step 2: Setup a development directory, stick to it."
}
[/block]
You're going to need to pick a directory to work from, it's suggested to create a `contracts` directory somewhere on your local drive. 
[block:code]
{
  "codes": [
    {
      "code": "mkdir contracts\ncd contracts",
      "language": "shell"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Step 3: Enter your local directory below."
}
[/block]
Get the path of that directory and save it for later, as you're going to need it, you can use the following command to get your absolute path.
```
pwd
```

Enter the absolute path to your contract directory below, and it will be inserted throughout the documentation to make your life a bit easier. _This functionality requires cookies_
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/3cdb3df-cli-2.2.2.gif",
        "cli-2.2.2.gif",
        622,
        94,
        "#020202"
      ]
    }
  ]
}
[/block]

[block:html]
{
  "html": "<div class=\"eosio-helper-box\">\n  <form> \n    <label>Absolute Path to Contract</label>\n    <input class=\"helper-cookie\" name=\"CONTRACTS_DIR\" type=\"text\" />\n    <input type=\"submit\" />\n    <span></span>\n  </form>\n</div>"
}
[/block]