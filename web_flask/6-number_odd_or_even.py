#!/usr/bin/python3
""" Task 6"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def route4(n):
    """
    Return n is a number.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def route5(n):
    """
    Return a HTML with the variable n in h1.
    """
    return render_template('5-number.html', n=f"Number: {n}")


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def route6(n):
    """
        Return a HTML with the variable n in h1.
    """
    return render_template(
        '6-number_odd_or_even.html',
        n=f"Number {n} is {'even' if n % 2 == 0 else 'odd'}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
