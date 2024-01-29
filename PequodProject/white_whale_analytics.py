
import nltk
import re
from nltk import sent_tokenize,word_tokenize
from useful_NLP_functions import cleanWordTokedSentences

mobyString = open('/Users/pkc/PycharmProjects/natLangProc1/NLTKbook/mobyDick.txt', 'r')
with mobyString as f:
    lines = f.readlines()
mobDickString = lines[0]

mobDickString=mobDickString[22240:]



sTokedMobDick= sent_tokenize(mobDickString)#len of this list is 9697 so Moby Dick has almost 10k sentences
wTokedMobDick= word_tokenize(mobDickString) # len is about 260k, need to clean out punctuation and stopwords

first_Par_sToked= sTokedMobDick[:9]

first_Par_String = ''.join(first_Par_sToked)

first_Par_wToked= word_tokenize(first_Par_String)

print(first_Par_wToked)

# print(first_Par_wToked)

clean_first_Par=cleanWordTokedSentences(first_Par_String)

print(clean_first_Par)

