
import requests
import random
import re
import pandas as pd
from bs4 import BeautifulSoup

from classes_bard2 import *


#
url='https://www.gutenberg.org/cache/epub/100/pg100-images.html'
req = requests.get(url)
collected_works = req.text
soup = BeautifulSoup(collected_works, 'html.parser')
table = soup.find('table')
td = table.find_all('td')

title_list=get_titles(soup)
play_list=title_list[1:-5]
poem_indexes=[i for i in range(-5,1)]
poem_list=[title_list[i] for i in poem_indexes]


# Selecting a particular play or poem(poem side doesn't work yet)

# query1=int(input("Greetings to the bard bot. Select 1 for plays and 2 for poems"))
query1=1
play_selection=0
#poem_selection=0

# this runs anyway, until i fix the poem part
if query1==1:
    print('list of plays')
    for i in range(len(play_list)):
        print(str(i+1)+". "+play_list[i])
play_query = int(input("select which play"))
# elif query1==2:
#     for i in range(len(poem_list)):
#         print(str(i+1)+". "+poem_list[i])
#     poem_query= int(input("select which poem"))

#The user inputs which one of the play to use

selected_play=title_list[play_query]
#selected_poem=poem_list[poem_query]

# if poems are selected, present a list of the poems
print("congratulations you selected: ")
print(selected_play)

#pulling the part of the play corresponding to play
chap=""
for i in td:
    if str(i).__contains__(selected_play):
        chapter=re.findall(r"chap..",str(i))
        chap=str(chapter)
        chap=chap[2:-2]

play=get_play(chap,collected_works,soup)

play=clean_html(play)

re.findall("Drama.*?ACT", play)
characters=get_characters(play)
# char_list=list(characters)
# for i in range(len(char_list)):
#     print(str(i+1)+". "+char_list[i])
# char_query=int(input("select which character"))-1
# character= char_list[char_query]
# print(f"\n\n congratulations you have selected {character}")

play_start=re.search(r'ACT I       SCENE I.*',play).group()[:-3]

# +
# act="ACT"
# scene="SCENE"
# numb= ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI"]
# act1= re.findall(act+numb[0]+"(.*?)"+act+numb[1],play_start)
# -

# The plan here is to get and set which act it is, which scene it is, which character it is and then the lines. create a data frame from that information.

# +
# acts=re.findall(act+'...',play_start)
# acts
# start1= acts[0]
# end1= acts[1]
# s=str(re.escape(start1))
# e=str(re.escape(end1))
# -

play_acts= Acts(play_start).return_acts()

#creating dataframe for lists
data_list=[]
for i in range(len(play_acts)):
    act_num= "act_"+str(play_acts.index(play_acts[i])+1)
    act=play_acts[i]
    play_scenes=Scenes(act).return_scenes()
    for j in range(len(play_scenes)):
        scene_num="scene_"+str(play_scenes.index(play_scenes[j])+1)
        scene=play_scenes[j]
        lines=re.findall(r"[A-Z]{3}.*?      ",play_scenes[j])
        for k in range(len(lines)):
            line=get_line(lines[k])
            character=line[0]
            char_line=line[1]
            data_list.append([act_num,scene_num,character,char_line])
            # data.update({"act_num":act_num,"scene_num":scene_num,"character":character,"line":char_line})


df_lines=pd.DataFrame(data_list,columns=['act_num','scene_num','character','line'])


while True:
    query=input(">")
    if query == ("exit" or "quit"):
        print('fare thee well, my liege')
        break
    else:
        print(random.choice(df_lines.line))



