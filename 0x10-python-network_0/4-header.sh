#!/bin/bash
# Takes URL as argument, sends GET request, displays body of response.
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
