import re


salleyGardenString= 'Down by the Salley Garden, my love and I did meet.'

matchCap= re.findall('\W', salleyGardenString)
print(matchCap)


blackSheepString= "baa baa black sheep, have you any wool? Yessir, yes sir, three bags full"
matchSheep = re.findall('ba*',blackSheepString)
print(matchSheep)




# listOfStuff= ['2',"the","police","1231.",'3', '16', '19', 'sun', '17', 'yet', 'H.', '4', 'Aw', '2', 'em', 'run', 'eh', '18', 'C', '_in', 'oh', '7', 'un', 't.', '12', 'D.', '30', 'B.', 'us', 'I.', 'ed', 'R.', 'lot', 'Ah', 'de', '11', '1', '14', '5', 'One', 'P.', '6', 'Mr', 'à', '8', 'L.', '9', '15', 'l', 'E.', '10', 'Si', 'W.', 'A.', 'n', 'go', 'du', 'Es', 'G.', 'sea', 'Go', 's.', 'II',]
#
# for word in listOfStuff:
#     if word[0].isdigit:
#         listOfStuff.remove(word)
#
# print(listOfStuff)
#
# modifList = [ i for i in listOfStuff if i[0].isalpha()  and '.' not in i]
# print(modifList)

# import nltk

# mobyString = open('/Users/pkc/PycharmProjects/natLangProc1/NLTKbook/mobyDick.txt', 'r')
# with mobyString as f:
#     lines = f.readlines()
# mobDickString = lines[0]
#
# charList = ['Ishmael', 'Queequeg', 'Elijah', 'Starbuck', 'Ahab', 'Flask', 'Peleg', 'Bildad','Stubb','Tashtego','Daggoo']
# def findCharListMentions(characterList):
#     matchList = [str('match') + str(i) for i in characterList]
#     for i in range(len(matchList)):
#         matchList[i] = re.findall(characterList[i], mobDickString)
#     print("\nMoby Dick Character and number of mentions in novel:\n")
#     for i in matchList:
#         try:
#             print((i[0].ljust(8) + ': ' + str(len(i)).rjust(3)).center(16))
#         except IndexError:
#             print("****WARNING*** the character'" + characterList[
#                 matchList.index(i)] + "' is not mentioned in the novel'")
#


# matchPequod = re.findall('Pequod', mobDickString)
# britBackside = "the british say arse while we americans say ass, i don't know if the Australians even discuss things down under"
# matchColour = re.findall('a[rs]se?', britBackside)
# matchWhiteWhale = re.findall('[wW]hite whale',mobDickString)
# matchWhiteness= re.findall('whiteness',mobDickString)

petOwnerString = "I used to want to get a cat, but then i got a dog, and now I am what i am, a miserable dog owner"
matchCatDog = re.findall('cat|dog',petOwnerString)

guppyString = "I decided that I wanted to get a guppy but then I got a good deal and ended up with twenty guppies"
matchGuppy = re.findall('guppy|guppies',guppyString)


#pick out the but not thee

theString = "The string is not for thee my friend but for the theatre where the theological theosophists theorize"
matchThe = re.findall('\bnot\b',theString)

loveString ="I totally love you babe, like, I like so love you, like our love is like a soullove, like no other love"
matchLove = re.findall('love{3,}',loveString)

#find references to sperm whales by the references of parmacetti, parm, or what have you

#
# matchParm = re.findall('parm',mobDickString)
#
# matchQuaker = re.findall('Quakers?',mobDickString)
#
# matchExclamation = re.findall('!',mobDickString)
#
# matchQuestion = re.findall('\?',mobDickString)
# matchChapter = re.findall('CHAPTER',mobDickString)
# print(len(matchChapter))
listOfNumbers = [1,2,3,4,1,5,6,7,1]
indexListOf1 = []
for i in range(0,len(listOfNumbers)):
    if listOfNumbers[i]==1:
        indexListOf1.append(i)
# print(indexListOf1)
#dispersion between each individual question mark and each exclamation point, suggesting excitability in author if more
#dispersion between question marks than exclamation points
# from nltk import word_tokenize,sent_tokenize
# wordTokeMD= word_tokenize(mobDickString)

#gives index for each occurence of CHAPTER therefore way to split up novel string into chapters
# chapterIndexList=[]
# for i in range(0,len(wordTokeMD)):
#     if wordTokeMD[i] == 'CHAPTER':
#         chapterIndexList.append(i)
#
# listSetWordTokeMD = list(set(wordTokeMD))
#
# listSetWordTokeMD.sort(key= len, reverse=True)
# longestMDword = listSetWordTokeMD[0:50][0]
#
# longerThan15MD = [w for w in listSetWordTokeMD if len(w)>15]

# print(len(longerThan15MD))
#
# for i in longerThan15MD:
#     print( (i.ljust(20)+str(len(i)).rjust(6)) )
#uninterpenetratingly

# print(mobDickString.index(
#     'CHAPTER 109'))

# print(mobDickString[1047413-4600:1047413+4600])
# print(mobDickString[500000-10370:500000+15000])
#
# ch48String= mobDickString[489631:513042]
#
# ch48sent= sent_tokenize(ch48String)
# ch48FirstSent= ch48sent[1]
#
#
# ch48FirstSentPoS= nltk.pos_tag(word_tokenize(ch48FirstSent))

# print(ch48FirstSentPoS[0][1])
# for i in ch48FirstSentPoS:
#     if i[1]=='JJ':
#         JJcounter+=1
    # print(i[1])
#
# ch48word_toke = word_tokenize(ch48String)
# ch48FirstPar=ch48word_toke[:225]
# # print(ch48word_toke)

# print(set([w for w in ch48word_toke if w.endswith('ing') and len(w)>4]))



#
# sent1= "the bitch was lying"
# sent2= "the lying bitch was right"
#
# print(nltk.pos_tag(word_tokenize(sent1)))
# print(nltk.pos_tag(word_tokenize(sent2)))

# ch48PoS= nltk.pos_tag(ch48word_toke)
# JJcounter=0
# for i in ch48PoS:
#     if i[1]=='JJ':
#         JJcounter+=1
# print(JJcounter)


# print(nltk.pos_tag(ch48FirstPar))

# print(mobDickString.index('CHAPTER 49'))

# listOfWords = ['apple','bear','cat','platypus','orangutan','pterydactal']
#
# listOfWords.sort(key=len,reverse= True)






aTaleOfTwo= "It was the best of times it was the worst of times, or so said Tiny tim, so to speak in a timely manner"
matchTimes = re.findall(r'^[tim]',aTaleOfTwo)



