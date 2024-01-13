from chatterbot import ChatBot
import logging
logging.basicConfig(level=logging.INFO)


bot = ChatBot(
    'Math and Time Bot',
    read_only=True,
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ]
)
response= bot.get_response('what is 4+9?')
print(response)
