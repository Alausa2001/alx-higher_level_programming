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
    commit_list = response.json()
    for commit in commit_list[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, author))
