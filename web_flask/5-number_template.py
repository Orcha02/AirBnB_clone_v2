#!/usr/bin/python3
"""
Script that starts a Flask web application
-> The application listens on 0.0.0.0, port 5000.
-> Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display HBNB
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: display n is a number only if n is an integer
"""
from flask import Flask, render_template
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


@app.route("/python/")
@app.route("/python/<text>")
def python(text="is cool"):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>")
def number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:num>")
def template(num):
    """Display a HTML page only if n is an integer:
        H1 tag: Number: n inside the tag BODY"""
    return render_template("5-number.html", n=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
