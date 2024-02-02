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
    temp_dict = {value.to_dict().get('name'): value.to_dict().get(arg)
                 for key, value in curr_objs.items()}
    keys = list(temp_dict.keys())
    keys.sort()
    temps = {key: temp_dict[key] for key in keys}
    return temps


@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id):
    """Returns HBNB"""
    try:
        states = get_list(State, 'id')
        if escape(id) not in states.values():
            abort(404)
        state = {key: value for key, value in states.items()
                 if value == escape(id)}
        city_ids = get_list(City, 'id')
        cities = get_list(City, 'state_id')
        return render_template('templates/9-states.html',
                               states=state, cities=cities, city_ids=city_ids)
    except ValueError as e:
        abort(404)


@app.route('/states', strict_slashes=False)
def states_lst():
    """Returns HBNB"""
    states = storage.all(State).values()
    print(states)
    return render_template('templates/7-states_list.html', States=states)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the current session storage engine"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
