#!/usr/bin/python3
"""
 Displays the value of the X-Request-Id variable found in the header
 of the response
"""

import urllib.request as request
from sys import argv


if __name__ == "__main__":
    r = request.Request(argv[1])
    with request.urlopen(r) as r:
        print(r.headers.get('X-Request-Id'))
