from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot= ChatBot('Victor Chaos')

trainer= ListTrainer(chatbot)

# trainer.train([
#     'Well, hey fellas',
#     'I\'ll bet you\'re looking to make yourself some money',
#     'My name is Vic, Vic Chaos',
#     'I\'m gonna let you in on a little secret',
#     'Have you ever heard of NFT\'s?'
# ])

trainer.train([
    'hi there',
    'hello'
])
trainer.train([
    'greetings',
    'hello'
])
print("why hello there")
response= chatbot.get_response(input())
print(response)

