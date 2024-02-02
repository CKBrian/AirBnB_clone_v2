#!/usr/bin/python3
"""Defines a module that starts a Flask web application"""
from flask import Flask, abort, render_template, url_for
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


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


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = get_list(State, 'id')
    cities = get_list(City, 'state_id')
    amenities = get_list(Amenity, 'id')
    return render_template('templates/10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the current session storage engine"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
