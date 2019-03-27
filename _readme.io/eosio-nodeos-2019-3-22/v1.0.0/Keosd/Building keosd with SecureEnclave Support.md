---
title: "Building keosd with SecureEnclave Support"
excerpt: "Add a keosd wallet that supports hardware key storage and signing via the YubiHSM 2."
---
In order to access the SecureEnclave an app must be signed.   For debugging and testing purposes, `keosd` can be self-signed by a developer.

In order to do this an active Apple ID and xcode will be required

# Step 1 Create Developer Signing Cert

1. Open `xcode` and click on `Xcode`->`Preferences...` in the menu bar.
1. click on the "Accounts" tab
1. select or add your apple ID to the left side list
1. click "Manage Certificates..."
1. click the plus sign in the bottom left and select "Mac Development"  

this should download a developer signing cert from Apple.   You will need the the SHA1 fingerprint of this certificate later.  This can be found by opening the "Keychain access" app, selecting the "login" entry on the left, selecting the "Mac Developer: ..." certificate on the right and clicking the `i` button on the bottom.

You should see a dialog with information including the "Organizational Unit" towards the top and  "SHA1 fingerprint" towards the bottom at the bottom.  You will need these to proceed.

# Step 2 create a signing profile

In order to sign `keosd` we need to create a profile using xcode

 1. open `xcode`
 1. create a new project and select "Cocoa App" for "macOS"
 1. set a Product Name and Organization Name to something memorable
     * observe the resulting Bundle Identifier, it will be important later
 1. complete the new project wizard
 1. under the "General" settings "Signing" section click "Enable Development Signing"
 1. under the "General" settings "Signing" section Select your Personal account as the "Team"
 1. press Command-B or use the menu to build, this will ask you for your password for keychain access.  Enter your password and click *always allow*

You can now close xcode

Your signing profile should be present in `~/Library/MobileDevice/Provisioning Profiles/<uuid>` you will need this path to continue

# Step 3 build signed `keosd`

`cmake` requires extra parameters in order to build a signed `keosd` given the certificate and provisioning profile previously created.  these are:

* `-DMAS_CERT_FINGERPRINT` which is the SHA1 fingerprint you collected in step 1. 
 For example `-DMAS_CERT_FINGERPRINT=9F62000000000000000000000000000000008391`
* `-DMAS_BASE_APPID` which is  `<Organization Unit from step 1>.<organization name from step 2>.` Note the trailing period.  For example `-DMAS_BASE_APPID=95000000YJ.myorg.`
* `-DMAS_PROVISIONING_PROFILE` which is the full absolute path to the provision profile. for instance `-DMAS_PROVISIONING_PROFILE=/Users/alice/Library/MobileDevice/Provisioning Profiles/xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.provisionprofile`
* `-DMAS_KEYCHAIN_GROUP` which is `<Organization Unit from step 1>.<any string with dots>` and defines a group of apps that can share access to the keys.  for example `-DMAS_KEYCHAIN_GROUP=95000000YJ.mykeys`

Once built with these `cmake` parameters in addition to the normal paramters you can find and run keosd normally at `<build director>/keosd.app/Contents/MacOS/keosd`