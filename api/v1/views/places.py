#!/usr/bin/python3
"""
This module handles all default RestFul API actions for Place objects.
It provides handlers to retrieve and manipulate place information stored in the system.
"""
from flask import request, abort, jsonify
from models import storage
from models.place import Place
from api.v1.views import app_views


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def places_search():
    """ Retrieves all Place objects depending on the JSON in the body of the request. """
    try:
        req_data = request.get_json()
    except Exception:
        abort(400, description="Not a JSON")

    if not req_data:
        # If the JSON is empty or not provided, return all places.
        places = storage.all(Place).values()
        return jsonify([place.to_dict() for place in places])

    states = req_data.get('states', [])
    cities = req_data.get('cities', [])
    amenities = req_data.get('amenities', [])

    places = set()

    # Fetch places based on states and cities
    if states or cities:
        for state_id in states:
            state = storage.get('State', state_id)
            if state:
                for city in state.cities:
                    places.update(city.places)

        for city_id in cities:
            city = storage.get('City', city_id)
            if city:
                places.update(city.places)
    else:
        places = storage.all(Place).values()

    if amenities:
        final_places = []
        for place in places:
            if all(am in place.amenities for am in amenities):
                final_places.append(place)
        places = final_places

    return jsonify([place.to_dict() for place in places])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
