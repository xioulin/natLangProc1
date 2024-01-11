
import nltk
import re
from statistics import mean,stdev,variance,median
from nltk.tokenize import sent_tokenize, word_tokenize

mobyString = open('/Users/pkc/PycharmProjects/natLangProc1/NLTKbook/mobyDick.txt', 'r')
with mobyString as f:
    lines = f.readlines()
mobDickString = lines[0]
mobDickString= mobDickString[22240:] #redefine the book string starting from chapter 1
#word tokenize and sentence tokenize the book string
wTokedMobDick= word_tokenize(mobDickString) # len is about 260k, need to clean out punctuation and stopwords
sTokedMobDick= sent_tokenize(mobDickString)#len of this list is 9697 so Moby Dick has almost 10k sentences

from useful_NLP_functions import cleanWordTokedSentences, words_per_sentList, returnBasicWordsPerSentStatsList
# cleanWordTokedSentences does a sent_tokenize on a string and word_tokenizes each sentence, cleaning out  non-words
mobyDickWordAndSentTokedClean= cleanWordTokedSentences(mobDickString)

w_per_s_Mob_d= words_per_sentList(mobyDickWordAndSentTokedClean) #calculates how many words per sentence

returnBasicWordsPerSentStatsList(w_per_s_Mob_d) # takes list of cleanly word and sent tokenized book and returns word per sentence stats

# print([word_tokenize(i) for i in sent_tokenize(mobDickString)[:10]])
# print(mobyDickWordAndSentTokedClean[:10])

from useful_NLP_functions import exclToTextRatio
from useful_NLP_functions import lexical_density
from useful_NLP_functions import findWordsLongerThan


sentLengthList=[] #initialize empty list to store the length of sentences as tokenized in the list, for data analysis
for i in sTokedMobDick:
    sentLengthList.append(len(i))
meanSentLength= 126.6 #round(mean(sentLengthList),1)

sentOver5List = [i for i in sentLengthList if i>5]
sortedSentLengthList = sTokedMobDick
# sortedSentLengthList.sort(key=len)
# cleanerSentTokeList = [i for i in sortedSentLengthList if len(i)>8] #this has cleaned out the sent_tokenized with small lens

from numpy import percentile
Q1 = percentile(sentOver5List,25, interpolation='midpoint')
Q3 = percentile(sentOver5List,75, interpolation='midpoint')
# print(median(sentOver10List))
# print(Q1)
# print(Q3)
# print(mean(sentOver10List))
# print(stdev(sentOver10List))

firstFiveSent= sTokedMobDick[:5]
wTokeFirstFive = [word_tokenize(i) for i in firstFiveSent] # how to word_tokenize every sentence


import matplotlib.pyplot as plt
import numpy as np
# plt.hist(sentOver10List,bins=80)
# plt.show()
# plt.boxplot(sentOver10List)
# plt.show()

#based on that terrible box and whiskers chart, that's why you need to clean data
#there's that one sentence that's the outlier, the whiteness intro

maxSentLength= 2843
indexMaxSentLength= "3375:3377"
maxSentence=''.join(sTokedMobDick[3375:3377])
numOfWordsMaxSent= 541 #word_tokenize(maxSentence) and find the len of it
# matchWhite=re.findall(r'[wW]hite',mobDickString)
# matchBlack=re.findall(r'[Bb]lack',mobDickString)
# for i in sTokedMobDick:
#     if len(i)>2000:
#         print(sTokedMobDick.index(i))

formedInSentence= ''
for i in sTokedMobDick:
    if "whiteness" in i:
        # print(sTokedMobDick.index(i))
        formedInSentence=i
# print(formedInSentence)



whitenessChapter = sTokedMobDick[3370:3470]
# print(whitenessChapter)
whitenessString = ''.join(whitenessChapter)
wTokeWhitenessCh= word_tokenize(whitenessString)
# print(whitenessString)
from nltk.tag import pos_tag
whitenessTagged = nltk.pos_tag(wTokeWhitenessCh)
# print(whitenessTagged)

from nltk.corpus import wordnet as wn
# print(whiteColorDef.hypernym_paths())
# print(wn.synset('achromatic_color.n.01').hyponyms())
# print(wn.synset('color.n.01').hyponyms())
# print(wn.synset('chromatic_color.n.01').hyponyms())


colorList=['white','black','grey','gray','blue','yellow','orange','red','green']
redList = []
for i in wTokedMobDick:
    if i.startswith('red'):
        redList.append(i)
whiteCounter=0
# for i in wTokeWhitenessCh:
#     if ("white" or "White") in i:
#         whiteCounter+=1
# print(whiteCounter)

theString= 'The theologian thought that they were in the theoretical apotheoiss.'
matchThe= re.findall(r'[tT]he',theString)


matchWhite = re.findall(r'[Ww]hite.',mobDickString)
# print(matchWhite)
#so about 61 mentions if white or something to do with whiteness in this chapter

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
# print(stopwords)

# whitenessCleaned=[]
# for i in wTokeWhitenessCh:
#     if i not in stopwords:
#         whitenessCleaned.append(i)

nessWords=[]
for i in wTokedMobDick:
    if i.endswith('ness'):
        nessWords.append(i)
from collections import Counter
# print(len(nessWords))
nessCounter= Counter(nessWords)

# for i in sTokedMobDick:
#     if "ebonness" in i:
#         print(sTokedMobDick.index(i))

# print(sTokedMobDick[3734:3750])

# print([i for i in nessCounter if nessCounter.values()!=1])


