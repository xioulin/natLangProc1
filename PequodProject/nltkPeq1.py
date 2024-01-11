import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

mobyDick = open('/Users/pkc/PycharmProjects/natLangProc1/NLTKbook/mobyDick.txt','r')
mobyDickString = mobyDick.read()
wTokeMobD = word_tokenize(mobyDickString)

mobyDickText = nltk.Text(wTokeMobD)

fMDdist = FreqDist(mobyDickText)


from nltk.corpus import wordnet as wn

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



# print(shipNoun)
# print(shipNoun.hyponyms())
# print(shipNoun.hypernym_paths())












