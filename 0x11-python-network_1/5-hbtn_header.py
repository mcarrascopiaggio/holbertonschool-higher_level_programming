#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
-You must use the package requests
-You are not allow to import packages other than requests
-The body of the response must be display like
the following example (tabulation before -)
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    ans = requests.get(url)
    print(ans.headers.get('X-Request-Id'))
