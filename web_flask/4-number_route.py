#!/usr/bin/python3
"""Defines a module that starts a Flask web application"""
from flask import Flask, abort
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def print_c(text):
    """Returns /c/<text>"""
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def print_python(text="is cool"):
    """Returns /python/<text>"""
    return "Python {}".format(escape(text.replace('_', ' ')))


@app.route('/number/<n>', strict_slashes=False)
def print_num(n):
    """Returns /number/<n>"""
    try:
        n = int(n)
        return "{} is a number".format(escape(n))
    except ValueError as e:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
