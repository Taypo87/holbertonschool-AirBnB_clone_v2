#!/usr/bin/python3
# starts a webflask app

from flask import Flask, render_template
from models import storage
from models.state import State


@app.route('/states_list')
"""states list"""


def states_list():
    return render_template('7-states_list.html',
                           states=storage.all("State"))


@app.teardown_appcontext
"""tear down"""


def teardown(err):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
