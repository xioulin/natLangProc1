import PyPDF2
from nltk import word_tokenize


import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
pdf= open('/Users/pkc/Dropbox/Mac/Desktop/shapiro_pride.pdf','rb')

pdfReader= PyPDF2.PdfReader(pdf)

pdfObj1= pdfReader.pages[0]
pdfObj2= pdfReader.pages[1]

page1= pdfObj1.extract_text()
page2= pdfObj2.extract_text()

page1= page1[463:-8]


page2=page2[238:837]

wholeColumn= page1+page2
print(wholeColumn)

text= word_tokenize(wholeColumn)

print(nltk.pos_tag(text))