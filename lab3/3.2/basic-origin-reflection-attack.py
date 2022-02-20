import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac2b1f741e748528c06f09f100c0004d.web-security-academy.net'

login_url = f"https://{site}/login"
login_response = s.get(login_url)
csrf = BeautifulSoup(login_response.text,'html.parser').find('input', {'name':'csrf'})['value']

login_data = {
        'csrf': csrf,
        'username': 'wiener',
        'password': 'peter'
}

resp = s.post(login_url,data=login_data)

s.headers.update({'Origin':'https://elafleur.com'})

details_url = f"https://{site}/accountDetails"
resp = s.get(details_url)

# View the response headers showing the Origin is echoed
print(resp.headers)

# Get the response containing the API key
print(resp.text)
