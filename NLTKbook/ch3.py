from urllib import request

import nltk

url= 'http://www.gutenberg.org/files/2554/2554-0.txt'

import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
response = request.urlopen(url)
raw=response.read().decode('utf8')


# url = "https://www.espn.com/soccer/report/_/gameId/671182"
# html=request.urlopen(url).read().decode('utf8')
# print(html[:150])


# path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
#
# f = open(path,encoding='latin2')
#
# for line in f:
#     line = line.strip()
#     print(line)
#

import re





