#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays
the body of the response"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            r = response.read()
            print(r.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code:', err.code)
