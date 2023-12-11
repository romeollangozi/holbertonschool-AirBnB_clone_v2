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


if __name__ == "__main__":
    app.run(debug=False)
