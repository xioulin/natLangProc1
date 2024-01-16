from chatterbot import ChatBot
from jimMorrisonList import theDoors
from chatterbot.trainers import ListTrainer
morrisonBot= ChatBot('Jim Morrison',
                     storage_adapter='chatterbot.storage.SQLStorageAdapter',
                     database_uri='sqlite:///database.sqlite3',
                     logic_adapters=[
                         'chatterbot.logic.MathematicalEvaluation',
                         'chatterbot.logic.BestMatch'
                     ]
                     )
print("what is your name?")

trainer = ListTrainer(morrisonBot)
trainer.train(theDoors)
while True:
    try:
        bot_input= morrisonBot.get_response(input())
        print(bot_input)
    except(KeyboardInterrupt,EOFError,SystemExit):
        break