---
title: "Suggesting Edits"
excerpt: ""
---
Our documentation has a suggested edits feature that enables anyone to submit corrections to documentation. If these suggestions are approved by an editor, they will be merged in a timely fashion
[block:api-header]
{
  "title": "How to Suggest Edits"
}
[/block]
At the top-right corner of most articles is a "suggested edits" link. 
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4b46a65-Screen_Shot_2018-06-06_at_10.21.21_AM.png",
        "Screen Shot 2018-06-06 at 10.21.21 AM.png",
        519,
        275,
        "#f8f9f9"
      ]
    }
  ]
}
[/block]
You will then be asked to login with a Readme.io account. Please create an account, and once you have, you will be permitted to make corrections to documentation. 
[block:api-header]
{
  "title": "Using the Editor"
}
[/block]
The editor utilizes markdown, but also includes some useful modules that extend markdown. 

* Header - An H1 helper that behaves the same as the markdown syntax `#`. The purpose of this module is to make seeing top-level headings more visible while editing. When `#` is used on large articles, the wall of text can be difficult to navigate in editor mode.
* Code Sample - This behaves the same as using markdown syntax for code with backticks. However, it will syntax highlight the code in the editor view, making it easier to identify problems before publishing
* Callout - This is a module that enables you to add elements on the page that either inform, warn, caution or express success to the end users. It's great for pointing out caveats, highlighting ideas and urging caution. 
* Table - If you've ever worked with large markdown tables, you're probably aware they are not fun to create nor edit. This module behaves the same as the markdown syntax for tables and looks the same when rendered too. However, it provides a beautiful interface for editing tables in an intuitive way, and makes management of tables far more simple for our editors. 
* Image - This provides an interface that will load an image to our provider's server, eliminating the need to handle image hosting. This reduces steps and makes adding and editing images far more intuitive for both you and our editors.
* Embed - Embed various media elements, such as YouTube videos, PDFs or anything you would normally use the **embed** tag for.
[block:api-header]
{
  "title": "Submitting Changes"
}
[/block]
Once you've made changes to the document, simply click the "Suggest Changes" button. We'll receive a notification, review the changes and either merge or reject them. 
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/64afacc-Screen_Shot_2018-06-06_at_10.21.27_AM.png",
        "Screen Shot 2018-06-06 at 10.21.27 AM.png",
        210,
        43,
        "#f2f0df"
      ]
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Disabled Suggestions"
}
[/block]
We have disabled submitting edits for documentation that is automatically generated from the source. In due time, we will instead link the "Suggested Edits" functions for those docs to an article explaining how you can make changes to these documentation items. In most cases, this would be through a Pull request on Github.