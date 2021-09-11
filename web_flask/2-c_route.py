#!/usr/bin/python3
"""
Script that starts a Flask web application
-> The application listens on 0.0.0.0, port 5000.
-> Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display HBNB
    /c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route("/c/<text>")
def c(text):
    return "C " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
