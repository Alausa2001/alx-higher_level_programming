#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter,
and finally displays the body of the response using requests package"""


if __name__ == "__main__":
    import requests
    from sys import argv
    value = {'email': argv[2]}
    response = requests.post(argv[1], data=value)
    print(response.text)
