#!/usr/bin/python3
"""Defines a module that starts a Flask web application"""
from flask import Flask, abort, render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__, template_folder='.')


@app.route('/states_list', strict_slashes=False)
def states_lst():
    """Returns HBNB"""
    curr_objs = storage.all(State)
    state_dict = {value.to_dict().get('name'): value.to_dict().get('id')
                  for key, value in curr_objs.items()}
    keys = list(state_dict.keys())
    keys.sort()
    states = {key: state_dict[key] for key in keys}
    return render_template('templates/7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the current session storage engine"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
