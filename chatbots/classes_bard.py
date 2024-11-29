
import requests
import re
from bs4 import BeautifulSoup


def get_soup(url):
    req = requests.get(url)
    collected = req.text
    soup = BeautifulSoup(collected, 'html.parser')
    return soup

def get_titles(soup):
    table = soup.find('table')
    td = table.find_all('td')
    title_list = []
    for i in range(len(td)):
        title = re.findall('\">(.*?)</a>', str(td[i]))
        title = str(title)
        title = title[2:-2]
        title_list.append(title)
    return title_list

#a simple function to produce chapter splits in text
def inc_ch(chapt):
    ch_num=re.search(r'\d{2}',chapt).group()
    ch=int(ch_num)
    ch+=1
    if ch<10:
        stringed= "0"+str(ch)

    else:
        stringed= str(ch)
    return chapt.replace(ch_num,stringed)


def clean_html(play):
    html = re.findall('<.*?>', play)
    for i in html:
        play = play.replace(i, " ")
    for i in ['\n', '\r', '\t', '_']:
        play = play.replace(i, " ")
    xss = re.findall('x.+[1-9]', play)
    for i in xss:
        play = play.replace(i, " ")
    thingy = re.findall('\\\xa0', play)

    for i in thingy:
        play = play.replace(i, " ")

    return play

def get_characters(play):
    characters = re.findall("Dramatis.*?ACT", play)

    characters = characters[0]

    descr = re.findall("[A-Z]{3}.+?[A-Z][a-z].*?   ", characters)

    # create a dictionary of characters, use all caps for character and what follows as description
    char_dict = {}
    for i in descr[:-1]:
        caps = re.findall(r'[A-Z]{2}.*?\b', i)
        f_name = " ".join(caps)
        char_d = re.sub(r"([A-Z]{2})", '', i)[1:]
        char_d = re.sub(r", ", '', char_d).lstrip().rstrip()
        # row = {'name':f_name,'descr':char_d}
        # print(f_name,char_d)
        char_dict.update({f_name: char_d})
    return char_dict