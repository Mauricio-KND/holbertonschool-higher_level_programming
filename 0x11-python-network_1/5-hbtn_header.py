#!/usr/bin/python3
"""Takes an URL, sends request, displays value of X-Request-Id."""
import requests
from sys import argv

if __name__ == "__main__":
    R = requests.get(argv[1])
    print(R.headers.get('X-Request-Id'))
