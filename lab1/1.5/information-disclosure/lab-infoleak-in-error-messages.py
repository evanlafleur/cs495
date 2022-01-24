import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac791ff21f42ed95c1e80d64005f00be.web-security-academy.net'
url = f'https://{site}'
product_url = f'{url}/product?productId="productId"'


resp = s.get(product_url)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)