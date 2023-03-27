#!/usr/bin/python3
"""task one starts flask web app"""

from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hey_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def heybnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def weluvpy(text="is cool"):
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    try:
        n = int(n)
        return "{} is a number".format(n)
    except TypeError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
