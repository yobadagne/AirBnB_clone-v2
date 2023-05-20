#!/usr/bin/python3
"""
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """a function that displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)
