#!/usr/bin/python3
"""City class module"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inherits from BaseModel
    Public class attr : name - state_id
    """
    name = ""
    state_id = ""
