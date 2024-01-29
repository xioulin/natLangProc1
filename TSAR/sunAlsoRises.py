from statistics import mean,stdev,variance,median
# from urllib import request
#
# url= 'https://www.gutenberg.org/cache/epub/67138/pg67138.txt'
#
# import ssl
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# response = request.urlopen(url)
# raw=response.read().decode('utf8')
hemingwayFile = open(r'SunAlsoRises.txt', 'r')
with hemingwayFile as f:
    wholeBook= f.read()
hemingwayFile.close()

from useful_NLP_functions import exclToTextRatio,lexical_density,findWordsLongerThan,word_tokenize,sent_tokenize,filterStopWordsList, filterStopandPunctList, filterPunct_Num_Contractions,returnBasicStatsList, cleanWordTokedSentences,returnBasicWordsPerSentStatsList, words_per_sentList

fromEpigraph= wholeBook[725:]
wordTokeTSARList= word_tokenize(fromEpigraph) # the len for this list is 88788
# print(wordTokeTSARList[:50])
# filtWordTokeList = filterPunctAndNumbers(wordTokeTSARList)

#cleanWordTokedSentences is a function that sent_tokenizes, then word tokenizes each sentence and filters for contractions and odd stuff
cleanWordTokeSent= cleanWordTokedSentences(fromEpigraph)
cleanWorSenToke= cleanWordTokeSent[12:] #the epigraphs are a mess, this is to basically start with the first chapter
firstPar=cleanWorSenToke[:13]


words_per_sent_LengthList= words_per_sentList(cleanWorSenToke)

# returnBasicWordsPerSentStatsList(words_per_sent_LengthList)
# print([i for i in words_per_sent_LengthList if i>80])
import matplotlib.pyplot as plt
words_per_sent_LengthList.sort(reverse=True)

longestSentWToked= cleanWorSenToke[2027:2028]
longestSent = fromEpigraph[134350-970:134350]




