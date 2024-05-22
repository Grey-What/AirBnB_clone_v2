#!/usr/bin/python3
"""script start flask web application listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """
    display n if n is a number

    Args:
    n (int): a number to display
    """
    if isinstance(n, int):
        return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n=None):
    """
    display a template if n is a number

    Args:
    n (int): number to evaluate
    """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n=None):
    """
    display template only if n is an int
    """
    if isinstance(n, int):
        if n % 2:
            val = "odd"
        else:
            val = "even"
        return render_template("6-number_odd_or_even.html", n=n, val=val)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
