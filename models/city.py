#!/usr/bin/python3

"""
Module for city class
"""


from models import base_model


class City(base_model.BaseModel):
    """
    city class, inherits attribs and methods from base class.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
