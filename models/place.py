#!/usr/bin/python3
"""the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Representation of place.

    Attributes:
        city_id (str): The unique identifier for the city.
        user_id (str): The unique identifier for the user.
        name (str): The name associated with the place.
        description (str): A brief description of the place.
        number_rooms (int): The total number of rooms available at the place.
        number_bathrooms (int): The total number of bathrooms available at the place.
        max_guest (int): The maximum number of guests allowed at the place.
        price_by_night (int): The cost per night for staying at the place.
        latitude (float): The geographical latitude of the place.
        longitude (float): The geographical longitude of the place.
        amenity_ids (list): A list of identifiers for amenities available at the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
