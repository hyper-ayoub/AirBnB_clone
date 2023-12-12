#!/usr/bin/python3
"""the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of  review.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): text of review.
    """

    place_id = ""
    user_id = ""
    text = ""
