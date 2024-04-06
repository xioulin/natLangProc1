import shutil
from getPrezName import getPrez
import requests
from bs4 import BeautifulSoup

url= 'https://www.loc.gov/free-to-use/presidential-portraits/'
page= requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results= soup.find(class_="search-results grid-view public-domain-results public-domain-set")
prez_images= results.find_all('img')

base_url= 'https://www.loc.gov/'
# url_ext= prez_img[0].attrs['src']
# full_url = base_url+url_ext
# r= requests.get(full_url, stream=True)


"""
this for loop runs through the entire prez_img


for i in range(len(prez_img)):
    url_ext = prez_img[i].attrs['src']
    full_url = base_url + url_ext
    r = requests.get(full_url, stream=True)
    if r.status_code==200:
        with open(f'prez_img/{getPrez(prez_img[i].attrs["src"])}.jpg','wb') as f:
            r.raw.decode_content=True
            shutil.copyfileobj(r.raw,f)
"""


