# from flask import Flask, render_template, redirect, request, url_for
#
# app = Flask(__name__)
#
#
# @app.route('/home')
# def nas():
#     return "if i ruled the word"
#
# @app.route('/success/<name>')
# def success(name):
#     return 'weclome %s' % name
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success', name=user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success', name=user))
#
#
#
# @app.route('/deadprez')
# def deadPrez():
#     return render_template('deadPrez.html',)
#
# if __name__ == '__main__':
#     app.run()


from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)