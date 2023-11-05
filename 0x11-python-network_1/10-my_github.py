#!/usr/bin/python3
"""
Script that takes GitHub credentials
and uses the GitHub API to display the user idscript
that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(r.json().get('id'))
