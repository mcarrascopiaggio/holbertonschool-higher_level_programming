#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and uses the
GitHub API to display your id
"""


import requests
from sys import argv


if __name__ == '__main__':
    repository = argv[1]
    owner = argv[2]
    ur = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repository)
    req = requests.get(ur)
    data = req.json()
    i = 0
    for d in data:
        if i < 10:
            print("{}: {}".format(x.get("sha"),
                  x.get('commit').get('author').get('name')))
            i = i + 1
