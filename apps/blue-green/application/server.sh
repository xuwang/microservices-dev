#! /usr/bin/env bash

gunicorn -w1 -b 0.0.0.0:80 app:app