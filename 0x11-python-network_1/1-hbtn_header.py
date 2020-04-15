#!/usr/bin/python3
"""Takes an URL, sends request, displays value of X-Request-Id variable."""
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
