import pytesseract, re,requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

site = 'ac561f7d1e603d91c06e42a4009a0070.web-security-academy.net'
post_url = f'https://{site}/post?postId=3'
s = requests.Session()

resp = s.get(post_url)
soup = BeautifulSoup(resp.text,'html.parser')
avatar_path = soup.find_all('img', src=re.compile(r'png$'))[0].get('src')
avatar_url = f'https://{site}{avatar_path}'
print(avatar_url)

# Use OCR package (Tesseract) to extract hostname
hostname = pytesseract.image_to_string(Image.open(BytesIO(requests.get(avatar_url).content)))

hostname = hostname.strip()
print(f'Exfiltrated hostname: {hostname}')

# Submit to solution URL
solution_url = f'https://{site}/submitSolution'                                 
solution_data = {                
    'answer' : hostname
}    
s.post(solution_url, data=solution_data)