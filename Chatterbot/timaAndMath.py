from chatterbot import ChatBot

bot = ChatBot(
    'Math and Time Bot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter'

    ]
)

response= bot.get_response('1+1')
print(response)