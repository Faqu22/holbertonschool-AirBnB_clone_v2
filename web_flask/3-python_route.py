#!/usr/bin/python3
""" Task 3"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Return 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Return 'HBNB'
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def displayC(text):
    """
    Return C with text.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def route3(text="is cool"):
    """
    Return Python with text.
    """
    return f"Python {text.replace('_', ' ')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
