from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def sayhello():
    return "<p>hellopeople</p>"


