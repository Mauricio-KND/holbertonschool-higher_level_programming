#!/usr/bin/python3
""" Uses requests module. Prints error code"""
import requests
from sys import argv

if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    Data = {"q": argv[1][0] if len(argv) > 1 else ""}
    R = requests.post(URL, data=Data)
    try:
        d = R.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")
