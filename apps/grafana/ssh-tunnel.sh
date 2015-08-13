#!/bin/sh

# setup a remote ssh tunnel for heapster
ssh -nNT -R 0.0.0.0:3000:172.17.8.101:3000 moni.jmcr