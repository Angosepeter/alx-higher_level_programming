#!/usr/bin/python3
"""Defines a class LockedClass"""

class LockedClass:
    """
    Prevents the user from  creting a new class instanvce attribute
    unless first_name instance attribute is called
    Attributes:
        first_name (str): first name of anything.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of Locked Class."""

        self.first_name = "first_name"
