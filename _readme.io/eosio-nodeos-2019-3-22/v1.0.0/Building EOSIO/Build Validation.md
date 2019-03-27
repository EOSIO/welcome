---
title: "Build Validation"
excerpt: ""
---
### Build validation 

Optionally, a set of tests can be run against your build to perform some basic validation.  To run the test suite after building, start `mongod` and then run `make test`.

On Linux platforms:
```bash
~/opt/mongodb/bin/mongod -f ~/opt/mongodb/mongod.conf &
```

On MacOS:
```bash
/usr/local/bin/mongod -f /usr/local/etc/mongod.conf &
```

Followed by this on all platforms:
```bash
cd build
make test
```