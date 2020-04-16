#!/usr/bin/python3
"""Takes an URL, sends request, displays response."""
import requests
from sys import argv

if __name__ == "__main__":
    R = requests.get(argv[1])
    if R.status_code > 400:
        print("Error code:", R.status_code)
    else:
        print(R.text)
