#!/usr/bin/python3
"""User class module"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from BaseModel:
        Attributes(public class):
            email - password - first-name - last-name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
