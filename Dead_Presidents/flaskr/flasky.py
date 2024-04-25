from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def nas():
    return "if i ruled the word"

@app.route('/deadprez')
def deadPrez():
    return render_template('deadPrez.html',)

if __name__ == '__main__':
    app.run()
