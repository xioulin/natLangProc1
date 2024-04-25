import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
def create_app(test_config=None):

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

@app.route('/')
def hello():
    return "<p>if i ruled the world<p>"

if __name__ == '__main__':
    app.run()




