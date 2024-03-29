import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import wordnet as wn
nltk.download('wordnet')

mobyDick = open('/PequodProject/mobyDick.txt', 'r')
mobyDickString = mobyDick.read()

wTokeMobD = word_tokenize(mobyDickString)

mobyDickText = nltk.Text(wTokeMobD)

fMDdist = FreqDist(mobyDickText)




synHarpoon= wn.synsets('harpoon')

whale = wn.synsets('whale')[1]

def returnLemDefEx(synset):
    print(synset.lemma_names())
    print(synset.definition())
    print(synset.examples())
    print(synset.lemmas())

orca= wn.synset('orca.n.01')

cetacean = wn.synset('cetacean.n.01')

print(cetacean.hypernyms())
print(cetacean.hypernym_paths())

print(cetacean.member_holonyms())












