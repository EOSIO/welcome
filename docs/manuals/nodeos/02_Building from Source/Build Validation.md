---
title: "Build Validation"
excerpt: ""
---
### Build validation 

Optionally, a set of tests can be run against your build to perform some basic validation.  To run the test suite after building, start `mongod` 

On Linux platforms:
```bash
~/opt/mongodb/bin/mongod -f ~/opt/mongodb/mongod.conf &
```

On MacOS:
```bash
/usr/local/bin/mongod -f /usr/local/etc/mongod.conf &
```

and set the build path to EOSIO_HOME by the following:
[block:code]
{
  "codes": [
    {
      "code": "export EOSIO_HOME=/repo/eos/build/",
      "language": "shell"
    }
  ]
}
[/block]
then run `make test`. Followed by this on all platforms:

```bash
cd build
make test
```

[block:callout]
{
  "type": "info",
  "body": "An optional but strongly suggested `make install` step that makes local development significantly more developer friendly",
  "title": "Recommend"
}
[/block]