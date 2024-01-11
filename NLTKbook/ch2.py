
import nltk
# print(nltk.corpus.gutenberg.fileids())

blake = nltk.corpus.gutenberg.words('blake-poems.txt')

# print(len(set(emma)))

from nltk.corpus import webtext

# from nltk.corpus import reuters
# print(reuters.words(fileids='training/999'))
# print(reuters.categories())
# print(reuters.categories('training/9865'))
# print(reuters.fileids('nickel'))

# print(len(reuters.words('training/9865')))

def listToSString(s):
    str1 = ' '
    return(str1.join(s))

# article9865=listToSString(reuters.words('training/9865'))
# print(article9865)

# from nltk.corpus import inaugural
# print(inaugural.words('2005-Bush.txt'))
#this short script creates a text file and writes into it President Harrison's inaugural address from 1841
# harrisonFile = open(r'/Users/pkc/PycharmProjects/natLangProc1/1841Harrison.txt','w')
# harrisonList = inaugural.words('1841-Harrison.txt')
# harrisonString = listToSString(harrisonList)
# harrisonFileW = open('/Users/pkc/PycharmProjects/natLangProc1/1841Harrison.txt','w')
# harrisonFileW.write(harrisonString)

from nltk.corpus import wordnet as wn


def returnLemDefEx(synset):
    print(wn.synset(synset).lemma_names())
    print(wn.synset(synset).definition())
    print(wn.synset(synset).examples())







