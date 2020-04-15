#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as response:
    HTML = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(HTML), HTML, HTML.decode('utf-8')))
