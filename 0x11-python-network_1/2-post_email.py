#!/usr/bin/python3
"""Takes an URL and email, sends POST request, displays body of response."""
from urllib import request, parse
import sys

if __name__ == "__main__":
    Data = parse.urlencode({"email": sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], Data) as response:
        print(response.read().decode('utf-8'))
