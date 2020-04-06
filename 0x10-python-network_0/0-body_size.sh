#!/bin/bash
# Takes in a URL, sends request, displays size of body.
curl -s "$1" | wc -c
