---
title: "DO NOT PUBLISH"
excerpt: ""
---
Notes
- This isn't lossless, some data is lost, oh well.

All six elements of readme.io has to be translated as described below

- 1 - Header --------------------------------------------------------------------------------------------------
[block:api-header]
{
  "title": "This is a header"
}
[/block]
translates to:

## This is a header


- 2 - Code Sample --------------------------------------------------------------------------------------------------
[block:code]
{
  "codes": [
    {
      "code": "int variable = 5;\nvoid cpp_function()\n{\n  bool code_goes_in_here = true;\n}\n",
      "language": "cplusplus",
      "name": "Name of the code sample"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "int variable = 5;\nbool java_script_code_here = true;",
      "language": "javascript",
      "name": "Name of the code sample"
    }
  ]
}
[/block]
translates to:

{{name}}
```{{language}}
{{code}}
```
make sure language is translated properly:
cplusplus -> cpp
javascript -> javascript


- 3 - Callouts ---------------------------------------------------------------------------------

- Alert success -------------------------------------------------------------------------------
[block:callout]
{
  "type": "success"
}
[/block]
- Alert danger -------------------------------------------------------------------------------
[block:callout]
{
  "type": "danger"
}
[/block]
- Alert info -------------------------------------------------------------------------------
[block:callout]
{
  "type": "info",
  "body": "This is an info",
  "title": "This is an info heading"
}
[/block]
- Alert warning -------------------------------------------------------------------------------
[block:callout]
{
  "type": "warning",
  "title": "...alert",
  "body": "alter body"
}
[/block]
translates to:

[[info]]
| This is an info heading
This is an info body

[[caution]]
| This is an caution heading
This is an caution body

[[success]]
| This is a success heading
This is an caution body

[[danger]]
| This is danger heading
This is an danger body


- 4 - table ------------------------------------------------------------------------------
[block:parameters]
{
  "data": {
    "0-0": "11",
    "0-1": "12",
    "0-2": "",
    "0-3": "14",
    "1-0": "21",
    "1-1": "",
    "1-2": "23",
    "2-1": "32",
    "h-0": "Column1",
    "h-1": "",
    "h-3": "",
    "h-2": "Col"
  },
  "cols": 4,
  "rows": 3
}
[/block]
translates to:
find out!

- 5 - image -----------------------------------------------------------------------
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dca095f-echipa_de_cercetare_a_berii_de_tap_Bucuresti.jpg",
        "echipa_de_cercetare_a_berii_de_tap_Bucuresti.jpg",
        2443,
        1374,
        "#232e4f"
      ],
      "caption": "Image accompanying text"
    }
  ]
}
[/block]
translates to:
find out!

- 6 - embed ------------------------------------------------------------------------
[block:embed]
{
  "html": false,
  "url": "https://block.one/",
  "title": "Block.one - High Performance Blockchain Solutions",
  "favicon": "https://qdkzytxlh7-flywheel.netdna-ssl.com/wp-content/uploads/2018/06/cropped-site-icon-1-192x192.png",
  "image": "https://qdkzytxlh7-flywheel.netdna-ssl.com/wp-content/uploads/2018/09/wordpress-share.png"
}
[/block]
translates to:
find out!