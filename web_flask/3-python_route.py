#!/usr/bin/python3
"""script start flask web application listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return string"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return string"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    display C and text variable value

    Args:
    text (string): string to insert
    """
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    display Python followed by text variable value with a default

    Args:
    text (string): string to insert; has default
    """
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
