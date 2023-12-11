#!/usr/bin/python3
"""
Module to initiate a flask app
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Index route
    """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb route
    """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Dynamic routing
    """
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python/')
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """
    Dynamic routing
    """
    if text:
        return "Python " + text.replace("_", " ")
    return "Python " + text


if __name__ == "__main__":
    app.run(debug=True)
