import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.nationalreview.com/2024/01/abortion-is-a-convenient-scapegoat-for-magas-political-weaknesses/')


soup= BeautifulSoup(r.content, 'html.parser')
s= soup.find('article',id="post-1588392")

print(s)
# content=s.find_all('p')
# print(content)





