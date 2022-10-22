#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the body of the response."""


if __name__ == "__main__":
    import requests
    from requests.exceptions import HTTPError
    from sys import argv
    try:
        response = requests.get(argv[1])
        print(response.text)
    except HTTPError as error:
        print(error.status_code)
