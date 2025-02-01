from flask import Flask, render_template, request, jsonify
from bardbot3002 import Bard_Bot
app = Flask(__name__)

class Chatbot:
    def get_response(self, message):
        return f"> {message}"
chatbot = Chatbot()
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_msg = request.json["message"]
    bot_rsp= chatbot.get_response(user_msg)
    return jsonify(bot_rsp)
if __name__ == "__main__":
    app.run(debug=True)