import nltk.corpus
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
# nltk.download('indian')
# print(nltk.corpus.indian.tagged_words())

print(nltk.corpus.brown.tagged_words(tagset='universal')[:15])

from nltk.corpus import brown
brown_news_tagged= brown.tagged_words(categories='news',tagset='universal')
# tag_fd= nltk.FreqDist(tag for (word,tag) in brown_news_tagged)
# print(tag_fd.most_common())
# print(tag_fd.plot(cumulative=True))

word_tag_pairs= nltk.bigrams(brown_news_tagged)
noun_preceders= [a[1]for (a,b) in word_tag_pairs if b[1]=='NOUN']
fdist= nltk.FreqDist(noun_preceders)
# print([tag for (tag,_) in fdist.most_common()])

brown_learned_text= brown.words(categories='learned')

# print(sorted(set(b for (a,b) in nltk.bigrams(brown_learned_text) if a=='often')))

brown_lrnd_tagged= brown.tagged_words(categories='learned',tagset='universal')
tags= [b[1] for (a,b) in nltk.bigrams(brown_lrnd_tagged) if a[0]=='often']
fd= nltk.FreqDist(tags)
# print(fd.tabulate())





