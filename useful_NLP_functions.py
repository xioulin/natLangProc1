import re
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
from statistics import mean,stdev,variance,median
def lexical_density(entireTextString):
    wordTokenized= word_tokenize(entireTextString)
    return "The lexical density is "+str(round((len(set(wordTokenized))/len(wordTokenized))*100,2))+'%'

def exclToTextRatio(text):
    matchExcl = re.findall(r'!',text)
    lenExcl= len(matchExcl)
    lenText= len(text)
    return "The ratio of exclamation marks to total text is "+str(  round((lenExcl/lenText)*100,3)  )+"%"

def findWordsLongerThan(text,int):
    word_Tokened= word_tokenize(text)
    largerThan= [i for i in word_Tokened if len(i)>int]
    return(Counter(largerThan))

def filterStopWordsList(list):
    stop_words= stopwords.words('english')
    filteredList = []
    for word in list:
        if word.casefold() not in stop_words:
            filteredList.append(word)
    return filteredList


def filterStopandPunctList(list):
    stop_words = stopwords.words('english')
    punctuationList = ["\'","\"",",",".","!","?",";",":",'”','$', '(', ')', '*','“','’','‘','_']
    stop_words= stop_words+punctuationList
    filteredList = []
    for word in list:
        if word.casefold() not in stop_words:
            filteredList.append(word)
    return filteredList

def filterPunct_Num_Contractions(list):
    newList = [i for i in list if i[0].isalpha() and '.' not in i]
    punctuationAndContractionList = ["\'", "\"", ",", ".", "!", "?", ";", ":", '”', '$', '(', ')', '*', '“', '’', '‘', 't', 'à', 'd', 'l', 's', 'C', 'm','S','o','Y','ve','re','ll','O','n','ed']
    filteredList = []
    for word in newList:
        if word.casefold() not in punctuationAndContractionList:
            filteredList.append(word)
    return filteredList

def returnBasicStatsList(list):
    Mean= ("the mean of this list is " + str(round(mean(list),2))      )
    Median= ("the median of this list is " + str(round(median(list),2))      )
    StDev= ("the standard deviation of this list is " + str(round(stdev(list),2))      )
    Variance= ("the variance of this list is " + str(round(variance(list),2))      )
    Max= ("the max value of this list is "+ str(max(list)))
    return print(' '+Mean,"\n",Median,"\n",StDev,"\n",Variance,"\n",Max)

def returnBasicWordsPerSentStatsList(list):
    Mean= ("the average number of words per sentence in this book is " + str(round(mean(list),2))      )
    Median= ("the median number of words per sentence in this book is  " + str(round(median(list),2))      )
    StDev= ("the standard deviation of words per sentence in this book is " + str(round(stdev(list),2))      )
    Variance= ("the variance words per sentence in this book is " + str(round(variance(list),2))      )
    Max= ("the most words per sentence in this book is  "+ str(max(list)))
    return print(' '+Mean,"\n",Median,"\n",StDev,"\n",Variance,"\n",Max)



def cleanWordTokedSentences(string):
    sentTokeWhole = sent_tokenize(string)
    wordTokeIt = [word_tokenize(i) for i in sentTokeWhole]
    filtered= [filterPunct_Num_Contractions(i) for i in wordTokeIt]
    return filtered

def words_per_sentList(sentList):
    wordsPerSentList = []
    for sent in sentList:
        wordsPerSentList.append(len(sent))
    return wordsPerSentList