#!/bin/bash
# Makes a request that causes to respond with message.
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
