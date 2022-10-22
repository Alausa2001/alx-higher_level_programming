#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header
using requests package"""

if __name__ == "__main__":
    import requests
    from sys import argv
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
