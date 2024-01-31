#!/usr/bin/python3
"""Defines a module that starts a Flask web application"""
from flask import Flask, abort, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__, template_folder='.')


def get_list(cls, arg):
    """Returns HBNB"""
    curr_objs = storage.all(cls)
    state_dict = {value.to_dict().get('name'): value.to_dict().get(arg)
                  for key, value in curr_objs.items()}
    keys = list(state_dict.keys())
    keys.sort()
    states = {key: state_dict[key] for key in keys}
    return states


@app.route('/cities_by_states', strict_slashes=False)
def states_lst():
    """Returns HBNB"""
    states = get_list(State, 'id')
    city_ids = get_list(City, 'id')
    cities = get_list(City, 'state_id')
    return render_template('templates/8-cities_by_states.html',
                           states=states, cities=cities, city_ids=city_ids)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the current session storage engine"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
