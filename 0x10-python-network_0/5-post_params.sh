#!/bin/bash
# Takes an URL, sends POST request, displays body's response.
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
