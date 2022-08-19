#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


import requests
from sys import argv


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        value = {"q": argv[1]}
    else:
        value = {"q": ""}
    req = requests.post(url, data=value)
    try:
        request = req.json()
        if len(request) == 0:
            print("No result")
        else:
            print("[{}] {}".format(request.get("id"), request.get("name")))
    except Exception:
        print("Not a valid JSON")
