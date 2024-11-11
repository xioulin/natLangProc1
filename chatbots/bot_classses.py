
from classess import TextFromFile
import random
from classess import TextFromFile
from nltk import sent_tokenize
import nltk
class TextToChat():


    def __init__(self, text_file_path):
        self.text_file_path = text_file_path


    def start_chat(self):
        text = TextFromFile(self.text_file_path)

        sent = sent_tokenize(text)
        exit_conditions= 'quit'

        print("Privet, Drug")
        nltk.download('punkt_tab')
        while True:
            query= input('>')
            if query in exit_conditions:
                print('da zvidhenia')
                break
            else:
                print(random.choice(sent))
