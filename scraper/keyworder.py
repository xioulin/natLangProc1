import keybert
from keybert import KeyBERT
import pathlib


directory = pathlib.Path('pol_russ_econ')
# for i in directory.iterdir():
#     if i.is_file():
#         print(i)

model = keybert.KeyBERT('distilbert-base-nli-mean-tokens')
for i in directory.iterdir():
    if i.is_file():
        file= open(i,'r')
        text = file.read()
        file.close()
        text = str(text)
        keywords = model.extract_keywords(text)
        listicle = [i for i in keywords]
        print(f'the keywords for {i} are: ')
        for j in listicle:
            print(j)
