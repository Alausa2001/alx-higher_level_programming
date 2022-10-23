#!/usr/bin/python3
"""list the 10 most recent commits in a repository
first arg : owner of repo
second arg: name of repo"""

if __name__ == "__main__":
    from sys import argv
    import requests

    que_str = 'https://api.github.com/repos/{}/{}/commits'\
              .format(argv[2], argv[1])
    response = requests.get(que_str)
    commit_list = response.json()
    for commit in commit_list[:10]:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print('{}: {}'.format(sha, author))
