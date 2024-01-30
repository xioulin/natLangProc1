#%%
from chatterbot import ChatBot
import pandas as pd
from chatterbot.trainers import ListTrainer
#%%
df_quotes = pd.read_pickle('/Users/pkc/PycharmProjects/natLangProc1/TSAR/df_quotes.pickle')
#%%
quotes_to_list = df_quotes.quotes.tolist()
#%%
bot = ChatBot(
    'TSAR',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri= 'sqlite:///TSARchat.db',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ]
)
#%%
trainer = ListTrainer(bot)
#%%
trainer.train(quotes_to_list)
#%%
while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break