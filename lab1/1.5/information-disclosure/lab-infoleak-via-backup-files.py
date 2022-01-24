import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac591f061fbb5fbbc0ad23f0005b0046.web-security-academy.net'
url = f'https://{site}'
backup_url = f'{url}/backup/ProductTemplate.java.bak'


resp = s.get(backup_url)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)
