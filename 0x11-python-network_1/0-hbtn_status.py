#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import urlopen

with urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
print('Body response:')
print('\t- type: {}'.format(type(html)))
print('\t- content: {}'.format(html))
print('\t- utf8 content: {}'.format(html.decode('utf-8')))
