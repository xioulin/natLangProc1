from classess import TextFromFile
from nltk import sent_tokenize
import random
wage = TextFromFile('wage_labor/Wage_Labour_and_Capital._Chapter_8.txt')

text = wage.replace('\n',' ')

sentences = sent_tokenize(text)

exit_conditions='quit'

print('Greetings, Comrade!')


while True:
    query=input('>')
    if query in exit_conditions:
        print('da zwidenia, tavarisch!')
        break
    else:
        print(random.choice(sentences))