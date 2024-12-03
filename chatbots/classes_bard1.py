
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
    for i in ['\n','\r', '\t', '_']:
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

def get_play(chap,collected_works,soup):
    start = re.search(chap, str(soup)).group()
    end = inc_ch(start)
    start = "id=\"" + start
    end = "id=\"" + end
    start_index = collected_works.index(start)
    end_index = collected_works.index(end)
    play = collected_works[start_index:end_index]
    return play


def get_lines(character,play_start):
    char_lines=re.findall(character+".*?[A-Z]{2}", play_start)
    final_lines=[]
    for i in char_lines:
        final_lines.append(re.sub(character+".",'',i)[:-2].lstrip().rstrip())
    return final_lines

def find_action(string):
    return str(re.findall(r"\[.*?\]",string))[2:-2]
def remove_action(dialogue_list):
    no_action=[]
    for i in dialogue_list:
        i=i.replace(find_action(i),"")
        i=i.lstrip().rstrip()
        no_action.append(i)
    return no_action


class Acts():
    def __init__(self,play):
        self.play = play
        act_list=[]



