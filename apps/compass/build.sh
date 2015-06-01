#!/usr/bin/env bash

source $(pwd)/envvars
docker build -t $IMAGE $(pwd)/docker
