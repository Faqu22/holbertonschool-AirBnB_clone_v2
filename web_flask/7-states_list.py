#!/usr/bin/python3
""" Task 6"""
from flask import Flask, render_template

from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def tearDown(arg=None):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def route7():
    return render_template(
        '7-states_list.html',
        states=storage.all(State).values()
    )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
