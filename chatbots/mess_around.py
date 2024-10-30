
from bs4 import BeautifulSoup
import requests
from classess import MarxTextParser
url = 'https://www.marxists.org/archive/marx/works/1847/wage-labour/ch08.htm'

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
print(soup.title.string)


wage_theft = MarxTextParser(url)

wage_theft.url_to_text()

