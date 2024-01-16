from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

theDoors= ['Hello',
               'I love you',
               'let me tell you name',
               'try to set the night on fire',
               'you know that it would be untrue',
               'you know that I would be a liar',
               'if i were to say to you',
               'girl, you couldn\'t get much higher'
               ]

doorsChatBot = ChatBot('Jim Morrison')

trainer= ListTrainer(doorsChatBot)
trainer.train(theDoors)

respons= doorsChatBot.get_response('hello')
print(respons)