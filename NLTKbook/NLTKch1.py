import nltk
# from nltk import FreqDist
#
from nltk.book import text1, text6,sent2


# print("\nthe number of different invidual words in moby dick is: "+str(len(set(text1)))+'\n')
#This is importing the frequency distribution and applying it to the text
# fdistMobyDick = FreqDist(text1)
#printing off the 50 most common words in Moby Dick
# print(fdistMobyDick.most_common(0:100))
# print(fdistMobyDick.hapaxes())


# print(sent2)
# hapaxList12 = [w for w in fdistMobyDick.hapaxes() if len(w)>10]

# adverbHapaxListMobyDick =[]
# for word in hapaxList12:
#     if word.endswith('ly'):
#         adverbHapaxListMobyDick.append(word)
#
# allCapsMobyDick=[]
# for word in text1:
#     if word.isupper() and len(word)>1:
#         allCapsMobyDick.append(word)
# print(allCapsMobyDick)
# print(adverbHapaxListMobyDick)

# print(text1.concordance('CHAPTER'))

# makePossAdverbList(hapaxList12)

# print(text1.collocations())

# print(text6.collocations())

# print(text6[0:100])

# first250HolyGrail = text6[0:250]

def join_text(list):
    text = ' '.join(list)
    return print(text)

# join_text(first250HolyGrail)

fileMobyDick = open(r'/PequodProject/mobyDick.txt', 'w')

fileMD = open('../PequodProject/mobyDick.txt', 'w')

mobyDickList=list(text1)

def listToString(s):
    str1 = ' '
    return(str1.join(s))

mobyDickString= listToString(mobyDickList)

# print(mobyDickString[0:125])

fileMD.write(mobyDickString)

