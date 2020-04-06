#!/bin/bash
# Sends request to an URL, displays status code of response.
curl -s -o /dev/null -I -w "%{http_code}" "$1"
