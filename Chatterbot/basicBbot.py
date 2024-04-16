from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot= ChatBot(
    'Victor Chaos'
    ,storage_adapter='chatterbot.storage.SQLStorageAdapter'
    ,logic_adapters=['chatterbot.logic.BestMatch']
    ,database_uri='sqlite:///database.sqlite3'
)

trainer= ListTrainer(chatbot)

trainer.train([
    'Well, hey fellas',
    'I\'ll bet you\'re looking to make yourself some money',
    'My name is Vic, Vic Chaos',
    'I\'m gonna let you in on a little secret',
    'Have you ever heard of NFT\'s?'
])


while True:
    try:
        user_input= input()
        bot_response= chatbot.get_response(user_input)
        print(bot_response)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break