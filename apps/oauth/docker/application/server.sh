#! /usr/bin/env bash

gunicorn -w3 -b 0.0.0.0:443 --certfile=certs/server.crt --keyfile=certs/server.key app:app