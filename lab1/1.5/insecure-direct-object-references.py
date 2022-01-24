import re, requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'acb61f851e34b6d6c0b40b2f0063001d.web-security-academy.net'
url = f'https://{site}'
download_url = f'{url}/download-transcript/1.txt'
login_url = f'{url}/login'



resp = s.get(download_url)
print(resp.text)
resp = s.get(login_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')
