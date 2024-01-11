from nltk.tokenize import sent_tokenize, word_tokenize

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
# nltk.download()
commieString = """
 A spectre is haunting Europe — the spectre of communism. All the powers of old Europe have entered into a holy alliance to exorcise this spectre: Pope and Tsar, Metternich and Guizot, French Radicals and German police-spies.
Where is the party in opposition that has not been decried as communistic by its opponents in power? Where is the opposition that has not hurled back the branding reproach of communism, against the more advanced opposition parties, as well as against its reactionary adversaries?"""


commieIntro = word_tokenize(commieString)





# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



stop_words = set(stopwords.words("english"))

filtered_list = []

for word in commieIntro:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
# print(filtered_list)

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

string_for_stemming = """
In the earlier epochs of history, we find almost everywhere a complicated arrangement of society into various orders, a manifold gradation of social rank. In ancient Rome we have patricians, knights, plebeians, slaves; in the Middle Ages, feudal lords, vassals, guild-masters, journeymen, apprentices, serfs; in almost all of these classes, again, subordinate gradations."""

words = word_tokenize(string_for_stemming)
stemmed_words = [stemmer.stem(word) for word in words]
# print(stemmed_words)


lincoln_quote = """
Others have been made fools of by the girls; but this can never be with truth said of me. I most emphatically, in this instance, made a fool of myself"""

words_in_lincoln_quote = word_tokenize(lincoln_quote)


# print(nltk.pos_tag(words_in_lincoln_quote))
