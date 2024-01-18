import requests
from bs4 import BeautifulSoup


url='https://www.lifesitenews.com/blogs/canadas-military-stigmatized-straight-white-dudes-now-it-has-a-recruitment-crisis/'
r= requests.get(url)

soup= BeautifulSoup(r.content, 'html.parser')

s=soup.find(id='primary')
lines= s.find_all('p')
# print(lines)
# print(lines[:25])
lines_list= list(lines)
# print(lines_list)
print(lines_list)
# content=s.find_all('p')
# print(content)





