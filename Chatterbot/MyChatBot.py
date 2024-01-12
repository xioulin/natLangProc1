from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot= ChatBot('MyChatBot')

trainer= ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

response = chatbot.get_response('Hello, i love you')

print(response)


from flask import Flask, render_template, request
app = Flask(__name__)
@app.rout('/')
def home():
    return render_template('index.html')
@app.route('/get')
def get_bot_response():
    userText= request.args.get('msg')
    return str(englishBot.get_response(userText))
if __name__ == '__main__':
    app.run()
