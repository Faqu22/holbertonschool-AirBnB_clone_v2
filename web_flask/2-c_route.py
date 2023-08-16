#!/usr/bin/python3
""" Task 1"""
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


@app.route('c/<text>', strict_slashes=False)
def displayC(text):
    """
    Return C with text.
    """
    new_text = text.replace(" ", "_")
    return f"C {new_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
