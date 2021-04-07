---
content_title: EOSIO Helm Tutorial
link_text: EOSIO Helm Tutorial
---

## Overview

This tutorial showcases how to install and use Helm Charts for local EOSIO deployment using Kubernetes and Docker Desktop. The tutorial is divided in three parts: Installation, Basic Usage, and EOSIO Helm Repositories.

## Before You Begin

* Get familiar with [Docker Desktop](https://docs.docker.com/desktop).
* Become acquainted with [Kubernetes](https://kubernetes.io/docs/reference/kubectl/).
* Familiarize with [Helm](https://helm.sh/docs/).
* Read the [EOSIO Helm Charts tool](index.md) guide.
* Install the following software on your local system:
    1. Install Docker Desktop:
        * [Docker Official: Desktop](https://docs.docker.com/desktop)
    1. Install Kubernetes command-line tool (kubectl):
        * [Kubernetes Official: Install and Set Up Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl)
    1. Install Helm:
        * [Helm Official: Installing Helm](https://helm.sh/docs/intro/install)

## Part 1: Installation

Perform the following steps to install EOSIO Helm Charts for local deployment:

1. Clone the EOSIO Help Charts github repository:

```sh
git clone https://github.com/EOSIO/eosio.helm.git
```
```console
Cloning into 'eosio.helm'...
remote: Enumerating objects: 204, done.
remote: Counting objects: 100% (204/204), done.
remote: Compressing objects: 100% (88/88), done.
remote: Total 204 (delta 109), reused 203 (delta 109), pack-reused 0
Receiving objects: 100% (204/204), 44.24 KiB | 1.11 MiB/s, done.
Resolving deltas: 100% (109/109), done.
```

1. Change directory to `eosio.helm`:

```sh
cd eosio.helm
ls -l
```
```console
-rw-r--r--   1 username  username   839 Apr  7 15:22 artifacthub-repo.yml
drwxr-xr-x  10 username  username   320 Apr  7 15:23 eosio
drwxr-xr-x   5 username  username   160 Apr  7 15:22 eosio-common
drwxr-xr-x   8 username  username   256 Apr  7 15:23 eosio-nodeos
-rw-r--r--   1 username  username  2767 Apr  7 15:22 CONTRIBUTING.md
-rw-r--r--   1 username  username  5614 Apr  7 15:22 IMPORTANT.md
-rw-r--r--   1 username  username  1119 Apr  7 15:22 LICENSE
-rw-r--r--   1 username  username  3330 Apr  7 15:22 README.md
```

1. Perform `helm dependency update` to cache the subchart metadata:

```sh
./eosio/scripts/helm-dependency-update.sh
```
```console
~/Work/eosio.helm/eosio-common ~/Work/eosio.helm
~/Work/eosio.helm
~/Work/eosio.helm/eosio-nodeos ~/Work/eosio.helm
Saving 1 charts
Deleting outdated charts
~/Work/eosio.helm
~/Work/eosio.helm/eosio ~/Work/eosio.helm
Saving 1 charts
Deleting outdated charts
~/Work/eosio.helm
```

1. Configure Kubernetes context to use local namespace:

```sh
kubectl config set-context --current --namespace=local
```
```console
Context "docker-desktop" modified.
```

1. Install EOSIO Helm chart itself:

```sh
helm upgrade --install eosio eosio -f eosio/local.yaml -f eosio/nodeos_config.yaml
```
```console
Release "eosio" does not exist. Installing it now.
NAME: eosio
NAMESPACE: local
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

## Part 2: Basic Usage

Now that the EOSIO node has been deployed, we can check its status:

```sh
kubectl get pods
```
```console
NAME                   READY    STATUS    RESTARTS   AGE
eosio-local-nodeos-0   1/1      Running   0          10s
```
