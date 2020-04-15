#!/usr/bin/python3
"""Takes an URL and email address, sends a POST, displays response."""
import requests
from sys import argv

if __name__ == "__main__":
    R = requests.post(argv[1], data={'email': argv[2]})
    print(R.text)
