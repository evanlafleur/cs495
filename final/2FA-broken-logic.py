'''
Level name: 2FA-broken-logic
Link to Level: https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-broken-logic

Vulnerability:
    -

Prevention/Remediation:
    -
'''
import requests, sys
from bs4 import BeautifulSoup

s = requests.Session()

site = sys.argv[1]

if 'https://' in site:
    site = site.rstrip('/').lstrip('https://')
    print(site)
