#!/usr/bin/env bash

# build xuwang/pyweb docker image
docker build --rm=true -t xuwang/pyweb /var/lib/apps/pyweb/docker

# push the new build to local registry
/var/lib/apps/bin/dkpush_to_local xuwang/pyweb:latest