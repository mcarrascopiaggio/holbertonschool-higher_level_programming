#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
-You must use the package requests
-You are not allow to import packages other than requests
-The body of the response must be display like
the following example (tabulation before -)
"""


import requests


if __name__ == "__main__":
    ans = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(ans.text)))
    print("\t- content: {}".format(ans.text))
