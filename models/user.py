#!/usr/bin/python3
"""the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str):  The email of user.
        password (str):  The password of user.
        first_name (str):  The first name of user.
        last_name (str): The last name of user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
