#!/usr/bin/python3
"""Takes Github credentials, uses Github API to display id."""
import requests
import sys

if __name__ == "__main__":
    R = requests.get('https://swapi.co/api/people/?search={}'
                     .format(sys.argv[1])).json()
    print('Number of results: {}'.format(R.get('count')))
    for res in R.get('results'):
        print(res.get('name'))
