import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.marxists.org/archive/luxemburg/1898/industrial-poland'

def get_html_links(main_page):
    response = requests.get(main_page)
    soup = BeautifulSoup(response.text, 'html.parser')
    root_menu=soup.find('p', class_='index')
    href_links=root_menu.find_all('a', href=True)
    html_links= [i.get('href') for i in href_links]
    return html_links

links=get_html_links(url)
print(links)
first_page= links[1]

req_url=(f'{url}/{first_page}')


def url_to_text(url_address):
    req = requests.get(url_address)
    soup = BeautifulSoup(req.text, 'html.parser')
    ending = re.findall(r'[^\/]+$', url_address)
    ending1 = ending[0]
    ending2= re.findall(f'..+[.]',ending1)
    p=soup.find_all('p')
    soup_list=[]
    for i in p:
        soup_list.append(i.get_text())
    file = open(f'pol_russ_econ/{ending2[0]}txt','w')
    for j in soup_list:
        file.write(j+'\n')
    file.close()

for i in range(len(links)):
    page = links[i]
    req_url=(f'{url}/{page}')
    url_to_text(req_url)

# url_to_text(req_url)

# for i in links:
#     first_page=i
#     req_url=(f'{url}/{first_page}')
#     r = requests.get(req_url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     p = soup.find_all('p')
#     listicle=[]
#     for j in p:
#         listicle.append(j.get_text())
#     file = open(f'{soup.title.string}.txt','w')
#     for k in listicle:
#         file.write(k+'\n')
#     file.close()
#

