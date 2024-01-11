import PyPDF2

#this creates a python object that takes in the pdf file specified
#and sorts it into a readable binary format
pdfObject = open('neruda-20-love-poems.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdfObject)

from nltk.tokenize import sent_tokenize,word_tokenize

# print(len(pdfReader.pages))

# print(pdfReader.pages[3].extract_text())

# print(type(pdfReader.pages))

# print(pdfReader.pages[3].extract_text())

cuerpoDeMujer = pdfReader.pages[3].extract_text()
cuerpoDeMujerWords = word_tokenize(cuerpoDeMujer)

theLightWrapsYou = pdfReader.pages[4].extract_text()
print(theLightWrapsYou)
# print(cuerpoDeMujer)


# print(cuerpoDeMujerWords)

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
punctuation = [',','.','!','?']
stop_words_and_punctuation = stop_words+punctuation
# print(stop_words_and_punctuation)

# print(stop_words)

cuerpoDeMujerFiltered_list = []
for word in cuerpoDeMujerWords:
     if word.casefold() not in stop_words_and_punctuation:
        cuerpoDeMujerFiltered_list.append(word)

def filterStopAndPunct(list):
    otherList = []
    for word in list:
        if word.casefold() not in stop_words_and_punctuation:
            otherList.append(word)
    return otherList
# filterStopAndPunct(cuerpoDeMujerWords)
# print(cuerpoDeMujerFiltered_list)

count = 0
for word in cuerpoDeMujerFiltered_list:
    if word.casefold() == 'woman':
        count +=1
# print(count)

moreThanOneTime = []
for word in cuerpoDeMujerFiltered_list:
    if cuerpoDeMujerFiltered_list.count(word) > 1:
        moreThanOneTime.append(word)
# print(set(moreThanOneTime))

# print(cuerpoDeMujer)
# print(sent_tokenize(cuerpoDeMujer))
cuerpoDeMujerList = list(cuerpoDeMujer)
firstSentenceList = cuerpoDeMujerList[2:104]
firstSentenceString = ''.join(firstSentenceList)
# print(firstSentenceString)
#
# print(cuerpoDeMujerList[105:200])
#
# print(cuerpoDeMujer.index('.'))


# print(cuerpoDeMujerList[2:103])



# def commaLineBreaker(poem):
#     poem.find()
#     return

# print(cuerpoDeMujer)



