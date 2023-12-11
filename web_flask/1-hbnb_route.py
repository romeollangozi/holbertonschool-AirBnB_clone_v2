#!/usr/bin/python3
"""
Module to initiate a flask app
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
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


if __name__ == "__main__":
    app.run(debug=True)
