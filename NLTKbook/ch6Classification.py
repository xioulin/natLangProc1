import nltk


def gender_features(word):
    return {'last_letter':word[-1]}

gender_features('Domina')

from nltk.corpus import names

labeled_names = ( [(name,'male') for name in names.words('male.txt')]
    + [ (name,'female') for name in names.words('female.txt')]
)

import random
random.shuffle(labeled_names)

featuresets= [(gender_features(n), gender) for (n,gender) in labeled_names]

train_set, test_set = featuresets[500:], featuresets[:500]

classifier= nltk.NaiveBayesClassifier.train(train_set)

# print(classifier.classify(gender_features('Troy')))
# print(classifier.classify(gender_features('Abdullah')))
#
# print(nltk.classify.accuracy(classifier,test_set))

from nltk.corpus import movie_reviews

documents= [(list(movie_reviews.words(fileid), category )
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)

             )]
random.shuffle(documents)

all_words= nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features= list(all_words)[:2000]

def document_features(document):
    document_words= set(document)
    features= {}
    for word in word_features:
        features['contains({})'.format(word)]=(word in document_words)
    return features

# print(document_features(movie_reviews.words('pos/cv957_8737.txt')))

from nltk.corpus import brown
suffix_fdist= nltk.FreqDist
# for word in brown.words():
#     word= word.lower()
#     suffix_fdist[word[-1:]] += 1
#     suffix_fdist[word[-2:]] += 1
#     suffix_fdist[word[-2:]] += 1

# common_suffixes= [suffix for (suffix,count) in suffix_fdist.most_common(100)]
# print(common_suffixes)

from nltk import word_tokenize

salleyGardens= "Down by the salley gardens, my love and I did meet."
taggedYeats = nltk.pos_tag(word_tokenize(salleyGardens))

grammar= 'NP: {<DT>?<JJ>*<NN>}'

cp= nltk.RegexpParser(grammar)
result= cp.parse(taggedYeats)


verbalize= "The rich old banker met the grizzled young prosecutor in a jail cell"
taggedV= nltk.pos_tag(word_tokenize(verbalize))
grammar=r"""
    NP:
        {<.*>+}
        }<VBD|IN>+{
"""
print(cp.parse(taggedV))


# import json
# import urllib
# import requests
#
# url= 'https://parseapi.back4app.com/classes/Complete_List_Names?count=1&limit=10'
#
# headers= {
#     'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I',  # This is the fake app's application id
#     'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK'  # This is the fake app's readonly master key
# }
#
# data=json.loads(requests.get(url,headers=headers).content.decode('utf-8'))
#
# print(json.dumps(data,indent=2))




