#!/bin/bash
# You are not allowed to use any pipe, redirection, etc.
curl -s -o /dev/null -w "%{http_code}" "$1"
