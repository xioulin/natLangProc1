from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#
chatbot= ChatBot('Elijah Bot')

conversation= [
    'Shipmates, have ye shipped in that ship?',
    'Have ye shipped in her?',
    'ye haven\'t seen Old Thunder yet, have ye?',
    'morning to ye, shipmates, morning',
    'the ineffable heavens bless thee'
]
trainer= ListTrainer(chatbot)
trainer.train(conversation)
response= chatbot.get_response('hullo!')
print(response)


