import pathlib
import requests
import re
import os
from bs4 import BeautifulSoup

from keybert import KeyBERT
import pathlib


def TextFromFile(file_path):
    file = open(file_path, 'r')
    text = file.read()
    file.close()
    return text

class MarxTextParser():
    def __init__(self, url):
        self.url = url

    def url_to_text(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'html.parser')
        title =soup.title.string.replace(' ','_')

        p = soup.find_all('p')
        soup_list = []
        for i in p:
            soup_list.append(i.get_text())
        query = input('what do you want to call this folder?')
        path = pathlib.Path(query)
        if not os.path.exists(path):
            os.mkdir(path)

        file = open(f'{path}/{title}.txt', 'w')
        for j in soup_list:
            file.write(j + '\n')
        file.close()


class DirectoryListDocs():
    def __init__(self,directory):
        list_of_docs=[]
        self.directory = directory


    def return_files(directory):
        path_name = str(directory)
        dire= pathlib.Path(path_name)
        list_of_docs=[]
        for i in dire.iterdir():
            if i.is_file():
                file = open(i, 'r')
                text = file.read()
                file.close()
                text = str(text)
                list_of_docs.append(text)
        return list_of_docs


class BookScraper():
    def __init__(self, url):
        url=self.url

    def url_to_text(url):
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        ending = re.findall(r'[^\/]+$', url)
        ending1 = ending[0]
        ending2 = re.findall(f'..+[.]', ending1)
        p = soup.find_all('p')
        soup_list = []
        for i in p:
            soup_list.append(i.get_text())
        file = open(f'pol_russ_econ/{ending2[0]}txt', 'w')
        for j in soup_list:
            file.write(j + '\n')
        file.close()


class PageTextScraper():
    def __init__(self,url,dir_path):
        self.url = url
        self.dir_path= dir_path
    def create_dir(self):
        pathlib.Path(self.dir_path).mkdir(parents=True, exist_ok=True)

    def extract_text(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'html.parser')
        # ending = re.findall(r'[^\/]+$', url_address)
        # ending1 = ending[0]
        # ending2= re.findall(f'..+[.]',ending1)
        p = soup.find_all('p')
        soup_list = []
        for i in p:
            soup_list.append(i.get_text())
        file = open(f'{self.dir_path}/call_of','w')
        for j in soup_list:
            file.write(j + '\n')
        file.close()

class KeywordExtractor():
    from keybert import KeyBERT
    import pathlib

    def __init__(self,directory):
        self.directory = pathlib.Path(directory)

    def extract_keywords(self):
        model = KeyBERT('distilbert-base-nli-mean-tokens')
        for i in self.directory.iterdir():
            if i.is_file():
                file = open(i, 'r')
                text = file.read()
                file.close()
                text = str(text)
                keywords = model.extract_keywords(text)
                listicle = [i for i in keywords]
                print(f'the keywords for {i} are: ')
                for j in listicle:
                    print(j)
