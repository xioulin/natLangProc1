import pathlib

from keybert import KeyBERT


class PageScraper():
    def __init__(self,url):
        self.url = url


class KeywordExtractor():
    from keybert import KeyBERT
    import pathlib

    def __init__(self,directory):
        self.directory = pathlib.Path(directory)

    def extract_keywords(self):
        model = KeyBERT('distilbert-base-nli-mean-tokens')
        for i in self.directory.iterdir():
            if i.is_file():
                file = open(i, 'r')
                text = file.read()
                file.close()
                text = str(text)
                keywords = model.extract_keywords(text)
                listicle = [i for i in keywords]
                print(f'the keywords for {i} are: ')
                for j in listicle:
                    print(j)
