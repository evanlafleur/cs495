import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'aca81f491eca784fc0bf59b300f900ec.web-security-academy.net'
url = f'https://{site}'
php_url = f'{url}/cgi-bin/phpinfo.php'


resp = s.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)

resp = s.get(php_url)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)