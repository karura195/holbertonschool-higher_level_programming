#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request as request
import urllib.parse as parse
from sys import argv


if __name__ == "__main__":
    val = {'email': argv[2]}
    info = parse.urlencode(values).encode('utf-8')
    r = request.Request(argv[1], info)
    with request.urlopen(r) as r:
        print(r.read().decode('utf-8'))
