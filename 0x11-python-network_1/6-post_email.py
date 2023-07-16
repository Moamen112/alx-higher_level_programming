#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")

    print(x_request_id)

