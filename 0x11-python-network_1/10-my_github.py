#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    from sys import argv
    basic = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                            auth=basic)
    print(response.json().get('id'))
