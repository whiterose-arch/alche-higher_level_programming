#!/usr/bin/python3
"""
Returns the JSON representation of an object (string).
Args:
    my_obj (object): The object to convert to JSON.
Returns:
    str: The JSON representation of the object.
"""

import json

def to_json_string(my_obj):
  return json.dumps(my_obj)
