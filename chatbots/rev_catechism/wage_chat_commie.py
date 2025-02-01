from classess import TextFromFile
from nltk import sent_tokenize
import random
wage = TextFromFile('_The_Revolutionary_Catechism_by_Sergey_Nechayev_1869.txt')

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