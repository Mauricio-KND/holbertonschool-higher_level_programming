#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    R = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(R.text), R.text))
