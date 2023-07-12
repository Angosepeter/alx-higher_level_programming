#!/usr/bin/python3
"""Defines a JSON file-writing function."""

import json

def to_json_string(my_obj):
    """Write an object to a text file using JSON representation."""
    return json.dumps(my_obj)
