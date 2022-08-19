#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
- use the package urllib
- use a with statement
"""


import shutil
import tempfile
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    	with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        	shutil.copyfileobj(response, tmp_file)

	with open(tmp_file.name) as html:
