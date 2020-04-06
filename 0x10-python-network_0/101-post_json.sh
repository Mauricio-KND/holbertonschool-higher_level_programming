#!/bin/bash
# Sends JSON POST request to a URL, displays.
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
