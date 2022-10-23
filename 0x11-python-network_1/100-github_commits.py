#!/usr/bin/python3
"""list the 10 most recent commits in a repository
first arg : owner of repo
second arg: name of repo"""

if __name__ == "__main__":
    from sys import argv
    import requests

    que_str = 'https://api.github.com/repos/{}/{}/commits'\
              .format(argv[1], argv[2])
    response = requests.get(que_str)
    for a in response.json()[:10]:
        
        sha = a.get('sha')
        author = a.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))
        
        """
        sha = a['sha']
        author = a['commit']['author']['name']
        print('{}: {}'.format(sha, author))
        """
