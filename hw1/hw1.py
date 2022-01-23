import sys, requests
from bs4 import BeautifulSoup

site = sys.argv[1]

if 'https://' in site:
    site = site.rstrip('/').lstrip('https://')

s = requests.Session()
login_url = f'https://{site}/login'
resp = s.get(login_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

logindata = {
    'csrf' : csrf,
    'username' : 'carlos',
    'password' : 'montoya'
}

print(f'Logging in as carlos:montoya')
resp = s.post(login_url, data=logindata)
print(f'Login response: {resp.text}')