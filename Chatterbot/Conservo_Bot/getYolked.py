import requests
from bs4 import BeautifulSoup



url='https://www.firstthings.com/web-exclusives/2024/01/more-confusion-about-same-sex-blessings'
r= requests.get(url)

soup= BeautifulSoup(r.content, 'html.parser')

elems = soup.find('div', class_='primary')
print(elems)
