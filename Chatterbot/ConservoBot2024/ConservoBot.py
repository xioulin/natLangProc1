from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

shapiroBot= ChatBot('Ben Shapiro',
                    storage_adapter='chatterbot.storage.SQLStorageAdapter',
                    database_uri= 'sqlite:///database.sqlite33',
                    )

shapirisms= [
    'Facts don\t care about your feelings',
    'Without a clear moral vision, we devolve into moral relatives, and from there, into oblivion',
    'The left no longer makes arguments about policies\' effectiveness. Their only argument left is character assassination.',
    'Nihilism, narcissism, and hedonism are natural results of the chaotic existential subjectivism popularized by the Left',
    'No picture should lower the moral standards of those who see it.',
     'The goal of same-sex marraige proponents is to elevate homosexuality to the same moral level as heterosexuality.'

]

trainer= ListTrainer(shapiroBot)
trainer.train(shapirisms)

print("will you vote for Trump in 2024?")

while True:
    try:
        bot_input = shapiroBot.get_response(input())
        print(bot_input)
    except(KeyboardInterrupt, EOFError,SystemExit):
        break