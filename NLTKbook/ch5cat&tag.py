from nltk import word_tokenize
import nltk

fault_stars=  word_tokenize('The fault, dear Brutus, lies not in our stars, But in ourselves, that we are underlings.')

print(nltk.pos_tag(fault_stars))



