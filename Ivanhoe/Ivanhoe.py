import PyPDF2
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# pdfObject = open('ivanhoe.pdf','rb')
# pdfReader = PyPDF2.PdfReader(pdfObject)
# #extracts the contents of the first pdf page and turns it into
# #a long string
# print(len(pdfReader.pages))

# obj = {}
# for i in range(0,16):
#     obj[i]=pdfReader.pages[i].extract_text()
#
# fullText = []
# for i in range(0,len(obj)):
#     fullText += obj[i]

# print(type(fullText))

# fullTextString = ''
# for i in fullText:
#     fullTextString += i

# print(len(fullTextString))
# print(type(fullTextString))

from nltk import word_tokenize,sent_tokenize

# wordTokenizedIvanhoe = word_tokenize(fullTextString)
# print(wordTokenizedIvanhoe[8920:9020])
# print(wordTokenizedIvanhoe[0:9000].index('ANHOE.CHAPTER'))
# print(wordTokenizedIvanhoe[0:13200].index('charge.CHAPTER'))



# ivanhoeTextFile = open('/Users/pkc/PycharmProjects/natLangProc1/Ivanhoe.txt','w')
# ivanhoeTextFile.write(fullTextString)
# ivanhoeTextFile.close()
#
from nltk.text import Text
from nltk.corpus import gutenberg

ivanhoeText = open('/Ivanhoe/Ivanhoe.txt')
raw = ivanhoeText.read()
print(raw)

# ivanhoeTextFile = open("/Users/pkc/PycharmProjects/natLangProc1/Ivanhoe.txt",'r')
# print(type(ivanhoeTextFile))
# corpus = gutenberg.words()
# ivanhoeTextText = Text(corpus)
# print(type(ivanhoeTextText))
# print(len(ivanhoeTextText))
# print(ivanhoeTextText.generate())
# print(type(ivanhoeRead))
# wordTokenizedIvanhoe[13000:15500].index('CHAPTER')

# ivanhoePage1 = pdfReader.pages[1].extract_text()
#the len of the string ivanhoePage1 is the number of characters
#it contains which is 74862. Quite a lot
##print(len(ivanhoePage1))

#let's turn that into a list
# ivanhoePage1List = list(ivanhoePage1)
# #now there are 74862 elements in the list ivanhoePage1list
# # print(len(ivanhoePage1List))
# #let's see how many unique letters/characters there are in that list
# # print(len(set(ivanhoePage1List)))
# #it says 75, how do we find how many unique words there are
# #probably need to use nltk
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
# #break down the first section string into separate word characters
# wordTokenizedIvanhoePage1 = word_tokenize(ivanhoePage1)
# sentenceTokenizedIvanhoePage1 = sent_tokenize(ivanhoePage1)
# #how many separate word characters are there in first section
# print(len(wordTokenizedIvanhoePage1))
# #how many unique words there are in first section
# print(len(set(wordTokenizedIvanhoePage1)))
# print(set(wordTokenizedIvanhoePage1))

#a function which returns which percentage of total words used
#are used uniquely once, basically what the variety is of words
def lexical_density(text):
    return len(set(text)) / len(text)

# print(len(sentenceTokenizedIvanhoePage1))
# print(type(sentenceTokenizedIvanhoePage1))
# print(sentenceTokenizedIvanhoePage1[0])


from nltk.corpus import stopwords
# print(type(stopwords))
punctuation = [',','.','!','?',';',':',')','(']
stop_words_and_punctuation = stopwords.words('english')+punctuation
# print(stop_words_and_punctuation)

# print(len(set(wordTokenizedIvanhoePage1)))
ivanhoePage1FilteredList = []
# for word in wordTokenizedIvanhoePage1:
#     if word.casefold() not in stop_words_and_punctuation:
#         ivanhoePage1FilteredList.append(word)
# print(len(ivanhoePage1FilteredList))
# ivanhoePage1FilteredList = set(ivanhoePage1FilteredList)
# print(len(ivanhoePage1FilteredList))


#this nifty little function basically just takes a
#empty list for collecting, and then just put the list of words
#that you want into the function filterStopAndPunct(list)
#and the empty list will populate with words that are not stopwords
def filterStopAndPunct(list):
    for word in list:
        if word.casefold() not in stop_words_and_punctuation:
            ivanhoePage1FilteredList.append(word)
# filterStopAndPunct(wordTokenizedIvanhoePage1)
# print(len(ivanhoePage1FilteredList))

setIvanhoePage1FilteredList = set(ivanhoePage1FilteredList)
# print(len(setIvanhoePage1FilteredList))


# print(ivanhoePage1FilteredList)
# print(len(stopwords.words('english')))
#most frequent words in first section



# print(ivanhoePage1)